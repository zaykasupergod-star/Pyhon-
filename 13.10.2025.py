#list1=[1,3,8]
#print(list1)
#counter=0
#for i in range (len(list1)):
#    for j in range(len(list1)):
#        if i==j:
#          continue
#        if list1[i]==list1[j]:
#            counter+=1
#            break
#print(len(list1)-counter)

#for i in range (0,6):
#    if list1[i]%2==0:
#        list1[i]=0
#print(list1)
#for i in list1:
#    print(i, end="

#for i in range (len(list1)//2):
#    list1[i],list1(len(list1)-i)
#           if i==j:
#print(len(list1) )
#summa=0
#for i in range(len(list1)):
#    summa+=list1[i]
#print(summa/len(list1))
#for i in list1:
#    summa+=i
#print(summa/len(list1))
#list2=[2,8,9,6,7]
#counter=0
#for i in range (len(list1)):
#    for j in range (len(list2)):
#        if i==j:
#           continue
#        if list1[i] == list2[j]:
#           counter+=1
#           break
#print(len(list1)-counter)
#for i in list1:
#    for j in list2:
#        if i==j:
#          print(i,end=" ")
#break

#numbers=int(input("введите число"))
#counter=0
#for i in list1:
#    if i==numbers:
#        counter+=1
#print((counter))
while True:
   try:
       num=int(input("ВВедите число"))
       break
   except:
        print("Неккоректный ввод")
print(num)
