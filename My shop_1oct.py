import math

class Products :
    productName = str()
    productId = int()
    productMRP = float()
    productSP = float()

    def __init__(self, productName : str, productId : int, productMRP : float, productSP : float) -> None:
        self.productId = productId
        self.productName = productName
        self.productMRP = productMRP
        self.productSP = productSP

    def getProductName(self) -> str:
        return self.productName
    
    def getProductId(self) -> int:
        return self.productId
    
    def getProductMRP(self) -> float:
        return self.productMRP
    
    def getProductSP(self) -> float:
        return self.productSP

    def applyDiscount(self) -> float:
        if (self.productMRP - self.productSP) < 10 and self.productSP > 1000:
            return self.productSP - 20
        return self.productSP


class Shop:

    def __init__(self, shopName : str, ownerName : str, city : str, pincode : int) -> None:
        self.shopName = shopName
        self.ownerName = ownerName
        self.city = city
        self.pincode = pincode
        self.productList = list()

    def getShopName(self) -> str:
        return self.shopName

    def getOwnerName(self) -> str:
        return self.ownerName
    
    def getCity(self) -> str:
        return self.city

    def getPincode(self) -> int:
        return self.pincode

    def addProduct(self, product : object) -> None:
        self.productList.append(product)

    def sortProductByName(self) -> list:
        pname = [x.getProductName() for x in self.productList]
        pname.sort()
        return pname

    def sortProductByPrice(self) -> list:
        price = [x.getProductSP() for x in self.productList]
        price.sort()
        return price
    
    def getProductTotalPrice(self) -> int:
        allprice = self.sortProductByPrice()
        if len(allprice) == 0:
            return 0
        total = 0
        for price in allprice:
            total += price
        return math.floor(total)
    
    def getProductCount(self) -> int:
        return len(self.productList)

if __name__=="__main__":
    shop = Shop("Toy Shop","Vaibhav","Parbhani",431401)
    print("Shop : "+shop.getShopName())
    print("Owner : "+shop.getOwnerName())
    print("City : "+shop.getCity())
    print("Zip : "+ str(shop.getPincode()))

    product1 = Products("Gun",123,720.50,710.20)
    product2 = Products("Mobile",124,920.50,880.20)
    product3 = Products("Doll",125,1200.50,1100.20)
    product4 = Products("RemoteCar",126,980.50,930.20)

    shop.addProduct(product4)
    shop.addProduct(product2)
    shop.addProduct(product1)
    shop.addProduct(product3)

    print("Toy name : " + " ".join(shop.sortProductByName()))
    print("Toy Price : " + " ".join(list(map(str,shop.sortProductByPrice()))))
    print("Total Price : ",(shop.getProductTotalPrice()))
    print("Product Count : "+ str(shop.getProductCount()))
