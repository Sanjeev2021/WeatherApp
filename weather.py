import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image

url = "https://weather.com/en-IN/weather/today/l/e1bbaf5ba44a74170e3bb9f892416301c36b3b17f37e1a666c6e1213de0f5668"

master = Tk()
master.title("Weather App")
master.config(bg = "white")

img = Image.open(r"C:\Users\ACCER\Desktop\weather1.png")
img = img.resize((200,200))
img = ImageTk.PhotoImage(img)

def getWeather():
    page = requests.get(url)
    soup = BeautifulSoup(page.content , "html.parser")
    location = soup.find('h1',class_="CurrentConditions--location--1Ayv3").text
    temperature = soup.find('span',class_="CurrentConditions--tempValue--3KcTQ").text
    weatherPrediction = soup.find('div',class_="CurrentConditions--phraseValue--2xXSr").text

    locationLabel.config(text =location)
    temperatureLabel.config(text=temperature)
    weatherPredictionLabel.config(text= weatherPrediction)

    temperatureLabel.after(60000,getWeather)
    master.update()

locationLabel = Label(master, font=("Calibri bold",30),bg="white")
locationLabel.grid(row=0,sticky="N",padx=100)
temperatureLabel = Label(master, font=("Calibri bold",70),bg="white")
temperatureLabel.grid(row=1,sticky="W",padx=40)
Label(master , image=img , bg="white").grid(row=1,sticky="E")
weatherPredictionLabel = Label(master,font=("Calibri bold",40),bg="white")
weatherPredictionLabel.grid(row=2,sticky="W",padx=40)
getWeather()

master.mainloop()