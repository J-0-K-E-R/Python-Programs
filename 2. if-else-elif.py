# This is game Rock, Paper Scissor using if else elif

flag = 1
p1 = 0
p2 = 0
while flag:
    print("""Rock/Paper/Scissor
              1. Play
              2. Exit""")
    choice = int(input())
    if choice > 0 & choice < 3:
        if choice == 1:
            while flag:
                print("""Player 1 Choose your option :
                        1. Rock
                        2. Paper
                        3. Scissor""")
                p1 = int(input())
                if p1 < 1 or p1 > 3:
                    print("\n\nPlease select a valid option(1-3)\n")
                else:
                    flag = 0
            flag = 1
            while flag:
                print("""Player 2 Choose your option :
                    1. Rock
                    2. Paper
                    3. Scissor""")
                p2 = int(input())
                if p2 < 1 or p2 > 3:
                    print("\n\nPlease select a valid option(1-3)\n")
                else:
                    flag = 0
            flag = 1
            print("Result :")
            if p1 == p2:
                print("\nIt's a draw!\n\n")
            elif p1 < p2:
                if p1 == 1 and p2 == 3:
                    print("Player 1 won!\n\n")
                else:
                    print("Player 2 won!\n\n")
            else:
                if p1 == 3 and p2 == 1:
                    print("Player 2 won!\n\n")
                else:
                    print("Player 1 won!\n\n")
        else:
            print("Exiting...")
            flag = 0
    else:
        print("Please enter valid option(1 or 2)\n\n")