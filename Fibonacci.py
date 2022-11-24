num = list(map(int,input("Enter The Number(s): ").split()))

for i in range(len(num)):
    
    if(num[i]< 0):
        print(f"{num[i]} is an Invalid Fibonacci Number\n")
    
    else:

        if(num[i] == 0 or num[i] == 1):
            print(f"{num[i]} is a Valid Fibonacci Number\n")

        else:
            n1 = 0
            n2 = 1
            Sum = n1 + n2

            while(Sum<num[i]):
                Sum = n1 + n2
                n1 = n2
                n2 = Sum
            
            if(Sum == num[i]):
                print(f"{num[i]} is a Valid Fibonacci Number\n")
            else:
                print(f"{num[i]} is an Invalid Fibonacci Number\n")