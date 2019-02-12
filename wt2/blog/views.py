from django.shortcuts import render
from . import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


#dummy data

#logic for home page
def home(request):
    context = {
        'posts': models.Post.objects.all() # select (*) from Posts
    }
    #any key in context can now iterate in the html file
    #for flow stream {% for post in posts %}, for variables use {{ post.title }}
    return render(request, 'blog/home.html', context) #takes a request and the template file


def about(request):
    return render(request, 'blog/about.html', context={'title': 'about'})


###################################################
##class based views##
##List,Detail,Create,Update,Delete and much more pre-made views.
###################################################

class PostListView(ListView):
    model = models.Post
    template_name = 'blog/home.html' #give it a manual url, need to define a content variable
    context_object_name = 'posts' #would be "object" otherwise
    ordering = ['-date_posted'] #will date the posts from newest to older (remove '-' in front for reverse order)


class PostDetailView(DetailView):
    model = models.Post


#the mixins is like a decorated for class based view - will redirect to login if not logged in
class PostCreateView(LoginRequiredMixin,CreateView):
    model = models.Post #automatically passes form
    fields = {'title', 'content'} #those will be the form fields

    #need to tell it who the author is in order to submit a form

    def form_valid(self, form):
        form.instance.author = self.request.user #the form you try to submit, set the author of the instance to be the user writing the post
        return super().form_valid(form)


#need to check if the person who wrote the post tries to edit it which is the UserPassesTestMixin
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = models.Post
    fields = {'title','content'}

    def form_valid(self, form):
        form.instance.author = self.request.user #the form you try to submit, set the author of the instance to be the user writing the post
        return super().form_valid(form)

    def test_func(self):
        post =self.get_object() #get the post we're trying to edit

        if self.request.user == post.author: #checks if the author post is the same as the editing author
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = models.Post
    success_url = '/' #send them to homepage if deleted

    def test_func(self):
        post =self.get_object() #get the post we're trying to edit

        if self.request.user == post.author: #checks if the author post is the same as the editing author
            return True
        else:
            return False
