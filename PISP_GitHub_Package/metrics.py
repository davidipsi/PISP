import numpy as np

def minmax(x, xmin=None, xmax=None):
    x = np.asarray(x, dtype=float)
    if xmin is None: xmin = np.nanmin(x)
    if xmax is None: xmax = np.nanmax(x)
    if xmax - xmin == 0:
        return np.zeros_like(x)
    return (x - xmin) / (xmax - xmin)

def coherence_phases(theta):
    """
    Coherencia como parámetro de orden r in [0,1].
    theta: array de fases (rad).
    """
    z = np.exp(1j*np.asarray(theta))
    return np.abs(z.mean())

def entropy_variance_phases(theta):
    """
    Entropía/variabilidad como varianza de fase (normalizar externamente a [0,1]).
    """
    return float(np.var(np.unwrap(theta)))

def efficiency_time_to_event(times):
    """
    Eficiencia como 1 - tiempo normalizado (menor tiempo, mayor EE).
    """
    t = np.asarray(times, dtype=float)
    t_norm = minmax(t)
    return 1.0 - t_norm

def integration_index(C, EE, H, alpha=1.0, beta=1.0, gamma=1.0):
    C = np.asarray(C, dtype=float)
    EE = np.asarray(EE, dtype=float)
    H = np.asarray(H, dtype=float)
    return alpha*C + beta*EE - gamma*H
