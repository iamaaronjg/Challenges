wordToReverse = input('Enter a word to reverse: ')

i = 0
palindrome = ''
userInputLength = len(wordToReverse)

for letter in wordToReverse:
    palindrome += wordToReverse[(userInputLength - 1) - i]
    i += 1

print(palindrome)