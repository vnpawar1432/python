class patient:
    name = None
    phoneNumber: None
    address: None
    pincode: None
    is_corona: None
    def __init__(self,name,phoneNumber,address,pincode):
        patient.name = name
        patient.phoneNumber = phoneNumber
        patient.address = address
        patient.pincode = pincode

class CoronaPatient:
    patient = []
    def addPatient(self,newPatient):
        return newPatient

vaibhav = patient("vaibhav",1234567890,"parbhani",431401)
pawar = CoronaPatient()
print(pawar.addPatient("vaibhav"))


print(patient.name)
print(patient.phoneNumber)
print(patient.address)
print(patient.pincode)








