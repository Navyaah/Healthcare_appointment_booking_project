 
# Create your views here.
from django.shortcuts import render, redirect
from .form import CustomUserForm

def CustomUser_create(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('amwell')  # Redirect to a view that lists books or any other page
    else:
        form = CustomUserForm()
    return render(request, 'CustomUser_form.html', {'form': form})