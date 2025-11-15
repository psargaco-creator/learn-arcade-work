import random

MAX_ENERGY = 10
MAX_HYDRATION = 10
MAX_ROUNDS = 3

"""
    Checks the player's hydration status and prints a message accordingly.

    Returns true if the player died of dehidration 
"""
def is_dead_by_dehidration(Hydration_level:int, Days_to_die:int, Canteen_level:int) -> bool:
    if Hydration_level < MAX_HYDRATION/2 and Hydration_level > 0:
        if Canteen_level > 0:
            print("Aren't you feeling thirsty? You can live three days without water, but do you really want to?")
        if Canteen_level == 0:
            print("I bet your tongue is feeling as dry as this desert. ", end=" ")
            print("If only you hadn't exhausted your canteen... ")
            print(f"{Days_to_die} more days and you'll die of thirst.")
    if Hydration_level == 0:
        if Days_to_die > 0:
            print(f"""The only thing you can think of is water. But your canteen is as dry 
                as your mouth and you only have {Days_to_die} days before you die of thirst""")
        else:
            print("I have terrible news! I'm afraid you died of dehidration." \
            "On hindsight, stealing the camel may not have been your best idea." \
            "But you had a good run.")
    return (Days_to_die == 0)

def is_caught(dist:int) -> bool:
    if dist > 0:
        print("""
Your camel gave its best, but I'm afraid the natives have caught you.
The natives have tied and slung you belly down over your camel's back.
You can hear the natives discuss what they'll do to you, but luckily you don't understand their language.
But don't worry, you'll find out soon enough.""")     
    return dist >= 0

def is_safe(dist:int) -> bool:
    if dist <= 0:
        print("You did it! You reached a military outpost and the natives have given up on the pursuit. You'll have a great story to tell your grandchildren one day.")
    return dist <= 0

"""
    Determines if it is day or night and decreases the number of
    rounds to play in the day or night depending on the user choice.

    All choices result in one round being decreased with two exceptions:
    1. Checking the status has no impact on the number of rounds.
    2. Choice E, "Stop for the night", takes the user to a new day.

    If the number of rounds reaches the limit, day switches to night and vice-
    versa, and the number of rounds is reset. 

    Returns a tuple with the resulting number of rounds and the boolean for day or night
"""
def day_or_night(Current_rounds:int, Is_day:bool, User_choice:str) -> tuple[int, int]:
    match User_choice:
        case "F":
            Current_rounds = MAX_ROUNDS
            Is_day = True        # If we're pausing for the night, then a new day will start
        case _:
            Current_rounds -= 1
            if Is_day:        
                if Current_rounds == 0:
                    Is_day = False
                    print("Night has arrived.")
                    Current_rounds = MAX_ROUNDS
            else:
                if Current_rounds == 0:
                    Is_day = True
                    print("The sun just rose.")
                    Current_rounds = MAX_ROUNDS
    return Current_rounds, Is_day

def is_camel_dead(camel:int) -> bool: 
    Dead:bool = False   
    if camel < MAX_ENERGY/2 and camel > 0:
        print("Your camel is showing signs of being tired. Remember, without a camel you won't last long in this desert.")
        Dead = False
    if camel <= 0:
        print("As you may have noticed by the fact that your camel is lying on the ground with its tongue out, " \
        "you have managed to kill it.")
        print("Now that you will be on foot in the middle of the desert, I wonder which will come first: death or capture? " \
        "Anyway, this game is called Camel, and without a camel it is not fun. I'm pronouncing you dead.")
        Dead = True
    return Dead

