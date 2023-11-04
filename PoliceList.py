import tkinter as tk
from tkinter import font

root = tk.Tk()

# Créez un label avec la police par défaut
label = tk.Label(root, text="Liste des polices disponibles")
label.pack()

# Obtenez la liste des polices disponibles
font_list = font.families()

# Affichez la liste des polices
for font in font_list:
    print(font)

root.mainloop()
