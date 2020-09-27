import zipfile

char_list='abcdefghijklmnopqrstuvwxyz' # add all the possible characters in the char_list
complete=[]

for current in range(4):
     a=[i for i in char_list]
     for x in range(current):
          a=[y+i for i in char_list for y in a]
     complete=complete+a

z=zipfile.ZipFile('#') # this is where you input the filepath for the zipfile

tries=0

for password in complete:
     try:
          tries+=1
          z.setpassword(password.encode('ascii'))
          z.extractall()
          print(f'Password was found after {tries} tries!!! The password is {password}')
          break
     except:
          pass