import tkinter as tk
import ttkbootstrap as ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import First_approach 

# fonctions utilisees tout au long du code pour le GUI
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

def quitApp():
    window.quit()

# fenetre
window = ttk.Window(themename = 'darkly')
fig, ax = plt.subplots()

# attributs de la fenetre 
window.title('Projet LU2IN013')
window.geometry('1280x960')
window.resizable(height = False, width = False)

# menu & notebook
menu = tk.Menu(window)

file_programme_menu = tk.Menu(menu, tearoff = False)
file_programme_menu.add_command(label = 'Quitter', command = quitApp)
file_interface_menu = tk.Menu(menu, tearoff = False)
file_interface_menu.add_command(label = 'Theme de base', command = lambda: ttk.Style().theme_use('clam'))
file_interface_menu.add_command(label = 'Theme sombre', command = lambda: ttk.Style().theme_use('darkly'))

menu.add_cascade(label = 'Programme', font = ("Arial", 11), menu = file_programme_menu)
menu.add_cascade(label = 'Interface', font = ("Arial", 11), menu = file_interface_menu)

notebook = ttk.Notebook(window)

# textes
title_label = ttk.Label(window, text = "Interface graphique du projet d'Akram et Ron", font = ("Arial", 22))
title_label.pack()

pres_label = ttk.Label(window, text = "Ci-dessous vous sont mises à disposition les différentes méthodes que l'on utilise afin de calculer les éléments du pseudo-spectre, accompagnées d'une interface graphique permettant de visualiser nos approches.", font = ("Arial", 12))

# arguments - premiere approche (fenetre 1)
tab1 = ttk.Frame(notebook)

label1 = ttk.Label(tab1, text = 'Entrez la taille souhaitée de la matrice:', font = ("Arial", 12))
label1.grid(row = 0, column = 0, sticky = tk.W)

dimension_val = tk.IntVar() 
dimension = ttk.Entry(tab1, textvariable = dimension_val)
dimension.grid(row = 0, column = 1, sticky = tk.W)

button1 = ttk.Button(tab1, text='OK', command = getMat)
button1.grid(row = 0, column = 1, sticky = tk.W, padx = (175, 0))

label2 = ttk.Label(tab1, text = "Entrez l'imprécision epsilon souhaitée:", font = ("Arial", 12))
label2.grid(row = 1, column = 0, sticky = tk.W)

imprecision_val = tk.StringVar() 
imprecision = ttk.Entry(tab1, textvariable = imprecision_val)
imprecision.grid(row = 1, column = 1, sticky = tk.W)

button2 = ttk.Button(tab1, text='OK', command = getEps)
button2.grid(row = 1, column = 1, sticky = tk.W, padx = (175, 0))

label3 = ttk.Label(tab1, text = "Entrez le nombre souhaité de points:", font = ("Arial", 12))
label3.grid(row = 2, column = 0, sticky = tk.W)

nbPoints_val = tk.IntVar() 
nbPoints = ttk.Entry(tab1, textvariable = nbPoints_val)
nbPoints.grid(row = 2, column = 1, sticky = tk.W)

button3 = ttk.Button(tab1, text = 'OK', command = getNbPoints)
button3.grid(row = 2, column = 1, sticky = tk.W, padx = (175, 0))

button4 = ttk.Button(tab1, text = 'Afficher', command = Affichage)
button4.grid(row = 3, column = 0, sticky = tk.W)

canvas = FigureCanvasTkAgg(fig, tab1)
canvas.get_tk_widget().grid(row = 4, column = 1, padx = (0, 175))

toolbar = NavigationToolbar2Tk(canvas, tab1, pack_toolbar = False)
toolbar.update()
toolbar.grid(row = 5, column = 1, padx = (0, 175))

# arguments - deuxieme approche (fenetre 2)
tab2 = ttk.Frame(notebook)

# arguments - deuxieme approche (fenetre 3)
tab3 = ttk.Frame(notebook)

# menu & notebook - ajouts des differentes fenetres 
window.configure(menu = menu)

notebook.add(tab1, text = 'Premiere approche')
notebook.add(tab2, text = 'Deuxieme approche')
notebook.add(tab3, text = 'Troisieme approche')
notebook.pack(pady = 15)

# run
window.mainloop()