def sum_of_n_inputs(solution):
    if solution == 0:
        x=lambda:int(input())#costs +1 byte to use x() instead of print, dont. it would be funny but dont.
        print(sum([x()for y in[x]*x()])) #53 chars + \n
    elif solution == 1:
        print(sum([int(input())for x in[1]*int(input())])) #50 chars    
    elif True:
        print(sum([int(input())for x in range(0,int(input()))])) #56 chars

def XYZAB(solution):
    if solution == 0:
        x=lambda:int(input())
        print(x()+x()+x()-x()-x()) #47 chars + newline = 48 chars
    elif solution == 1:
        print(sum([int(input())*(1if x<3else-1)for x in range(0,5)]))#61 chars
    elif solution == 2:
        print(sum([int(input())*x for x in[1]*3+[-1]*2])) #49
choice = int(input("Which golf? "))
if choice == 0:
    sum_of_n_inputs(int(input("Which solution for sum of N inputs? ")))
elif choice == 1:
    XYZAB(int(input("Which solution for X+Y+Z-A-B? ")))