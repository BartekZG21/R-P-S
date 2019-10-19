print('Hello')
print('Twój wybór:')
x = input()
x = x.capitalize()
allowed_letters = ['P', 'R', 'S']
if x not in allowed_letters:  # not x == 'P' and not x == 'R' and not x == 'S':
    print("Błąd")
else:
    print('Dobrze')
    ai_response = 'r'  # Docelowo odp komuputera będzie losowa
    if ai_response == x or ai_response.capitalize() == x:
        print('Remis')

    ai_response = 'p'
    if x == 'r' and ai_response == 'p':
        print("Komputer wygral")
    if x == 's' and ai_response == 'p':
        print('Wygrales')

    ai_response = 'r'
    if x == 'p' and ai_response == 'r':
        print("Wygrales")