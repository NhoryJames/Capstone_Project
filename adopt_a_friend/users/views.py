from django.shortcuts import render, redirect
from .forms import UsersForm

# Create your views here.

def create_user(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            # Save the user object
            user = form.save()
            # Redirect to a success page or do something else
            return redirect('success_page')
    else:
        form = UsersForm()

    return render(request, 'users/signup.html', {'form': form})
