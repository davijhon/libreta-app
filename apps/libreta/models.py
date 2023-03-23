from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    edad = models.CharField(max_length=250)
    dni = models.CharField(max_length=9, unique=True)

    class Meta:
        verbose_name = "persona"
        verbose_name_plural = "personas"

    def __str__(self):
        return "{nombre} - {dni}".format(
            nombre=self.nombre,
            dni=self.dni
        )

class Direccion(models.Model):
    pais = models.CharField(max_length=250)
    region = models.CharField(max_length=250)
    ciudad = models.CharField(max_length=250)
    codigo_postal = models.CharField(max_length=250)
    telefono = models.CharField(max_length=250)
    correo = models.EmailField(max_length=350)
    direccion = models.CharField(max_length=250)
    persona = models.ManyToManyField(Persona, related_name="direcciones")
    

    class Meta:
        verbose_name = "direccion"
        verbose_name_plural = "direcciones"

    def __str__(self):
        return f"{self.direccion}"