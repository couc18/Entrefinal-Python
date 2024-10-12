from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm

def about_me_view(request):
    return render(request, 'about_me.html')

def blog_detail_view(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog_detail.html', {'blog': blog})


def blog_list_view(request):
    blogs = Blog.objects.all().order_by('-created_at')  # Ordenar por fecha de creación
    return render(request, 'blog_list.html', {'blogs': blogs})

@login_required
def blog_create(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user  # Asignar el autor
            blog.save()
            return redirect('blog_detail', pk=blog.pk)  # Redirigir a la vista de detalle del blog creado
    else:
        form = BlogForm()
    return render(request, 'blog_form.html', {'form': form, 'action': 'Crear'})

@login_required
def blog_update(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', pk=blog.pk)  # Redirigir a la vista de detalle del blog actualizado
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog_form.html', {'form': form, 'action': 'Actualizar'})

@login_required
def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        blog.delete()
        return redirect('blog_list')  # Redirigir a la lista de blogs
    return render(request, 'blog_confirm_delete.html', {'blog': blog})

