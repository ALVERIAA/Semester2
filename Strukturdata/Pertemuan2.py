#pertemuan 2, list

import sys
animals:list[str] = ["cat"]
print(animals)
print(sys.getsizeof(animals))

#menambahkan elemen ke dalam list
animals.append("dog")
print(animals)
print(sys.getsizeof(animals))

animals.insert(0, "bird")
print(animals)
print(sys.getsizeof(animals))

animals.append("fish")
print(animals)
print(sys.getsizeof(animals))

animals.append("horse")
print(animals)
print(sys.getsizeof(animals))

animals.append("elephant")
print(animals)
print(sys.getsizeof(animals))

animals.append("monkey")
print(animals)
print(sys.getsizeof(animals))

animals.append("turtle")
print(animals)
print(sys.getsizeof(animals))

animals.append("rabbit")
print(animals)
print(sys.getsizeof(animals))


#menghapus elemen dari list
animals.pop()
print(animals)
print(sys.getsizeof(animals))

animals.remove("dog")
print(animals)
print(sys.getsizeof(animals))

animals.reverse()
print(animals)
print(sys.getsizeof(animals))

numbers: list[int] = [3.60, 3.80, 3.60, 3.80, 3.60, 3.80, 3.60, 3.80]
print(sum(numbers))
print(len(numbers))
print(sys.getsizeof(numbers))
print(numbers)

backup_numbers: list[float] = numbers.copy()
print(backup_numbers)
print(sys.getsizeof(backup_numbers))