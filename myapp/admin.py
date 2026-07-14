from django.contrib import admin
from .models import Perfil, Categoria, Publicacion, Pagina


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "edad",
        "peso",
        "altura",
        "objetivo",
    )

    search_fields = (
        "user__username",
        "user__email",
    )



@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):

    list_display = (
        "nombre",
    )

    search_fields = (
        "nombre",
    )



@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):

    list_display = (
        "titulo",
        "autor",
        "categoria",
        "fecha",
    )

    list_filter = (
        "categoria",
        "fecha",
    )

    search_fields = (
        "titulo",
        "contenido",
        "autor__username",
    )

    readonly_fields = (
        "fecha",
    )



@admin.register(Pagina)
class PaginaAdmin(admin.ModelAdmin):

    list_display = (
        "titulo",
        "fecha",
    )

    search_fields = (
        "titulo",
        "contenido",
    )

    readonly_fields = (
        "fecha",
    )