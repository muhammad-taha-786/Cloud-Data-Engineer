# Tuples :-

# tup1 = (1,3,5,7,8)
# tup2 = ("Red", "Blue", "Green")

# print(tup1)
# print(tup2)

# Tuples does not changed
# tup1[0] = 900
# print(tup1)


# countries = ("Spain", "Italy", "India", "England")
# print(countries)
# print(type(countries))

# temp = list(countries)
# temp.append("Finland")  # -> Add item 
# temp.pop(2)     # -> Remove Item
# temp[0] = "Pakista"     # -> Change Item
# countries = tuple(temp)
# print(countries)


# TUPLES METHODS :-

tup1 = (0,1,2,13,4,5,6,2,4,3,4,3,3,3)
print(tup1)

res = tup1.count(3)
res = tup1.index(3)
res = len(tup1)
print(tup1)
print("3 in tuples is : ", res)