#Парсинг в Python – это метод извлечения большого количества данных с нескольких веб-сайтов.
#Термин «парсинг» относится к получению информации из другого источника (веб-страницы)
#и сохранению ее в локальном файле.

person={}
s= "IVANOV IVAN Samara SGU 5 3 5 5 4 3 5"
s=s.split()
person["lastName"]= s[0]
person["firstName"]= s[1]
person["city"]= s[2]
person["university"]= s[3]
person["marks"] = []
for i in s[4:]:
	person["marks"].append(int(i))
print(person)




#

#d={
	#key:valye,
#	1:"one",
#	2:"two",
#	3:"three"
#}
#d[4]="four"
#print(d[2])

