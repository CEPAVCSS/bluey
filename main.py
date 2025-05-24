import customtkinter as ctk
from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkEntry
from customtkinter import CTkImage
from PIL import Image

from bluey.views import login_view as lv
# from bluey.assets.img import img_path

class main():
    def __init__(self):
        # Create the main window
        self.root = ctk.CTk()

        # Dimensiones de la ventana
        window_width = 350
        window_height = 450


        self.root.geometry(f"{window_width}x{window_height}")
        self.root.title("Bluey")

        # Obtener dimensiones de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcular posición para centrar la ventana
        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)

        # Establecer la posición de la ventana
        self.root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")


        img = Image.open("bluey/assets/img/bluey.png")
        imagen = None 

        try:
            img = Image.open("bluey/assets/img/bluey.png")
            img = img.resize((100, 100), Image.Resampling.LANCZOS)
            imagen = CTkImage(img, size=(100, 100))
            self.logo = imagen
        except Exception as e:
            print(f"Error: No se encontró la imagen en la ruta: {e}")
            imagen = None
            self.logo = None

        # image_label = CTkLabel(self.root, image=imagen, text="Bluey", text_font=("Arial", 20, "bold"), text_color="white")
        # image_label.pack(pady=20)

        # Import a frame for the login view
        self.login_frame = lv.LoginView(self.root)


    def run(self):
        # Start the main loop
        self.root.mainloop()

if __name__ == "__main__":
    app = main()
    app.run()