""" Chatbot
        steps:
            1. input/ listen
            2. process/ decide
            3. output/ talk back
"""
greet_words = ['hi', 'hello', 'yo']
bye_words = ['bye', 'tata', 'hasta la vista']
dangerous_word = ['die', 'fire', 'kill', 'killer', 'missile', 'bomb', 'burst', 'shoot', 'president', 'burn']

def listen():
    return input("Say something: ")

def decide(command):
    # print(command)
    command = command.lower()
    broken_words = command.split(" ")

    for word in broken_words:
        if word in greet_words:
            talkBack("he said greetings")
            break
        elif word in bye_words:
            talkBack("he said bye")
            break

def talkBack(response):
    print(response)

command = listen()
decide(command)

