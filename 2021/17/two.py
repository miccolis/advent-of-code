input = 'target area: x=195..238, y=-93..-67'
testinput = 'target area: x=20..30, y=-10..-5'

# [[min_x, max_x], [min_y, max_y] ]
target = ([
    [ int(vv) for vv in v[2:].split('..') ]
    for v in input[13:].split(', ')
])



def fire(x_vel, y_vel, target):
    max_y = 0
    x = 0
    y = 0
    while True:
        x = x + x_vel
        if x_vel > 0:
            x_vel = x_vel - 1
        elif x_vel < 0:
            x_vel = x_vel + 1
        y = y + y_vel
        if y_vel > 0:
            max_y = y
        y_vel = y_vel - 1

        # print((x,y))

        if x < target[0][0] and y > target[1][1]:
            continue
        elif x > target[0][1] or y < target[1][0]:
            return -1 

        if x >= target[0][0] and x <= target[0][1] and y >= target[1][0] and y <= target[1][1]:
            return max_y


# print(fire(6, 9, target))

x_vel_max = target[0][1] * 2 # not actually sure what the correct padding is
y_vel_max = abs(target[1][0]) * 2
y_vel_min = target[1][0] * 2

tops = []
for x_vel in range(0, x_vel_max):
    y_vel = y_vel_min 
    while y_vel < abs(y_vel_max):
        ret = fire(x_vel, y_vel, target) 
        if ret > -1:
            tops.append(ret)
        y_vel = y_vel + 1

print(len(tops))
