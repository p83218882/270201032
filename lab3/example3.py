
#number of lectures = nol


GPA = float(input('GPA: '))
nol = int(input('nol: '))

if (nol < 47 ):
  if GPA < 2.0 :
    print('Not enough numbers of lectures and GPA!')
  
  else:
    print('Not enough number of lectures!')
else:
  if (GPA < 2.0):
    print('Not enough GPA!')

  else:
    print('GRADUATED!!')