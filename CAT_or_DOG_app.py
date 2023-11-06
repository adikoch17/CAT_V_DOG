import tensorflow as tf
import numpy as np
import pandas as pd
import tkinter
import customtkinter
import os
from tkinter import filedialog
from PIL import Image
import cv2

os.environ["CUDA_VISIBLE_DEVICES"]="-1"
model = tf.keras.models.load_model("dog_v_cat_model.h5")
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

image_path = ""
image =None

def cat_or_dog(img_path):
    img_array = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array,(50,50))
    model = tf.keras.models.load_model("dog_v_cat_model.h5")
    prediction = float(model.predict(np.array([new_array])))
    print(prediction)
    if prediction<0.5:
        return "Probably a Dog"
    else:
        return "Probably a Cat"


def predict_animal(image_path):
    global label
    pred = cat_or_dog(image_path)
    try:
        label.configure(text=pred)
    except:
        label = customtkinter.CTkLabel(app, text=pred)
        label.pack(pady=20)


def set_image():
    global image_label
    filename = filedialog.askopenfile(initialdir = "/", title = "Select a File", filetypes = (('Jpeg Files', '*.jpeg'),('Jpg Files', '*.jpg')))
    print(filename.name)
    image_path=filename.name   
    image = customtkinter.CTkImage(Image.open(image_path),size=(200,200))
    if image:
        try:
            image_label.configure(image=image)
            predict_animal(image_path)
        except:
            image_label = customtkinter.CTkLabel(app,text="",image=image)
            image_label.pack(pady=20)
            predict_animal(image_path)
    else:
        pass


app = customtkinter.CTk()
app.geometry("720x480")
app.title("Cat or Dog")

choose_image = customtkinter.CTkButton(app, text='Choose image',command=set_image)
choose_image.pack(padx =10,pady=10)


app.mainloop()

