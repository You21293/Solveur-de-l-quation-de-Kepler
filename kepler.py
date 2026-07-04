import math

def kepler(M, e, iterations=25, alpha=0.6):

    E = M

    for _ in range(iterations):

        E_next = M + e * math.sin(E)
        E = (1 - alpha) * E + alpha * E_next

    return E


M_deg = float(input("M (deg) : "))
e = float(input("e : "))

M = math.radians(M_deg)

E = kepler(M, e)

print("\nRESULTAT")
print("E (rad) =", E)
print("E (deg) =", math.degrees(E))
