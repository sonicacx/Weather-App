from tkinter import *

from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

window = Tk()
window.title("Weather App")
window.geometry("890x470+500+300")
window.configure(bg="#64B2FF")
window.resizable(False, False)


def getweather():
    city = textfield.get()
    #convert address into coordinates
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)

    #the time and the longitute and latitude coordinates
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    timezone.config(text=result)

    long_lat.config(text=f"{round(location.latitude, 1)}°N {round(location.longitude, 1)}°E")

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    #api: https://openweathermap.org/api/one-call-3
    api = "https://api.openweathermap.org/data/2.5/onecall?lat=" + str(location.latitude) + "&lon=" + str(
        location.longitude) + "&units=metric&exclude=hourly&appid=5af712723f23a93ec8a3ea04bcc6319d"

    json_data = requests.get(api).json()

    # current

    temp = json_data['current']['temp']
    humidity = json_data['current']['humidity']
    pressure = json_data['current']['pressure']
    wind = json_data['current']['wind_speed']
    description = json_data['current']['weather'][0]['description']

    t.config(text=(temp, "°C"))
    h.config(text=(humidity, "%"))
    p.config(text=(pressure, "hPa"))
    w.config(text=(wind, "m/s"))
    d.config(text=(description))

    # firstcell
    firstdayimage = json_data['daily'][0]['weather'][0]['icon']
    photo1 = ImageTk.PhotoImage(file=f"icon/{firstdayimage}@2x.png")
    firstimage.config(image=photo1)
    firstimage.image = photo1

    tempday1 = json_data['daily'][0]['temp']['day']
    tempnight1 = json_data['daily'][0]['temp']['night']

    day1temp.config(text=f"Day:{tempday1}°C\nNight:{tempnight1}°C")

    # secondcell
    seconddayimage = json_data['daily'][1]['weather'][0]['icon']
    img = (Image.open(f"icon/{seconddayimage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.image = photo2

    tempday2 = json_data['daily'][1]['temp']['day']
    tempnight2 = json_data['daily'][1]['temp']['night']

    day2temp.config(text=f"Day:{int(tempday2)}°C\nNight:{int(tempnight2)}°C")

    # thirdcell
    thirddayimage = json_data['daily'][2]['weather'][0]['icon']
    img = (Image.open(f"icon/{thirddayimage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo3 = ImageTk.PhotoImage(resized_image)
    thirdimage.config(image=photo3)
    thirdimage.image = photo3

    tempday3 = json_data['daily'][2]['temp']['day']
    tempnight3 = json_data['daily'][2]['temp']['night']

    day3temp.config(text=f"Day:{int(tempday3)}°C\nNight:{int(tempnight3)}°C")

    # fourthcell
    fourthdayimage = json_data['daily'][3]['weather'][0]['icon']
    img = (Image.open(f"icon/{fourthdayimage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo4 = ImageTk.PhotoImage(resized_image)
    fourthimage.config(image=photo4)
    fourthimage.image = photo4

    tempday4 = json_data['daily'][3]['temp']['day']
    tempnight4 = json_data['daily'][3]['temp']['night']

    day4temp.config(text=f"Day:{int(tempday4)}°C\nNight:{int(tempnight4)}°C")

    # fifthcell
    fifthdayimage = json_data['daily'][4]['weather'][0]['icon']
    img = (Image.open(f"icon/{fifthdayimage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo5 = ImageTk.PhotoImage(resized_image)
    fifthimage.config(image=photo5)
    fifthimage.image = photo5

    tempday5 = json_data['daily'][4]['temp']['day']
    tempnight5 = json_data['daily'][4]['temp']['night']

    day5temp.config(text=f"Day:{int(tempday5)}°C\nNight:{int(tempnight5)}°C")

    # sixthcell
    sixthdayimage = json_data['daily'][5]['weather'][0]['icon']
    img = (Image.open(f"icon/{sixthdayimage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo6 = ImageTk.PhotoImage(resized_image)
    sixthimage.config(image=photo6)
    sixthimage.image = photo6

    tempday6 = json_data['daily'][5]['temp']['day']
    tempnight6 = json_data['daily'][5]['temp']['night']

    day6temp.config(text=f"Day:{int(tempday6)}°C\nNight:{int(tempnight6)}°C")

    # seventhcell
    seventhdayimage = json_data['daily'][6]['weather'][0]['icon']
    img = (Image.open(f"icon/{seventhdayimage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo6 = ImageTk.PhotoImage(resized_image)
    seventhimage.config(image=photo6)
    seventhimage.image = photo6

    tempday7 = json_data['daily'][6]['temp']['day']
    tempnight7 = json_data['daily'][6]['temp']['night']

    day7temp.config(text=f"Day:{int(tempday7)}°C\nNight:{int(tempnight7)}°C")

    # days
    first = datetime.now()
    day1.config(text=first.strftime("%A"))

    second = first + timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third = first + timedelta(days=2)
    day3.config(text=third.strftime("%A"))

    fourth = first + timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))

    fifth = first + timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))

    sixth = first + timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))

    seventh = first + timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))


image_icon = PhotoImage(file="images/logo.png")
window.iconphoto(False, image_icon)

first_label = Label(window, bg="#203243").place(x=30, y=112, width=195, height=120)

label1 = Label(window, text="Temperature", font=("Helvetica", 11), fg="white", bg="#203243")
label1.place(x=50, y=120)

label2 = Label(window, text="Humidity", font=("Helvetica", 11), fg="white", bg="#203243")
label2.place(x=50, y=140)

label3 = Label(window, text="Pressure", font=("Helvetica", 11), fg="white", bg="#203243")
label3.place(x=50, y=160)

label4 = Label(window, text="Wind Speed", font=("Helvetica", 11), fg="white", bg="#203243")
label4.place(x=50, y=180)

label5 = Label(window, text="Description", font=("Helvetica", 11), fg="white", bg="#203243")
label5.place(x=50, y=200)

# search_box

Search_image = PhotoImage(file="images/Search Rectangle.png")
myimage = Label(image=Search_image, bg="#64B2FF")
myimage.place(x=270, y=112)

weat_image = PhotoImage(file="images/Search_logo.png")
weather_image = Label(window, image=weat_image, bg="#203243")
weather_image.place(x=290, y=120)

textfield = Entry(window, justify='left', width=15, font=("poppins", 24, 'bold'), bg="#203243", border=0, fg='white')
textfield.place(x=360, y=125)
textfield.focus()

Search_icon = PhotoImage(file="images/Search_icon.png")
myimage_search = Button(image=Search_icon, borderwidth=0, cursor='hand2', bg="#203243", command=getweather)
myimage_search.place(x=705, y=125)

# Bottom boxes

frame = Frame(window, width=900, height=180, bg="#212120")
frame.pack(side=BOTTOM)

# 1 box - bigger one
Label(frame, relief=RIDGE, bg="#333333").place(x=30, y=20, width=240, height=140)

# 2-7 box - smaller ones
coordinates = [(300, 30), (400, 30), (500, 30), (600, 30), (700, 30), (800, 30)]
for i, (x, y) in enumerate(coordinates):
    Label(frame, relief=RIDGE, bg="#333333").place(x=x, y=y, width=80, height=120)

# clock(the time)

clock = Label(window, font=("Helvetica", 30, 'bold'), fg='white', bg="#64B2FF")
clock.place(x=30, y=20)

# timezone

timezone = Label(window, font=("Helvetica", 20), fg="white", bg="#64B2FF")
timezone.place(x=650, y=20)

long_lat = Label(window, font=("Helvetica", 20), fg="white", bg="#64B2FF")
long_lat.place(x=650, y=50)

t = Label(window, font=("Helvetica", 11), fg="white", bg="#203243")
t.place(x=150, y=120)

h = Label(window, font=("Helvetica", 11), fg="white", bg="#203243")
h.place(x=150, y=140)

p = Label(window, font=("Helvetica", 11), fg="white", bg="#203243")
p.place(x=150, y=160)

w = Label(window, font=("Helvetica", 11), fg="white", bg="#203243")
w.place(x=150, y=180)

d = Label(window, font=("Helvetica", 11), fg="white", bg="#203243")
d.place(x=150, y=200)

# BOTTOM CELLS
# 1
firstframe = Frame(window, width=235, height=132, bg="#2F2F30")
firstframe.place(x=33, y=313)

day1 = Label(firstframe, font="arial 16", bg="#2F2F30", fg="white")
day1.place(x=100, y=5)

firstimage = Label(firstframe, bg="#2F2F30")
firstimage.place(x=1, y=15)

day1temp = Label(firstframe, bg="#2F2F30", fg="#64B2FF", font="arial 15 bold")
day1temp.place(x=100, y=50)

# 2
secondframe = Frame(window, width=73, height=115, bg="#2F2F30")
secondframe.place(x=303, y=323)

day2 = Label(secondframe, bg="#2F2F30", fg="white")
day2.place(x=10, y=5)

secondimage = Label(secondframe, bg="#2F2F30")
secondimage.place(x=7, y=20)

day2temp = Label(secondframe, bg="#2F2F30", fg="#64B2FF")
day2temp.place(x=2, y=70)

# 3
thirdframe = Frame(window, width=73, height=115, bg="#2F2F30")
thirdframe.place(x=403, y=323)

day3 = Label(thirdframe, bg="#2F2F30", fg="white")
day3.place(x=10, y=5)

thirdimage = Label(thirdframe, bg="#2F2F30")
thirdimage.place(x=7, y=20)

day3temp = Label(thirdframe, bg="#2F2F30", fg="#64B2FF")
day3temp.place(x=2, y=70)

# 4
fourthframe = Frame(window, width=73, height=115, bg="#2F2F30")
fourthframe.place(x=503, y=323)

day4 = Label(fourthframe, bg="#2F2F30", fg="white")
day4.place(x=10, y=5)

fourthimage = Label(fourthframe, bg="#2F2F30")
fourthimage.place(x=7, y=20)

day4temp = Label(fourthframe, bg="#2F2F30", fg="#64B2FF")
day4temp.place(x=2, y=70)

# 5
fifthframe = Frame(window, width=73, height=115, bg="#2F2F30")
fifthframe.place(x=603, y=323)

day5 = Label(fifthframe, bg="#2F2F30", fg="white")
day5.place(x=10, y=5)

fifthimage = Label(fifthframe, bg="#2F2F30")
fifthimage.place(x=7, y=20)

day5temp = Label(fifthframe, bg="#2F2F30", fg="#64B2FF")
day5temp.place(x=2, y=70)

# 6
sixthframe = Frame(window, width=73, height=115, bg="#2F2F30")
sixthframe.place(x=703, y=323)

day6 = Label(sixthframe, bg="#2F2F30", fg="white")
day6.place(x=10, y=5)

sixthimage = Label(sixthframe, bg="#2F2F30")
sixthimage.place(x=7, y=20)

day6temp = Label(sixthframe, bg="#2F2F30", fg="#64B2FF")
day6temp.place(x=2, y=70)

# 7
seventhframe = Frame(window, width=73, height=115, bg="#2F2F30")
seventhframe.place(x=803, y=323)

day7 = Label(seventhframe, bg="#2F2F30", fg="white")
day7.place(x=10, y=5)

seventhimage = Label(seventhframe, bg="#2F2F30")
seventhimage.place(x=7, y=20)

day7temp = Label(seventhframe, bg="#2F2F30", fg="#64B2FF")
day7temp.place(x=2, y=70)

mainloop()
