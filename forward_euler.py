# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 20:15:29 2025

@author: mellv
"""

import numpy as np
import matplotlib.pyplot as plt


def forward_euler (f, U0, T, n):
    u = np.zeros(n+1)
    t = np.zeros(n+1)
    u0 = U0
    t0 = 0
    dt = T/n
    
    for k in range(n):
        u[k+1] = u[k] + dt*f(u[k], t[k])
        t[k+1] = t[k] +dt
    return u, t
    
if __name__ == "__main__":        
        def f(u ,t):
            return u
        
        for n in range(5, 10, 20):
            u, t = forward_euler(f, U0 = 1, T =4, n = n)
            plt.plot(t, u, linestyle="dashed", label =f"n={n}" )
            
        tf = np.linspace(0, 4, 1001)
        plt.plot(tf, np.exp(tf), label="exact")
        plt.legend()
        plt.show()
        
        
        