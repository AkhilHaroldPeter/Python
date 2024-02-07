# BLACKJACK


### The code for generating cards as ASCII characters was borrowed from the following source: https://copyprogramming.com/howto/ascii-fication-of-playing-cards.

### To play blackjack, please click here : https://replit.com/@akhilpeter/Project7-Blackjack?v=1


## Description

Welcome to the Blackjack game! This project implements a simple text-based version of the classic casino card game Blackjack. Test your luck and skills against the dealer as you aim to reach 21 without busting!
The goal is to assemble a hand with a total value surpassing that of the dealer's without exceeding 21. Cards with face values of Kings, Queens, Jacks, and Tens are assigned a value of 10 each. An Ace holds a value of either 1 or 11. All other cards retain their face values in the counting process.

## How to Play

1. **Start the Game**: Launch the Blackjack game.

2. **Deal Cards**: The game will deal two cards to each player (you and the dealer). One of the dealer's cards will be face up, and the other will be face down.

3. **Make Your Moves**: You will have the following options:
   - **Hit**: Take an additional card to try to improve your hand.
   - **Stand**: Keep your current hand and end your turn.
   - **Double Down**: Double your initial bet and receive one more card.
   - **Split**: If you have two cards of the same rank, split them into two separate hands.

4. **Dealer's Turn**: Once you've completed your moves, the dealer will reveal their face-down card and take additional cards according to the house rules (typically hit until reaching a total of 17 or higher).

5. **Compare Hands**: After the dealer's turn, compare your hand with the dealer's hand to determine the winner. The winner is the one with the highest total value without busting (going over 21).

6. **End of Round**: The round ends, and you can choose to play again or quit the game.

## Rules

- The objective of Blackjack is to beat the dealer's hand without going over 21.
- Aces can be counted as 1 or 11 points, face cards (King, Queen, Jack) count as 10 points, and all other cards count as their face value.
- If the total value of your hand exceeds 21, you bust and lose the round.
- If the dealer busts, you win the round.
- If both you and the dealer have the same total value, it's a push (tie), and you neither win nor lose your bet.
- Blackjack (an Ace and a 10-point card) pays 3:2.

## Key Concepts

1. **Card Deck**: Implementing a deck of cards containing suits (hearts, diamonds, clubs, spades) and ranks (2 through Ace) to simulate a standard deck used in Blackjack.
2. **Card Values**: Assigning values to cards based on Blackjack rules, including special cases for Aces.
3. **Game Logic**: Implementing game logic to manage player actions, dealer's moves, hand comparisons, and determining winners.
4. **User Input Handling**: Handling user input to interpret player actions during their turn (hit, stand, double down, split).
5. **Randomization**: Utilizing randomness to shuffle the deck and deal cards, ensuring fair gameplay.

Enjoy playing Blackjack and may the odds be ever in your favor!
