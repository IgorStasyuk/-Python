my_list_f = list()
print('Введите количество товаров для ввода в систему')
num = int(input())

for i in range(1, num+1):
  print('Введите название товара №', i)
  str1 = input()
  print('Введите цену товара №', i)
  str2 = input()
  print('Введите количество товара №', i)
  str3 = input()
  print('Введите единицы измериния товара №', i)
  str4 = input()
  my_dict = dict(название=str1, цена=str2, количество=str3, ед=str4)
  my_tuple = (i, my_dict)
  my_list_f.append(my_tuple)

#print('выводим название товаров')

for i in range(0, num):
  print(my_list_f[i][2].get(1))

#print(my_list_f)