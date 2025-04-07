class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return f"{self.size *'🍪'}"

    def deposit(self, n):
        if (self.size + int(n)) > self.capacity:
            raise ValueError("Cannot deposit that many cookies!")
        else:
            self.size += n

    def withdraw(self, n):
        if self.size < int(n):
            raise ValueError("Cannot withdraw that many cookies!")
        else:
            self.size -= n


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
           raise ValueError("Wrong Capacity")
        else:
            self._capacity = capacity


    @size.setter
    def size(self, size):
        self._size = size




def main():
    try:
        jar = Jar()

        print("Empty Jar" if str(jar)=='' else jar , f"jar capacity: {jar.capacity}", sep="\n")
        jar.deposit(4)
        print(jar)
        jar.withdraw(3)
        print("Empty Jar" if str(jar)=='' else jar)

    except (ValueError , TypeError) as e:
        print(e)



if __name__ == "__main__":
    main()
