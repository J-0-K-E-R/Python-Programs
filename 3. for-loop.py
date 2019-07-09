from typing import List

sentence: List[str] = ['There', 'is', 'a', 'tree', 'on', 'top', 'of', 'the', 'hill.']

for f in sentence:
    print("Word in the list :", f)
    print("Length :", len(f))

for f in sentence[::2]:
    print("Word in the list :", f)
    print("Length :", len(f))

for f in sentence[::-3]:
    print("Word in the list :", f)
    print("Length :", len(f))

for i in range(0, 100, 10):
    print(i);