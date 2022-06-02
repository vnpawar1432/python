class A:
    # def __init__(self):
    #     print("vaibhav")
    def Adata(self):
        print("Method From class A ")
class B(A):
    def Bdata(self):
        print("Method From class B")
class C(A):
    def Cdata(self):
        print("Method From class C")
class D(B,C):
    def Ddata(self):
        print("Method From class D")

obj = D()

obj.Adata()
obj.Bdata()
obj.Cdata()
obj.Ddata()