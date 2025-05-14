from tkinter import messagebox
import customtkinter as ctk

ctk.set_appearance_mode("system")

#variables
current_page = None
active_button = None

def main_window():
    root = ctk.CTk()
    root.geometry(f"1000x600")
    root.title("Gestion de Stock")
    root.resizable(False,False)
    Navigation(root)
    acceuil_stat(root)

    root.mainloop()

def Navigation(root):

    title_frame = ctk.CTkFrame(root)

    title_label = ctk.CTkLabel(
        title_frame, text="Shoes and Co",
        font=("Gabriola", 35 ,"bold")
    )

    title_frame.pack(side="left")
    title_frame.pack_propagate(False)
    title_frame.configure(width=250, height=600)
    title_label.pack(pady = 10)
    btn_navigation(title_frame, root)

def btn_navigation(title_frame, root):
    frame_color = title_frame.cget("fg_color")
    window_color = root.cget("fg_color")

    btn_acceuil = ctk.CTkButton(
        title_frame, 
        text="Acceuil",
        font=("Arial", 20),
        fg_color=frame_color,
        hover_color=window_color
    )
    btn_acceuil.pack()
    btn_acceuil.pack_propagate(False)
    btn_acceuil.configure(width=250, height=50)

    btn_article = ctk.CTkButton(
        title_frame, 
        text="Articles",
        font=("Arial", 20),
        fg_color=frame_color,
        hover_color=window_color
    )
    btn_article.pack()
    btn_article.pack_propagate(False)
    btn_article.configure(width=250, height=50)

    btn_etat = ctk.CTkButton(
        title_frame, 
        text="Etat de Stock",
        font=("Arial", 20),
        fg_color=frame_color,
        hover_color=window_color
    )
    btn_etat.pack()
    btn_etat.pack_propagate(False)
    btn_etat.configure(width=250, height=50)

    btn_stat = ctk.CTkButton(
        title_frame, 
        text="Statistiques",
        font=("Arial", 20),
        fg_color=frame_color,
        hover_color=window_color
    )
    btn_stat.pack()
    btn_stat.pack_propagate(False)
    btn_stat.configure(width=250, height=50)

    btn_histo = ctk.CTkButton(
        title_frame, 
        command=afficher,
        text="Historique",
        font=("Arial", 20),
        fg_color=frame_color,
        hover_color=window_color
    )
    btn_histo.pack()
    btn_histo.pack_propagate(False)
    btn_histo.configure(width=250, height=50)

def acceuil_stat(root):
    window_color = root.cget("fg_color")
    
    stat_frame = ctk.CTkFrame(root, fg_color= window_color)
    stat_frame.pack(pady=20)
    stat_frame.pack_propagate(False)
    stat_frame.configure(width=700, height=190)

    stock_stat = ctk.CTkFrame(stat_frame)
    stock_stat.grid(column=0,row=0,padx=9)
    stock_stat.configure(height=190)

    article_stat = ctk.CTkFrame(stat_frame)
    article_stat.grid(column=1,row=0, padx=7)
    article_stat.configure(height=190, width=485)

    histo_frame = ctk.CTkFrame(root)
    histo_frame.pack()
    histo_frame.pack_propagate(False)
    histo_frame.configure(width=700, height=350)

    histo_label = ctk.CTkLabel(
        histo_frame,
        text="historique"
    )
    histo_label.pack()
#     statistic(stock_stat)
def afficher():
    print("histo")
# def statistic(stock_stat):


# main_window()