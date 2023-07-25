import pyttsx3

if __name__ == '__main__':
    print('This is a roboSpeaker')
    while True:
        engiene = pyttsx3.init()
        x = input('What you want to hear? ')
        if x == 'q':
            engiene.say('Bye')
            engiene.runAndWait()
            break

        engiene.say(x)
        engiene.runAndWait()
