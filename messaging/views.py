from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.messages import get_messages
from .models import Message
from .forms import MessageForm
from django.contrib import messages

@login_required
def send_message(request):

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user  # Asignar el usuario actual como remitente
            message.save()
            messages.success(request, 'Mensaje enviado con éxito.')
            return redirect('send_message')  # Cambia esto al nombre de tu URL de bandeja de entrada
    else:
        form = MessageForm()

    return render(request, 'send_message.html', {'form': form})

@login_required
def inbox(request):
    messages = Message.objects.filter(recipient=request.user).order_by('-sent_at')
    return render(request, 'inbox.html', {'messages': messages})