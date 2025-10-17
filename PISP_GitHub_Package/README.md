# Principio de Integración Sistémica Presente (PISP) / Present Systemic Integration Principle

**ES — Presentación**  
El PISP propone un índice **I = α·C + β·EE − γ·H** para sintetizar **coherencia (C)**, **eficiencia (EE)** y **entropía (H)** a fin de explicar y predecir **estabilidad y resiliencia (R)** en sistemas humanos, biológicos y sociales. El índice se **normaliza a [0,1]** y se aplica de forma comparable en distintos dominios (simulaciones, neurofisiología, equipos).

**EN — Overview**  
The PISP introduces **I = α·C + β·EE − γ·H** to combine **coherence (C)**, **efficiency (EE)** and **entropy (H)** for explaining and predicting **stability and resilience (R)** across human, biological and social systems. The index is **normalized to [0,1]** and is comparable across domains (simulations, neurophysiology, teams).

---

## ES — Función y variables / EN — Core function and variables
- **C (coherencia / coherence)**: grado de sincronía/orden efectivo (p. ej., parámetro de orden *r* en Kuramoto, coherencia HRV/EEG, equilibrio de turnos).  
- **EE (eficiencia / efficiency)**: desempeño por unidad de tiempo/costo (p. ej., **1 −** tiempo normalizado por acierto; **1 −** tiempo a consenso).  
- **H (entropía / entropy)**: variabilidad no integrada/ruido (p. ej., varianza de fase; desviación de RTs; entropía de turnos).  
- **R (resiliencia / resilience)**: inverso del tiempo de recuperación o **1 −** AUC de variabilidad post-perturbación (usado como *outcome*).

**Normalización:** z-score → min–max o sigmoide; métricas “menos es mejor” se invierten (**1 − x̃**).  
**Pesos:** iniciar con **α=β=γ=1**; estimar por regresión con restricciones no negativas y validación cruzada.

---

## ES — Reproducibilidad / EN — Reproducibility
- **Simulación base:** `sims/kuramoto.py` (osciladores acoplados con ruido; barrido de acoplamiento K y ruido σ).  
- **Métricas:** `metrics.py` (C, EE, H, R e índice I).  
- **Notebook:** `notebooks/01_kuramoto_basics.ipynb` (ejecución y gráficos).  
- **Docs:** anexo técnico y carta ética en `docs/`.

**Cita / Citation:** Martínez, D. *PISP v2* (Zenodo) — DOI: **10.5281/zenodo.17364336**  
**Contacto / Contact:** **contact@ipsi-institute.org**  
**Licencia / License:** CC0 1.0 Universal (para este repositorio).

---

## ES — Estructura / EN — Repository structure
```
PISP/
├─ README.md
├─ LICENSE
├─ .gitignore
├─ sims/
│  └─ kuramoto.py
├─ metrics.py
├─ notebooks/
│  └─ 01_kuramoto_basics.ipynb
└─ docs/
   ├─ Technical_Annex_PISP_v2.1.md
   ├─ Ethical_Open_Continuity_Letter_PISP_v2.1.md
   └─ references.txt
```

---

## ES — Guía rápida / EN — Quick start
```bash
# 1) Opcional: crear entorno
python -m venv .venv && source .venv/bin/activate  # (Windows: .venv\Scripts\activate)

# 2) Instalar dependencias mínimas
pip install numpy matplotlib

# 3) Correr simulación Kuramoto
python sims/kuramoto.py

# 4) Abrir notebook (si deseas)
pip install jupyter && jupyter notebook notebooks/01_kuramoto_basics.ipynb
```
Resultados esperados: al aumentar **K** y reducir **σ** sube **C** (orden) y baja **H** (variabilidad); **EE** mejora (tiempo a consenso menor).  
Se puede calcular **I = αC + βEE − γH** y observar transición de régimen (umbral **I\***).

---

## ES — Nota de colaboración / EN — Collaboration note
**ES:** El PISP se ofrece como modelo abierto para validación y discusión interdisciplinaria. Enviar observaciones, datos o informes técnicos a **contact@ipsi-institute.org** citando el DOI.  
**EN:** PISP is released as an open model for validation and interdisciplinary discussion. Please share observations, data or technical reports to **contact@ipsi-institute.org** citing the DOI.
