

class Bank():
    crisis=False
    def create_atm(self):
        while not self.crisis:
            yield "$100"
            
china=Bank()

sk=china.create_atm()
print (sk.next())


print [sk.next() for cash in range(10)]

china.crisis = True

#print (sk.next())

soho=china.create_atm()
#print (soho.next())

china.crisis = False
print (soho.next())

cc=china.create_atm()
print cc.next()