import customtkinter
import tkinter
import os
import json


def InputMinAge():
    global min_age
    dialogMin = customtkinter.CTkInputDialog(text="Напиши минимальный возраст", title="Диапозон возраста")
    min_age = dialogMin.get_input()
    with open("config.json", "r+") as jsonFile:
        data = json.load(jsonFile)

        data["min_age"] = min_age

        jsonFile.seek(0)  # rewind
        json.dump(data, jsonFile)
        jsonFile.truncate()
    print("От:", min_age)
    
    
def InputMaxAge():
    global max_age
    dialogMax = customtkinter.CTkInputDialog(text="Напиши максимальный возраст", title="Диапозон возраста")
    max_age = dialogMax.get_input()
    with open("config.json", "r+") as jsonFile:
        data = json.load(jsonFile)

        data["max_age"] = max_age

        jsonFile.seek(0)  # rewind
        json.dump(data, jsonFile)
        jsonFile.truncate()
    print("До:", max_age)
    

def changeStateButtons():
    valueSwitchAge = switchAge_var.get()
    
    if valueSwitchAge == 'on':
        AgeButton1.configure(state='normal')
        AgeButton2.configure(state='normal')
    if valueSwitchAge == 'off':
        AgeButton1.configure(state='disabled') 
        AgeButton2.configure(state='disabled')


def radiobutton1_event():
    valueRadio1 = radio_var1.get()
    global language
    if valueRadio1 == 1:
        language = 'ru'
        print('name ru')
    else: 
        language = 'en'
        print('name en')
    with open("config.json", "r+") as jsonFile:
        data = json.load(jsonFile)

        data["lang"] = language

        jsonFile.seek(0)  # rewind
        json.dump(data, jsonFile)
        jsonFile.truncate()

def radiobutton2_event():
    valueRadio2 = radio_var2.get()
    global phone_num
    if valueRadio2 == 3:
        phone_num = 'ru'
        print('phone ru')
    else: 
        phone_num = 'us'
        print('phone us')
    with open("config.json", "r+") as jsonFile:
        data = json.load(jsonFile)

        data["phone_num"] = phone_num

        jsonFile.seek(0)  # rewind
        json.dump(data, jsonFile)
        jsonFile.truncate()

def InputNameDB():
    DataName = customtkinter.CTkInputDialog(text="Напиши название базы данных", title="Навание БД")
    nameDB = DataName.get_input()
    labelData.configure(text='Текущее: ' + nameDB + '.db')
    with open("config.json", "r+") as jsonFile:
        data = json.load(jsonFile)

        data["nameDB"] = nameDB

        jsonFile.seek(0)  # rewind
        json.dump(data, jsonFile)
        jsonFile.truncate()

def inputStr():
    global valueStr
    InputValue = customtkinter.CTkInputDialog(text="Напиши название базы данных", title="Навание БД")
    valueStr = InputValue.get_input()
    labelStr.configure(text='Текущее: ' + valueStr)
    with open("config.json", "r+") as jsonFile:
        data = json.load(jsonFile)

        data["valueStr"] = valueStr

        jsonFile.seek(0)  # rewind
        json.dump(data, jsonFile)
        jsonFile.truncate()

def Generation():
    valueFN = switchFirstName_var.get()
    valueLN = switchLastName_var.get()
    valueAge = switchAge_var.get()
    valueNum = switchNum_var.get()
    valueCity = switchCity_var.get()
    if valueFN == 'off' and valueLN == 'off' and valueAge == 'off' and valueNum == 'off' and valueCity == 'off':
        label_error.configure(text_color="red")
    else:
        label_error.configure(text_color="#242424")
        print('Generation Started')
    exec(open('database-dd.py').read())

def gg():
    a = [0, 0, 0, 0 ,0]



app = customtkinter.CTk()
app.iconbitmap('databasee.ico')

app.title("DataBase Configurator")
app.geometry("600x600")
app.resizable('False', 'False')

app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure((0,1,2,3,4,5,6), weight=2)
app.grid_rowconfigure(7, weight=1)




# верхняя надпись


label_1 = customtkinter.CTkLabel(app, text='Сonfiguration BD', fg_color="transparent", font=customtkinter.CTkFont(size=28))
label_1.grid(row=0, column=1, padx=20, pady=0)


frameDataName = customtkinter.CTkFrame(app)
frameDataName.grid(row=1, column=1,padx=20,pady=0)
frameDataName.grid_columnconfigure((0), weight=1)
frameDataName.grid_rowconfigure((0,1), weight=1)

DataButton = customtkinter.CTkButton(frameDataName, text="Задать название БД", command=InputNameDB)
DataButton.grid(row=0, column=1, padx=20, pady =10)

labelData = customtkinter.CTkLabel(frameDataName, text='Текущее: database.db', fg_color="transparent", font=customtkinter.CTkFont(size=12))
labelData.grid(row=1, column=1, padx=20, pady=2)


