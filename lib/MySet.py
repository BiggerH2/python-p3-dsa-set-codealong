class MySet:

    def __init__(self, enumerable=[]):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary

    def __str__(self):
        set_list = []
        for key, value in self.dictionary.items():
            set_list.append(str(key))
        return f'MySet: {{{",".join(set_list)}}}'

    def add(self, value):
        self.dictionary[value] = True  # Add a value as a key on the Dictionary
        return self

    def delete(self, value):
        self.dictionary.pop(value, None)
        return self

    def size(self):
        return len(self.dictionary)

    def clear(self):
        self.dictionary.clear()

# Testing the implementation
if __name__ == "__main__":
    set1 = MySet([1, 2, 3, 3])
    print(set1)  # Output: MySet: {1,2,3}

    print(set1.has(2))  # Output: True
    print(set1.has(4))  # Output: False

    set1.add(4)
    print(set1)  # Output: MySet: {1,2,3,4}

    set1.delete(3)
    print(set1)  # Output: MySet: {1,2,4}

    print(set1.size())  # Output: 3

    set1.clear()
    print(set1)  # Output: MySet: {}
