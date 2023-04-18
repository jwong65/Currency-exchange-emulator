class Currency:

  currencies =  {'CHF': 0.930023, #swiss franc 
                 'CAD': 1.264553, #canadian dollar
                 'GBP': 0.737414, #british pound
                 'JPY': 111.019919, #japanese yen
                 'EUR': 0.862361, #euro
                 'USD': 1.0} #us dollar
      
  def __init__(self, value, unit="USD"):
    self.value = value
    self.unit = unit

  def changeTo(self, new_unit):
    """
      An Currency object is transformed from the unit "self.unit" to "new_unit"
    """
    self.value = (self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit])
    self.unit = new_unit
  
  #add magic methods here
  def __repr__(self):
  # This method returns the string to be printed. This should be the value rounded to two digits, accompanied by its acronym.
    return (str(round(self.value, 2)) +str(self.unit))
  
  def __str__(self):
    #This method returns the same value as __repr__(self).
    return (str(round(self.value, 2)) +str(self.unit))
  
  def __add__(self,other):
    #Defines the '+' operator. If other is a Currency object, the currency values are added and the result will be the unit of self. If other is an int or a float, other will be treated as a USD value.
    x = isinstance(other, Currency)
    if (x == True):
    #   Implement the change to other currency, dividing the value by the currency will get number and then convert it using the self.value
      return ((round(((other.value/Currency.currencies[other.unit]*Currency.currencies[self.unit]) + self.value), 2)), self.unit)
    else:
        y = isinstance(other, (int, float))
        if (y == True):
    #   USD is 1.0 so it's multiplied by currency.currencies
            return (round(((other * Currency.currencies[self.unit]) + self.value), 2), self.unit)
        else:
          pass
  
  def __radd__(self, other):
    #  Only when other is not a currency.
    other = other * Currency.currencies[self.unit]
    return (self.value + other, self.unit)
  
  def __iadd__(self, other):
        return (Currency.__add__(self,other))
  
  def __sub__(self, other):
     x = isinstance(other, Currency)
     if (x == True):
        return ((round(self.value - (other.value/Currency.currencies[other.unit]*Currency.currencies[self.unit]),2)), self.unit)
     
     

  

# v1 = Currency(23.43, "EUR")

v1 = Currency(23.43, "EUR")
# print(v1.__repr__())
# print(v1)
v2 = Currency(19.97, "USD")
# 15*.0862361
# print(v1.__add__(15))
# print(v1.__add__(v2))
# print (v1.__iadd__(13))
# print(v2.__radd__(3))
print(v1.__sub__(v2))
# print(v1 + v2)
# print(v2 + v1)
# print(v1 + 3) # an int or a float is considered to be a USD value
# print(3 + v1)
# print(v1 - 3) # an int or a float is considered to be a USD value
# print(30 - v2) 
