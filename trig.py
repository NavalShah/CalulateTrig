import math

def trig(θ):
    #initialise values
    x = 0.6072529350088812
    y = 0
    φ = θ
    n = 0
    change = 1
    maxIterations = 99
    
    while n < maxIterations and change > 0:
        d = φ/abs(φ)
        
        x_next = x - (d * y * math.pow(2,-n))
        y_next = y + (d * x * math.pow(2,-n))
        φ_next = φ - (d * math.atan(math.pow(2,-n)))
        change = abs(x_next - x) + abs(y_next - y)
        x = x_next
        y = y_next
        φ = φ_next
        
        n = n + 1
    
    print("sin(" + str(θ) + ") = " + str(y))
    print("cos(" + str(θ) + ") = " + str(x))
    print("tan(" + str(θ) + ") = " + str(y/x))
    print("Iterations: " + str(n))

trig(1)