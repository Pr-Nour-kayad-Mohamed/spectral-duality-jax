import jax
import jax.numpy as jnp

@jax.jit
def extended_arcsin_dispersion(z):
    """
    Prolongement analytique de arcsin(z) basé sur la forme logarithmique complexe.
    Garantit la continuité spectrale globale lors du franchissement de |z| = 1.
    """
    term_sqrt = jnp.sqrt(1.0 - z**2 + 0j)
    inner = 1j * z + term_sqrt
    return -1j * jnp.log(inner)

@jax.jit
def dispersion_relation_k(k, delta):
    """
    Relation de dispersion du modèle jouet (ex: type SSH ou oscillateurs).
    """
    z = (1.0 + delta) * jnp.cos(k)
    return extended_arcsin_dispersion(z)

_grad_real = jax.grad(lambda k, d: jnp.real(dispersion_relation_k(k, d)))
_grad_imag = jax.grad(lambda k, d: jnp.imag(dispersion_relation_k(k, d)))

@jax.jit
def compute_dos_components(k, delta):
    """
    Calcule la contribution à la densité d'états (DOS) issue de la relation de dispersion.
    """
    dk_real = _grad_real(k, delta)
    dk_imag = _grad_imag(k, delta)
    
    epsilon = 1e-10
    
    dos_real = 1.0 / (jnp.abs(dk_real) + epsilon)
    dos_imag = 1.0 / (jnp.abs(dk_imag) + epsilon)
    
    return dos_real, dos_imag

analyze_dos_profile = jax.jit(jax.vmap(compute_dos_components, in_axes=(0, None)))
