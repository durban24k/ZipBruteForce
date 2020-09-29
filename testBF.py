from numba import jit
import numpy as np
from timeit import default_timer as timer

class GpuFunction:
     def func(self):
          k='abcdefghijklmnopqrstuvwxyz' # add all the possible characters in the char_list
          complete=np.array([])
          for j in range(5):
               a=[i for i in k]
               for x in range(j):
                    a=[y+i for i in k for y in a]
               complete=np.append(complete,a)

     @jit(nopython=True,target='gpu')
     def func2(self):
          k='abcdefghijklmnopqrstuvwxyz' # add all the possible characters in the char_list
          complete=np.array([])
          for j in range(5):
               a=[i for i in k]
               for x in range(j):
                    a=[y+i for i in k for y in a]
               complete=np.append(complete,a)

if __name__ == '__main__':
     
     startTimeA=timer()
     without=GpuFunction()
     without.func()
     endTimeA=(timer() - startTimeA)
     print(endTimeA)

     startTimeB=timer()
     withgpu= GpuFunction()
     withgpu.func2()
     endTimeB=(timer() - startTimeB)
     print(endTimeB)