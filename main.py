import tkinter as tk
from tkinter import ttk
from functools import partial

import switch as switch
from sklearn.feature_extraction import DictVectorizer

from terrain_classifier import *
import csv
import marketplace

window = tk.Tk()
window.geometry("600x450")
window.title("Form")
window.resizable(False, False)
window.configure(background="#67BD66")


def send_info(listTerrain, listMq):
    # per cancellare la scritta precedente
    text = "                                   "
    aux = False
    text_output = tk.Label(window, text=text, fg="#67BD66", bg="#67BD66", font=("Times New Roman", 16)
                           ).place(x=250, y=350)
    inputDim = float(textDim.get("1.0", "end-1c"))
    if inputDim < 0:
        aux = True
    inputPh = float(textPh.get("1.0", "end-1c"))
    if inputPh < 0 or inputPh > 14:
        aux = True
    inputPrec = float(textPrec.get("1.0", "end-1c"))
    if inputPrec < 0:
        aux = True
    inputUmi = float(textUmidita.get("1.0", "end-1c"))
    if inputUmi < 0:  #
        aux = True
    inputTemp = float(textTemp.get("1.0", "end-1c"))
    if inputTemp < 0:
        aux = True
    inputN = float(textN.get("1.0", "end-1c"))
    if inputN < 0:
        aux = True
    inputP = float(textP.get("1.0", "end-1c"))
    if inputP < 0:
        aux = True
    inputK = float(textK.get("1.0", "end-1c"))
    if inputK < 0:
        aux = True
    if aux:
        text = "Dati Errati"
    else:
        text = "Dati Inviati"

    text_output = tk.Label(window, text=text, fg="green", font=("Times New Roman", 16)).place(x=250, y=350)
    if aux == False:
        listTerrain.append(int(inputN))
        listTerrain.append(int(inputP))
        listTerrain.append(int(inputK))
        listTerrain.append(inputTemp)
        listTerrain.append(inputUmi)
        listTerrain.append(inputPh)
        listTerrain.append(inputPrec)
        listMq.append(inputDim)
    #textDim.delete("1.0", "end")
    #textPh.delete("1.0", "end")
    #textUmidita.delete("1.0", "end")
    #textPrec.delete("1.0", "end")
    #textTemp.delete("1.0", "end")
    #textN.delete("1.0", "end")
    #textP.delete("1.0", "end")
    #textK.delete("1.0", "end")


title = tk.Label(text="Inserimento Dati Terreno", fg="#282828", bg="#67BD66", font=("Georgia", 20)).place(x=160, y=0)

# dimensioni
labelDim = tk.Label(text="Dimensioni ", fg="#282828", bg="#67BD66", font=("Georgia", 14)).place(x=150, y=50)
textDim = tk.Text(width=12, height=1, font=14)
textDim.place(x=300, y=55)
labelDim = tk.Label(text="m²", fg="#282828", bg="#67BD66", font=("Georgia", 8)).place(x=415, y=58)
# Ph terreno
labelPh = tk.Label(text="Ph Terreno", fg="#282828", bg="#67BD66", font=("Georgia", 14)).place(x=150, y=80)
textPh = tk.Text(width=12, height=1, font=14)
textPh.place(x=300, y=85)
labelPh = tk.Label(text="da 0 a 14", fg="#282828", bg="#67BD66", font=("Georgia", 8)).place(x=415, y=88)
# Precipitazioni
labelPrec = tk.Label(text="Precipitazioni", fg="#282828", bg="#67BD66", font=("Georgia", 14)).place(x=150, y=110)
textPrec = tk.Text(width=12, height=1, font=14)
textPrec.place(x=300, y=115)
labelPrec = tk.Label(text="mm", fg="#282828", bg="#67BD66", font=("Georgia", 8)).place(x=415, y=118)
# Umidità
labelUmidita = tk.Label(text="Umidità", fg="#282828", bg="#67BD66", font=("Georgia", 14)).place(x=150, y=140)
textUmidita = tk.Text(width=12, height=1, font=14)
textUmidita.place(x=300, y=145)
labelUmidita = tk.Label(text="%", fg="#282828", bg="#67BD66", font=("Georgia", 8)).place(x=415, y=148)
# Temperatura
labelTemp = tk.Label(text="Temperatura", fg="#282828", bg="#67BD66", font=("Georgia", 14)).place(x=150, y=170)
textTemp = tk.Text(width=12, height=1, font=14)
textTemp.place(x=300, y=175)
labelTemp = tk.Label(text="°C", fg="#282828", bg="#67BD66", font=("Georgia", 8)).place(x=415, y=178)
# Azoto
labelN = tk.Label(text="Azoto", fg="#282828", bg="#67BD66", font=("Georgia", 14)).place(x=150, y=200)
textN = tk.Text(width=8, height=1, font=10)
textN.place(x=150, y=230)
labelN = tk.Label(text="mg/Kg", fg="#282828", bg="#67BD66", font=("Georgia", 8)).place(x=150, y=252)
# Fosforo
labelP = tk.Label(text="Fosforo", fg="#282828", bg="#67BD66", font=("Georgia", 14)).place(x=260, y=200)
textP = tk.Text(width=8, height=1, font=10)
textP.place(x=260, y=230)
labelP = tk.Label(text="mg/Kg", fg="#282828", bg="#67BD66", font=("Georgia", 8)).place(x=260, y=252)
# Potassio
labelK = tk.Label(text="Potassio", fg="#282828", bg="#67BD66", font=("Georgia", 14)).place(x=370, y=200)
textK = tk.Text(width=8, height=1, font=14)
textK.place(x=370, y=230)
labelK = tk.Label(text="mg/Kg", fg="#282828", bg="#67BD66", font=("Georgia", 8)).place(x=370, y=252)

