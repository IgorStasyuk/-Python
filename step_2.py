print ('Введите время в секундах')
number = int(input())
print ('время в формате: чч:мм:сс')
print (number // 3600,':', number % 3600 // 60, ':', number % 60)