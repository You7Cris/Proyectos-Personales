# pyttsx3
# speech_recognition
# webbrowser
# pywhatkit
# yfinance
# pyjokes

# py -m pip install pyttsx3
# py -m pip install SpeechRecognition
# py -m pip install whatkit
# py -m pip install yfinance
# py -m pip install pyjokes # Asistente de chistes

import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import pyaudio

# escuchar nuestro microfono y devolver el audio como texto
def transformar_audio_en_texto():

    # almacenar recognizer en variable
    r = sr.Recognizer()

    # configurar el microfono
    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzo la grabacion
        print("Ya puedes hablar")

        # Guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google_cloud(audio, language = "es-co")

            # prueba de que pudo ingresar
            print("Dijiste: " + pedido)

            # devolver pedido
            return pedido
        
        # en caso de que no comprenda el audio
        except sr.UnknownValueError:

            # prueba de que no comprendio el audio
            print("Ups, no entendi")

            # devolver error
            return "Sigo esperando"
        
        # En caso de no resolver el pedido
        except sr.RequestError:

            # prueba de que no comprendio el audio
            print("Ups, no hay servicio")

            # devolver error
            return "Sigo esperando"
        
        # error inesperado
        except:

            # prueba de que no comprendio el audio
            print("Ups, algo ha salido mal")

            # devolver error
            return "Sigo esperando"

# escuchar nuestro microfono y devolver el audio como texto
#transformar_audio_en_texto()

# funcion para que el asistente pueda ser escuchado
def hablar(mensaje):

    # encender el motor pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()



engine = pyttsx3.init()
for voz in engine.getProperty('voices'):
    print(voz)

# Solo cuento con este
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

hablar("Hola Cristian, espero que tengas un excelente dia")
hablar("Hola Santiago Muñoz Arango")
hablar('Today you are going to create a virtual systems')

# informar el dia de la semana
def pedir_dia():

    # crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    # crear variable para el dia de semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # diccionario con nombres de dias
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}
    
    # decir dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')

pedir_dia()

# informar la hora
def pedir_hora():

    # crear una variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En estos momentos son las {hora.hour} horas con {hora.minute} con {hora.second} segundos'
    print(hora)

    # decir la hora
    hablar(hora)

pedir_hora()

# funcion saludo inicial
def saludo_inicial():

    # crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif hora.hour >= 6 and hora.hour < 13:
        momento = 'Buen dia'
    else:
        momento = 'Buenas tardes'



    # decirle el saludo
    hablar('{momento}, soy Zira, tu asistente virtual, en que te puedo ayudar? ')


# Funcion central del sistema
def pedir_cosas():

    # activar saludo inicial
    saludo_inicial()

    # variable de corte
    comenzar = True

    # loop central
    while comenzar:

        # activar el micro y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué dia es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'buscar en wikipedia' in pedido:
            hablar('Buscando en wikipedia')
            pedido = pedido.replace('wikipedia','')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente: ')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Ya mismo estoy en eso')
            pedido = pedido.replace('busca en internet','')
            pywhatkit.search(pedido)
            hablar("Esto es lo que he encontrado")
            continue
        elif 'reproducir' in pedido:
            hablar('Buena idea, ya comenzao a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple':'APPL',
                       'amazon':'AMZN',
                       'google':'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar("Pérdon pero no la he encontrado")
                continue
        elif 'adios' in pedido:
            hablar("Me voy a descansar, cualquier cosa me avisas")
            break


pedir_cosas()








