import random
import time
import os


print('Hello')

clear = lambda: os.system('cls')

ai_score = 0
my_score = 0
# True or False => True
# True and False => False
while my_score < 3 and ai_score < 3:
    print('Twój wybór:')
    x = input()
    x = x.capitalize()
    allowed_letters = ['P', 'R', 'S']
    if x not in allowed_letters:  # not x == 'P' and not x == 'R' and not x == 'S':
        print("Błąd")
    else:
        ai_response = random.choice(allowed_letters)
        print('Wybor Komputera:', ai_response)

        # TODO: Move all of the if's to another function
        # and return who_won, then print result and increment score variables
        if ai_response == x:
            print('Remis')

        if ai_response == 'P' and x == 'R':
            print('Komputer wygrał')
            ai_score = ai_score + 1

        if ai_response == 'P' and x == 'S':
            print('wygrałeś')
            my_score = my_score + 1

        if ai_response == 'R' and x == 'S':
            print('Komputer wygrał')
            ai_score = ai_score + 1

        if ai_response == 'R' and x == 'P':
            print('wygrałeś')
            my_score = my_score + 1

        if ai_response == 'S' and x == 'P':
            print('Komputer wygrał')
            ai_score = ai_score + 1

        if ai_response == 'S' and x == 'R':
            print('wygrałeś')
            my_score = my_score + 1

        time.sleep(2)
        clear()

        print('my score:', my_score)
        print('ai score:', ai_score)

    if my_score == 3:
        print('Wygrałeś całą rozgrywkę')

    if ai_score == 3:
        print('Komputer wygrał całą rozgrywkę')