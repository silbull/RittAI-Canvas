from sympy import symbols, Eq, solve, sqrt
def compute_pyramid_vertex_coordinates(name, a_val, b_val, c_val, d_val, e_val, f_val):
    # Define the variables
    x, y, z = symbols('x y z')
    a, b, c, d, e, f = symbols('a b c d e f')
    
    # Coordinates for A, B
    A = (0, 0, 0)
    B = (a_val, 0, 0)
    
    # Coordinate for C using the cosine rule
    xC = (a_val**2 + c_val**2 - b_val**2) / (2*a_val)
    yC = sqrt(c_val**2 - xC**2)
    C = (xC, yC, 0)
    
    # Spherical equations based on distances from A, B, C to P
    eq1 = Eq((x - A[0])**2 + (y - A[1])**2 + (z - A[2])**2, d**2)
    eq2 = Eq((x - B[0])**2 + (y - B[1])**2 + (z - B[2])**2, e**2)
    eq3 = Eq((x - C[0])**2 + (y - C[1])**2 + (z - C[2])**2, f**2)

    # Solve the system of equations
    solutions = solve((eq1, eq2, eq3), (x, y, z))
    
    # Select the solution with positive z-coordinate
    P_solution = None
    subs = {a: a_val, b: b_val, c: c_val, d: d_val, e: e_val, f: f_val}
    for sol in solutions:
        if sol[2].subs(subs) > 0:
            P_solution = sol
            break
            
    P = tuple([coord.subs(subs) for coord in P_solution])
    
    return {name[0]: P, name[1]: A, name[2]: B, name[3]: C}

# Test the function
print(compute_pyramid_vertex_coordinates("PABC", 3, 4, 5, 6, 7, 8))