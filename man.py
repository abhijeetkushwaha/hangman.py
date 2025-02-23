import random

word_chosen = ["balloon","apple", "orange", "banana", "grape", "pineapple", "watermelon"]
word = random.choice(word_chosen)
word_length = len(word)
display = []
for i in range(word_length):
  display += "_"
print(display)
counter = 10
while counter>0:
  guess = (input("\nGuess a letter: ")).lower()
  if guess not in word:
    counter -= 1  
    print(f"You have {counter} lives left")
  for pos in range(len(word)):
    letter = word[pos]
    if letter == guess:
      display[pos]=letter
  print(display)
  if "_" not in display:
    print("You win")
    break
if counter == 0:
  print("You lose")