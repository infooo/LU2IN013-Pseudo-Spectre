import tkinter as tk
import ttkbootstrap as ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import first_approach 

def firstFunc():
    ax.clear()
    n = dimension_val.get()
    epsilon = float(imprecision_val.get())
    first_approach.affichage(n, epsilon)

    canvas.draw()

# fenetre
window = ttk.Window(themename = 'darkly')
fig, ax = plt.subplots()

# attributs de la fenetre 
window.title('Projet LU2IN013')
window.geometry('1280x960')
window.resizable(height = False, width = False)

# textes
title_label = ttk.Label(window, text = "Interface graphique du projet d'Akram et Ron", font = '48')
title_label.pack()

# menu & notebook
menu = tk.Menu(window)
file_interface_menu = tk.Menu(menu, tearoff = False)
file_interface_menu.add_command(label = 'Default theme', command = lambda: ttk.Style().theme_use('clam'))
file_interface_menu.add_command(label = 'Dark theme', command = lambda: ttk.Style().theme_use('darkly'))
menu.add_cascade(label = 'Interface', font = '16', menu = file_interface_menu)

notebook = ttk.Notebook(window)

# arguments - premiere approche (fenetre 1)
tab1 = ttk.Frame(notebook)

label1 = ttk.Label(tab1, text = 'Entrez la dimension souhaitee:')
label1.pack()

dimension_val = tk.IntVar() 
dimension = ttk.Entry(tab1, textvariable = dimension_val)
dimension.pack()

label2 = ttk.Label(tab1, text = "Entrez l'imprecision epsilon souhaitee:")
label2.pack()

imprecision_val = tk.StringVar() 
imprecision = ttk.Entry(tab1, textvariable = imprecision_val)
imprecision.pack()

button1 = ttk.Button(tab1, text = 'Confirmer', command = firstFunc)
button1.pack()

canvas = FigureCanvasTkAgg(fig, tab1)
canvas.get_tk_widget().pack()

toolbar = NavigationToolbar2Tk(canvas, tab1, pack_toolbar = False)
toolbar.update()
toolbar.pack()

# arguments - deuxieme approche (fenetre 2)
tab2 = ttk.Frame(notebook)

# arguments - deuxieme approche (fenetre 3)
tab3 = ttk.Frame(notebook)

# menu & notebook - ajouts des differentes fenetres 
window.configure(menu = menu)

notebook.add(tab1, text = 'Premiere approche')
notebook.add(tab2, text = 'Deuxieme approche')
notebook.add(tab3, text = 'Troisieme approche')
notebook.pack(pady = 10)

# run
window.mainloop()