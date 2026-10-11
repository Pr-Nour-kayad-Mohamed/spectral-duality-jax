import numpy as jnp

def create_effective_hamiltonian(H_0, Gamma):
    assert H_0.shape == Gamma.shape, "Les dimensions doivent être identiques."
    return H_0 - 1j * Gamma

def generate_test_system(dim, key_seed=42):
    import numpy as np
    np.random.seed(key_seed)
    X = np.random.randn(dim, dim) + 1j * np.random.randn(dim, dim)
    H_0 = 0.5 * (X + X.conj().T)
    Gamma = np.diag(np.linspace(0.1, 2.5, dim))
    return H_0, Gamma
