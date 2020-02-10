def PrintTimesTable(XStart = 1,
                    XEnd = 11,
                    YStart = 1,
                    YEnd = 11):
   X = XStart
   Y = YStart

   print ('{:>4}'.format(' '), end= ' ')

   for X in range(YStart, YEnd):
      print('{:>4}'.format(X), end=' ')
      
   print()
      
   for X in range(XStart, XEnd):
      print('{:>4}'.format(X), end=' ')
      while Y < YEnd:
         print('{:>4}'.format(X * Y), end=' ')
         Y+=1
      print()
      Y=YStart

PrintTimesTable()
print()
PrintTimesTable(8, 12)
print()
PrintTimesTable(4, 6, 5, 8)
print()
PrintTimesTable(YStart = 5, YEnd = 9)
