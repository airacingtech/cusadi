import os
import time
import torch
from casadi import Function
from CusadiFunction import CusadiFunction

n = 50
BATCH_SIZE = 10000

fn_casadi = Function.load("src/casadi_functions/fn_heavy_demo.casadi")

x = torch.rand((BATCH_SIZE, n), dtype=torch.float64, device='cuda')
u = torch.rand((BATCH_SIZE, n), dtype=torch.float64, device='cuda')

# Convert to NumPy for CPU CasADi eval
x_np = x.cpu().numpy()
u_np = u.cpu().numpy()

start = time.time()
for i in range(BATCH_SIZE):
    _ = fn_casadi(x_np[i], u_np[i])
casadi_time = time.time() - start
print(f"[CasADi CPU] Time for {BATCH_SIZE} evaluations: {casadi_time:.4f} s")

cusadi_fn = CusadiFunction(fn_casadi, BATCH_SIZE)
cusadi_fn.evaluate([x, u])
torch.cuda.synchronize()
print(f"[CusADi GPU] Time for {BATCH_SIZE} evaluations: {cusadi_fn.eval_time:.4f} s")

# Optionally verify output
# print(cusadi_fn.outputs_sparse[0])
