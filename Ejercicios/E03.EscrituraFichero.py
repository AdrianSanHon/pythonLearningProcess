
#Escritura en fichero
# ¿Cómo haría para escribir en fichero en el disco duro?

def escribirFichero():
    #Ojo que lo sobrescribe
    f = open("archivoTexto.txt","w", encoding = "UTF-8")
    f.write("Ahora lo cambio")
    f.close()
escribirFichero()