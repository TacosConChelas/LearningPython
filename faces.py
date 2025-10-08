import re
emoticons = [ "🙂", "🙁" ]
new_phrase = ""


def main():
    global new_phrase
    new_phrase = ""

    phrase = input()
    phrase = phrase.split()


    for word in phrase:
        if word == ":)" :
            word = emoticons[0]
        if word == ":(" :
            word = emoticons[1]

        new_phrase += (word + " ")

    print(new_phrase)

main()