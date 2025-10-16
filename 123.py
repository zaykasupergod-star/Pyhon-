list1=[12,15,70,80,90]
#summa=0
#for i in list1:
#    summa+=i
#    print(summa, end=" ")

#summa=0
#for i in range(len(list1)):
#    summa+=i
#print(summa, end=" ")

#summa=0
#for i in list1:
#   if i%2==0:
#      summa+=1
#print(summa)
#
#for i in range (list1):
#for i in range(5,-1,-1):
#    print(list1[i],end=" ")

#max=list1[0]
#max_index=0
#for i in range(len(list1)):
#   if max<list1[i]:
#      max=list1[i]
#      max_index=i
#print(max_index)
_min=int(input("ВВедите первое число"))
_max=int(input("ВВедите первое число"))
if _min>_max:
  _min,_max=_max,_min
for i in list1:
    if _min<=i<=_max:
        print(i)