def main():    
    Kms_traveled:int = 0
    Hydration:int = 10
    Camel_energy:int = 10
    Dist_from_natives:int = -20
    Canteen:int = 3
    Safety:int = 75
    Days_to_die_of_thirst:int = 3
    Rounds:int = MAX_ROUNDS
    Day:bool = True

    print("""Welcome to Camel!
You have stolen  a camel to make your way across the great Mobi desert.
The natives want their camel back and are chasing you down! Survive your
desert trek and outrun the natives"""
          )    
    Done:bool = False    
    while not(Done):
        print("""
A. Drink from your canteen.
B. Ahead slow speed
C. Ahead moderate speed.
D. Ahead full speed.
E. Stop for the night.
F. Status check.
Q. Quit.              
"""
              )
        print("What is your choice? ")
        Choice:str = input()
        match Choice.upper():
            case "A":                       # A. Drink from your canteen.
                Natives_kms = random.randrange(10, 20)
                Dist_from_natives += Natives_kms
                if Canteen > 0:
                    Hydration += 1
                    Canteen -= 1
                else:
                    print("Ah, wouldn't it be wonderful if you had some water? Unfortunately you", end= " ")
                    print("didn't manage your canteen very well and it is with a sense of dread that you put the canteen to your mouth", end=" ")
                    print("and realise there's nothing in it.")
                    Hydration -= 1
                
                res = day_or_night(Rounds, Day, Choice.upper())
                Rounds = res[0]
                Day = res[1]
                Done = is_dead_by_dehidration(Hydration, Days_to_die_of_thirst, Canteen)
                if not Done:
                    Done = is_caught(Dist_from_natives)
                if not Done:
                    print("Fiddling with your canteen resulted in losing ground to " \
                    "your pursuers.")
                    print(f"They are now {-Dist_from_natives} kms from you.")
                                    
            case "B":                       # B. Slow speed.                
                res = day_or_night(Rounds, Day, Choice.upper())
                Rounds = res[0]
                Day = [1]
                My_kms = random.randrange(3,5)
                if Day:                                        
                    Natives_kms = random.randrange(10, 20)                    
                    print("You do well to conserve you camel's energy. " \
                    "Just mind the distance to your pursuers.")                    
                else:
                    Natives_kms = random.randrange(1, 3)
                    print("Traveling at night is dangerous, but at least you'll increase " \
                    "your distance to the natives.")
                
                Hydration -= 1
                Camel_energy -= 1                
                Kms_traveled += My_kms              
                Safety -= My_kms     
                Dist_from_natives += Natives_kms - My_kms 
                Done = is_safe(Safety)
                if not Done:
                    Done = is_caught(Dist_from_natives)    
                if not Done:
                    Done = is_camel_dead(Camel_energy)
                if not Done:
                    Done = is_dead_by_dehidration(Hydration, Days_to_die_of_thirst, Canteen)
                if not Done:
                    print(f"You have travelled {Kms_traveled} kms and the natives are {-Dist_from_natives} kms from you.")                        
                
            case "C":                       #C. Moderate speed
                res = day_or_night(Rounds, Day, Choice.upper())
                Rounds = res[0]
                Day = [1]
                if Day:                    
                    My_kms = random.randrange(7,14)
                    Natives_kms = random.randrange(10, 20)                    
                    Dist_from_natives += Natives_kms - My_kms
                    Kms_traveled += My_kms
                    Safety -= My_kms
                    Hydration -= 1
                    Camel_energy -= random.randrange(1, 2)
                    Done = is_safe(Safety)
                    if not Done:
                        Done = is_caught(Dist_from_natives)    
                    if not Done:
                        Done = is_camel_dead(Camel_energy)
                    if not Done:
                        Done = is_dead_by_dehidration(Hydration, Days_to_die_of_thirst, Canteen)
                    if not Done:
                        print(f"You have travelled {Kms_traveled} kms and the natives are {-Dist_from_natives} kms from you.")                        
                        
                else:
                    print("The night has fallen and is too dark to ride faster than at slow pace. Choose options B or E.")
            
            case "D":                       #C. Ahead full speed
                res = day_or_night(Rounds, Day, Choice.upper())
                Rounds = res[0]
                Day = [1]
                if Day:                    
                    My_kms = random.randrange(15,25)
                    Natives_kms = random.randrange(10, 20)                    
                    Dist_from_natives += Natives_kms - My_kms
                    Kms_traveled += My_kms
                    Safety -= My_kms
                    Hydration -= 2
                    Camel_energy -= random.randrange(2, 4)
                    Done = is_safe(Safety)
                    if not Done:
                        Done = is_caught(Dist_from_natives)    
                    if not Done:
                        Done = is_camel_dead(Camel_energy)
                    if not Done:
                        Done = is_dead_by_dehidration(Hydration, Days_to_die_of_thirst, Canteen)
                    if not Done:
                        print(f"You have travelled {Kms_traveled} kms and the natives are {-Dist_from_natives} kms from you.")                        
                        
                else:
                    print("The night has fallen and is too dark to ride faster than at slow pace. Choose options B or E.")

            case "E":                       # E. Stop for the night
                day_or_night(MAX_ROUNDS, Day,Choice)
                Camel_energy = MAX_ENERGY
                Dist_from_natives += random.randrange(1, 5)
                if Dist_from_natives >= 0:
                    print("""Your camel is fully rested and happy, but unfortunaltely you overslept and the natives have caught you.
Resting is good, but not having been caught would have been better.
The natives have tied you and you are now lying unconfortably over your camel's back.
The natives discuss what they'll do to you, but luckily you don't understand their language.
Well, you'll find out soon enough.""")
                    Done = True
                else:
                    print(f"Your camel is fully rested and happy, but the natives are now {-Dist_from_natives} from you")
            
            case "F":                       # F. Status check.
                print(f"""You have travelled {Kms_traveled} kms, there are {Canteen} drinks in the canteen, 
                      and the natives are {-Dist_from_natives} kms from you.""")
            case "Q":
                Done = True
                
    print("Thank you for playing camel :-). See you next time!")
    
main()