import random 

print('SCHERE STEIN PAPIER')
print('===================')

wins = 0
losses = 0
ties = 0

play = True 

result = (losses, wins, ties)

while play:
    print('('+str(wins)+' Siege, '+str(losses)+' Niederlagen, '+str(ties)+' Unentschieden)')
    while True:
        playerMove = input('Zug eingeben: (s)chere, (r)ock, (p)apier oder (q)uit')
        if playerMove == 'q':
            play = False
            break
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
             break
        print('Bitte einer der folgenden Buchstaben eingeben: r, p, s oder q.')
        
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPIER versus...')
    elif playerMove == 's':
        print('SCHERE versus...')
        
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPIER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCHERE')
        
    if playerMove == computerMove:
        print('Es ist ein unentschieden!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('Du hast gewonnen!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('Du hast gewonnen!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('Du hast gewonnen!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('Du hast verloren!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('Du hast verloren!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('Du hast verloren!')
        losses = losses + 1
        

if playerMove == "q":
    print('=========')
    print('GAME OVER')
    print('=========')
        
    if losses > wins and losses > ties:
        print('Du hast verloren!')
    elif wins > losses and wins > ties:
        print('Du hast gewonnen!')
    elif ties > wins and ties > losses:
        print('Es ist ein unentschieden!')
    elif wins == ties and ties > losses:
        print('Du hast eher gewonnen.')
    elif wins == losses and ties > wins:
        print('Es ist ein unentschieden!')
    elif losses == ties and ties > wins
        print('Du hast eher verloren.')
    elif losses == wins == ties
        print('Es ist ein Unentschieden.')
        

