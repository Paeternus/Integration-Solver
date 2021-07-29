print("Pedro")
print("matt")

# test commit

# https://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html
# https://www.instructables.com/How-to-Make-a-Numerical-Integration-Program-in-Pyt/


# can you see this - Matt
# Here the parameters for numerical integration are defined

N = int(input("Enter how many times you want to sum: ")) ## more times = more accrate
a = float(input("Enter the lower integration bound: "))
b = float(input("Enter the upper integration bound: "))

def Integrate(N, a, b):
    def f(x):
        #type your function after return
        return x**2
    value=0
    value=0
    for n in range(1 , N+1):
        value += f(a+((n-(1/2))*((b-a)/N)))
    value2 = ((b-a)/N)*value
    return value2
