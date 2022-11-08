def rpsWinner(player1, player2):
    if player1 == player2:
        return 'tie'
    if player1 == 'rock' and player2 == 'paper':
        return 'player 2'
    elif player1 == 'rock' and player2 == 'scissors':
        return 'player 1'
    elif player1 == 'paper' and player2 == 'scissors':
        return 'player 2'
    elif player1 == 'paper' and player2 == 'rock':
        return 'player 1'
    elif player1 == 'scissors' and player2 == 'rock':
        return 'player 2'
    elif player1 == 'scissors' and  player2 == 'paper':
        return 'player 1'
    else: 
        return 'someone fucked up. Only lowercase rock, paper or scissors allowed'

one = input("Ready player one: ")
two = input("Ready player two: ")
print("The result is: " + rpsWinner(one, two))

assert rpsWinner('rock', 'paper') == 'player 2'

assert rpsWinner('rock', 'scissors') == 'player 1'

assert rpsWinner('paper', 'scissors') == 'player 2'

assert rpsWinner('paper', 'rock') == 'player 1'

assert rpsWinner('scissors', 'rock') == 'player 2'

assert rpsWinner('scissors', 'paper') == 'player 1'

assert rpsWinner('rock', 'rock') == 'tie'

assert rpsWinner('paper', 'paper') == 'tie'

assert rpsWinner('scissors', 'scissors') == 'tie'