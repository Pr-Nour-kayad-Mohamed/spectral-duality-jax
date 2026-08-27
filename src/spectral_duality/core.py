import jax
import jax.numpy as jnp

@jax.jit
def compute_metric_tensor(x, y):
    """
    Calcule les composantes du tenseur métrique g_xx et g_yy sur le plan complexe z = x + iy
    associé au pullback de l'arcsin, incluant la singularité aux points de ramification z = ±1.
    """
    term_real = 1.0 - x**2 + y**2
    denominator_squared = term_real**2 + 4.0 * (x**2) * (y**2)
    
    epsilon = 1e-12
    metric_component = 1.0 / jnp.sqrt(denominator_squared + epsilon)
    
    return metric_component

@jax.jit
def analyze_divergence_near_branch_points(x_grid, y_val):
    """
    Évalue la métrique le long d'une coupe pour observer la divergence en z -> ±1.
    """
    return jax.vmap(lambda x: compute_metric_tensor(x, y_val))(x_grid)
