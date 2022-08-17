##basic exercise

def value(a, b):
    product = a * b
    if product <= 1000:
        return product
    else:
        return a + b
        
answer = value(20, 30)
print("The answer is", answer)

answer = value(40, 30)
print("The answer is", answer)
