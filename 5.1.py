import random

# generate 30 random points inside the cube
x = [30]
for x_i in range(0,30):
    x_i = []
    for i in range(0,100):
        x_i.append(random.uniform(-0.5,0.5))
    x.append(x_i)

