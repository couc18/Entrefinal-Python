from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.messages import get_messages
from django.contrib import messages
from .forms import ProfileUpdateForm
from .models import Profile

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blog_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def profile_view(request):
    # Intenta obtener el perfil existente
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)  # Crea un perfil vacío si no existe

    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        password = request.POST.get('password')
        # Verifica la contraseña
        if request.user.check_password(password):
            if form.is_valid():
                form.save()
                messages.success(request, 'Tu perfil ha sido actualizado con éxito.')
                return redirect('profile')  # Redirigir a la vista de perfil
            else:
                messages.error(request, 'Hubo un error al actualizar tu perfil. Revisa los datos ingresados.')
        else:
            messages.error(request, 'La contraseña ingresada es incorrecta. No se han guardado los cambios.')
    else:
        form = ProfileUpdateForm(instance=profile)

    return render(request, 'profile.html', {'form': form, 'profile': profile})

def logout_view(request):
    logout(request)  # Cierra la sesión del usuario
    messages.success(request, 'Gracias por su visita, vuelva pronto.')
    return redirect('logout_message')  # Redirige a la página de agradecimiento

def render_logout_message(rq):
    return render(rq, 'logout_message.html')