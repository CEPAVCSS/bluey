import customtkinter as ctk

from ..controllers.login_controller import validate_login
from .dashboard_view import DashboardView

class LoginView(ctk.CTkFrame):
    # pass
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True)
        self.create_widgets() 
        

    def create_widgets(self):
        # Título
        self.title_label = ctk.CTkLabel(self, text="Bluey Login", font=("Arial", 24))
        self.title_label.pack(pady=10)

        # Usuario
        self.username_label = ctk.CTkLabel(self, text="Usuario")
        self.username_label.pack(pady=5)
        self.username_entry = ctk.CTkEntry(self)
        self.username_entry.pack(pady=5)

        # Contraseña
        self.password_label = ctk.CTkLabel(self, text="Contraseña")
        self.password_label.pack(pady=5)
        self.password_entry = ctk.CTkEntry(self, show="*")
        self.password_entry.pack(pady=5)

        # Botón login
        self.submit_button = ctk.CTkButton(self, text="Login", command=self.submit_login)
        self.submit_button.pack(pady=20)

        # Label para mostrar mensajes
        self.message_label = ctk.CTkLabel(self, text="")
        self.message_label.pack(pady=5)

    def submit_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        is_valid, role, user = validate_login(username, password)
        self.user = user 
        # print(f"Username: {username}, Password: {password}")

        if is_valid:
            self.message_label.configure(text= f"¡Login exitoso! {role} ", text_color="green")
            self.after(1000, self.show_dashboard(user) ) # Espera 1 segundo antes de mostrar el dashboard
        else:
            self.message_label.configure(text="Credenciales inválidas. Intenta de nuevo.", text_color="red")


    def show_dashboard(self, user):
        self.pack_forget()  # Oculta el login
        self.destroy()      # Destruye el frame de login
        self.master.geometry("800x600")  # Cambia el tamaño de la ventana
        

        rol = self.user['rol_id']
        
        if rol == 1:
            self.master.title("Bluey - Administrador")
            DashboardView(self.master, user) 
        elif rol == 2:
            self.master.title("Bluey - Alumno")
            
        elif rol == 3:
            self.master.title("Bluey - Profesor")
        
        