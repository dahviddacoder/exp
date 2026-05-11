
     
class Stock():
    def __init__(self, p_e_ratio, eps):
        self.p_e_ratio = p_e_ratio
        self.eps = eps
    def valuation(self, smp, eps, smp_eps, p_e_ratio):
            if p_e_ratio < smp and eps>smp_eps:
                print("your stock is valueable")
            else:
                 print("your stock is not valueable")
def main():
    smp = float(input("What is the current pe ratio of smp 500: "))
    smp_eps = float(input("What is the current eps of smp 500: "))
    p_e_ratio = float(input("What is your p_e_ratio: "))
    eps = float(input("What is your current eps: "))

    stock1 = Stock(p_e_ratio, eps)
    stock1.valuation(smp, eps, smp_eps, p_e_ratio)

if input("Would you like your stock to be valueated, yes or no? ") == "yes":
     main()
else:
     print("bye bye")