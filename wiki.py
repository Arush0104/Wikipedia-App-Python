from googlesearch import search
import wikipedia

global user 
user = ''
while (user != 'nothing'):
    try:
        '''
        wikipedia search for the input(user)
        '''
        user = input("What do you want to search: ")
        wikipedia.set_lang("en")
        print(wikipedia.summary(user, sentences=2))
    except:
        '''
        google search for the input(user)
        '''
        print('''OOPS!.... I cant find what you want in Wikipedia! Try these links below, I'm sure you'll get it ''')
        response = search(query=user,tld='co.in',lang='en',num=10,stop=1,pause=2)
        for i in response:
            print(i)
