# 🐐 NBA GOAT Index

Análisis comparativo de Michael Jordan, Kobe Bryant y LeBron James mediante un índice cuantitativo reproducible.

---

## 📌 Descripción del proyecto

El debate sobre quién es el **GOAT (Greatest Of All Time)** de la NBA es uno de los más recurrentes en el mundo del deporte. Este proyecto busca aportar una mirada **data-driven**, construyendo un **GOAT Index** que combine métricas ofensivas, defensivas, de eficiencia y éxito colectivo.

El objetivo no es declarar una verdad absoluta, sino ofrecer un **marco cuantitativo transparente y defendible** que permita comparar a tres de los principales candidatos históricos:

* Michael Jordan
* Kobe Bryant
* LeBron James

---

## 🎯 Objetivos

* Construir un índice numérico que sintetice el rendimiento integral de un jugador
* Normalizar estadísticas para permitir comparaciones justas entre eras y contextos
* Incorporar tanto **rendimiento individual** como **éxito colectivo (títulos)**
* Practicar un flujo de trabajo completo de análisis de datos (Python + SQL)

---

## 📊 Metodología

### 1. Recolección de datos

Se utilizan datos oficiales de la NBA y datasets históricos, incluyendo:

* Estadísticas de carrera por temporada
* Resultados de Finales NBA
* Cantidad de campeonatos ganados

### 2. Preparación de los datos

* Selección de métricas relevantes
* Normalización por minuto y por 36 minutos
* Escalado de variables mediante **MinMaxScaler**

### 3. Métricas incluidas

**Ofensivas**

* Puntos por 36 minutos
* Asistencias por 36 minutos

**Defensivas**

* Rebotes por 36 minutos
* Robos por 36 minutos
* Tapones por 36 minutos

**Eficiencia**

* Field Goal %
* Three Point %
* Free Throw %

**Éxito colectivo**

* Campeonatos NBA (normalizados)

### 4. Construcción del GOAT Index

El índice se calcula como una **suma ponderada** de las métricas escaladas:

* GOAT Index base: rendimiento individual
* GOAT Index final: 90% rendimiento + 10% títulos

Las ponderaciones pueden ajustarse para análisis de sensibilidad.

---

## 🧮 Tecnologías utilizadas

* **Python** (pandas, numpy, scikit-learn)
* **SQLite** (análisis y validación con SQL)
* **Jupyter Notebook**
* **VS Code**

---

## 📈 Resultados (preliminares)

El ranking final devuelve una única fila por jugador, con un GOAT Index agregado a nivel carrera.

> ⚠️ Los resultados deben interpretarse en el contexto de la metodología y ponderaciones elegidas.

---

## 📂 Estructura del proyecto

```
ProyectoNBA/
├── Proyecto NBA GOAT.ipynb
├── Ordered.Analysis.ipynb
├── NBA_PLAYERS.csv
├── NBA_TEAMS.csv
├── NBA_Finals_and_MVP.csv
├── NBA_FINALS_STATS.ipynb
├── README.md
```

---

## 🔍 Próximos pasos

* Añadir visualizaciones finales (ranking y comparación por métricas)
* Análisis de sensibilidad de ponderaciones
* Extensión del modelo a más jugadores históricos
* Comparación por picos de carrera vs longevidad

---

## 📎 Disclaimer

Este proyecto es educativo y exploratorio. El GOAT Index no pretende ser una verdad absoluta, sino una herramienta analítica para enriquecer el debate.

---

## ✍️ Autor

Proyecto desarrollado como ejercicio de análisis de datos aplicado al deporte.
