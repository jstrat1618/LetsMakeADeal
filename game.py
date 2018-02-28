import random
from actors import Door


def main():
    play_again ='y'

    while play_again in ['y', 'yes']:
        run_main_loop()

        play_again = input("Would you like to play again? [y/n] ")

        while play_again.lower() not in ['y', 'yes', 'n', 'no']:
            print('Sorry we didn\'t understand "{}".'.format(play_again))
            play_again = input("Would you like to play again? [y/n] ")

        play_again = play_again.lower()


def run_main_loop():
    # print header
    print_header()
    #get player name
    name = get_player_name()
    print("Hello, {}!".format(name))
    #assign doors
    doors = assign_doors()
    #ask player to choose a door
    first_choice = get_players_first_choice()
    #reveal goat
    goat_doors = get_goat_doors(first_choice, doors)
    goats = get_goat(goat_doors, first_choice)
    goat = goats[0]
    print(goat)
    #get remaining doors
    rmn_door_id = remaining_door_id(first_choice, goat.id, doors)
    print("Door {} remains".format(rmn_door_id))
    #ask play if he/she would like to switch
    answer = decide_to_switch()
    #determine players final choice
    players_choice_id = players_final_choice(answer, first_choice, rmn_door_id)
    print("You choice is Door Number {}".format(players_choice_id))
    final_door = get_final_door(players_choice_id, doors)
    print(final_door)
    print_outcome(final_door)


def print_header():
    print("-------------------------------------")
    print("             Let's Make a Deal       ")
    print("-------------------------------------")


def get_player_name():
    name = input("What's is your name? ")
    return name

def assign_doors():
    prizes = ['goat', 'goat', 'prize']
    random.shuffle(prizes)

    door1 = Door(1,prizes[0])
    door2 = Door(2,prizes[1])
    door3 = Door(3,prizes[2])

    return [door1, door2, door3]

def get_goat_doors(first_choice, doors):
    goat_doors = [d for d in doors if d.prize =='goat' and d.id != first_choice]

    return goat_doors

def get_players_first_choice():
    choice = input("Which door would you like to choose: [1], [2] or [3]? ")

    choice = choice.strip()
    choice = int(choice)

    return choice

def get_goat(goat_doors, first_choice):
    random.shuffle(goat_doors)
    goat_doors = [door for door in goat_doors if door.id != first_choice]
    return goat_doors

def decide_to_switch():
    answer = 'h'

    while answer not in ['yes', 'y', 'n', 'no']:
        answer = input("Would you like to switch [Y]/[N]? ")
        answer = answer.strip()

        if answer.lower() in ["y", "yes"]:
            return "yes"
        elif answer.lower() in ["n", "no"]:
            return "no"
        else:
            print("Sorry, we didn't understand {}".format(answer))



def players_final_choice(answer, first_choice, remaining_door_id):

    player_choice_id = remaining_door_id if answer == 'yes' else first_choice

    return player_choice_id


def remaining_door_id(first_choice, goat_id, doors):
    for door in doors:
        if door.id != first_choice and door.id != goat_id:
            return door.id
        else:
            continue

def get_final_door(players_choice_id, doors):
    for door in doors:
        if door.id == players_choice_id:
            return door
        else:
            continue

def print_outcome(final_door):
    if final_door.prize == 'prize':
        print("Congradulations!!!!")
        print("YOU WON!!!!!!!!!!!!!!!!!")
    else:
        print("Sorry, you lost :(")



if __name__ == '__main__':
    main()