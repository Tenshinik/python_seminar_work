# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел
#(каждый элемент ряда меньше или равен предыдущему).
#У пользователя необходимо запрашивать новый элемент рейтинга.
#Если в рейтинге существуют элементы с одинаковыми значениями,
#то новый элемент с тем же значением должен разместиться после них

number = int(input("Enter number: "))
my_list = [9, 5, 3, 2, 1]
a = my_list.count(number)
for element in my_list:
    if a > 0:
        i = my_list.index(number)
        my_list.insert(i+a, number)
        break
    else:
        if number > element:
            j = my_list.index(element)
            my_list.insert(j, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)