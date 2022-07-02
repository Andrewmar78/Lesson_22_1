# Как то вечером три разработчика написали 
# три метода класса `SomeClass`, каждый под себя. 
# Методы по сути своей почти одинаковые.
#
# Напишите свой метод `sorted_func`, 
# учитывая особенности всех представленных методов

class SomeClass:
    def __init__(self):
        self.lst = [3, 2, 1, 4, 2, 1]

    def sorted_func(self):
        # Не работает метод sort
        return self.lst.sort(reverse=False)
        # return sorted(self.lst, reverse=False)

if __name__ == "__main__":
    some_item = SomeClass()
    print(some_item.sorted_func())
