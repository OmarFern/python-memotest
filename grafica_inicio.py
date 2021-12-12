from tkinter import *
from tkinter import messagebox
from grafica_funciones import agregar_participante
from grafica_registro import interfaz_grafica_registro
from grafica_funciones import lista_de_participantes


def registrar_participante(root,lista_participantes):
    """Intercambia la interfaz de inicio con la de registro de participantes
    Autor: Galvan Nicolas
    """
    root.destroy()
    interfaz_grafica_registro()
    interfaz_grafica_inicio(lista_participantes)
    
def cerrar_inicio(root,lista_participantes):
    """Cierra la interfaz grafica
    Autor: Galvan Nicolas
    """
    if lista_participantes == []:
        messagebox.showerror("Memotest Spam", "No hay participantes ingresados")
    else:
        messagebox.showinfo("Memotest Spam", "Que comience el juego")
        root.destroy()

def cerrar_inicio_admin(root):
    """Cierra la interfaz grafica
    Autor: Galvan Nicolas
    """
    messagebox.showinfo("Memotest Spam", "Que comience el juego")
    root.destroy()

def interfaz_grafica_inicio(lista_participantes):
    """Muestra la interfaz grafica de inicio
    Autor: Galvan Nicolas
    """
    root = Tk()
    root.title("Memotest Spam")
    root.resizable(0, 0)
    root.iconbitmap("spam.ico")
    root.geometry("1000x500")

    var_nombre = StringVar()
    var_contraseña = StringVar()
    var_participantes = StringVar()

    fondo = PhotoImage(file="fondo.png")

    lienzo = Canvas(root, width=500, height=346)
    lienzo.pack(fill="both", expand=True)

    lienzo.create_image(0, 0, image=fondo, anchor="nw")
    lienzo.create_text(500, 50, text="MEMOTEST", font=("Curlz MT", 40))
    lienzo.create_text(250, 180, text="Ingrese nombre y contraseña del participante", font=("Curlz MT", 20))

    #------------------------------------------------------------------------------

    lienzo.create_text(100, 250, text="Nombre", font=("Curlz MT", 20))
    entrada_nombre = Entry(root, font=("Curlz MT", 20), width=14, bd=0, justify=CENTER, textvariable=var_nombre)
    lienzo.create_window(300, 250, window=entrada_nombre)
    
    lienzo.create_text(100, 300, text="Contraseña", font=("Curlz MT", 20))
    entrada_contraseña = Entry(root, font=("Curlz MT", 20), width=14, bd=0, justify=CENTER, textvariable=var_contraseña, show="*")
    lienzo.create_window(300, 300, window=entrada_contraseña)

    #------------------------------------------------------------------------------ 

    boton_registrar= Button(lienzo, text="REGISTRAR", command=lambda: registrar_participante(root,lista_participantes))
    boton_registrar.config(font=("Curlz MT", 14))
    lienzo.create_window(500, 300, window=boton_registrar)

    boton_jugar = Button(lienzo, text="  JUGAR  ", command=lambda: cerrar_inicio(root,lista_participantes))
    boton_jugar.config(font=("Curlz MT", 14))
    lienzo.create_window(500, 435, window=boton_jugar)

    boton_añadir = Button(lienzo, text="  AÑADIR  ", command=lambda: agregar_participante(lista_participantes, var_nombre, var_contraseña,entrada_participantes))
    boton_añadir.config(font=("Curlz MT", 14))
    lienzo.create_window(500, 250, window=boton_añadir)

    boton_config = Button(lienzo, text="*Admin", command=lambda:cerrar_inicio_admin(root))
    boton_config.config(font=("Curlz MT", 14))
    lienzo.create_window(30, 435, window=boton_config)

    #------------------------------------------------------------------------------

    boton_ayuda = Button(lienzo, text="¿?", command=lambda: messagebox.showinfo("Memotest Spam", """    Botón REGISTRAR - Registra a los participantes 
    
    Botón JUGAR - Comienza el juego con los participantes ingresados 
    
    Botón AÑADIR - Agrega un participante registrado al juego"""))
    boton_ayuda.config(font=("Curlz MT", 14))
    lienzo.create_window(980, 435, window=boton_ayuda)

    #----------------------------------karen--------------------------------------------
    
    lienzo.create_text(780, 180, text="Participantes", font=("Curlz MT", 20))
    
    lienzo.create_rectangle(600,160,960,400,outline="Black",width = 2)
    
    lienzo_2 = Canvas(root,width = 250, height = 100,)
    lienzo.create_window(780, 300,height= 150, window = lienzo_2)
    
    
    entrada_participantes = Listbox(lienzo_2,height= 5,font=("Curlz MT", 14), listvariable = var_participantes )
    entrada_participantes.grid(row=0,column=0,sticky="e",padx=10,pady= 5 )
    
    barra_scroll = Scrollbar(lienzo_2, command = entrada_participantes.yview,width=20)
    barra_scroll.grid(row=0,column=1,sticky="e",padx=5)
    
    entrada_participantes.config(yscrollcommand=barra_scroll)
    
    lista_de_participantes(entrada_participantes,lista_participantes)
    
    #------------------------------------------------------------------------------
    root.mainloop()

    return lista_participantes