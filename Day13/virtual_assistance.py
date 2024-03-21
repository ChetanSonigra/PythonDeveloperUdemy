import pyttsx3
import wikipedia
import speech_recognition as sr
import pywhatkit
import pyjokes, datetime, webbrowser
import yfinance as yf

# hear the microphone and return the audio as text
def transform_audio_to_text():
    
    # store recognizer in variable
    r = sr.Recognizer()
    
    # set microphone
    with sr.Microphone() as source:
        
        # waiting time
        r.pause_threshold = 0.8
        
        # report that recording has begun
        print('You can now speak')
        
        # save what you hear as audio
        audio = r.listen(source)
        
        try:
            # search on google
            request = r.recognize_google(audio,language='en-us')
            
            # test in text
            print("you said: " + request)
            
            # return request
            return request
        
        # In case it doesn't understand audio
        except sr.UnknownValueError:
            
            # Show proof that it didn't understand audio
            print('Ups! I didn\'t understand audio')
            
            return 'I am still waiting..'
            
        # In case request can't be resolved.
        except sr.RequestError:
            
            # Show proof that it didn't understand audio
            print('Ups! There is no service')
            
            return 'I am still waiting..'
        
        # Unexpected error
        except:
            
            # Show proof that it didn't understand audio
            print('Ups! Something went wrong')
            
            return 'I am still waiting..'
        
        
transform_audio_to_text()

# Function so that assistant can be heard.
def speak(message):
    
    # start engine of pyttsx3
    engine = pyttsx3.init()
    
    engine.setProperty('voice',id2)
    # deliver message
    engine.say(message)
    engine.runAndWait()

#engine = pyttsx3.init()
#for voice in engine.getProperty('voices'):
#    print(voice)  
# voice/langauge option
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

def ask_day():
    
    # create a variable with today's information
    day = datetime.date.today()
    #print(day)
    
    # create a variable for day of the week
    week_day = day.weekday()
    #print(week_day)
    
    calender = ['Monday','Tuesday', 'Wednesday', 'Thursday','Friday', 'Saturday', 'Sunday']
    
    speak(f'Today is {calender[week_day]}.')

def ask_time():
    time = datetime.datetime.now()
    #print(time)
    speak(f'At this moment, it is {time.hour} hours and {time.minute} minutes.')

def initial_greetings():
    speak('Hello, I am Zira. How may I help you? ')
    
ask_day()
ask_time()
initial_greetings()


def my_assistant():
    
    # Activate the intial greeting.
    initial_greetings()
    
    # Cut-off variable
    go_on = True
    
    # Main loop
    while go_on:
        
        # Activate microphone and save request
        my_request =  transform_audio_to_text().lower()
        
        if 'open youtube' in my_request:
            speak('Sure, I am opening youtube.')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'open browser' in my_request:
            speak('Of course, I am on it.')
            webbrowser.open('https://www.google.com')
            continue
        elif 'what day is today' in my_request:
            ask_day()
            continue        
        elif 'what time it is' in my_request:
            ask_time()
            continue
        elif 'wikipedia search for' in my_request:
            my_request = my_request.replace('wikipedia search for', '')
            summary = wikipedia.summary(my_request,sentences=1)
            speak('According to wikipedia: ')
            speak(summary)
            continue
        elif 'search internet for' in my_request:
            my_request = my_request.replace('search internet for', '')
            pywhatkit.search(my_request)
            speak('Here what I found')
            continue
        elif 'play' in my_request:
            my_request = my_request.replace('play', '')
            pywhatkit.playonyt(my_request)
            continue
        elif 'joke' in my_request:
            speak(pyjokes.get_joke())
            continue
        elif 'stock price' in my_request:
            share = my_request.split()[-2].strip()
            portfolio = {
                'apple': 'APPL',
                'amazon': 'AMZN',
                'google': 'GOOGL',
                'tcs': 'TCS',
                'infosys': 'INFY'
            }
            try:
                searched_stock = portfolio[share]
                searched_stock = yf.Ticker(searched_stock)
                price = searched_stock.info['regularMarketPrice']
                speak(f'I found it. The price of {share} is {price}')
                continue
            except:
                speak("I am sorry, but I didn't find it.")
                continue
        elif 'good bye' in my_request:
            speak('I am going to rest. Let me know if you need anything')
            break
my_assistant()
        