
def try_find_legal_v0(x_range, y_range):
    v0y = (-y_range[0]) - 1 # most optimistic V0y

    x = (x_range[0] + x_range[1])/2

    while True:
        t = find_t(y_range, v0y)

        v0x_primitive = find_primitive_v0x(x, t)
        theoretical_vx = find_theoretical_vx(v0x_primitive, t)
        educated_v0x_guess = round(v0x_primitive + (theoretical_vx/2))

        if try_solution(x_range, y_range, educated_v0x_guess, v0y):
            return (educated_v0x_guess, v0y)

        found, v0x = try_vary_x(x_range, y_range, educated_v0x_guess, v0y)

        if found:
            return (v0x, v0y)

        v0y -= 1


def find_t(y_range, v0):
    y = 0
    t = 0
    v = v0

    while not (y_range[0] <= y <= y_range[1]):
        y += v
        v -= 1
        t += 1

    return t

def find_primitive_v0x(s, t):
    v0 = 2*s
    v0 += pow(t, 2)
    v0 /= (2 * t)
    return v0

def find_theoretical_vx(v0, t):
    return v0 - t

def try_solution(x_range, y_range, v0x, v0y):
    vx = v0x
    vy = v0y
    x = 0
    y = 0

    while x <= x_range[1] and y >= y_range[0]:
        x += vx
        y += vy
        if vx > 0:
            vx -= 1
        vy -= 1

        if x_range[0] <= x <= x_range[1] and y_range[0] <= y <= y_range[1]:
            return True

    return False

def try_vary_x(x_range, y_range, v0x, v0y):
    v0xm = v0xp = v0x

    v0xm -= 1
    v0xp += 1

    while v0xm > 0:
        if try_solution(x_range, y_range, v0xm, v0y):
            return True, v0xm
        if try_solution(x_range, y_range, v0xp, v0y):
            return True, v0xp
        v0xm -= 1
        v0xp += 1

    return False, None