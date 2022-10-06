"""
                            Rock Paper Scissor Game
                                    (Only for fun)            
"""

while True:
    check = input("Do you want to play?(y/n): ")
    if check == 'y':
        p1 = input("Player 1: ")
        p2 = input("Player 2: ")
        if p1 == 'rock' and p2 == 'scissor':
            print("Player 1 is the winner!!!")
        elif p1 == 'scissor' and p2 == 'rock':
            print("Player 2 is the winner!!!")
        elif p1 == 'rock' and p2 == 'paper':
            print("Player 2 is the winner!!!")
        elif p1 == 'paper' and p2 == 'rock':
            print("Player 1 is the winner!!!")
        elif p1 == 'scissor' and p2 == 'paper':
            print("Player 1 is the winner!!!")
        elif p1 == 'paper' and p2 == 'scissor':
            print("Player 2 is the winner!!!")
        else:
            print("Both are same!!! Please try again!")
    else:
        print("Game exit!")
        break;