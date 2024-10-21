# Test de cualquier funcion

# Cálculos de teoría de colas
v_rho = 4 / 6
v_po = (1 - v_rho)
v_ls = round(v_rho / v_po, 0)
v_lq = (v_rho**2) / v_po
v_ws = v_ls / 4
v_wq = v_lq / 4
n = 0

# Calcular n
v_pn_temp = 1
while v_pn_temp > 0:
    v_pn_temp = round(v_po*(v_rho**n), 4)
    if v_pn_temp > 0:
        n += 1

def v_pn(n: int):
    return round(v_po*(v_rho**n), 4)

def v_fn(n: int):
    v_pn_temp = 0
    for i in range(0, n+1):
        v_pn_temp += v_pn(i)
        print(i)
    return v_pn_temp

def v_n():
    n = 0
    v_pn_temp = 1
    while v_pn_temp > 0:
        v_pn_temp = v_pn(n)
        if v_pn_temp > 0:
            n += 1
    return n

print(v_n())