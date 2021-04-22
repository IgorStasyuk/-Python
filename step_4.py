print('Введите строку из нескольких слов через пробел')
str = input()
my_str = str.split()
for i in range(0,len(my_str)):
  print(i, '.', my_str[i][0:10], sep='')