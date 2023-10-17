heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

# get length of list
print(f"length of the list is {len(heros)}")

# add black panther to list
heros.append('black panther')
print(f"new list is: {heros}")

# remove black panther and add it after hulk instead
heros.pop()
index = heros.index('hulk')
heros.insert(index + 1, 'black panther')
print(f"new list is: {heros}")

# remove thor and hulk and replace with doctor strange
heros[1:3] = ['doctor strange']
print(f"updated list is: {heros}")

# Sort the heros list in alphabetical order
heros.sort()
print(f"sorted list is: {heros}")
