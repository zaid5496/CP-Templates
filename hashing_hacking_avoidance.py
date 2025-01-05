from random import getrandbits

RANDOM = getrandbits(32)

class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM


'''Unlike C++, Python does not provide a way to define its own hash function
   for an existing type (or I just don't know about it), but nobody prevents
   you from defining your type with a different hash function.'''

'''basically solutions hack hone se bachate he agar hum saare by default items ko is Wrapper me wrap karde to !(hashing_hacking_avoidance)'''
