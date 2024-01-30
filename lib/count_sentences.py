#!/usr/bin/env python3

class MyString:
  def __init__(self, value = ""):
    self.value = value

  def get_value(self):
    return self._value
  def set_value(self, value):
    if type(value) is str:
      self._value = value
    else:
      print("The value must be a string.")
  value = property(get_value, set_value)
    
  def is_sentence(self):
    a = self._value
    b = list(a)
    if b[-1] == ".":
      return True
    else:
      return False

  def is_question(self):
      a = self._value
      b = list(a)
      if b[-1] == "?":
        return True
      else:
        return False

  def is_exclamation(self):
      a = self._value
      b = list(a)
      if b[-1] == "!":
        return True
      else:
        return False

  def count_sentences(self):
    a = self._value
    b = list(a)
    count =0
    for i in range(len(b)):
      if b[i] == "." and b[i-1] !=".":
        count = count + 1
      elif b[i] == "?" and b[i-1] !="?":
        count = count + 1
      elif b[i] == "!" and b[i-1] !="!":
        count = count + 1
      else:
        count = count
      
        

    return count
    
  


test = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
print(test.count_sentences())


#a = Anagram("listen")
#print(a.match(['enlists', 'google', 'inlets', 'banana']))
 
 