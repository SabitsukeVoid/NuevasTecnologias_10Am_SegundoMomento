from com.apuntes.poo.Persona import Persona

class Estudiante(Persona):

    def __init__(self,id, nombre, correo, contrasena, programa, semestre):
        super().__init__(id,nombre,correo,contrasena)
        self.programa = programa
        self.semestre = semestre


    def verPersona(self):
        print(f"\n",
              f"Id: {self.id} \n",
              f"Nombre: {self.nombre} \n",
              f"Correo: {self.correo} \n",
              f"Compania: {self.compania} \n",
              f"Programa: {self.programa} \n",
              f"Semestre: {self.semestre} \n")



estudiante1 = Estudiante(2,"Alex","jarojohe@cesde.edu.co","1234","Programacion",4)
estudiante1.verPersona()