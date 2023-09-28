from math import hypot

class Vector:
    def __init__(self  , x , y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector {self.x} , {self.y}"

    def __abs__(self):
        return hypot(self.x , self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x , y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar , self.y * scalar)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self
if __name__ == "__main__":

    vec1 = Vector(2 ,3)
    vec2 = Vector(3 ,4)

    print(vec1)
    print(vec1 + vec2)
    print(vec1 * 2)
    print(abs(vec1))

    print('before iadd')
    print(vec1)
    print(vec2)
    print(id(vec1))


    vec1 += vec2
    print('after iadd')
    print(vec1)
    print(vec2)
    print(id(vec1))

    b = [3]

    b += [50 , 60]
    print(b)

    t = (1, 2, [30, 40])
    #t[2]+= [50, 60]
