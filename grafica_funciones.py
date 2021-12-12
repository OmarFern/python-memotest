from tkinter import *
from tkinter import messagebox

        
def leer(archivo): 
    """Saca las lineas del archivo CVS y las convierte en listas
    Autor: Galvan Nicolas
    """
    linea = archivo.readline()
    if (linea):
        linea = linea.rstrip()
        devolver = linea.split(',')
    else:
        devolver = None
    return devolver

def agregar_participante(lista_participantes,var_nombre, var_contraseña,entrada_participantes):
    """Agrega participantes al juego cuando el nombre y la contraseña sean correctos según el registro
    Autor: Galvan Nicolas
    """
    var_nombre = var_nombre.get()
    var_contraseña = var_contraseña.get()

    if not var_nombre in lista_participantes:
        participantes_registrados = open("participantes registrados.csv", 'r')
        linea = leer(participantes_registrados)
        seguir = True
        while linea and seguir == True:
            if linea[0] == var_nombre:
                if linea[1] == var_contraseña:
                    seguir = False
                    lista_participantes += [var_nombre]
                    messagebox.showinfo("Memotest Spam", "Agregado con éxito")
                    entrada_participantes.insert(END,var_nombre)
                else:
                    seguir = False
                    messagebox.showerror("Memotest Spam", "Contraseña incorrecta")
            linea = leer(participantes_registrados)
        if seguir == True:
            messagebox.showerror("Memotest Spam", "Participante no registrado")
        participantes_registrados.close()
    else:
        messagebox.showerror("Memotest Spam", "Participante ya agregado")
        
#------------------------------------------------------------------------------
def verificar_contraseña(var_contraseña, var_contraseña2):
    """Verifica que la contraseña sea válida según los requisitos
    Autor: Galvan Nicolas
    """
    seguir = True
    """
    if not var_contraseña == var_contraseña2:
        messagebox.showerror("Memotest Spam", "La contraseña no es igual")
        seguir = False
    if not len(var_contraseña) <= 8 and not len(var_contraseña) >= 12:
        messagebox.showerror("Memotest Spam", "Longitud de contraseña incorrecta")
        seguir = False

    if seguir == True:
        a=b=c=d=e = False
        for i in range(len(var_contraseña)):
            if var_contraseña[i].isupper():#alguna letra mayuscula
                a=True
            elif var_contraseña[i].isdigit():#algun numero
                b=True
            elif var_contraseña[i].islower():#alguna letra minuscula
                c=True
            elif var_contraseña[i] == "-" or var_contraseña[i] == "_":
                d=True
            if not var_contraseña[i].isalnum() and (var_contraseña[i] == "_" or var_contraseña[i] == "-"):
                e=True
        if a and b and c and d and e:
            seguir = True
        else:
            seguir = False
            messagebox.showerror("Memotest Spam", "La contraseña no cumple con los requisitos necesarios")
            """
    return seguir

def verificar_nombre(var_nombre):
    """Verifica que el nombre sea válido según los requisitos
    Autor: Galvan Nicolas
    """
    seguir = True
    """
    if len(var_nombre) >= 4 and len(var_nombre) <= 12:
        seguir = True
    else:
        messagebox.showerror("Memotest Spam", "Longitud del nombre incorrecta")
        seguir = False
    
    if seguir == True:
        a=b=c = False
        for i in range(len(var_nombre)):
            if var_nombre[i]  == "_":#que tenga guion bajo
                a=True
            elif var_nombre[i].isdigit():#algun numero
                b=True
            elif var_nombre[i].isalpha():#alguna letra
                c=True
        if a and b and c:
            seguir = True
        else:
            seguir = False
            messagebox.showerror("Memotest Spam", "El nombre no cumple con los requisitos necesarios")
    """      
    return seguir

def guardar_registro(var_nombre, var_contraseña):
    """Guarda en un archivo CSV el nombre y contraseña del participante 
    Autor: Galvan Nicolas
    """
    archivo = open("participantes registrados.csv", 'a')
    linea = var_nombre + "," + var_contraseña
    archivo.write(linea + "\n")
    archivo.close()
    messagebox.showinfo("Memotest Spam", "Guardado con éxito")

def verificar_registro(var_nombre, var_contraseña, var_contraseña2):
    """Guarda en un archivo CSV el nombre y contraseña del participante si estos cumplen con los requisitos
    Autor: Galvan Nicolas
    """
    var_nombre = var_nombre.get()
    var_contraseña = var_contraseña.get()
    var_contraseña2 = var_contraseña2.get()
    
    if verificar_nombre(var_nombre):
        participantes_registrados = open("participantes registrados.csv", 'r')
        linea = leer(participantes_registrados)
        seguir = True
        while linea and seguir == True:
            if linea[0] == var_nombre:
                seguir = False
                messagebox.showerror("Memotest Spam", "Participante ya registrado")
            linea = leer(participantes_registrados)
        participantes_registrados.close()

    if seguir == True and verificar_contraseña(var_contraseña, var_contraseña2):
        guardar_registro(var_nombre, var_contraseña)

#------------------------------------karen------------------------------------------

def lista_de_participantes(entrada_participantes,lista_participantes):
    for i in lista_participantes:
        if i != "":
            entrada_participantes.insert(END,i)
            
   
        
        
        