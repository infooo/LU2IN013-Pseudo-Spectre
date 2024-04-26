import tkinter as tk
import ttkbootstrap as ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import GRID 

# fonctions utilisees tout au long du code pour le GUI
def getMat():
    global n
    n = dimension_val.get()
    global A 
    A = GRID.creerMat(n)

def getEps():
    global epsilon
    epsilon = float(imprecision_val.get())

def getNbPoints():
    global nbPoints
    nbPoints = nbPoints_val.get()

def getTolContour():
    global tolContour
    tolContour = float(tolContour_val.get())

def getPas():
    global pas
    pas = float(pas_val.get())

def GridMethod():
    ax.clear()
    GRID.affichage(n, A, epsilon, nbPoints)
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

pres_label = ttk.Label(window, text = "Ci-dessous vous sont mises à disposition les différentes méthodes que l'on utilise afin d'étudier le pseudo-spectre, accompagnées d'une interface graphique permettant de visualiser nos approches.", font = ("Arial", 12))
pres_label.pack()

# arguments - deuxieme approche (fenetre 0)
tab0 = ttk.Frame(notebook)

label00 = ttk.Label(tab0, text = "Entrez les valeurs que vous souhaitez en veillant à cliquer (re-cliquer) sur OK après l'insertion (la modification).", font = ("Arial", 12))
label00.grid(row = 0, column = 0, sticky = tk.W)

label01 = ttk.Label(tab0, text = 'Entrez la taille souhaitée de la matrice:', font = ("Arial", 12))
label01.grid(row = 1, column = 0, sticky = tk.W)

dimension_val = tk.IntVar() 
dimension = ttk.Entry(tab0, textvariable = dimension_val)
dimension.grid(row = 1, column = 0, sticky = tk.W, padx = (280, 0))

button01 = ttk.Button(tab0, text='OK', command = getMat)
button01.grid(row = 1, column = 0, sticky = tk.W, padx = (455, 0))

label02 = ttk.Label(tab0, text = "Entrez l'imprécision souhaitée epsilon:", font = ("Arial", 12))
label02.grid(row = 2, column = 0, sticky = tk.W)

imprecision_val = tk.StringVar() 
imprecision = ttk.Entry(tab0, textvariable = imprecision_val)
imprecision.grid(row = 2, column = 0, sticky = tk.W, padx = (280, 0))

button02 = ttk.Button(tab0, text='OK', command = getEps)
button02.grid(row = 2, column = 0, sticky = tk.W, padx = (455, 0))

label03 = ttk.Label(tab0, text = "(GRID) Entrez le nombre souhaité de points:", font = ("Arial", 12))
label03.grid(row = 3, column = 0, sticky = tk.W)

nbPoints_val = tk.IntVar() 
nbPoints = ttk.Entry(tab0, textvariable = nbPoints_val)
nbPoints.grid(row = 3, column = 0, sticky = tk.W, padx = (320, 0))

button03 = ttk.Button(tab0, text = 'OK', command = getNbPoints)
button03.grid(row = 3, column = 0, sticky = tk.W, padx = (495, 0))

label04 = ttk.Label(tab0, text = "(Prédiction-correction) Entrez la tolérance de fin souhaitée pour le contour:", font = ("Arial", 12))
label04.grid(row = 4, column = 0, sticky = tk.W)

tolContour_val = tk.StringVar() 
tolContour = ttk.Entry(tab0, textvariable = tolContour_val)
tolContour.grid(row = 4, column = 0, sticky = tk.W, padx = (535, 0))

button04 = ttk.Button(tab0, text = 'OK', command = getTolContour)
button04.grid(row = 4, column = 0, sticky = tk.W, padx = (710, 0))

label05 = ttk.Label(tab0, text = "(Prédiction-correction) Entrez le pas souhaité pour le contour:", font = ("Arial", 12))
label05.grid(row = 5, column = 0, sticky = tk.W)

pas_val = tk.StringVar() 
pas = ttk.Entry(tab0, textvariable = pas_val)
pas.grid(row = 5, column = 0, sticky = tk.W, padx = (440, 0))

button05 = ttk.Button(tab0, text = 'OK', command = getPas)
button05.grid(row = 5, column = 0, sticky = tk.W, padx = (615, 0))

# arguments - premiere approche (fenetre 1)
tab1 = ttk.Frame(notebook)

button11 = ttk.Button(tab1, text = 'Afficher', command = GridMethod)
button11.grid(row = 0, column = 0, sticky = tk.N, padx = (100, 0))

canvas = FigureCanvasTkAgg(fig, tab1)
canvas.get_tk_widget().grid(row = 1, column = 0, padx = (75, 0))

toolbar = NavigationToolbar2Tk(canvas, tab1, pack_toolbar = False)
toolbar.update()
toolbar.grid(row = 2, column = 0, padx = (75, 0))

# arguments - deuxieme approche (fenetre 2)
tab2 = ttk.Frame(notebook)


# menu & notebook - ajouts des differentes fenetres 
window.configure(menu = menu)

notebook.add(tab0, text = 'Valeurs')
notebook.add(tab1, text = 'GRID')
notebook.add(tab2, text = 'Prédiction-correction')
notebook.pack(pady = 15)

# run
window.mainloop()