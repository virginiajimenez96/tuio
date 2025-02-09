# Discusión sobre la elección del modelo

En este problema de clasificación he entrenado tres modelos:

- Logistic regression
- Random forest
- XGBoost

El objetivo era predecir la probabilidad de que un cliente presente una reclamación en los prócximos 12 meses.

## Entrenamiento de los modelos con parámetros iniciales

Al entrenar los tres modelos con unos parámetros iniciales escogidos al azar, los resultados son:

| Model                | Precision | Recall | F1-Score | ROC-AUC |
|----------------------|-----------|--------|----------|---------|
| Logistic Regression  | 0.537     | 0.483  | 0.509    | 0.579   |
| Random Forest        | 0.833     | 0.674  | 0.745    | 0.859   |
| XGBoost              | 0.758     | 0.843  | 0.798    | 0.864   |

- Logistic regression:
  - Tiene un mal resultado, lo que nos indica que no es un buen modelo para este problema.
  - Un motivo puede ser porque el modelo supone que las variables tienen una relación lineal con la probabilidad que estamos calculando.
  - El modelo no conseguirá identificar correctamente a los clientes que presentarán una reclamación, generando un alto número de falsos negativos (debido a un recall muy bajo).
  - Además ROC-AUC está cerca de 0.5, lo que sugiere que es casi una predicción aleatoria.

- Random forest:
  - Mejora con respecto a logistic regression.
  - Recall de 0.674 indica que tendría falsos negativos.
  - Aún tiene margen de mejora.

- XGBoost:
  - Modelo con mejores resultados.
  - Los valores un poco más altos de precision y recall indican que sus predicciones son lás más fiables de los tres modelos (menos falsos positivos y falsos negativos).
  - El valor ROC-AUC indica su buena capacidad predictiva.

## Entrenamiento de los modelos utilizando parameters tunning

Para mejorar el rendimiento de los modelos que mejor se han comportado (random forest y XGBoost), se ha intentado realizar un ajuste de sus parámetros, de forma que se ecuentren los valores más óptimos.

Después de encontrar los parámetros óptimos, los resultados han sido:

| Model          | Precision | Recall | F1-Score | ROC-AUC |
|----------------|-----------|--------|----------|---------|
| Random Forest  | 0.793     | 0.820  | 0.807    | 0.918   |
| XGBoost        | 0.880     | 0.910  | 0.895    | 0.949   |

- XGBoost sigue siendo el mejor modelo y mejora un poco su recall y F1-Score.
- Random forest mejora su recall, detectando más reclamaciones que antes.
- Los valores de XGBoost después del ajuste pueden indicar overfitting.
  
## Futuros pasos para mejorar el modelo

- Explorar otros valores para los parámetros.
- Comprobar overfitting comparando el rendimiento en el conjunto de entrenamiento vs test. Ajustar el tamaño de las muestras que se usan para entrenar y para testing.
- Analizar las features elegidas, crear nuevas o descartar las que no aporten información importante.
- Mejorar la calidad de los datos.
