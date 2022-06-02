class A:
    def Adata(self):
        print("Method From class A ")
class B(A):
    def Bdata(self):
        print("Method From class B")
obj = B()

obj.Bdata()
obj.Adata()