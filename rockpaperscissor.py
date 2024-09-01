import random

options=['Rock','Paper','Scissor']
name=input("Enter your name :")
print(f"Welcome {name.title()} :)")
gameOn=True
playing=True

while playing:
    NumberOfRounds=0
    PlayerScore=ComputerScore=0
    while NumberOfRounds<=5:
        ComputerOption=random.choice(options)
        PlayerOption=input("Enter Rock/ Paper/ Scissor :").title()
        print(f"Computer option :{ComputerOption}")
        print(f"{name.title()} option :{PlayerOption}")
        NumberOfRounds += 1

        if ComputerOption==PlayerOption:
            print('Tie')

        elif (ComputerOption=='Rock' and PlayerOption == 'Scissor') or (ComputerOption=='Scissor' and PlayerOption=='Paper') or (ComputerOption=='Paper' and ComputerOption=='Rock'):
            print("Computer wins")
            ComputerScore += 1

        elif (PlayerOption=='Rock' and ComputerOption == 'Scissor') or (PlayerOption=='Scissor' and ComputerOption=='Paper') or (PlayerOption=='Paper' and ComputerOption=='Rock'):
            print(f"{name.title()} wins")
            PlayerScore += 1

        else:
            print("Choose a valid option to play this game.")
            NumberOfRounds -=1
        print("-------------------------")
        print("")
        print(f"Round No: {NumberOfRounds}")
        print("------ Score Board ------")
        print(f"{name.title()}: {PlayerScore} | Computer: {ComputerScore}")
        print("===============================")
        print("")

        if NumberOfRounds==5:
            gameOn=False
            break

        if PlayerScore==ComputerScore:
            print("Draw!!")

        elif PlayerScore>ComputerScore:
            print(f"Congrats {name.title()}, You won the game!!")

        else:
            print(f"Oops Computer won the game!! Better luck next time {name.title()}!")

    again=input('play again? (Y/N): ').lower()
    if not again =='y':
        playing=False
        print('Thanks for playing!')
