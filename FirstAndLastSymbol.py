#Дана строка. Если в этой строке буква f встречается только один раз, выведите её индекс.
#  Если она встречается два и более раз, выведите индекс её первого и последнего появления. 
# Если буква f в данной строке не встречается, ничего не выводите. 
x=input()
if x.count('f')>1:
    print (x.find('f'),x.rfind('f'))
elif x.find('f')>-1:
    print (x.find('f'))