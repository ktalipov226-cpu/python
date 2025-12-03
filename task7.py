#Задание 1 
table = [
    ['folder', 'coursework.doc', 'folder', 'pict.png', 'data.accdb'],
    ['icon.ico', 'script.js', 'index.html', 'style.css', 'prog.py'],
    ['my_song.mp3', 'anapa-2003.jpg', 'cs_1.6.exe', 'folder', 'cheat.txt'],
    ['notes.txt', 'main.py', 'work.pdf', 'cartoon.mp4', 'array.py'],
    ['project.psd', 'cycle.py', 'folder', 'cycle.js', 'turtle.py']
]


print("1. Исходный массив:")
for row in table:
    print(row)
print()


modified_table = []
for row in table:
    new_row = []
    for item in row:
        if item != 'folder':
            if item == 'data.accdb':
                new_row.append('data.sql')
            else:
                new_row.append(item)
    modified_table.append(new_row)

print("2. Массив после удаления папок и замены data.accdb:")
for row in modified_table:
    print(row)
print()


py_files = []
for row in table:
    for item in row:
        if item.endswith('.py'):
            py_files.append(item)

print("3. Файлы с расширением .py:")
print(py_files)
print()


js_files = []
for row in table:
    for item in row:
        if item.endswith('.js'):
            js_files.append('new_' + item)

print("4. Файлы с расширением .js с префиксом 'new_':")
print(js_files)

#Задание 2
word_numb = ["ноль","один","два","три","четыри","пять","шесть","семь","восемь","девять"]

n = int(input("Введите число от 0 до 9: "))

if 0 <= n <= 9:
  for i in range(n + 1):
    print(word_numb[i])
else:
  print('Введите число <= 9') 

#Задание 3
bin_sy = ['11011111', '11011101', '11000111', '11011100', '11011110']
becimal_number = []
print("Элементы списка в десятичной системе счисления:")
for binary in bin_sy:
  becima1 = int(binary, 2)
  becima1_numbers.append(becimal)
  print(f"{binary} = {decimal}")
max_number = max(decimal_numbers)
min_number + min(decimal_numbers)
print(f"\nМаксимальное число: {max_number}")
print(f"Минимальное число: {min_number}")

#Задание 4
random_elements = [['toy', 'bee', 'cheese', 'ear'],
                   [False, 'word', '0110110', 10],
                   ['happiness', 'luck', None],
                   ['car', '<- code ->', 4.7, True],
for index, element in enumerate(random_elements)
                   if index % 2 == 1:
                      print(element)
                   
