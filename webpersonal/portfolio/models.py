from django.db import models

# Create your models here.
class Project(models.Model): # Super clase models.Model representa tabla en BD
    title = models.CharField(max_length=200, verbose_name="Título")     # los campos charfield siempre deben tener un valor maximo
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")  # agregamos atributo 'upload_to' para indicar donde deben almacenar las imagenes del proyecto subidas por el usuario
    link = models.URLField(verbose_name="Dirección Web", null=True, blank=True)
    
    link = models.URLField(verbose_name="Dirección Web", null=True, blank=True)   # ejercicio final curso
    
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    

    class Meta:     # subclase para agregar metadatos extendidos
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]     # campo de ordenación de nuestros registros, en este caso se ordenan por fecha de creacion '-created' (+ antiguo a + nuevo) si queremos en orden inverso agregar '-' (+ nuevo a + antiguado)

    def __str__(self):          # metodo para que el proyecto se muestre con el titulo definido en el proyecto
        return self.title