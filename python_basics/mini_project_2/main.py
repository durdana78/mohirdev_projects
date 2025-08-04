from uzwords import words
import random as r

word = r.choice(words)

chars = []
chars_found = []
chars_inserted = ''

for char in word :
    chars.append(char)

for n in range(len(word)) :
    chars_found.append('-')    


print(word)


while True:   
    print('"',end = '')
    for char in chars_found :
        print(char, end = '')
    print('"')    
 

    print("Try to guess the characters of the word")
    
    ans = input(">>>") 
    if ans not in chars_inserted:
        if ans in chars :
            for n in range(len(chars)) :
                if ans == chars[n] :
                    chars_found[n] = ans
        else :
            print("Try again") 
        chars_inserted += ans    
    else :
        print("you have already inserted this character.") 


    
    print("The characters you have used>>>",'"',chars_inserted,'"')            

    if '-' not in chars_found:
        break   


print(f"Congratulations! You found the word {word}")
print(f"The chars you have used>>>{chars_inserted}")

