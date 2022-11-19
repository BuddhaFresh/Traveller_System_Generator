import random

def twodsix():
  yield (random.randint(2,12))

def onedsix():
  yield (random.randint(1,6))

def threedsix():
  yield (random.randint(3,18))

def dsixsix():
  x = onedsix()
  y = onedsix()
  z = str(x)+str(y)
  yield int(z)

DSIZE = twodsix()

def SIZE():
  return wsize = DSIZE-2

print(SIZE())