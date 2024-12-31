# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 16:56:57 2024

@author: mellv
"""

#temperatura de Einstein

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font', size = True )

#constantes
mu_B = 9.274e-24 
k_B = 1.381e-23
g=1.0
S=5/2

figura = plt.figure(figsize=(10, 8))

def Brillouin (S, eta):
    a1 = (S + 0.5) * np.cosh((S + 0.5) * eta) / np.sinh((S + 0.5) * eta)
    a2 = 0.5 * np.cosh(eta / 2) / np.sinh(eta / 2)
    
    return (1/S)*(a2-a1)

def Spin (B, T):
    eta = (g*mu_B*B) / (k_B*T)
    return (S*Brillouin(S, eta))

valores_B =  np.linspace(0, 10, 500)
temperaturas = (5, 10, 50)

for T in temperaturas:
    sz_vals = [Spin(B, T) for B in valores_B]
    plt.plot(valores_B, sz_vals, label=f"T={T}K")
    
plt.title(r"Spin médio $\langle S_z \rangle$ vs. Campo magnético $B$ por temperatura")
plt.xlabel(r"Campo magnético $B$ (T)")
plt.ylabel(r"$\langle S_z \rangle$")
plt.legend()





