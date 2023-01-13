'''
Papaer, Rock, Scissors game
---------------------------
'''
import random
punkty = 0
def wygrana():
    global punkty
    punkty += 1
    print(f'Wygrałeś! Masz {punkty} punktów')

def przegrana():
    global punkty
    punkty -= 1
    print(f'Przegrałeś! Masz {punkty} punktów')

def remis():
    print(f'Remis! Masz {punkty} punktów')

def get_user_choice():
    user_choice=input("Wybierz Papier, Kamień lub Nożyce: \n")
    if user_choice.lower() in ["papier", "kamień", "nożyce","p","k","n","kamien","nozyce"]:
        return user_choice.lower()
    else:
        print("Nieprawidłowy wybór")
        return get_user_choice()

def get_computer_choice():
    choices=["papier", "kamień", "nożyce"]
    return random.choice(choices)

def choice():
    global wybor
    wybor = input('Grasz na rundy czy punkty?\nWpisz "r" dla rund lub "p" dla punktów:\n')
    if wybor.lower() in ['r', 'p']:
        return wybor.lower()
    else:
        print('Nieprawidłowy wybór')
        return choice()

def r_and_p():
    global rounds
    global points
    global punkty
    global enemy_points
    choice()
    if wybor=='r':
        rounds=int(input('Podaj liczbę rund:\n'))
        return rounds
    elif wybor=='p':
        points=int(input('Podaj liczbę punktów, aby wygrać:\n'))
        enemy_points=int(input('Podaj liczbę punktów, aby przeciwnik wygrał:\n'))
        enemy_points=enemy_points*-1
        return points, enemy_points

def determine_winner(user_choice, computer_choice):
    print("Twój wybór: ", user_choice)
    print("Wybór komputera: ", computer_choice)
    if user_choice==computer_choice:
        remis()
    elif user_choice=="papier" or user_choice=="p":
        if computer_choice=="kamień" or computer_choice=="k" or computer_choice=="kamien":
            wygrana()
        else:
            przegrana()
    elif user_choice=="kamień" or user_choice=="k" or user_choice=="kamien":
        if computer_choice=="nożyce" or computer_choice=="n" or computer_choice=="nozyce":
            wygrana()
        else:
            przegrana()
    elif user_choice=="nożyce" or user_choice=="n" or user_choice=="nozyce":
        if computer_choice=="papier" or computer_choice=="p":
            wygrana()
        else:
            przegrana()

def play_PKM():
    global punkty
    global wybor
    global rounds
    global points
    global enemy_points
    r_and_p()

    if wybor=='r':
        for i in range(rounds):
            user_choice=get_user_choice()
            computer_choice=get_computer_choice()
            determine_winner(user_choice, computer_choice)
    elif wybor=='p':
        while punkty<points and punkty>enemy_points:
            user_choice=get_user_choice()
            computer_choice=get_computer_choice()
            determine_winner(user_choice, computer_choice)
    if punkty==points:
        print('Wygrałeś Grę! Gratulacje! Zapraszamy ponownie!')
    elif punkty==enemy_points:
        print('Tym razem wygrał komputer. Spróbuj ponownie!')

    next_game=input("Czy chcesz zagrać ponownie? (T/N): \n")
    if next_game.lower()=="t":
        punkty=0
        play_PKM()
    elif next_game.lower()=="n":
        print("Koniec gry")
        print(f"Twój wynik to {punkty} punktów")
        quit()
    else:
        print("Nieprawidłowy wybór, zaczniemy gre od nowa.")
        play_PKM()
    

if __name__=="__main__":
    play_PKM()