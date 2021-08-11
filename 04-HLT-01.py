#vowels

word = input("Please enter a word ")

vowel = "aeiouAEIOU"

cont = 0

for i in vowel:
    if i in word:
        cont = 1
        break
    
if(cont==1): 
    print("Word contains vowel!")
else:
    print("word does not contain a vowel")