frame_1 = customtkinter.CTkFrame(app)
frame_1.grid(row=2, column=1, padx=40, pady=0 )
frame_1.grid_columnconfigure((0,1), weight=1)
frame_1.grid_rowconfigure((0,1), weight=1)

switchFirstName_var = customtkinter.StringVar(value='off')
switchFirstName = customtkinter.CTkSwitch(frame_1, text='Имя', variable=switchFirstName_var, onvalue='on', offvalue='off')
switchFirstName.grid(row=1, column=1, padx=20, pady=20)

# фамилия
switchLastName_var = customtkinter.StringVar(value='off')
switchLastName = customtkinter.CTkSwitch(frame_1, text='Фамилия', variable=switchLastName_var, onvalue='on', offvalue='off')
switchLastName.grid(row=2, column=1, padx=20, pady=20)

# радио имя фамилия


radio_var1 = tkinter.IntVar(value=0)
radiobutton_1 = customtkinter.CTkRadioButton(frame_1, text="Ru",
                                             command=radiobutton1_event, variable= radio_var1, value=1)
radiobutton_1.grid(row=1, column=2,padx=20,pady=20)
radiobutton_2 = customtkinter.CTkRadioButton(frame_1, text="En",
                                             command=radiobutton1_event, variable= radio_var1, value=2)
radiobutton_2.grid(row=2, column=2,padx=20,pady=20)


# возраст
frameAge = customtkinter.CTkFrame(app)
frameAge.grid(row=3, column=1,padx=40, pady=0)
frame_1.grid_columnconfigure((0,1,2), weight=1)
frame_1.grid_rowconfigure((0), weight=1)

switchAge_var = customtkinter.StringVar(value='off')
switchAge = customtkinter.CTkSwitch(frameAge, text="Возраст", command=changeStateButtons, variable=switchAge_var, onvalue='on', offvalue='off')
switchAge.grid(row=0, column=0, padx=20, pady=0)


# настройка возраста
AgeButton1 = customtkinter.CTkButton(frameAge, state='disabled', text="Задать мин. возраст", command=InputMinAge)
AgeButton1.grid(row=0, column=1, padx=20, pady =20)
AgeButton2 = customtkinter.CTkButton(frameAge, state='disabled', text="Задать макс. возраст", command=InputMaxAge)
AgeButton2.grid(row=0, column=2, padx=20, pady =20)


frame_2= customtkinter.CTkFrame(app)
frame_2.grid(row=4,column=1, padx=20,pady=0)
frame_2.grid_columnconfigure((0,1), weight=1)
frame_2.grid_rowconfigure((0,1), weight=1)

switchNum_var = customtkinter.StringVar(value='off')
switchNum = customtkinter.CTkSwitch(frame_2, text='Номер телефона', variable=switchNum_var, onvalue='on', offvalue='off')
switchNum.grid(row=0, column=0, padx=10, pady=10)



switchCity_var = customtkinter.StringVar(value='off')
switchCity = customtkinter.CTkSwitch(frame_2, text='Город', variable=switchCity_var, onvalue='on', offvalue='off')
switchCity.grid(row=1, column=0, padx=10, pady=10)



radio_var2 = tkinter.IntVar(value=0)
radiobutton_3 = customtkinter.CTkRadioButton(frame_2, text="Ru",
                                             command=radiobutton2_event, variable= radio_var2, value=3)
radiobutton_3.grid(row=0, column=1,padx=10, pady=10)
radiobutton_4 = customtkinter.CTkRadioButton(frame_2, text="Us",
                                             command=radiobutton2_event, variable= radio_var2, value=4)
radiobutton_4.grid(row=1, column=1,padx=10, pady=10)

frameStr = customtkinter.CTkFrame(app)
frameStr.grid(row=5, column = 1,padx=0,pady=0)
frameStr.grid_columnconfigure((0), weight=1)
frameStr.grid_rowconfigure((0,1), weight=1)

InputStrBtn = customtkinter.CTkButton(frameStr, text='Задать количество заполняемых строк', command=inputStr)
InputStrBtn.grid(row=0, column=0, padx=0, pady=0, sticky='ew')

labelStr = customtkinter.CTkLabel(frameStr, text='Текущее: 0', fg_color="transparent", font=customtkinter.CTkFont(size=12))
labelStr.grid(row=1, column=0, padx=20, pady=2)





frameGen = customtkinter.CTkFrame(app)
frameGen.grid(row=6, column = 1,padx=0,pady=0)
frameGen.grid_columnconfigure((0), weight=1)
frameGen.grid_rowconfigure((0,1), weight=1)
generateButton = customtkinter.CTkButton(frameGen, text='Generate', command=Generation)
generateButton.grid(row=0, column=0, padx=0, pady=0, sticky='ew')

label_error = customtkinter.CTkLabel(frameGen, text='Выберите хотя бы 1 элемент', text_color='#242424', fg_color='#242424')
label_error.grid(row=1, column=0, padx=0, pady=0)




app.mainloop()