listTerrain = []
listMq = []

info_button = tk.Button(text="Invia dati", fg="#282828", bg="#7EA87E", font="Georgia",
                        width=61, command=partial(send_info, listTerrain, listMq)).place(x=20, y=300)


if __name__ == '__main__':
    window.mainloop()
    h = int(len(listTerrain) / 7)
    w = 7
    m = [[0 for x in range(w)] for y in range(h)]
    j, y, k = 0, 0, 0
    for x in listTerrain:
        if y < 7:
            m[j][y] = listTerrain[k]
            y += 1
        else:
            j += 1
            y = 0
            m[j][y] = listTerrain[k]
            y += 1
        k += 1

    plantPredict = clf.predict(m)
    dictPlant = {'plant': []}
    k = 0
    for x in plantPredict:
        if plantPredict[k] in dictPlant:
            dictPlant[plantPredict[k]] = dictPlant.get(plantPredict[k]) + listMq[k]
        else:
            dictPlant[plantPredict[k]] = listMq[k]
        k += 1
    dictPlant.pop('plant')

    # pop up colture selezionate
    popUp = tk.Tk()
    popUp.geometry("600x450")
    popUp.title("Colture inserite")
    popUp.resizable(False, False)
    popUp.configure(background="#67BD66")
    title = tk.Label(text="Colture inserite", fg="#282828", bg="#67BD66",
                     font=("Georgia", 20)).place(x=160, y=0)
    j = 150
    k = 50
    j = 0
    for x, y in dictPlant.items():
        if j == 0:
            labelDim = tk.Label(text=x + ":", fg="#282828", bg="#67BD66", font=("Georgia", 14)).place(x=j, y=50)
            textDim = tk.Label(text=y, fg="#282828", bg="#67BD66", font=("Georgia", 14)).place(x=j+150, y=50)
        elif j == 1:
            labelDim = tk.Label(text=x + ":", fg="#282828", bg="#67BD66", font=("Georgia", 14)).place(x=j, y=80)
            textDim = tk.Label(text=y, fg="#282828", bg="#67BD66", font=("Georgia", 14)).place(x=j + 150, y=80)
        elif j == 2:
            labelDim = tk.Label(text=x + ":", fg="#282828", bg="#67BD66", font=("Georgia", 14)).place(x=j, y=110)
            textDim = tk.Label(text=y, fg="#282828", bg="#67BD66", font=("Georgia", 14)).place(x=j + 150, y=110)
        elif j == 3:
            labelDim = tk.Label(text=x + ":", fg="#282828", bg="#67BD66", font=("Georgia", 14)).place(x=j, y=140)
            textDim = tk.Label(text=y, fg="#282828", bg="#67BD66", font=("Georgia", 14)).place(x=j + 150, y=140)
        elif j == 4:
            labelDim = tk.Label(text=x + ":", fg="#282828", bg="#67BD66", font=("Georgia", 14)).place(x=j, y=170)
            textDim = tk.Label(text=y, fg="#282828", bg="#67BD66", font=("Georgia", 14)).place(x=j + 150, y=170)
        j += 1
    popUp.mainloop()
    marketplace.gen_kinds(dictPlant)
    marketplace.gen_Bags()
    print("Colture disponibili sul mercato: ")
    print("{:<12} {:<20} {:<10} {:<10}".format('Varietà','Incassi previsti','Costi', 'Area coltivata in mq'))
    for b in marketplace.bags:
        print("{:<12} {:<20} {:<10} {:<10}".format(b.id, b.value, b.weight, b.mq))
    budget = input("Inserire un budget: ")
    print("Incassi previsti: ")
    print(marketplace.knapsack(marketplace.bags, int(budget), dictPlant))