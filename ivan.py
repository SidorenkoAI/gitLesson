import random
from random import randint
import time

print("Заранее предупреждаю, это тестовая версия кода и врятли будет работать правильно\n")

def gen_capcha(lenght):
	return "".join((chr(randint(65, 90)) + chr(randint(48, 57)) + chr(randint(97, 122))) for _ in range(lenght))

tooz = 11
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, tooz]

user_balance = 5000
attempt = 2
login = (gen_capcha(3)[:-2])
time_leave = 5

print(f'Приветствуем, вы попали на страницу входа в систему *******')
time.sleep(1)
print(f'Для продолжения введите имя пользователя и сгенерированный логин-ключ: {login}')
time.sleep(1)
enter_name = input('Имя пользователя: ')
enter_login = input('Логин-ключ: ')

if enter_name == "":
	enter_name = "User"
else:
	pass

if enter_login != login:
	while attempt > 0:
		if enter_login == login:
			break



		if attempt == 2:
			print(f'У вас осталось {attempt} попытки входа')
		elif attempt == 1:
			print(f'У вас осталось {attempt} попытка входа')
		enter_login = input(f'Логин-ключ: ')
		attempt -= 1
		time.sleep(1)
print('Проверка введеных данных...')
time.sleep(1)
print('Успешно')
time.sleep(1)
print(f'{enter_name}, добро пожаловать в систему PALADIN ')
time.sleep(1)
while user_balance != 0:
	print(f'Ваш баланс {user_balance}')
	time.sleep(1)
	black_start = input('Желаете сыграть в Блэкджек? \n[да / нет]: ')
	if black_start == "нет":
		time.sleep(1)
		print('Отказ принят, выход из системы через:')
		while time_leave > 0:
			print(f'{time_leave}с')
			time_leave -= 1
			time.sleep(1)
		break

	elif black_start == "да":
		time.sleep(1)
		player_stavka = int(input('Введите свою ставку: '))
		user_balance = user_balance - player_stavka
		time.sleep(1)
		print(f'Ставка в {player_stavka} принята, запуск игры через:')
		while time_leave > 0:
			print(f'{time_leave}с')
			time_leave -= 1
			time.sleep(1)
		time.sleep(1)
		print('Партия началась')
		time.sleep(1)
	while True:
		player_point = random.choice(numbers)
		pc_point = random.choice(numbers)

		if (player_point or pc_point) > 10:
			tooz = 1
		elif (player_point or pc_point) < 11:
			tooz = 11

		print(f'Ваш счет: {player_point}, счет диллера: {pc_point}')
		if ((player_point and pc_point) and (player_point > pc_point)) < 21:
			print(f'Желаете взять еще карту или забрать свой выигрыш в размере {player_stavka} ?')
			vopros1 = input('[карта / выигрыш]')
			time.sleep(1)
			if vopros1 == "выигрыш":
				user_balance = user_balance + player_stavka
				print('Раунд завершен, выигрышь начислен на ваш счет')
				break
			if vopros1 == "карта":
				player_point = player_point + random.choice(numbers)
				print(f'Ваш счет: {player_point}, счет диллера: {pc_point}')
				print(f"Желаете взять еще карту или забрать свой выигрыш в размере {player_stavka} ?")
				v = input(": ")
