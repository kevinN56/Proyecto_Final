from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [

    # ---------------- Inicio ----------------
    path("", views.InicioView, name="inicio"),
    path("sobre/", views.SobreView, name="sobre"),
    path("contacto/", views.ContactoView, name="contacto"),

    # ---------------- Blog ----------------
    path("posts/", views.ListaPostView.as_view(), name="lista_post"),
    path("posts/<int:pk>/",views.DetallePostView.as_view(),name="detalle_post"),
    path("posts/crear/",views.CrearPostView.as_view(),name="crear_post"),
    path("posts/<int:pk>/editar/",views.EditarPostView.as_view(),name="editar_post"),
    path("posts/<int:pk>/eliminar/",views.EliminarPostView.as_view(),name="eliminar_post"),
    path("buscar/",views.buscarCategoria,name="buscar_categoria"),
    path("categoria/<int:pk>/",views.publicaciones_por_categoria,name="categoria_post"),

    # ---------------- Perfil ----------------
    path("perfil/",views.PerfilView.as_view(),name="perfil"),
    path("perfil/editar/",views.EditarPerfilView.as_view(),name="editar_perfil"),

    # ---------------- Autenticación ----------------
    path("login/",views.LoginView.as_view(),name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path("registro/",views.RegisterView.as_view(),name="registro"),
    path("cambiar-contrasenia/",views.Cambiar_ContraseniaView.as_view(),name="cambiar_contrasenia"),
]