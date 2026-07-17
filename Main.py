from tkinter import messagebox
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import simpledialog
import tkinter
import numpy as np
from tkinter import filedialog
import torch
import cv2
import os
import socket
import pickle
import pathlib
from pathlib import Path
pathlib.PosixPath = pathlib.WindowsPath

main = tkinter.Tk()
main.title("Illuminating Autonomy: Federated Learning for Object Detection in Autonomous Vehicles under Low-Light Conditions")
main.geometry("1300x1200")

global filename, model
labels = ['Bus', 'Car', 'Motorbike', 'Person', 'Truck']
CONFIDENCE_THRESHOLD = 0.3
GREEN = (0, 255, 0)

def loadDataset():
    global filename
    text.delete('1.0', END)
    filename = filedialog.askdirectory(initialdir=".") #upload dataset file
    text.insert(END,filename+" loaded\n\n")

def loadModel():
    global filename, model
    text.delete('1.0', END)
    model = torch.hub.load('yolov5', 'custom', path='model/best.pt', force_reload=True,source='local')
    text.insert(END,"Yolov5 Vehicle Object Detection Model Loaded")
    
def updateModel():
    text.delete('1.0', END)
    global model
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 2222))
    with open("model/best.pt", "rb") as file:
        data = file.read()
    file.close()    
    s.sendall(data)
    data = s.recv(100)
    data = data.decode()
    text.insert(END,"Server Response : "+data+"\n\n")
    s.close()

def adjust_gamma(image, gamma=1.0):
   invGamma = 1.0 / gamma
   table = np.array([((i / 255.0) ** invGamma) * 255
      for i in np.arange(0, 256)]).astype("uint8")

   return cv2.LUT(image, table)    

def detectVehicle():
    global model
    filename = filedialog.askopenfilename(initialdir="testImages") #upload dataset file
    img1 = cv2.imread(filename)
    img1 = cv2.resize(img1, (512, 512))
    img = adjust_gamma(img1, gamma=2.0)
    results = model(img1)
    results.xyxy[0]  # im predictions (tensor)
    out = results.pandas().xyxy[0]  # im predictions (pandas)
    print(out)
    if len(out) > 0:
        for i in range(len(out)):
            xmin = int(out['xmin'].ravel()[i])
            ymin = int(out['ymin'].ravel()[i])
            xmax = int(out['xmax'].ravel()[i])
            ymax = int(out['ymax'].ravel()[i])
            name = out['name'].ravel()[i]
            cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (255, 0, 0), 2)
            cv2.putText(img, name, (xmin, ymin-20), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 0), 2)
    cv2.imshow("Illuminate Image",img)
    cv2.imshow("Original Image", img1)
    cv2.waitKey(0)

def graph():
    grp = cv2.imread('model/results.png')
    grp = cv2.resize(grp, (800, 600))
    cv2.imshow("YoloV5 Performance Graph", grp)
    cv2.waitKey(0)
    
font = ('times', 16, 'bold')
title = Label(main, text='Illuminating Autonomy: Federated Learning for Object Detection in Autonomous Vehicles under Low-Light Conditions')
title.config(bg='chocolate', fg='white')  
title.config(font=font)           
title.config(height=3, width=120)       
title.place(x=0,y=5)

font1 = ('times', 13, 'bold')
datasetButton = Button(main, text="Upload Vehicle Dataset", command=loadDataset)
datasetButton.place(x=700,y=150)
datasetButton.config(font=font1)  

loadButton = Button(main, text="Generate & Load Yolov5 Model", command=loadModel)
loadButton.place(x=700,y=200)
loadButton.config(font=font1)

updateButton = Button(main, text="Federated Update Model to Server", command=updateModel)
updateButton.place(x=700,y=250)
updateButton.config(font=font1) 

detectButton = Button(main, text="Low Light Vehicle Detection", command=detectVehicle)
detectButton.place(x=700,y=300)
detectButton.config(font=font1)

graphButton = Button(main, text="Yolo Performance Graph", command=graph)
graphButton.place(x=700,y=350)
graphButton.config(font=font1)

font1 = ('times', 12, 'bold')
text=Text(main,height=30,width=80)
scroll=Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.place(x=10,y=100)
text.config(font=font1)


main.config(bg='light salmon')
main.mainloop()
