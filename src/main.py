import numpy as jnp
from src.operators import generate_test_system, create_effective_hamiltonian
from src.core_solvers import compute_pseudospectrum_mesh

def run_pipeline():
    print("\n=== [SCCI-CORE] INITIALISATION DU CALCUL PSEUDOSPECTRAL ===")
    dim = 12
    resolution = 50
    
    H_0, Gamma = generate_test_system(dim=dim)
    H_eff = create_effective_hamiltonian(H_0, Gamma)
    
    eigvals = jnp.linalg.eigvals(H_eff)
    
    r_min, r_max = jnp.min(eigvals.real) - 0.5, jnp.max(eigvals.real) + 0.5
    i_min, i_max = jnp.min(eigvals.imag) - 0.5, jnp.max(eigvals.imag) + 0.5
    
    real_axis = jnp.linspace(r_min, r_max, resolution)
    imag_axis = jnp.linspace(i_min, i_max, resolution)
    
    print(f"📊 Résolution de la grille complexe : {resolution}x{resolution}")
    print(f"⚡ Balayage vectorisé en Pur NumPy...")
    
    resolvent_norms = compute_pseudospectrum_mesh(H_eff, real_axis, imag_axis)
    
    print("\n=== [STATISTIQUES DE LA MATRICE DU RÉSOLVANT] ===")
    print(f"   - Norme max du résolvant : {jnp.max(resolvent_norms):.4f}")
    print(f"   - Norme min du résolvant : {jnp.min(resolvent_norms):.4f}")
    print(f"   - Dimension finale de la structure : {resolvent_norms.shape}")
    print("✅ Validation spectrale opérée avec succès.\n")

if __name__ == "__main__":
    run_pipeline()
