a = input("Введите пароль: ")
while a != 0:
    if len(a) > 0:
        if int(len(a)) < 8:
            print('Короткий пароль')
            a = input("Введите пароль: ")

        for i in a:
            if i !=("1"):
                break
        else:
            print("В пароле должны быть цифры")
            break

        for i in a:
            if i != ("A"):
                continue
            break
        else:
            print("В пароле должны быть буквы из верхнего регистра")
            break
        for i in a:
            if i != ("a"):
                continue
        else:
            print("В пароле должны быть буквы из нижнего регистра")
            break
    else:
        print("Вы ничего не ввели.Введите пароль")
        break
