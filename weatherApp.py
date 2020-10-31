from tkinter import *
import json
import requests
from urllib.request import urlopen
import datetime
import webbrowser
import config

app = Tk()
app.title("Python Wheater Conditions")

# # ÍCONE
# photoIcon = PhotoImage(file = 'images/logo.png')
# app.iconphoto(False, photoIcon)

# defino o tamanho da janela e set pra false o redimensionamento
app.geometry('445x450')
app.resizable(0, 0)

apiKey = config.apiKey
city = 'Belo Horizonte'

# pega apenas o dia atual
callAPI = f'https://api.weatherapi.com/v1/current.json?key={apiKey}&q={city}'

# pega 3 dias, dia atual e + 2
forecastAPI = f'https://api.weatherapi.com/v1/forecast.json?key={apiKey}&q={city}&days=3'

try:
    apiRequest = requests.get(forecastAPI)
    results = json.loads(apiRequest.content)
except Exception as e:
    results = "Error..."


# FRAMES SETADOS
# ESPÉCIE DE DIV DO HTML

actualDayFrame = Frame(app, bd=0, relief="solid", pady=10, padx=8)
actualDayFrame.grid(columnspan=3, stick="", padx=5)

wrapperDays = Frame(app)
wrapperDays.grid()

# day1Frame = Frame(wrapperDays, bd=2, relief="solid", pady=10, padx=8)
# day1Frame.grid(row=1, column=0, padx=5)

# day2Frame = Frame(wrapperDays, bd=2, relief="solid", pady=10, padx=8)
# day2Frame.grid(row=1, column=1, padx=5)

# day3Frame = Frame(wrapperDays, bd=2, relief="solid", pady=10, padx=8)
# day3Frame.grid(row=1, column=2, padx=5)


# INFO DO DIA

weatherLocation = Label(actualDayFrame, text=results['location']['name'])
weatherLocation.pack()

actualDate = results['forecast']['forecastday'][0]['date']
actualDataFormated = datetime.datetime.strptime(actualDate, '%Y-%m-%d').strftime('%d/%m/%Y')

wheaterDate = Label(actualDayFrame, text=actualDataFormated)
wheaterDate.pack()

weatherTemp = Label(actualDayFrame, text='{} C°'.format(results['current']['temp_c']))
weatherTemp.pack()

climateURL = results['current']['condition']['icon']
climateimageURLFetch = 'https:{}'.format(climateURL)


# aqui eu faço o "fetch" da imagem usando a url da cdn da API
with urlopen(climateimageURLFetch) as handle:
    data = handle.read()

finalImage = PhotoImage(master=actualDayFrame, data=data)


# Dia atual
weatherImage = Label(actualDayFrame, image=finalImage)
weatherImage.pack()

weatherCondition = Label(actualDayFrame, text='The weather conditions are {}'
    .format(results['current']['condition']['text']))
weatherCondition.pack()

weatherFeel = Label(actualDayFrame, text='The temperature feels like {} C°'
    .format(results['current']['feelslike_c']))
weatherFeel.pack()

weatherHumidity = Label(actualDayFrame, text='Relative humidity are {}%'
    .format(results['current']['humidity']))
weatherHumidity.pack()


# Quadrinho inferior com 3 dias

for index in range(0, 3):    
    # PRA CADA DIA, EU CRIO UM DAYFRAME, MAS SÓ MUDO A COLUMN
    dayFrame = Frame(wrapperDays, bd=2, relief="solid", pady=10, padx=8)
    dayFrame.grid(row=1, column=index, padx=5)
    
    # DATA ATUAL
    dayDate = results['forecast']['forecastday'][index]['date']
    formatedDate = datetime.datetime.strptime(dayDate, '%Y-%m-%d').strftime('%d/%m/%Y')

    # LABEL RECEBENDO COMO TEXTO O DIA ATUAL
    labelDay = Label(dayFrame, font="bold", text=dayDate)
    labelDay.grid()

    # LABEL RECENBENDO COMO TEXTO A TEMP MÁXIMA DO DIA ATUAL
    forecastDayMax = Label(dayFrame, fg="red", text='max: {} C°'.format(results['forecast']['forecastday'][index]['day']['maxtemp_c']))
    forecastDayMax.grid()

    forecastDayMin = Label(dayFrame, fg="blue", text='min: {} C°'.format(results['forecast']['forecastday'][index]['day']['mintemp_c']))
    forecastDayMin.grid()

    forecastDayAvg = Label(dayFrame, text='med: {} C°'.format(results['forecast']['forecastday'][index]['day']['avgtemp_c']))
    forecastDayAvg.grid()

    forecastdayHumidity = Label(dayFrame, fg="dodgerblue", text='humidity: {}%'.format(results['forecast']['forecastday'][index]['day']['avghumidity']))
    forecastdayHumidity.grid()


# DIA 1

# day1 = results['forecast']['forecastday'][0]['date']

