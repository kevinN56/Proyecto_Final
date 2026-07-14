from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="perfil")
    avatar = models.ImageField(upload_to='avatars/',blank=True,null=True)
    bio = models.TextField(blank=True)
    edad = models.PositiveIntegerField(blank=True, null=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    altura = models.PositiveIntegerField(blank=True, null=True)
    objetivo = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
    
class Categoria(models.Model):

    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Publicacion(models.Model):

    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to="publicaciones/",blank=True,null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.titulo   

class Pagina(models.Model):

    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    imagen = models.FileField(upload_to='imagenes/')
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo    