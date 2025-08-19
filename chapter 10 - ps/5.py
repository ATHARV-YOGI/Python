from random import randint
class train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"ticket is booked in train no : {self.trainNo}")

    def getStatus(self):
        print(f"train no: {self.trainNo} is running on time  ")

    def getFare(self, fro, to):
        print(f"ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222,555)}")


temp = train(3873458)

temp.book("jaipur","goa")

temp.getStatus()

temp.getFare("jaipur","goa")