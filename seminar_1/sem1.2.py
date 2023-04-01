'Узнайте у пользователя целое положительное число n. Найти сумму чисел n+nn+nnn'


n = int(input("Введите свое число - "))
total = (n + int(str(n) + str(n)) + int(str(n) + str(n)+ str(n)))
print("Сумма чисел n + nn + nnn - %d" % total)