import math

def kepler(M, e, iterations=25, alpha=0.6):

    E = M
    
    for _ in range(iterations):

        E_next = M + e * math.sin(E)
        E = (1 - alpha) * E + alpha * E_next

    return E

M_deg = float(input("M (degres) : "))
e = float(input("e : "))

M = math.radians(M_deg)

E = kepler(M, e)

E_rad = E % (2 * math.pi)

E_deg = math.degrees(E_rad)

print("\nRESULTAT")
print("E (radians) =", E_rad)
print("E (degres) =", E_deg)
