from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import views as auth_views
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from .models import Publicacion,Perfil,Categoria
from .forms import RegistroUsuarioForm,BusquedaCategoriaFormulario


def buscarCategoria(request):
    form = BusquedaCategoriaFormulario(request.GET or None)

    resultados = None

    if form.is_valid():
        categoria = form.cleaned_data["categoria"]
        resultados = Publicacion.objects.filter(categoria=categoria)

    return render(
        request,
        "blog/resultado_buscador.html",
        {
            "form": form,
            "resultados": resultados,
        },
    )


#-------- templates/myapp --------

def SobreView(request):
    return render(request, "myapp/sobre.html") 

def InicioView(request):
    ultimos_posts = Publicacion.objects.order_by("-fecha")[:3]

    return render(
    request,"myapp/inicio.html",
    {"ultimos_posts": ultimos_posts,"form": BusquedaCategoriaFormulario(),},
    )

def ContactoView(request):
    return render(request, "myapp/contacto.html") 

class PerfilView(LoginRequiredMixin, DetailView):
    model = Perfil
    template_name = "myapp/perfil.html"

    def get_object(self):
        perfil, creado = Perfil.objects.get_or_create(
            user=self.request.user
        )
        return perfil

class EditarPerfilView(LoginRequiredMixin, UpdateView):

    model = Perfil

    fields = [
        "avatar",
        "bio",
        "edad",
        "peso",
        "altura",
        "objetivo",
    ]

    template_name = "myapp/editar_perfil.html"

    success_url = reverse_lazy("perfil")

    def get_object(self):
        perfil, creado = Perfil.objects.get_or_create(
            user=self.request.user
        )
        return perfil
   
#-------- templates/blog --------     
   
class ListaPostView(ListView):
    model = Publicacion
    template_name = "blog/lista_post.html"
    context_object_name = "posts"
    ordering = ["-fecha"]
    
    
class DetallePostView(DetailView):
    model = Publicacion
    template_name = "blog/detalle_post.html"
    context_object_name = "post"
 
class CrearPostView(LoginRequiredMixin, CreateView):
    model = Publicacion
    template_name = "blog/crear_post.html"
    fields = [
        "titulo",
        "contenido",
        "imagen",
        "categoria",
    ]
    success_url = reverse_lazy("lista_post")

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
 
class EditarPostView(LoginRequiredMixin, UpdateView):
    model = Publicacion
    template_name = "blog/crear_post.html"
    fields = [
        "titulo",
        "contenido",
        "imagen",
        "categoria",
    ]
    success_url = reverse_lazy("lista_post")    
    
    def get_queryset(self):
        return Publicacion.objects.filter(autor=self.request.user)
    
class EliminarPostView(LoginRequiredMixin, DeleteView):
    model = Publicacion
    template_name = "blog/eliminar_post.html"
    success_url = reverse_lazy("lista_post")
    
    def get_queryset(self):
        return Publicacion.objects.filter(
            autor=self.request.user
        ) 

def publicaciones_por_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)

    posts = Publicacion.objects.filter(categoria=categoria)

    return render(
        request,
        "blog/lista_post.html",
        {
            "posts": posts,
            "categoria": categoria,
        },
    )    

# -------- template/registration --------

class LoginView(auth_views.LoginView):
    template_name = "registration/login.html"
    
class RegisterView(CreateView):
    template_name = "registration/register.html"
    form_class = RegistroUsuarioForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        response = super().form_valid(form)
        Perfil.objects.get_or_create(user=self.object)
        return response
    
class Cambiar_ContraseniaView(LoginRequiredMixin,PasswordChangeView):

    template_name="registration/cambiar_contrasenia.html"

    success_url=reverse_lazy("perfil")