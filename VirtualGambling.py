import random
import sys

print("                                                          ----------Virtual Gambling---------- ")
print("                                                  Where the only thing at risk is your WiFi connection!")
print("")
print("""rules: 1) We will roll our virtual die. If you guess it correctly, you will get double the amount you placed as a bet. If not, you will lose the money you placed as a bet""")
print("""rules: 2) You will be kicked out from our virtual casino if you enter an option other than 1, 2, 3 in the bet section and 1, 2, 3, 4, 5, 6 in guessing the number on the die""")
print("")
print("            Alert: Breaking rules will result in a mandatory virtual dance-off with our disco-loving security bots. Trust us, they've got moves!")
bank_bal = 100000

def gamble():
    global bank_bal
    rand_value = random.randint(1, 6)
    print("Die value:", rand_value)

    print("Your Bank Balance:", bank_bal)
    print("""Place your bets
             1. 10000
             2. 50000
             3. 100000 """)

    bet = int(input("Choose the bet amount: "))
    if bet not in [1, 2, 3]:
        print("Attention all rule-breakers: Prepare to face the music! Breaking our rules means you're about to engage in a mandatory virtual dance-off with our disco-loving security bots. They've got moves that'll make your pixelated head spin! So, if you're ready to boogie your way out of here, keep breaking those rules. Otherwise, play nice or prepare to be escorted to the virtual exit by our groove-savvy bouncers. ")
        sys.exit()

    if bet == 1:
        bet = 10000
    elif bet == 2:
        bet = 50000
    elif bet == 3:
        bet = 100000

    choice = int(input("Guess the value on the die: "))
    if choice < 1 or choice > 6:
        print("Attention all rule-breakers: Prepare to face the music! Breaking our rules means you're about to engage in a mandatory virtual dance-off with our disco-loving security bots. They've got moves that'll make your pixelated head spin! So, if you're ready to boogie your way out of here, keep breaking those rules. Otherwise, play nice or prepare to be escorted to the virtual exit by our groove-savvy bouncers. ")
        sys.exit()

    if choice == rand_value:
        winamt = bet * 2
        print("Congratulations! You won", winamt, "rupees")
        bank_bal += winamt
    else:
        print("You lost", bet, "rupees")
        bank_bal -= bet

while bank_bal > 0:
    gamble()
else:
    print("Game over! You are in debt. When life gives you debt from virtual gambling, just hit 'refresh' and hope for a miracle!")