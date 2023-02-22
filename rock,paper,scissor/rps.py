import random

options = ("rock","paper","scissor")


you_count = 0
computer_count = 0
playing = True 

while playing:

    you = None
    
    while you not in options:
        you = input("Enter a choice (rock,paper,scissor):")
        computer =random.choice(options)
    print(f"you:{you}")
    print(f"computer:{computer}")


    if you == computer:
        print("It's a tie")
    elif you == 'rock' and computer == 'scissor':
        print("you win!")
        you_count += 1
    elif you == 'paper' and computer == 'rock':
        print('you win!')
        you_count += 1
    elif you == 'scissor' and computer == 'paper':
        print('you win!')
        you_count += 1
    else:
        print('you lose')
        computer_count += 1
    play_again = input("play again ? (y/n): ").lower()
    if not play_again == 'y':
        playing = False

print('*************************')
print('* you won ',you_count,' games     *') 
print('*************************')

print('* computer won ',computer_count,' games*') 
print('*************************')
print('thanks for playing')