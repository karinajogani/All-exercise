  
    
num = 7536
n=0
while num>0:
    a = num%10
    num = num - a
    num = num/10
    print(int(a),end=" ")  
print(n)