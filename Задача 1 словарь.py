#Задача#cлова сделать ключами,а числа- значениями.
a=["first", 1, 2, 3, "second", 10, 20, "third", 15, 56, 70, "fourth", -50]

my_dict={}
current_str=None

for e in a:
	if(type(e)==str):
		my_dict[e]=[]
		current_str=e
	else:
		my_dict[current_str].append(e)


print(my_dict)

#Задача 2#Узнать количество каждого слова  
my_text = "Привет пока как дела привет привет ну что и как угу привет"
my_dict2={}

for word in my_text.split():
	if word in my_dict2:
		my_dict2[word]= my_dict2[word]+ 1
	else:
		my_dict2[word]= 1

print(my_dict2)

#Узнаем сколько слов в стоке
v=len(set(my_text.split()))
print(v)



#Альтернативное решение

