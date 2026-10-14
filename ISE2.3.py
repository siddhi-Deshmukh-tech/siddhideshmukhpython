
group1 = ["Reading", "Gaming", "Cooking", "Reading", "Painting", "Music"]
group2 = ["Music", "Dancing", "Cooking", "Traveling", "Gaming", "Dancing"]


set1 = set(group1)
set2 = set(group2)

print("Unique hobbies in Group 1:", sorted(set1))
print("Unique hobbies in Group 2:", sorted(set2))


print("Union of hobbies:", sorted(set1 | set2))


print("Common hobbies:", sorted(set1 & set2))

print("Hobbies unique to Group 1:", sorted(set1 - set2))


print("Hobbies unique to Group 2:", sorted(set2 - set1))