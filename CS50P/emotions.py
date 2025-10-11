emotion = "v.v"

def main():
    global emotion 
    say("Hi, I'm emotion face")

    emotion = ":D"
    say("Is anyone here?")
    

def say(phrase):
    print(phrase, emotion)


main()