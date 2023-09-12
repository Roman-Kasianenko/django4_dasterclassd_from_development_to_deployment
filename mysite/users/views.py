from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import CustomUserForm
from .models import Profile


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


@login_required
def create_profile(request):
    if request.method == 'POST':
        contact_number = request.POST.get('contact_number')
        image = request.FILES['upload']
        user = request.user

        profile = Profile(user=user, image=image, contact_number=contact_number)
        profile.save()
    return render(request=request, template_name='users/createprofile.html')


def seller_profile(request, id):
    seller = User.objects.get(id=id)
    context = {'seller': seller}
    return render(request, 'users/sellerprofile.html', context=context)
