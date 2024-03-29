import tkinter as tk
import ttkbootstrap as ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import First_approach 

def getMat():
    global n
    n = dimension_val.get()
    global A 
    A = First_approach.creerMat(n)

def getEps():
    global epsilon
    epsilon = float(imprecision_val.get())

def getNbPoints():
    global nbPoints
    nbPoints = nbPoints_val.get()

def Affichage():
    ax.clear()

    First_approach.affichage(n, A, epsilon, nbPoints)

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

label1 = ttk.Label(tab1, text = 'Entrez la taille de la matrice souhaitee:')
label1.grid(row = 0, column = 0, sticky = tk.W)

dimension_val = tk.IntVar() 
dimension = ttk.Entry(tab1, textvariable = dimension_val)
dimension.grid(row = 0, column = 1, sticky = tk.W)

button1 = ttk.Button(tab1, text='OK', command = getMat)
button1.grid(row=0, column=2, sticky=tk.W)

label2 = ttk.Label(tab1, text = "Entrez l'imprecision epsilon souhaitee:")
label2.grid(row=1, column=0, sticky=tk.W)

imprecision_val = tk.StringVar() 
imprecision = ttk.Entry(tab1, textvariable = imprecision_val)
imprecision.grid(row=1, column=1, sticky=tk.W)

button2 = ttk.Button(tab1, text='OK', command = getEps)
button2.grid(row=1, column=2, sticky=tk.W)

label3 = ttk.Label(tab1, text = "Entrez le nombre de points souhaite:")
label3.grid(row=2, column=0, sticky=tk.W)

nbPoints_val = tk.IntVar() 
nbPoints = ttk.Entry(tab1, textvariable = nbPoints_val)
nbPoints.grid(row=2, column=1, sticky=tk.W)

button3 = ttk.Button(tab1, text='OK', command = getNbPoints)
button3.grid(row=2, column=2, sticky=tk.W)

button4 = ttk.Button(tab1, text='Afficher', command = Affichage)
button4.grid(row=3, column=1, sticky=tk.W)

canvas = FigureCanvasTkAgg(fig, tab1)
canvas.get_tk_widget().grid(row = 4, column = 1)

toolbar = NavigationToolbar2Tk(canvas, tab1, pack_toolbar = False)
toolbar.update()
toolbar.grid(row = 5, column = 1)

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