"""
We will investigate populations of bunnies and foxes over time.
Author: Samuel Marks
CSCI1100 Spring 2018
Version 1
"""
def b_next(f,b):
    return int((float((10*b))/(1+0.1*(float(b))) - 0.05*(float(b))*(float(f))))
    
def f_next(f,b):
    return int((0.4*(float(f))) + (0.02*(float(f))*float(b)))

bpop= int(input("Number of bunnies ==> "))
print(bpop)
fpop = int(input("Number of foxes ==> "))
print(fpop)

bpop_next = int((float((10*bpop))/(1+0.1*(float(bpop))) - 0.05*(float(bpop))*(float(fpop))))
fpop_next = int((0.4*(float(fpop))) + (0.02*(float(fpop))*float(bpop)))

print("Year 1: "+str(max(0,bpop)),str(max(0,fpop)))
print("Year 2: "+str(max(0,bpop_next)),str(max(0,fpop_next)))
print("Year 3: "+str(max(0,(b_next(fpop_next,bpop_next)))),str(max(0,(f_next(fpop_next,bpop_next)))))
fpop = f_next(fpop_next,bpop_next)
bpop = b_next(fpop_next,bpop_next)
print("Year 4: "+str(max(0,(b_next(fpop,bpop)))),str(max(0,(f_next(fpop,bpop)))))
fpop_next = f_next(fpop,bpop)
bpop_next = b_next(fpop,bpop)
print("Year 5: "+str(max(0,(b_next(fpop_next,bpop_next)))),str(max(0,(b_next(fpop_next,bpop_next)))))