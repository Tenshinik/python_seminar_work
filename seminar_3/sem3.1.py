seasons_list = ['зима','весна','лето','осень']
month = int(input('Введите число месяца'))
if month > 11:
    month = 0
print(seasons_list[month // 3]) 
seasons_dict = {1 : 'зима', 2 : 'зима', 3 : 'весна', 4 : 'весна', 5 : 'весна', 6 : 'лето', 7 : 'лето', 8 : 'лето', 9 : 'осень', 10 : 'осень', 11 : 'осень', 0 : 'зима'}
print(seasons_dict[month])
