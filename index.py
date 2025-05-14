import customtkinter as ctk
from tkinter import messagebox

# Configuration de l'apparence
ctk.set_appearance_mode("system")  # Thème : "light", "dark" ou "system"
ctk.set_default_color_theme("green")  # Couleur : "blue", "dark-blue", etc.

class LoginApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre
        self.title("Connexion")
        self.geometry("400x500")
        self.resizable(False, False)

        # Logo (remplacez par votre image si besoin)
        self.logo = ctk.CTkLabel(
            self, 
            text="Mon App", 
            font=("Arial", 24, "bold")
        )
        self.logo.pack(pady=30)

        # Frame principale
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Champ "Nom d'utilisateur"
        self.label_username = ctk.CTkLabel(
            self.frame, 
            text="Nom d'utilisateur",
            font=("Arial", 12)
        )
        self.label_username.pack(pady=(10, 5))

        self.entry_username = ctk.CTkEntry(
            self.frame, 
            placeholder_text="Entrez votre nom d'utilisateur",
            width=200
        )
        self.entry_username.pack(pady=5)

        # Champ "Mot de passe"
        self.label_password = ctk.CTkLabel(
            self.frame, 
            text="Mot de passe",
            font=("Arial", 12)
        )
        self.label_password.pack(pady=(10, 5))

        self.entry_password = ctk.CTkEntry(
            self.frame, 
            placeholder_text="Entrez votre mot de passe",
            width=200,
            show="*"  # Masquer le mot de passe
        )
        self.entry_password.pack(pady=5)

        # Case à cocher "Se souvenir de moi"
        self.checkbox = ctk.CTkCheckBox(
            self.frame, 
            text="Se souvenir de moi"
        )
        self.checkbox.pack(pady=10)

        # Bouton de connexion
        self.button_login = ctk.CTkButton(
            self.frame, 
            text="Connexion", 
            command=self.verify_login,
            fg_color="#2E8B57",  # Couleur personnalisée
            hover_color="#3CB371"
        )
        self.button_login.pack(pady=20)

        # Lien "Mot de passe oublié ?"
        self.link_forgot = ctk.CTkLabel(
            self.frame, 
            text="Mot de passe oublié ?",
            font=("Arial", 10, "underline"),
            cursor="hand2"  # Curseur en forme de main
        )
        self.link_forgot.pack()
        self.link_forgot.bind("<Button-1>", lambda e: messagebox.showinfo("Info", "Fonctionnalité à implémenter"))

    # Fonction de vérification du login
    def verify_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if not username or not password:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs !")
        elif username == "admin" and password == "1234":  # Exemple simple
            messagebox.showinfo("Succès", f"Bienvenue, {username} !")
            self.destroy()  # Ferme la fenêtre de login
            # Ouvrir une nouvelle fenêtre ici (ex: MainApp())
        else:
            messagebox.showerror("Erreur", "Identifiants incorrects")

# Lancer l'application
if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()