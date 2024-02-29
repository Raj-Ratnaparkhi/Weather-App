import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image,ImageTk
import ttkbootstrap

def get_weather(city):
    API_KEY = "a7cb97471a56e587d406e51d13d93b19"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"
    res = requests.get(url)

    if res.status_code ==404:
        messagebox.showerror("Error", "City not found.")
        return None

    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temprature = weather['main']['temp'] - 273.15
    description =weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temprature, description, city, country)

def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return
    icon_url, temprature, description, city, country = result
    location_label.configure(text=f"{city}, {country}")

    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    temprature_label.configure(text=f"Temprature: {temprature: 2f}°C")
    description_label.configure(text="Description: {description}")

root = ttkbootstrap.Window(thename="morph")
root.title("Weather App")
root.geometry("400x400")

city_entry = ttkbootstrap.Entry(root, font="Helvetica ,18")
city_entry.pack(pady=10)

search_button = ttkbootstrap.Button(root, text="Search", command=search, bootstyle="warning")
search_button.pack(pady=10)

location_label = tk.Label(root, font="Helvetica, 25")
location_label.pack(pady=20)

icon_label = tk.Label(root)
icon_label.pack()

temprature_label = tk.Label(root, font="Helvetica, 20")
temprature_label.pack()

description_label = tk.Label(root, font="Helvetica, 20")
description_label.pack()

root.mainloop()