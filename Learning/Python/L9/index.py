# Introduction to Lists in Python

# lst1 = [0,3,5,6,7,3,1]
# lst2 = ["Taha", "Owais", "Saim"]

# print(lst1)
# print(lst2)

# lst1 = [0,3,5,6,3,1]

# if 7 in lst1:
#     print("Yes 7 in list ")
# else:
#     print("NO")


# LIST METHODS :-

# APPEND  -> LAST VALUE ADD 
# l = [2,5,4,8,4,3,5]
# l.append(9)
# print(l)

# SORT   -> VALUE SORTING 

# l = [99,3,5,2,8,5]
# l.sort()
# print(l)

# SORT REVERSE :

# l = [99,3,5,2,8,5]
# l.sort(reverse=True)
# print(l)

# REVERSE : 

# l = [99,3,5,2,8,5,89]
# l.reverse()
# print(l)


# COPY 

# l = [99,3,5,2,8,5]
# l.sort()
# print(l)

# m = l.copy()
# m[3] = 0
# print(m)


# COUNT : 

# l = [99,3,5,2,8,5]
# print(l.count(5))

# INDEX :- 

# l = [99,3,5,2,8,5]
# print(l.index(3))

# INSERT :-

# l = [99,3,5,2,8,5]
# print(l.insert(1,899))
# print(l)

# EXTENDS :-

l = [99,3,5,2,8,5]
print(l)

m = [900, 1000, 4500, 547]
l.extend(m)
print(l)