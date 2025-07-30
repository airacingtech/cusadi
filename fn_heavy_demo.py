from casadi import *
import numpy as np

n = 50
x = SX.sym("x", n)
u = SX.sym("u", n)

expr = x
for i in range(20):  # Increase to deepen the expression graph
    expr = sin(expr + u) * cos(expr - u) + exp(-expr*u)

f = Function("fn_heavy_demo", [x, u], [expr])
f.save("src/casadi_functions/fn_heavy_demo.casadi")
