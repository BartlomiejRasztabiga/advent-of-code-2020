import re

fp = "input.txt"
instructions = re.findall(r"(\w)(\d+)", open(fp).read())
moveset = {
    "N": lambda _x, _r, _v: (_x + _v * (+0 + 1j), _r),
    "E": lambda _x, _r, _v: (_x + _v * (+1 + 0j), _r),
    "S": lambda _x, _r, _v: (_x + _v * (+0 - 1j), _r),
    "W": lambda _x, _r, _v: (_x + _v * (-1 + 0j), _r),
    "F": lambda _x, _r, _v: (_x + _v * _r, _r),
    "L": lambda _x, _r, _v: (_x, _r * 1j ** (_v // 90)),
    "R": lambda _x, _r, _v: (_x, _r / 1j ** (_v // 90)),
}

x = 0 + 0j
r = 1 + 0j
for k, v in instructions:
    x, r = moveset[k](x, r, int(v))
print(abs(x.real) + abs(x.imag))
