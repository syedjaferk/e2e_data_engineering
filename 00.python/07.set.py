rose_garden = {"red rose", "white rose", "red rose"}  # duplicate is dropped
print(len(rose_garden))
print(set(["rose", "tulip", "rose", "daisy"]) == {"rose", "tulip", "daisy"})
empty = set()  # NOT {} — that's an empty dictionary
print(type(empty), type({}))

# names = []
# marks = {}
# tuple = ()
# garden = set()
#
print("#" * 30)

rose = {"red rose", "white rose", "pink rose"}
botanical = {"sunflower", "tulip", "red rose"}

print("red rose" in botanical, "############")

print(sorted(rose | botanical), rose.union(botanical))  # union: in either
print(sorted(rose & botanical), rose.intersection(botanical))  # intersection: in both
print(sorted(rose - botanical), rose.difference(botanical))  # difference: only in rose
print(
    sorted(rose ^ botanical), rose.symmetric_difference(botanical)
)  # symmetric difference: in one, not both
