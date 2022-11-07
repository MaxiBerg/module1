a = input("Введите пароль: ")
while a != 0:
    if len(a) > 0:
        if int(len(a)) < 8:
            print('Короткий пароль')
            break
        elif a != ('0' and '1' and '2' and '3' and '4' and '5' and '6' and '7' and '8' and '9'):
            print('Пароль должен содержать цифры')
            break
        elif a != ("a" and "b"and "c" and"d" and"e" and"f" and"g"and "h" and"i"and "j"and "k" and"l" and"m" and"n" and"o" and"p"and "q"and "r" and"s" and"t" and"u"and "v" and"w"and "x"and "y"and "z"):
            print('Введите малые буквы')
            break
        elif a != ("A" "B" "C" "D" "E" "F" "G" "H" "I" "J" "K" "L" "M" "N" "O" "P" "Q" "R" "S" "T" "U" "V" "W" "X" "Y" "Z"):
            print('В пароле должны быть буквы из верхнего регистра')
            break
    else:
        print("Вы ничего не ввели.Введите пароль")
        break
