class estudiante():
    num_estudiantes = 0
    def __init__(self, nombre, apellido, universidad):
        self.nombre = nombre
        self.apellido = apellido
        self.universidad = universidad
        estudiante.num_estudiantes += 1


estudiante1 = estudiante("Adrian", "Sanchez", "Complutense")
estudiante2 = estudiante("Ricardo", "Whoknows", "LaVida")
estudiante3 = estudiante("Pepe", "Maderas", "ElBosque")

clase = [estudiante1, estudiante2, estudiante3]

i = 1
for estudiante in clase:
    print(i,".", estudiante.nombre, estudiante.apellido, estudiante.universidad)
    i=i+1
