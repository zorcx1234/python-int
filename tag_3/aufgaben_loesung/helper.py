vowels = ["a", "e"]
word = "hasfdjaskfdjsadklfjasdljadslfökj"
[char for char in word if word in vowels]


word = "a334b"
y = "".join([char for char in word if char.isdigit()])
print(y)

from typing import Iterable

x = 3
print(isinstance([1, 2], Iterable))

import time

# start = time.perf_counter()
# for .....
# end = time.perf_counter()
# print(end - start)
