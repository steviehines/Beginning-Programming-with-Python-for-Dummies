try:
   Value1 = int(input("Type the first number: "))
   Value2 = int(input("Type the second number: "))
   Output = Value1 / Value2
except ValueError:
   print("You must type a whole number!")
except KeyboardInterrupt:
   print("You pressed Ctrl+C!")
except ArithmeticError:
   print("An undefined math error occurred.")
except ZeroDivisionError:
   print("Attempted to divide by zero!")
else:
   print(Output)
