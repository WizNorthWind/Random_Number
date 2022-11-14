from random import randrange

def is_valid(num):
    return num.isdigit() and 1 <= int(num) <= int(edge)

def maingame():
    while True:
        global edge
        edge = input('Для победы в игре угадай число от 1 до "введите желаемое значение, которое больше 0" - ')
        if edge.isdigit() and int(edge) > 0:
            edge = int(edge)
            break
        else:
            print('Введено неверное значение')
            continue

    random_number = randrange(1, edge + 1)
    count = 0

    while True:
        entered_number = input('Мы загадали цифру, угадай какую? ')
        if not is_valid(entered_number):
            print('А может быть все-таки введем число из заданного числового отрезка?')
            continue
        else:
            entered_number = int(entered_number)

        if entered_number > random_number:
            count += 1
            print('Слишком много, попробуйте еще раз')
            continue
        elif entered_number < random_number:
            count += 1
            print('Слишком мало, попробуйте еще раз')
            continue
        else:
            count += 1
            print('Вы угадали, поздравляем! \nКоличество корректных попыток составило -', count)
            break

print('Добро пожаловать в числовую угадайку!')

while True:
    maingame()
    print('Еще разок?')
    restart = input('Нажмите Да(Д) или Yes(Y) для повтора!')
    if restart.lower() in ('да', 'д', 'yes', 'y'):
        continue
    else:
        break

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
print()
print()
print('product by Andrey \ntelegram contact @Northwiz_best')
input()