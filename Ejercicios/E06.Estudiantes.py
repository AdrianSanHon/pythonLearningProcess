class Estudiante():
    def __init__(self, nombre, apellido, universidad):
        self.nombre = nombre
        self.apellido = apellido
        self.universidad = universidad


estudiante1 = Estudiante("Adrian", "Sanchez", "Complutense")
estudiante2 = Estudiante("Ricardo", "Whoknows", "LaVida")
estudiante3 = Estudiante("Pepe", "Maderas", "ElBosque")

clase = [estudiante1, estudiante2, estudiante3]

i = 1
for estudiante in clase:
    print(i,".", estudiante.nombre, estudiante.apellido, estudiante.universidad)
    i=i+1
