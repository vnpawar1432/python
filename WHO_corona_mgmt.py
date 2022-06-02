class Patient:
    is_corona = bool()

    def __init__(self, name: str, phoneNumber: int, address: str, pincode: int) -> None:
        self.name = name
        self.phoneNumber = phoneNumber
        self.address = address
        self.pincode = pincode

    def getAddress(self) -> str:
        return self.address

    def getName(self) -> str:
        return self.name

    def getPincode(self) -> int:
        return self.pincode

    def getPhoneNumber(self) -> int:
        return self.phoneNumber

    def getIs_corona(self) -> bool:
        return self.is_corona


class CoronaPatient:
    patient = list()

    def addPatient(self, newPatient: object) -> None:
        self.patient.append(newPatient)

    def getLessCases(self) -> int:
        corona_case = dict()
        for i in self.patient:
            if i.getIs_corona() == True:
                if str(i.getPincode()) not in corona_case:
                    corona_case[str(i.getPincode())] = 0
                corona_case[str(i.getPincode())] += 1
        print(corona_case)
        if bool(corona_case):
            return int(min(corona_case, key=corona_case.get))
        else:
            return 0

    def countPositiveCase(self) -> int:
        positive_case = 0
        for i in self.patient:
            if i.getIs_corona() == True:
                positive_case += 1
        return positive_case


if __name__ == "__main__":
    p1 = Patient("kajal", 9863021457, "arihant colony", 431001)
    p2 = Patient("mayuri", 6258931407, "samrat society", 431401)
    p3 = Patient("ritesh", 7851423876, "lokmany nagar", 431001)
    p4 = Patient("yogesh", 8604795225, "shivaji maharaj colony", 431005)

    p1.is_corona = True
    p2.is_corona = False
    p3.is_corona = True
    p4.is_corona = True

    cp = CoronaPatient()
    cp.addPatient(p1)
    cp.addPatient(p3)
    cp.addPatient(p4)
    cp.addPatient(p2)

    less = cp.getLessCases()
    positive = cp.countPositiveCase()

    print("Pincode with less case: " + str(less))
    print("Total positve case: " + str(positive))