# # essa "fórmula" eu converto a data do formato original para o formato brasileiro
# day1Formated = datetime.datetime.strptime(day1, '%Y-%m-%d').strftime('%d/%m/%Y')
# forecastDay1 = Label(day1Frame, font="bold", text=day1Formated)
# forecastDay1.grid()

# forecastDay1Max = Label(day1Frame, fg="red", text='max: {} C°'.format(results['forecast']['forecastday'][0]['day']['maxtemp_c']))
# forecastDay1Max.grid()

# forecastDay1Min = Label(day1Frame, fg="blue", text='min: {} C°'.format(results['forecast']['forecastday'][0]['day']['mintemp_c']))
# forecastDay1Min.grid()

# forecastDay1Avg = Label(day1Frame, text='med: {} C°'.format(results['forecast']['forecastday'][0]['day']['avgtemp_c']))
# forecastDay1Avg.grid()

# forecastday1Humidity = Label(day1Frame, fg="dodgerblue", text='humidity: {}%'.format(results['forecast']['forecastday'][0]['day']['avghumidity']))
# forecastday1Humidity.grid()

# # forecastDay1Rain = Label(day1Frame, text='prob. of rain: {}%'.format(results['forecast']['forecastday'][0]['day']['daily_chance_of_rain']))
# # forecastDay1Rain.grid()


# # DIA 2

# day2 = results['forecast']['forecastday'][1]['date']

# # essa "fórmula" eu converto a data do formato original para o formato brasileiro
# day2Formated = datetime.datetime.strptime(day2, '%Y-%m-%d').strftime('%d/%m/%Y')
# forecastDay2 = Label(day2Frame, font="bold", text=day2Formated)
# forecastDay2.grid()

# forecastDay2Max = Label(day2Frame, fg="red", text='max: {} C°'.format(results['forecast']['forecastday'][1]['day']['maxtemp_c']))
# forecastDay2Max.grid()

# forecastDay2Min = Label(day2Frame, fg="blue", text='min: {} C°'.format(results['forecast']['forecastday'][1]['day']['mintemp_c']))
# forecastDay2Min.grid()

# forecastDay2Avg = Label(day2Frame, text='med: {} C°'.format(results['forecast']['forecastday'][1]['day']['avgtemp_c']))
# forecastDay2Avg.grid()

# forecastday2Humidity = Label(day2Frame, fg="dodgerblue", text='humidity: {}%'.format(results['forecast']['forecastday'][1]['day']['avghumidity']))
# forecastday2Humidity.grid()


# #  DIA 3

# day3 = results['forecast']['forecastday'][2]['date']

# # essa "fórmula" eu converto a data do formato original para o formato brasileiro
# day3Formated = datetime.datetime.strptime(day3, '%Y-%m-%d').strftime('%d/%m/%Y')
# forecastDay3 = Label(day3Frame, font="bold", text=day3Formated)
# forecastDay3.pack()

# forecastDay3Max = Label(day3Frame, fg="red", text='max: {} C°'.format(results['forecast']['forecastday'][2]['day']['maxtemp_c']))
# forecastDay3Max.pack()

# forecastDay3Min = Label(day3Frame, fg="blue", text='min: {} C°'.format(results['forecast']['forecastday'][2]['day']['mintemp_c']))
# forecastDay3Min.pack()

# forecastDay3Avg = Label(day3Frame, text='med: {} C°'.format(results['forecast']['forecastday'][2]['day']['avgtemp_c']))
# forecastDay3Avg.pack()

# forecastday3Humidity = Label(day3Frame, fg="dodgerblue", text='humidity: {}%'.format(results['forecast']['forecastday'][2]['day']['avghumidity']))
# forecastday3Humidity.pack()



#  GROUP BUTTON LOGO
buttonFrame = LabelFrame(app, text="Weather API", bd=1, relief="solid")
buttonFrame.grid(row=2, stick="we", pady=15, padx=5)

frameBtn = Frame(buttonFrame)
# frameBtn.grid(row=0, column=0, padx=5, pady=5)
frameBtn.pack(side=LEFT, padx=5, pady=5)
# frameBtn.place(anchor=W)

frameLogo = Frame(buttonFrame)
# frameLogo.grid(row=0, column=1, padx=5, pady=5)
frameLogo.pack(side=RIGHT, padx=5, pady=5)
# frameLogo.place(anchor=E)

# Icone das condições climáticas atuais
apiLOGO = 'https://cdn.weatherapi.com/v4/images/weatherapi_logo.png'

with urlopen(apiLOGO) as handle:
    logoImage = handle.read()

imageLogoFinal = PhotoImage(master=frameLogo, data=logoImage)

def linkWheaterAPI(url):
  webbrowser.open_new(url)

logoRender = Label(frameLogo, image=imageLogoFinal, cursor="hand2")
logoRender.pack()
# crio um hiperlink com esse bind e essa sintaxe
logoRender.bind('<Button-1>', lambda e: linkWheaterAPI('https://www.weatherapi.com/'))

btnExit = Button(frameBtn, text="quit", command=app.quit, cursor="spider")
btnExit.pack()

app.mainloop()
