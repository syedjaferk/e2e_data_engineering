# List
vowels = ["a", "e", "i", "o", "u", True, 90.89, ["a", "z"]]
print("Vowels ", vowels)
print("First char ", vowels[0])
print("Last Char ", vowels[-1])

vowels.append("H")
print(vowels)

vowels.insert(1, "G")
print(vowels)
vowels[1] = "C"
print(vowels)

print(dir(vowels))
