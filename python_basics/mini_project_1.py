import random as r

while True:
    print("Keling 1 dan 10gacha o'ylangan sonni topish o'yini o'ynaymiz.")
    print("Birinchi men son o'ylayman, siz topishga harakat qilasiz")

    num1 = r.randint(1,10)
    guess_num = int(input("O'yladim, topishga harakat qilib ko'ringchi? "))
    tries = 1

    while guess_num != num1 :
        if guess_num < num1 :
            print(f"O'ylagan sonim {guess_num}dan katta. Yana harakat qilib ko'ring.")
            guess_num = int(input())
            tries += 1
        elif guess_num > num1 :
            print(f"O'ylagan sonim {guess_num}dan kichik. Yana harakat qilib ko'ring.")
            guess_num = int(input())
            tries += 1

    print(f"To'g'ri topdingiz. Men {num1} sonini o'ylagan edim. Tabriklayman!!")     
    print(f"Siz {tries} urinishda topdingiz!\n")   
            

    print("Endi siz son o'ylang. Men topishga harakat qilaman. ")
    input("Davom ettirish uchun xohlagan tugmani bosing.")

    tries_comp = 1
    guess_num_comp = r.randint(1,11)
    max = 10
    min = 1


    print(f"O'ylagan raqamingiz {guess_num_comp}mi? (Agar o'ylagan raqamingiz kichikroq bo'lsa (-), to'g'ri bo'lsa (t), kattaroq bo'lsa (+) bosing)")
    answer = input()

    while answer != 't' :
        tries_comp += 1
        if answer == '+' :
            min = guess_num_comp +1
            
        elif answer == '-' :
            max = guess_num_comp - 1
            
        guess_num_comp = r.randint(min,max)
        print(f"O'ylagan raqamingiz {guess_num_comp}mi? (Agar o'ylagan raqamingiz kichikroq bo'lsa (-),\n to'g'ri bo'lsa (t), kattaroq bo'lsa (+) bosing)")
        answer = input()

    print("Yesss, topdim!!")

    if tries == tries_comp :
        print(f"Ikkalamiz ham {guess_num} urinishda topdik. Durrang).")
    elif tries < tries_comp :
        print(f"Siz {tries} urinishda, men esa {tries_comp} urinishda topdim.")
        print("Demak, siz yutdingiz!!")
    else :
        print(f"Men {tries_comp} urinishda, siz esa {tries} urinishda topdingiz.")
        print("Demak, men yutdim!!")

    quest = input("Yana o'ynashni xohlaysizmi(ha\yo'q)? ")
    if quest == "yo'q" :
        break




