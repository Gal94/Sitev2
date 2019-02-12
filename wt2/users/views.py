from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post
from .models import User, Profile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()#saves to database
            username = form.cleaned_data.get('username') #from form ->cleaned_data get username
            messages.success(request, f'Account created for {username}')
            return redirect('login')
     #   else:
      #      messages.warning(request, f'Please try a different username/password')
       #     return redirect('register')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


#try to build it with DetailView
@login_required #makes the view only visible with being logged in, makes me able to use "user"
def profile(request):
    if request.method == 'POST':
        #request.post to pass in the post's data
        u_form = UserUpdateForm(request.POST, instance=request.user)#display the current logged in user
        p_form = ProfileUpdateForm(request.POST, request.FILES ,instance=request.user.profile)#display the current logged in user profile
        #for images add request.FILES

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)  # display the current logged in user
        p_form = ProfileUpdateForm(instance=request.user.profile)  # display the current logged in user profile


    context ={
        'u_form' : u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)


class UserDetailView(DetailView):
    model = User
    template_name = 'users/user_detail.html'
