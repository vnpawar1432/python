class Patient:
    def __init__(self, name, phoneNumber, address, pincode):
        self.name = name
        self.phoneNumber = phoneNumber
        self.address = address
        self.pincode = pincode
        self.is_corona = False
    def setIs_corona(self):
        self.is_corona = True
    def getName(self):
        return self.name
    def getPhoneNumber(self):
        return self.phoneNumber
    def getAddress(self):
        return self.address
    def getPincode(self):
        return self.pincode
    def getIs_corona(self):
        return self.is_corona

class CoronaPatient:
    patient = []
    def addPatient(self, newPatient):
        self.patient.append(newPatient)
    def getLessCases(self):
        pincode_count = {}
        for pat in self.patient:
            if pat.is_corona:
                if pat.pincode in pincode_count:
                    pincode_count[pat.pincode] += 1
                else:
                    pincode_count[pat.pincode] = 1
        sorted_pin = sorted(pincode_count, key=pincode_count.get)
        return sorted_pin[0]
    def countPositiveCase(self):
        positive_count = 0
        for pat in self.patient:
            if pat.is_corona:
                positive_count += 1
        return positive_count

if __name__ == '__main__':
    p1 = Patient("xyz", 1234569877, "abcde", 431401)
    p2 = Patient("abc", 9874662112, "fghijk", 431402)
    p3 = Patient("wxt", 5874556966, "qwertt", 431403)
    p4 = Patient("efg", 7845669964, "hythjksk",431404)

    p1.is_corona = False
    p2.is_corona = True
    p3.is_corona = False
    p4.is_corona = True

    cp = CoronaPatient()
    cp.addPatient(p1)
    cp.addPatient(p3)
    cp.addPatient(p4)
    cp.addPatient(p2)

    less = cp.getLessCases()
    positive = cp.countPositiveCase()
    
    print("Pincode with less case: "+str(less))
    print("Total positve case: "+str(positive))