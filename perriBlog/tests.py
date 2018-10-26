from django.test import TestCase
from .models import Perro, Cliente
# Create your tests here.

class TestCase1( TestCase ):
    def test1( self ):

        #Arrange
        expected = 1
        result = 0
        #Act
        Perro.objects.create(Nombre="cachupin", Raza="prueba", Descripcion="ola k ase", Estado="adopatado", Imagen="prueba")
        result = len(Perro.objects.all())

        #Assert
        self.assertEqual(expected,result)

    def test2( self ):

        #Arrange
        expected = 1
        result = 0
        #Act
        Cliente.objects.create(Correo="123@gmail.com", Rut=12345678-9, Nombre="ola k ase", Telefono=12354785, Region="Arica y Parinacota",
                            Ciudad="Santiago", Vivienda="Departamento")
        result = len(Cliente.objects.all())

        #Assert
        self.assertEqual(expected,result)
