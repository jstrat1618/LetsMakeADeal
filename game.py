import random
import actors


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

    name = input("What's is your name? ")

    player = actors.Player(name=name)

    print("Hello, {}!".format(name))
    #assign doors
    doors = assign_doors()

    #ask player to choose a door
    first_choice = get_players_first_choice()
    player.door_choice(first_choice)

    #reveal goat
    goat_doors = get_goat_doors(player, doors)
    goats = get_goat(goat_doors, first_choice)
    goat = goats[0]
    print(goat)
    #get remaining doors
    rmn_door = remaining_door(first_choice, goat, doors)

    print("Door {} remains".format(rmn_door.id))
    #ask play if he/she would like to switch
    answer = decide_to_switch()

    player.strategy(answer)

    #determine players final choice
    final_choice_id = players_final_choice(player, rmn_door)
    player.door_choice(final_choice_id)

    print("You choice is Door Number {}".format(player.choice))
    final_door = get_final_door(player, doors)
    #final_door = final_door[0]
    print()
    print(final_door)
    print_outcome(final_door)


def print_header():
    print("-------------------------------------")
    print("             Let's Make a Deal       ")
    print("-------------------------------------")


def assign_doors():
    prizes = ['goat', 'goat', 'prize']
    random.shuffle(prizes)

    door1 = actors.Door(1,prizes[0])
    door2 = actors.Door(2,prizes[1])
    door3 = actors.Door(3,prizes[2])

    return [door1, door2, door3]

def get_goat_doors(player, doors):
    goat_doors = [d for d in doors if d.prize =='goat' and d.id != player.choice]

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

    while answer not in ['yes', 'y', 'n', 'no', 'stay', 'switch']:
        answer = input("Would you like to switch [Y]/[N]? ")
        answer = answer.strip()

        if answer.lower() in ["y", "yes", 'switch']:
            return "switch"
        elif answer.lower() in ["n", "no", 'stay']:
            return "stay"
        else:
            print("Sorry, we didn't understand {}".format(answer))



def players_final_choice(player, remaining_door):

    choice_id = remaining_door.id if player.answer == 'switch' else player.choice

    return choice_id


def remaining_door(first_choice, goat, doors):
    for door in doors:
        if door.id != first_choice and door.id != goat.id:
            return door
        else:
            continue

def get_final_door(player, doors):
    for door in doors:
        if door.id == player.choice:
            final_door = actors.Door(door.id, door.prize)
            return final_door
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
