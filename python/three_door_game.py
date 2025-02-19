import random as rd
    
def three_door_game(move: int, strategy: bool) -> bool:
    doors = rd.sample([0,1,2],3)
    result = False
    if doors[0] == move:
        if strategy == False:
            result = True
    else:
        if strategy == True:
            doors.pop(0)
            move = rd.choice(doors)
            if doors[0] == move:
                result = True
    return result

loop_size = 100000
strategy_a = 0
strategy_b = 0

for i in range(loop_size):
    if three_door_game(rd.choice([0,1,2]), False):
        strategy_a += 1
    if three_door_game(rd.choice([0,1,2]), True):
        strategy_b += 1

print("I played the three door problem a lot...", end="\n")
print("I won " + str(strategy_a) + " times without changing doors.", end="(")
print("{:.2f}".format(100 * strategy_a / loop_size), end="%)\n")
print("I won " + str(strategy_b) + " times changing doors.", end="(")
print("{:.2f}".format(100 * strategy_b / loop_size), end="%)\n")
