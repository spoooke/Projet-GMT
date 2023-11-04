import pytz
from datetime import datetime
import tkinter as tk
from tkinter import ttk

def convert_time():
    city1 = city1_var.get()
    city2 = city2_var.get()

    timezone1 = pytz.timezone(city1)
    timezone2 = pytz.timezone(city2)

    current_time = datetime.now()
    current_time_start = timezone1.localize(current_time)
    current_time_end = current_time_start.astimezone(timezone2)
    
    result_label.config(text=f"Heure à {city1}: {current_time_start.strftime('%Y-%m-%d %H:%M:%S')}\nHeure à {city2}: {current_time_end.strftime('%Y-%m-%d %H:%M:%S')}", foreground="green")

root = tk.Tk()
root.title("Convertisseur d'Heures")
root.geometry("600x900")  # Taille de la fenêtre
root.configure(bg="light gray")  # Couleur de fond

# Liste de noms de fuseaux horaires UTC
utc_timezones = [
    "Etc/GMT-12",
    "Etc/GMT-11",
    "Etc/GMT-10",
    "Etc/GMT-9",
    "Etc/GMT-8",
    "Etc/GMT-7",
    "Etc/GMT-6",
    "Etc/GMT-5",
    "Etc/GMT-4",
    "Etc/GMT-3",
    "Etc/GMT-2",
    "Etc/GMT-1",
    "Etc/GMT",
    "Etc/GMT+1",
    "Etc/GMT+2",
    "Etc/GMT+3",
    "Etc/GMT+4",
    "Etc/GMT+5",
    "Etc/GMT+6",
    "Etc/GMT+7",
    "Etc/GMT+8",
    "Etc/GMT+9",
    "Etc/GMT+10",
    "Etc/GMT+11",
    "Etc/GMT+12",
]

# Creer un conteneur pour le contenu principal
main_frame = ttk.Frame(root, style="Main.TFrame")
main_frame.pack(fill=tk.BOTH, expand=True)

# Ajouter un titre
title_label = ttk.Label(main_frame, text="Convertisseur d'Heures", font=("Lucida Grande", 32, "bold"), style="Title.TLabel")
title_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew")

# Ajouter un logo
logo_image = tk.PhotoImage(file="lhorloge.png")
logo_label = ttk.Label(main_frame, image=logo_image, style="Logo.TLabel")
logo_label.grid(row=1, column=0, columnspan=2)

# Creer un cadre pour les listes déroulantes et le bouton
input_frame = ttk.Frame(main_frame, style="Input.TFrame")
input_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Liste déroulante 1
city1_var = tk.StringVar()
# Ajouter l'option 'height' pour augmenter la hauteur de la liste déroulante
city1_combobox = ttk.Combobox(input_frame, textvariable=city1_var, values=utc_timezones, style="Combobox.TCombobox", height=10)
city1_combobox.grid(row=1, column=0, padx=5, pady=5, columnspan=2)
city1_combobox.set(utc_timezones[len(utc_timezones)//2])  # Sélectionnez le fuseau horaire du milieu
city1_combobox.configure(background="light gray")  # Couleur de fond

# Liste déroulante 2
city2_var = tk.StringVar()
# Ajouter l'option 'height' pour augmenter la hauteur de la liste déroulante
city2_combobox = ttk.Combobox(input_frame, textvariable=city2_var, values=utc_timezones, style="Combobox.TCombobox", height=10)
city2_combobox.grid(row=3, column=0, padx=5, pady=5, columnspan=2)
city2_combobox.set(utc_timezones[len(utc_timezones)//2])  # Sélectionnez le fuseau horaire du milieu
city2_combobox.configure(background="light gray")  # Couleur de fond

style = ttk.Style()
style.configure("Round.TButton", relief=tk.RAISED, borderwidth=5, background="green")
convert_button = ttk.Button(input_frame, text="Convertir", command=convert_time, style="Round.TButton")
convert_button.grid(row=4, column=0, columnspan=2, pady=10)

# Résultats
result_frame = ttk.Frame(main_frame, style="ResultFrame.TFrame")
result_frame.grid(row=3, column=0, columnspan=2)

# Ajouter une marge autour du résultat
result_frame.grid(padx=10, pady=10)

result_label = ttk.Label(result_frame, text="", font=("Lucida Grande", 16, "bold"), style="Result.TLabel")
result_label.pack()

# Personnalisation des styles
style = ttk.Style()
style.configure("Main.TFrame", background="light gray")
style.configure("Logo.TLabel", background="light gray")
style.configure("Title.TLabel", foreground="black", background="light gray")
style.configure("Input.TFrame", background="light gray")
style.configure("Label.TLabel", foreground="black", background="light gray")
style.configure("Combobox.TCombobox", foreground="black")
style.configure("Button.TButton", foreground="black", background="green", relief=tk.RAISED)
style.configure("ResultFrame.TFrame", background="light gray")
style.configure("Result.TLabel", foreground="green", background="light gray")

root.mainloop()
