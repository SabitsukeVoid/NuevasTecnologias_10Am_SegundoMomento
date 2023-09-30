class Persona:
    compania = "xyz"

    def __init__(self,id,nombre,correo,contrasena):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena


    def verPersona(self):
        print(f"\n",
              f"Id: {self.id} \n",
              f"Nombre: {self.nombre} \n",
              f"Correo: {self.correo} \n",
              f"Compania: {self.compania} \n")


if __name__ == "__main__":
    maria = Persona(1, "Maria", "maria@cesde.edu.co", "qwe123")
    maria.verPersona()


    maria.correo = "maria@gmail.com"
