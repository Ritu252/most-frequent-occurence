s = input("enter the string:")
list1 = []
for i in s:
    list1.append(i)
list2 = []
for i in range(0,len(s)):
    x = list1.count(s[i])
    list2.append(x)
for ele in list1:
    if list1.count(ele)>1:
        list1.remove(ele)
        pass
        
for ele in list2:
    if list2.count(ele)>1:
        list2.remove(ele)
dict1 = {list1[i]:list2[i] for i in range(len(list2))}
x = sorted(dict1.items())
print(x)
