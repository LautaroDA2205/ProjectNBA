# 🏀 Proyecto NBA GOAT (Greatest Of All Time)

## 📌 Descripción del proyecto

Este proyecto tiene como objetivo construir un **índice cuantitativo** que permita comparar a tres de los jugadores más influyentes en la historia de la NBA — **Michael Jordan, LeBron James y Kobe Bryant** — y generar un **ranking GOAT** basado en estadísticas de carrera, eficiencia y logros colectivos.

El análisis combina datos oficiales de la NBA, normalización estadística y un sistema de ponderaciones diseñado para equilibrar rendimiento individual y éxito competitivo.

---

## 🎯 Objetivos

* Analizar el rendimiento histórico de tres jugadores legendarios de la NBA.
* Construir métricas comparables entre jugadores de distintas épocas.
* Diseñar un **GOAT Index** reproducible y transparente.
* Visualizar los resultados mediante gráficos claros e interpretables.

---

## 🧠 Metodología

### 1. Obtención de datos

Se utilizan:

* Datos de jugadores (`NBA_PLAYERS.csv`)
* Datos de equipos (`NBA_TEAMS.csv`)
* Datos de Finales y MVP (`NBA Finals and MVP.csv`)
* Estadísticas de carrera obtenidas mediante la librería `nba_api`

### 2. Preparación de métricas

A partir de las estadísticas de carrera se calculan métricas por 36 minutos para facilitar la comparación:

* PTS_PER_36
* REB_PER_36
* AST_PER_36
* STL_PER_36
* BLK_PER_36

Además, se incorporan métricas de eficiencia:

* FG_PCT
* FG3_PCT
* FT_PCT

Todas las métricas son **normalizadas** mediante `MinMaxScaler`.

---

### 3. GOAT Index

Se define un índice ponderado combinando las métricas normalizadas:

```
GOAT_INDEX = Σ (métrica × peso)
```

Pesos utilizados:

| Métrica    | Peso |
| ---------- | ---- |
| PTS_PER_36 | 0.25 |
| REB_PER_36 | 0.15 |
| AST_PER_36 | 0.15 |
| STL_PER_36 | 0.05 |
| BLK_PER_36 | 0.05 |
| FG_PCT     | 0.15 |
| FG3_PCT    | 0.10 |
| FT_PCT     | 0.10 |

---

### 4. Campeonatos y índice final

Se añade el impacto de los campeonatos ganados, normalizados respecto al máximo:

```
GOAT_INDEX_FINAL = GOAT_INDEX × α + CHAMPIONSHIPS_NORM × (1 - α)
```

Con:

* `α = 0.9`

Esto prioriza el rendimiento individual sin ignorar el éxito colectivo.

---

## 📊 Visualizaciones

El proyecto incluye:

1. **Ranking final GOAT** (barra horizontal)
2. **Impacto de campeonatos vs GOAT Index** (scatter plot)
3. **Radar chart** con el perfil estadístico de cada jugador

Los colores del radar están alineados con los equipos históricos:

* Michael Jordan → Rojo (Chicago Bulls)
* Kobe Bryant → Amarillo (Los Angeles Lakers)
* LeBron James → Morado

---

## 🏆 Resultados

El ranking final obtenido es:

1. **Michael Jordan**
2. **LeBron James**
3. **Kobe Bryant**

Los resultados reflejan un equilibrio entre eficiencia, producción ofensiva y campeonatos.

El ranking final se exporta como archivo CSV:

```
goat_ranking_final.csv
```



---

## ⚙️ Tecnologías utilizadas

* Python
* pandas
* numpy
* matplotlib
* scikit-learn
* nba_api
* Jupyter Notebook

---

## 🔮 Trabajo futuro

* Ajustes por era y ritmo de juego
* Inclusión de métricas avanzadas (PER, WS, BPM)
* Ampliación del análisis a más jugadores

---

## 📌 Nota final

Este proyecto no pretende declarar un GOAT absoluto, sino ofrecer una **herramienta cuantitativa** que ayude a estructurar el debate de forma objetiva y reproducible.

---

*(Existe también una versión del README en inglés para uso internacional o portfolio profesional.)*
