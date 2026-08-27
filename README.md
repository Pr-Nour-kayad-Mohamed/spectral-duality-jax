# Computational Framework for Inter-Scale Spectral Duality: Riemann Surface Metric and Non-Hermitian DOS Continuity using JAX

[![License: CC BY 4.0](https://shields.io)](https://creativecommons.org)

Ce dépôt fournit l'implémentation numérique vectorisée et différentiable associée au chapitre de manuscrit sur la **Dualité Inter-Échelles**. Il formalise le prolongement analytique de la relation de dispersion via l'opérateur \(\arcsin\) complexe, cartographie la métrique de Kähler sur la surface de Riemann et calcule la densité d'états (DOS) à travers la transition nappe physique \(\mathcal{S}_0\) → nappe non-hermitienne \(\mathcal{S}_1\).

## 🚀 Fonctionnalités Clés

* **Prolongement Analytique Rigoureux :** Formulation logarithmique complexe de l'opérateur \(\arcsin\) éliminant les sauts de phase non physiques (`branch cuts`).
* **Pullback de la Métrique :** Calcul exact et cartographie du tenseur métrique \(g_{xx}\) exhibant les divergences critiques aux points exceptionnels (z = ± 1).
* **DOS Différentiable :** Utilisation de la différentiation automatique (`jax.grad`) pour extraire les composantes réelles et évanescentes de la Densité d'États.
* **Haute Performance :** Code entièrement écrit sous **JAX**, nativement compatible avec la compilation juste-à-temps (`@jax.jit`) et la vectorisation de masse (`jax.vmap`) sur CPU/GPU/TPU.

## 📂 Structure du Dépôt

```text
├── LICENSE
├── README.md
├── requirements.txt
├── src/
│   └── spectral_duality/
│       ├── __init__.py
│       ├── core.py          # Primitives extended_arcsin et calcul de métrique
│       └── models.py        # Modèle jouet type SSH et calcul de la DOS
```

## 🛠️ Installation & Configuration

```bash
git clone https://github.com
cd spectral-duality-jax
pip install -r requirements.txt
```

## 📊 Exemple Rapide d'Utilisation

```python
import jax.numpy as jnp
from src.spectral_duality.models import analyze_dos_profile

k_grid = jnp.linspace(-jnp.pi, jnp.pi, 1000)
delta_coupling = 0.5 

dos_real, dos_imag = analyze_dos_profile(k_grid, delta_coupling)
print("DOS Réelle max:", jnp.max(dos_real))
print("DOS Imaginaire max:", jnp.max(dos_imag))
```
