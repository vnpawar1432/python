class A:
    def Adata(self):
        print("Method From class A ")
class B(A):
    def Bdata(self):
        print("Method From class B")
class C(A):
    def Cdata(self):
        print("Method From class C")

obj = C()
obj.Adata()
obj.Cdata()