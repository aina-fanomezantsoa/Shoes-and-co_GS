import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class InvoiceDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Invoice Statistics Dashboard")
        self.geometry("900x700")
        
        # Données exactes de l'image
        self.data = {
            "Total": 1135,
            "Paid": 234,      # 24% dans l'image
            "Overdue": 514,
            "Unpaid": 345
        }
        
        self.create_widgets()
    
    def create_widgets(self):
        # Frame principale
        main_frame = ctk.CTkFrame(self, fg_color="white")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Titre
        ctk.CTkLabel(main_frame, 
                    text="Invoice Statistics",
                    font=("Arial", 24, "bold"),
                    text_color="#2c3e50").pack(pady=20)
        
        # Diagramme circulaire
        self.create_donut_chart(main_frame)
        
        # Légende
        self.create_legend(main_frame)
    
    def create_donut_chart(self, parent):
        fig, ax = plt.subplots(figsize=(8, 6), dpi=80)
        ax.axis('equal')
        
        # Couleurs exactes comme sur l'image
        colors = ['#4CAF50', '#FFA726', '#EF5350']
        categories = ["Paid", "Overdue", "Unpaid"]
        values = [self.data["Paid"], self.data["Overdue"], self.data["Unpaid"]]
        
        # Création du donut chart
        wedges, _ = ax.pie(
            values,
            colors=colors,
            startangle=90,
            wedgeprops=dict(width=0.4, edgecolor='white'),  # Contrôle l'épaisseur de l'anneau
            pctdistance=0.85  # Position des pourcentages
        )
        
        # Ajout des pourcentages
        total = sum(values)
        for i, wedge in enumerate(wedges):
            angle = (wedge.theta2 - wedge.theta1)/2 + wedge.theta1
            x = 0.85 * np.cos(np.deg2rad(angle))
            y = 0.85 * np.sin(np.deg2rad(angle))
            ax.text(x, y, f'{values[i]/total:.0%}', 
                   ha='center', va='center', 
                   fontsize=12, fontweight='bold')
        
        # Cercle central avec le total
        center_circle = plt.Circle((0, 0), 0.2, color='white')
        ax.add_patch(center_circle)
        ax.text(0, 0, f"{self.data['Total']:,}\nArticles",
               ha='center', va='center',
               fontsize=16, fontweight='bold')
        
        # Style minimaliste
        ax.axis('off')
        
        # Intégration dans CustomTkinter
        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
    
    def create_legend(self, parent):
        legend_frame = ctk.CTkFrame(parent, fg_color="white")
        legend_frame.pack(pady=10)
        
        categories = [
            ("Paid", "#4CAF50", "24%"),
            ("Overdue", "#FFA726", f"{self.data['Overdue']}"),
            ("Unpaid", "#EF5350", f"{self.data['Unpaid']}")
        ]
        
        for text, color, value in categories:
            item_frame = ctk.CTkFrame(legend_frame, fg_color="white")
            item_frame.pack(side="left", padx=20)
            
            # Carré de couleur
            ctk.CTkLabel(item_frame, 
                        text="",
                        width=20,
                        height=20,
                        fg_color=color).pack(side="left", padx=5)
            
            # Texte
            ctk.CTkLabel(item_frame,
                        text=f"{text}: {value}",
                        font=("Arial", 14),
                        text_color="#2c3e50").pack(side="left")

if __name__ == "__main__":
    app = InvoiceDashboard()
    app.mainloop()