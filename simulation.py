import game
import actors
import random

def main():
    print("----------------------------------------------")
    print("        LET'S MAKE A DEAL SIMULATION")
    print("----------------------------------------------")

    run_again = 'y'

    while run_again.lower() in ['y', 'yes']:

        n = 10000
        player_A, player_B = run_main_loop(n)

        print("{} won {}% of the time.".format(player_A.name, round(player_A.num_wins/n, 4)*100))
        print("{} won {}% of the time.".format(player_B.name, round(player_B.num_wins/n, 4)*100))
        run_again = input("Would you like to run the simulation again? [y/n] ")

        while run_again not in ['y', 'n', 'yes', 'no']:
            print("Sorry, we didn't understand {}.".format(run_again))
            run_again = input("Would you like to run the simulation again? [y/n] ")


def run_main_loop(n):
    iter = 1
    while(iter <= n):
        # assign doors
        doors = game.assign_doors()
        # get player's name who wants to switch (we'll call player A)

        if iter==1:
            player_A_name, player_B_name = get_player_names()

            player_A = actors.Player(player_A_name)
            player_A.strategy('switch')
            player_B = actors.Player(player_B_name)
            player_B.strategy('stay')


        #get player's choice
        door_choice_id = choose_door()

        #Reveal goat
        goats = get_goats(doors, initial_choice=door_choice_id)
        random.shuffle(goats)
        goat = goats[0]

        #get remaining door
        rmn_door = game.remaining_door(door_choice_id, goat, doors)


        player_A.door_choice(rmn_door.id)
        player_B.door_choice(door_choice_id)

        #get winning door
        prize_door = winning_door(doors)

        #update records
        if player_A.choice == prize_door.id:
            player_A.num_wins +=1
        else:
            player_B.num_wins +=1


        if iter == n:
            return player_A, player_B

        iter += 1


def get_player_names():
    player_A_name = input("For the player who would like to switch, input your name? ")
    player_B_name = input("For the player who would like to switch, input your name? ")

    return player_A_name, player_B_name

def get_goats(doors, initial_choice):
    goats = []
    for d in doors:
        if d.prize == 'goat' and d.id != initial_choice:
            goats.append(d)
        else:
            continue

    return goats

def choose_door():
    door_nums = [1,2,3]

    random.shuffle(door_nums)

    door_choice_id = door_nums.pop()

    return door_choice_id

def winning_door(doors):
    for door in doors:
        if door.prize != 'goat':
            return door
        else:
            continue


if __name__ == '__main__':
    main()