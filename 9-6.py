a=[1,2,3]                           #چیزایی که تو لیست اوله
b=[4,5,6]                         #اینم مثل لیست اول
c=[]                         #این خالیه
for i in  zip(a,b):              # میزاره کنار هم لیست بالا و پایینش رو 
    for j in i:                     #
      c.append(j)     #یکی یکی میکنه
print(c)                    #میریزه تو این