"""TODO"""

def set_glider(r, c):
    """Initializes a glider"""
    return (
        (r, c),
        (r - 2, c + 1),
        (r, c + 1),
        (r - 1, c + 2),
        (r, c + 2),
    )

def set_Gosper_glider_gun(r, c):
    return (
        (r, c),
        (r, c + 1),
        (r + 1, c),
        (r + 1, c + 1),
        (r, c + 10),
        (r + 1, c + 10),
        (r + 2, c + 10),
        (r - 1, c + 11),
        (r - 2, c + 12),
        (r - 2, c + 13), 
        (r - 1, c + 15),
        (r, c + 16),
        (r + 1, c + 16),
        (r + 2, c + 16),
        (r + 3, c + 15),
        (r + 1, c + 14),
        (r + 1, c + 17),
        (r, c + 20),
        (r - 1, c + 20),
        (r - 2, c + 20),
        (r, c + 21),
        (r - 1, c + 21),
        (r - 2, c + 21),
        (r - 3, c + 22),
        (r - 3, c + 24),
        (r - 4, c + 24),
        (r + 1, c + 22),
        (r + 1, c + 24),
        (r + 2, c + 24),
        (r - 1, c + 34),
        (r - 2, c + 34),
        (r - 1, c + 35),
        (r - 2, c + 35),
        (r + 3, c + 11),
        (r + 4, c + 12),
        (r + 4, c + 13),
    )

# def set_B(r, c):
#     """:)"""
#     h = 15
#     l = 6
#     B = [(r + i, c) for i in range(15)]
#     B.extend([(r, c + i) for i in range(l)])
#     B.extend([(r + h // 2, c + i) for i in range(l)])
#     B.extend([(r + h, c + i) for i in range(l)])
#     B.extend([(r + 1 + i, c + l) for i in range(h // 2 - 1)])
#     B.extend([(r + h // 2 + 1 + i, c + l) for i in range(h // 2)])
#     return B

# def set_O(r, c):
#     """:)"""
#     diag = 4
#     ver = 8
#     hor = 2
#     O = [(r, c)]
#     O.extend([(r + i, c - i) for i in range(diag)])
#     O.extend([(r + i + diag, c - diag + 1) for i in range(ver)])
#     O.extend([(r + i + diag + ver, c - diag + 1 + i) for i in range(diag)])
#     O.extend([(r + 2 * diag + ver - 1, c - diag + 1 + diag + i) for i in range(hor)])
#     last = O[-1]
#     O.extend([(last[0] - i, last[1] + i) for i in range(diag - 1)])
#     last = O[-1]
#     O.extend([(last[0] - i - 1, last[1] + 1) for i in range(ver + 2)])
#     last = O[-1]
#     O.extend([(last[0] - i, last[1] - i) for i in range(diag)])
#     O.extend([(r, c + 1)])
#     return O

# def set_Z(r, c):
#     hor = 13
#     diag = 14
#     Z = [(r, c + i) for i in range(hor)]
#     last = Z[-1]
#     Z.extend([(last[0] + i + 1, last[1] - i) for i in range(diag + 1)])
#     last = Z[-1]
#     Z.extend([(last[0], last[1] + i) for i in range(hor)])
#     return Z

# def set_E(r, c):
#     hor = 8
#     ver = 16
#     Z = [(r, c + i) for i in range(hor)]
#     last = Z[-1]
#     Z.extend([(r + i, c) for i in range(ver)])
#     last = Z[-1]
#     Z.extend([(last[0], last[1] + i) for i in range(hor)])
#     Z.extend([(r + ver/2, c + i) for i in range(hor)])
#     return Z
