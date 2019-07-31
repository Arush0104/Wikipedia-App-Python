import wikipedia
while 1:
    try:
        user = input("What do you want to search: ")
        wikipedia.set_lang("en")
        print(wikipedia.summary(user, sentences=2))
    except:
        print("oops!.... cant find what you want try something else")
