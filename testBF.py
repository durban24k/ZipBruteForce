import numba
import time





def func(complete):
     for current in range(5):
          a=[i for i in char_list]
          for x in range(current):
               a=[y+i for i in char_list for y in a]
          complete=complete+a

@numba.jit()
def func2():
     for current in range(5):
          a=[i for i in char_list]
          for x in range(current):
               a=[y+i for i in char_list for y in a]
          complete=complete+a


if __name__ == '__main__':
     complete=[]
     char_list='abcdefghijklmnopqrstuvwxyz' # add all the possible characters in the char_list
     startTimeA=time.time()
     func()
     endTimeA=(time.time() - startTimeA)
     print(endTimeA)

     startTimeB=time.time()
     func2()
     endTimeB=(time.time() - startTimeB)
     print(endTimeB)