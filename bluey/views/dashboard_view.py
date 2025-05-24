import customtkinter as ctk

from ..controllers.cursos_controller import *

class DashboardView(ctk.CTkFrame):
    def __init__(self, master=None, user=None):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        self.user = user

        if master is not None:
            self.master = master
            self.master.title("Dashboard")
            self.master.geometry("800x600")
            self.master.configure(theme="light")  # Cambia el tema a oscuro
            self.master.resizable(True, True)

        
        # label = ctk.CTkLabel(self, text=f"¡Bienvenido, {self.user['nombre']}!", font=("Arial", 24))
        # label.pack(pady=20)

        self.configure(fg_color="#23272D")


        rol = ctk.CTkLabel(self, text=f"Administrador: {self.user['nombre']}!" , font=("Arial", 24))
        rol.configure(fg_color="#E4E2E2", width=80, height=40, text_color="#000")
        rol.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        
        menu_lateral = ctk.CTkFrame(self)
        menu_lateral.configure(fg_color="#EDECEC")
        menu_lateral.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
        # frame.place(x=194, y=114)

        cursos = ctk.CTkButton(menu_lateral, text="Cursos")
        cursos.configure(fg_color="#029CFF", width=80, height=40, text_color="#fff", border_color="#000", command=self.show_cursos)
        cursos.pack()

        alumnos = ctk.CTkButton(menu_lateral, text="Alumnos")
        alumnos.configure(fg_color="#029CFF", width=80, height=40, text_color="#fff", border_color="#000", command=self.show_alumnos)
        alumnos.pack()

        profesores = ctk.CTkButton(menu_lateral, text="Profesores")
        profesores.configure(fg_color="#029CFF", width=80, height=40, text_color="#fff", border_color="#000", command=self.show_profesores)
        profesores.pack()


        self.areaTrabajo = ctk.CTkFrame(self)
        self.areaTrabajo.configure(fg_color="#FFF999")
        self.areaTrabajo.grid(row=2, column=1, padx=10, pady=20, sticky="nsew")

        self.titulo = ctk.CTkLabel(self.areaTrabajo, text="Mis Cursos", font=("Arial", 24), text_color="#000000")
        self.titulo.pack()

        self.show_cursos()

        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure(2, weight=1)

    
    def show_cursos(self):
        self.titulo.configure(text="Mis Cursos")
        # Limpiar widgets previos excepto el título
        for widget in self.areaTrabajo.winfo_children():
            if widget != self.titulo:
                widget.destroy()

        cursos = obtener_cursos()

        for index, curso in enumerate(cursos):
            ctk.CTkLabel(
                self.areaTrabajo,
                text=curso['nombre_curso'],
                font=("Arial", 16),
                text_color="#000000"
            ).pack(anchor="w", fill="x", padx=10, pady=(10 if index == 0 else 2, 0))
            ctk.CTkLabel(
                self.areaTrabajo,
                text=curso['descripcion'],
                font=("Arial", 12),
                text_color="#000000"
            ).pack(anchor="w", fill="x", padx=20, pady=(0, 10))




        # Aquí puedes implementar la lógica para mostrar los cursos
        print(cursos)

    def show_alumnos(self):
        self.titulo.configure(text="Alumos")
        # Aquí puedes implementar la lógica para mostrar los alumnos

        # Limpiar widgets previos excepto el título
        for widget in self.areaTrabajo.winfo_children():
            if widget != self.titulo:
                widget.destroy()

        print("alumnos")

    def show_profesores(self):
        self.titulo.configure(text="Profesores")

        # Limpiar widgets previos excepto el título
        for widget in self.areaTrabajo.winfo_children():
            if widget != self.titulo:
                widget.destroy()
        # Aquí puedes implementar la lógica para mostrar los profesores
        print("Profesores")