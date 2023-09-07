from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserForm


def register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            return redirect('myapp:products')
    form = CustomUserForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    return render(request=request, template_name='users/profile.html')
