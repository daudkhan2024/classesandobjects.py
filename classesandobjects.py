class Car:
    def __init__(self,modelname,yearm,price):
        self.modelname  = modelname
        self. yearm =  yearm
        self.price = price

honda = Car("city",2022 ,100000)
minicopper = Car("Bolt",2018,342333)


print(honda.yearm)
print(honda.modelname)
print(minicopper.yearm)
print(minicopper.price)

#now lets add speed
honda.cc = 1500


#to print all details
print(honda.__dict__)
print(minicopper.__dict__)
