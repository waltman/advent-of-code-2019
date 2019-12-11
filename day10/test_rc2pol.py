import math

# given a vector x,y, returns:
# - the angle in radians (clockwise with 12:00 = 0)
# - eucludian distance from the origin
def xy2pol(x,y):
    print(f"{x=} {y=} {math.atan2(x,y)=:.2f} {math.atan2(y,x)=:.2f}")
    theta = math.atan2(x,y)
    if theta < 0:
        theta = 2 * math.pi + theta
    dist = math.sqrt(x**2 + y**2)
    return theta, dist

print(f"{xy2pol(0,1)=}")
print(f"{xy2pol(1,1)=}")
print(f"{xy2pol(1,0)=}")
print(f"{xy2pol(1,-1)=}")
print(f"{xy2pol(0,-1)=}")
print(f"{xy2pol(-1,-1)=}")
print(f"{xy2pol(-1,0)=}")
print(f"{xy2pol(-1,1)=}")
