from math import log as ln

# Givens
m = 10
g = 9.81
A = 1
v = 2  # volume
P = 10e5
Pext = 101325

# Initial Conditions
X = 0
V = 0
W = 0

i = 0
t = 0
dt = 1e-6
while P > Pext:
    # Time Integration
    i += 1
    t += dt
    
    # Position Integration
    dX = V * dt
    X += dX
    
    # Velocity Integration
    dV = (P-Pext-m*g)/m * dt
    V += dV
    
    # Work Integration
    dv = dX * A
    dW = P * dv
    W += dW

    # New Pressure and Volume
    P = P*v/(v+dv)
    v = v + dv
    
    # External Work
    Wext = 1/2*m*V**2 + Pext*A*X + m*g*X
    
    # Display
    if i % 100 == 0:
        print(t, X, V, P, v, W, Wext)
    
