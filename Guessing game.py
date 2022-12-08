# You have to guess my fav color. You only have 3 lives
color = 'red'
lives = 3
while lives > 0:
    guess = input('What is my favorite color? ')
    if guess.lower() != color:
        lives -= 1
        if lives > 1:
            print(f'you only have {lives} lives left')
        if lives == 1:
            print(f'you only have {lives} life left')
    else:
        print('Congratulations you win!')
        break

if lives == 0:
    print('You lost')
