def Hello4(ArgCount, *VarArgs):
    print("You passed ", ArgCount, " arguments.")
    for Arg in VarArgs:
       print(Arg)

Hello4(1, "A Test String.")
Hello4(3, "One", "Two", "Three")
