import ctypes

class DynArray(object):

    def __init__(self):
        self.n=0
        self.capacity=1
        self.A=self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, p):    # Getting item at a specific interest

        if not 0<= p <self.n:
            return Error('P is out of bounds')       #If P is out of range of the array, It'll not be possible to fetch that item

        return self.A[p]

    def additem(self, element):     # inserting element at the end

        if self.n == self.capacity:     #must increase the array size if that array is already full. i.e. size = capacity of that array
            self._resize(2 * self.capacity)

        self.A[self.n] = element
        self.n = self.n+1

    def insertElement(self, item, index):  #inserting an element

        if index<0 or index>self.n:
            print('Invalid')

        if self.n == self.capacity:
            self._resize(2 * self.capacity)

        for i in range(self.n - 1, index - 1, -1):
            self.A[i + 1] = self.A[i]

        self.A[index] = item
        self.n += 1

    def delete(self, index):       # deleting an element

        if self.n == 0:
            print("Array is empty deletion not Possible")
            return

        if index < 0 or index >= self.n:
            return IndexError("Invalid index, deletion not possible")

        if index == self.n - 1:
            self.A[index] = 0
            self.n -= 1
            return

        for i in range(index, self.n - 1):
            self.A[i] = self.A[i + 1]

        self.A[self.n - 1] = 0
        self.n -= 1

    def _resize(self, new_cap):   #resizing the array
        B = self.make_array(new_cap)

        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):

        return (new_cap * ctypes.py_object)()

# Instantiate
arr = DynArray()
arr.additem(3)
print(len(arr))

arr.additem(2)   #Adding an item
print(len(arr))

print(arr[0]

      





