class A:
    def Adata(self):
        print("Method From class A ")
class B:
    def Bdata(self):
        print("Method From class B")
class C(A,B):
    def Cdata(self):
        print("Method From class C")


obj = C()

obj.Cdata()
obj.Bdata()
obj.Adata()