
def main():

    names = ["Mario", "Luigi", "Daisy", "Yoshi"]
    # print(write_letter("Mario", "Princess Peach"))
    # print(write_letter("Luigi", "Princess Peach"))
    # print(write_letter("Daisy", "Princess Peach"))
    # print(write_letter("Yoshi", "Princess Peach"))

    for name in names:
        print(write_letter(name, "Princess Peach"))        
        #print(names[i])




def write_letter(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
    Dear {receiver},

    You are cordially invited to a ball at Peach's
    Castle this evening, 7:00 PM.

    Sincerely,
    {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*        
    """

main()