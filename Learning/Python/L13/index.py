# DICTIONARIES :-

# dic = {
#     "name" : "Syed Taha",
#     "age" : 25,
#     "Gender" : "Male"
# }
# print(dic)
# print(dic["name"])
# print(dic.keys())
# print(dic.values())
# print(dic.items())


# DICTIONARY METHODS :-

ep1 = {122:45, 123:89, 567:69}
ep2 = {222:67, 566:90}

print(ep1)
print(ep2)

ep1.update(ep2)
print(ep1)

ep1.pop(122)
print(ep1)

ep1.popitem()
print(ep1)

ep1.clear()
print(ep1)