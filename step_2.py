my_list = []
print('Введите количество элементов списка')
num = int(input())
print('Введите элементы списка')
for i in range(0,num):
  my_list.append(input()) 
print(my_list)  
for i in range(0,num // 2 * 2,2):
  my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
  
print(my_list)  