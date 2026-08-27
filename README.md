# Python ML Learning

Repositorio de aprendizaje de Python + ML, partiendo de experiencia previa en C y Java.

## Progreso
- [x] Configuración inicial: repo, SSH con GitHub, estructura de carpetas
- [ ] Fase 0: Python idiomático (comprehensions, iteradores, generadores, decoradores)
- [ ] Fase 1: NumPy + pandas
- [ ] Fase 2: scikit-learn
- [ ] Fase 3: Keras/TensorFlow
- [ ] Fase 4: PyTorch

## Progreso

### Fase 0: Python idiomático (desde C/Java)

- **Sintaxis básica completada**: app de ejemplo (`00-python-fundamentals/my_app`) con
  cálculo de promedio y desviación estándar, manejo de excepciones (`ValueError`, `ZeroDivisionError`),
  entorno virtual (`venv`) y estructura multi-archivo (`main.py` / `operaciones.py`).

- **Comprehensions**: ejercicio de conteo de palabras largas en un texto
  (`00-python-fundamentals/ejercicios/ejercicio-1-Comprehension`).

- **Generadores**: implementación de `ventana_deslizante` con `collections.deque`
  para generar ventanas solapadas de forma perezosa, más un ejemplo didáctico del
  mecanismo `yield`/`next()`/`StopIteration`
  (`00-python-fundamentals/ejercicios/ejercicio-2-ventana-deslizante`).

- **Pendiente**: decorador `cache_simple` (memoización manual sin `functools.lru_cache`).
  Tras esto, Fase 0 queda cerrada.

### Próximos pasos (Fase 1)

- Introducción a Jupyter/Google Colab.
- Primer contacto con NumPy (`01-numpy-pandas`).
