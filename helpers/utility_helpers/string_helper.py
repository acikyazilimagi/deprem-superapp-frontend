import re

def tr_upper(self):
    self = re.sub(r"i", "İ", self)
    self = re.sub(r"ı", "I", self)
    self = re.sub(r"ç", "Ç", self)
    self = re.sub(r"ş", "Ş", self)
    self = re.sub(r"ü", "Ü", self)
    self = re.sub(r"ğ", "Ğ", self)
    self = self.upper() # for the rest use default upper
    return self


def tr_lower(self):
    self = re.sub(r"İ", "i", self)
    self = re.sub(r"I", "ı", self)
    self = re.sub(r"Ç", "ç", self)
    self = re.sub(r"Ş", "ş", self)
    self = re.sub(r"Ü", "ü", self)
    self = re.sub(r"Ğ", "ğ", self)
    self = self.lower() # for the rest use default lower
    return self