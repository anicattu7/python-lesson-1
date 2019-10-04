happy_mood = "It is great to see you happy!"
nervous_mood = "Take a deep breath 3 times."
sad_mood = "Sorry to hear that."
excited_mood = "That sounds Amazed!!!"
relaxed_mood = "Mellow out!!!"

while(True):
    mood = input("Please tell me how you feel (options: happy,nervous,sad,excited,relaxed):  ")

    if mood == "happy":
        print(happy_mood)
    elif mood == "sad":
        print(sad_mood)
    elif mood == "nervous":
        print(nervous_mood)
    elif mood == "excited":
        print(excited_mood)
    elif mood == "relaxed":
        print(relaxed_mood)
    else:
        print("I don't recognize this mood.")

