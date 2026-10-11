import numpy as jnp

def compute_resolvent_norm(z, H_eff):
    dim = H_eff.shape[0]
    M = z * jnp.eye(dim, dtype=jnp.complex128) - H_eff
    s = jnp.linalg.svd(M, compute_uv=False)
    return 1.0 / jnp.where(s[-1] == 0, 1e-20, s[-1])

def compute_pseudospectrum_mesh(H_eff, real_axis, imag_axis):
    # Grille de calcul par double boucle optimisée pour NumPy
    grid = jnp.zeros((len(imag_axis), len(real_axis)))
    for i, im in enumerate(imag_axis):
        for j, re in enumerate(real_axis):
            grid[i, j] = compute_resolvent_norm(re + 1j * im, H_eff)
    return grid
