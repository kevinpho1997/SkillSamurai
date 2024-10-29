import random as rd

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
tempWord = ""

pwLength = 6

for i in range(pwLength):
    randomIndex = rd.randint(0, len(alphabet))
    tempWord = tempWord + alphabet[randomIndex]

finalWord = tempWord
print(finalWord)