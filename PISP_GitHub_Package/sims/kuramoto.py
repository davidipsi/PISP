#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def kuramoto(N=100, K=1.5, sigma=0.1, T=20.0, dt=0.01, seed=42):
    rng = np.random.default_rng(seed)
    omega = rng.normal(0, 1, N)
    theta = rng.uniform(0, 2*np.pi, N)
    steps = int(T/dt)
    rs = []
    for t in range(steps):
        noise = rng.normal(0, sigma, N) * np.sqrt(dt)
        s = np.sin(theta[:,None] - theta[None,:])
        coupling = (K/N) * s.sum(axis=1)
        theta += (omega + coupling)*dt + noise
        r = np.abs(np.exp(1j*theta).mean())
        rs.append(r)
    return np.array(rs), theta

def main():
    N=200; T=20; dt=0.01
    Ks = [0.5, 1.0, 2.0]
    plt.figure()
    for K in Ks:
        rs, _ = kuramoto(N=N, K=K, sigma=0.1, T=T, dt=dt, seed=0)
        t = np.linspace(0, T, len(rs))
        plt.plot(t, rs, label=f"K={K}, sigma=0.1")
    plt.xlabel("Time")
    plt.ylabel("Order parameter r (≈ C)")
    plt.title("Kuramoto — coherence vs coupling")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
