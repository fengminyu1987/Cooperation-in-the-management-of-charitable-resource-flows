import numpy as np
from scipy.integrate import odeint
import json

font = {'family': 'Times New Roman',
        'weight': 'bold',
        'style':'italic',
        'size': 26,
        }

C1 = 4
C2 = 5
C3 = 5
C4 = 6
R1 = 5
R2 = 6
R3 = 5
R4 = 6
F = 5
S1_list = np.arange(0, 11, 1)
S2_list = np.arange(0, 11, 1)
P1 = 1
I = 4
G = 3
B = 3
P2 = 5
x_1 = 0.5
y_1 = 0.5
z_1 = 0.5
def func(w, t):
    x, y, z = w
    Fx = x * (1 - x) * (y * B - y * S1 - y * P1 - z * S2 + F + P1 - I + G)
    Fy = y * (1 - y) * (x * S1 + x * P1 + R2 + C1 - R1 - C2)
    Fz = z * (1 - z) * (x * S2 + y * R4 - y * C4 + R3 - C3)
    return np.array([Fx, Fy, Fz])
t = np.arange(0, 10, 0.1)
colors = ["#0000FF", "#000000", "#FF0033", "#00CC00", "#ff7500", '#56004f']
result_f_r = {}
result_f_u = {}
result_f_p = {}
for S1 in S1_list:
    f_r_p = []
    f_u_p = []
    f_p_p = []
    for S2 in S2_list:
        sol = odeint(func, [x_1, y_1, z_1], t)
        f_r_p.append(np.mean(sol[:, 0][-5:]))
        f_u_p.append(np.mean(sol[:, 1][-5:]))
        f_p_p.append(np.mean(sol[:, 2][-5:]))
    result_f_r["S1={:.3f}".format(S1)] = f_r_p
    result_f_u["S1={:.3f}".format(S1)] = f_u_p
    result_f_p["S1={:.3f}".format(S1)] = f_p_p
json_f_r = json.dumps(result_f_r)
json_f_u = json.dumps(result_f_u)
json_f_p = json.dumps(result_f_p)