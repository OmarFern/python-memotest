from tkinter import *
from tkinter import messagebox
from grafica_funciones import verificar_registro

def volver_inicio(raiz):
    """Cierra la interfaz grafica de registro, para volver a la interfaz de inicio
    Autor: Galvan Nicolas
    """
    raiz.destroy()

def cerrar_registro(raiz):
    """Cierra la interfaz grafica.
    Autor: Galvan Nicolas
    """
    raiz.destroy()

def interfaz_grafica_registro():
    """Muestra la interfaz grafica de registro
    Autor: Galvan Nicolas
    """
    raiz = Tk()
    raiz.title("Memotest Spam")
    raiz.resizable(0, 0)
    raiz.iconbitmap("spam.ico")
    raiz.geometry("700x500")

    var_nombre = StringVar()
    var_contraseña = StringVar()
    var_contraseña2 = StringVar()

    lienzo = Canvas(raiz, width=500, height=346)
    lienzo.pack(fill="both", expand=True)
    lienzo.config(bg="#A0CAF4")

    lienzo.create_text(250, 30, text="Registro", font=("Curlz MT", 30))

    #------------------------------------------------------------------------------

    lienzo.create_text(120, 120, text="Nombre", font=("Curlz MT", 20))
    entrada_nombre = Entry(raiz, font=("Curlz MT", 20), width=14, bd=0, justify=CENTER, textvariable=var_nombre)
    lienzo.create_window(330, 120, window=entrada_nombre)
    
    lienzo.create_text(120, 170, text="Contraseña", font=("Curlz MT", 20))
    entrada_contraseña = Entry(raiz, font=("Curlz MT", 20), width=14, bd=0, justify=CENTER, textvariable=var_contraseña, show="*")
    lienzo.create_window(330, 170, window=entrada_contraseña)

    lienzo.create_text(120, 220, text="Repetir contraseña", font=("Curlz MT", 20))
    entrada_contraseña2 = Entry(raiz, font=("Curlz MT", 20), width=14, bd=0, justify=CENTER, textvariable=var_contraseña2, show="*")
    lienzo.create_window(330, 220, window=entrada_contraseña2)

    #------------------------------------------------------------------------------ 

    boton_jugar = Button(lienzo, text="GUARDAR", command=lambda: verificar_registro(var_nombre, var_contraseña, var_contraseña2))
    boton_jugar.config(font=("Curlz MT", 14))
    lienzo.create_window(250, 310, window=boton_jugar)

    boton_jugar = Button(lienzo, text="INICIO", command=lambda: volver_inicio(raiz))
    boton_jugar.config(font=("Curlz MT", 14))
    lienzo.create_window(100, 310, window=boton_jugar)

    #------------------------------------------------------------------------------

    boton_jugar = Button(lienzo, text="¿?", command=lambda: messagebox.showinfo("Memotest Spam", """    REQUISITOS NOMBRE
    - Entre 4 a 12 carteres
    - Una letra
    - Un números
    - Un guin bajo “_”

    REQUISITOS CONTRASEÑA
    - Entre 8 a 12 caracteres alfanuméricos
    - Una mayúscula
    - Una minúscula
    - Un numero
    - Alguno de estos caracteres (“_”, ”-”)

    GUARDAR - Guarda las credenciales del participante

    INICIO - Vuelve a la pantalla de inicio
    """))
    boton_jugar.config(font=("Curlz MT", 14))
    lienzo.create_window(480, 320, window=boton_jugar)

    #------------------------------------------------------------------------------
    raiz.mainloop()

