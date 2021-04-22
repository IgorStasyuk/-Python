my_list = [7,5,3,3,2]
print('Введите новое значение рейтинга')
num = int(input())
for i in range(0,len(my_list)):
  if num <= my_list[i]: my_index = i+1
  if num > my_list[i]: my_index = 0

my_list.insert(my_index, num)    
print(my_list)
