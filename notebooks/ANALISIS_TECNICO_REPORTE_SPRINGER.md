# Analisis tecnico para reporte academico estilo Springer Nature

Nota de alcance: este documento se elaboro a partir de la inspeccion de la carpeta del proyecto y de los artefactos ya generados. No se reinventaron resultados ni se modifico la logica principal. Solo se agrego una prueba minima de evidencia en `tests/test_evidence_artifacts.py`, la cual valida archivos existentes.

## 1. Resumen del proyecto analizado

Nombre tentativo del proyecto: **Sistema de recomendacion de candidatos para reclutamiento basado en similitud estructurada y modelos de aprendizaje automatico**.

Descripcion del sistema: el proyecto implementa un prototipo local para priorizar candidatos frente a vacantes de tecnologia. El flujo carga insumos en Excel y PDF, normaliza candidatos y vacantes, expande la base con datos artificiales, genera pares candidato-vacante, calcula variables de similitud, asigna pseudo-etiquetas auditables, entrena modelos comparables y exporta metricas, tablas, graficas, validaciones y libros Excel. Tambien incluye una interfaz Streamlit para explorar rankings, metricas, auditoria y QA.

Objetivo principal: construir una evidencia reproducible para evaluar y documentar un prototipo de recomendacion en RRHH, con comparacion entre implementaciones base y optimizadas de algoritmos desde cero, resultados cuantitativos y visualizacion interactiva.

Lenguaje, librerias y frameworks usados:

| Categoria | Herramientas |
|---|---|
| Lenguaje | Python |
| Datos | pandas, numpy, openpyxl |
| Modelos | scikit-learn: DecisionTreeClassifier, MultinomialNB, MLPClassifier, TfidfVectorizer, TruncatedSVD, StandardScaler |
| Visualizacion | matplotlib, Streamlit |
| Exportacion | CSV, Parquet, Excel con openpyxl |
| Documentacion | scripts `export_docs.py`, `convert_docs.py`, documentos `.docx` y `.odt` |

Flujo general:

1. `run_pipeline.py` crea carpetas, copia insumos y carga candidatos/vacantes.
2. `src/ingestion/loaders.py` limpia Excel y extrae un ejemplo PDF mediante `pdftotext`.
3. `src/ingestion/synthetic_data.py` expande la base hasta 400 candidatos y 20 vacantes para obtener 8000 pares.
4. `src/features/engineering.py` genera todos los pares, calcula features de similitud y etiqueta con regla heuristica.
5. `src/models/training.py` entrena modelos `decision_tree`, `multinomial_nb` y `mlp`.
6. `src/evaluation/algorithm_benchmarks.py` compara implementaciones ingenuas y optimizadas de Naive Bayes y KNN.
7. `src/evaluation/reporting.py` exporta CSV, Parquet, Excel, graficas, QA, validacion de primeros 100 y proyeccion de 6 meses.
8. `src/app/streamlit_app.py` muestra rankings, metricas, auditoria, validacion y descargas.

## 2. Archivos revisados

Archivos de orquestacion y configuracion:

| Archivo | Uso principal |
|---|---|
| `run_pipeline.py` | Orquesta carga, datos sinteticos, features, entrenamiento, reportes y graficas. |
| `requirements.txt` | Declara pandas, numpy, openpyxl, scikit-learn, matplotlib, streamlit y tabulate. |
| `.env.example` | Define parametros como `SYNTHETIC_TARGET_PAIR_RECORDS=8000` y `SYNTHETIC_TARGET_VACANCY_RECORDS=20`. |
| `Dockerfile` | Contenedor del prototipo. |
| `README.md` | Describe ejecucion rapida, estructura y flujo. |

Archivos de logica principal:

| Archivo | Contenido |
|---|---|
| `src/ingestion/loaders.py` | Carga y limpieza de candidatos, vacantes y PDF. |
| `src/ingestion/synthetic_data.py` | Generacion de candidatos y vacantes sinteticas. |
| `src/features/engineering.py` | Construccion de pares, features de similitud, score heuristico y etiquetas. |
| `src/models/training.py` | Entrenamiento y evaluacion de modelos de sklearn. |
| `src/models/from_scratch.py` | Algoritmos base y optimizados desde cero. |
| `src/evaluation/algorithm_benchmarks.py` | Medicion de tiempos y metricas de algoritmos base/optimizados. |
| `src/evaluation/reporting.py` | Exportacion de resultados, QA, Excel, graficas y proyeccion. |
| `src/app/streamlit_app.py` | Interfaz Streamlit. |

Datos y artefactos principales:

| Ruta | Descripcion |
|---|---|
| `data/raw/CV_Example.xlsx` | Insumo original de candidatos, 100 registros. |
| `data/raw/Vacancies_Example.xlsx` | Insumo original de vacantes, 10 registros. |
| `data/processed/candidates_clean.csv` | Base limpia expandida de candidatos, 400 registros. |
| `data/processed/vacancies_clean.csv` | Base limpia expandida de vacantes, 20 registros. |
| `data/processed/pairwise_scores.csv` | Base principal de 8000 pares candidato-vacante. |
| `data/processed/candidate_label_audit.csv` | Mejor match por candidato y etiqueta asignada, 400 registros. |
| `artifacts/benchmarks/algorithm_benchmarks.csv` | Tiempos y metricas de versiones base/optimizadas. |
| `artifacts/validation/qa_test_results.csv` | Pruebas QA generadas por el pipeline. |
| `artifacts/validation/first_100_validation.csv` | Validacion inicial de primeros 100 registros. |
| `artifacts/validation/six_month_projection.csv` | Proyeccion proporcional a 6 meses. |
| `artifacts/exports/*.xlsx` | Resultados exportables a Excel. |
| `artifacts/figures/*.png` | Graficas y evidencia visual. |

## 3. Algoritmos identificados

Se identificaron dos algoritmos con versiones base y optimizadas explicitas:

| Algoritmo | Archivo | Version base | Version optimizada | Proposito |
|---|---|---|---|---|
| Naive Bayes Gaussiano desde cero | `src/models/from_scratch.py` | `NaiveBayesNaive` | `NaiveBayesOptimized` | Clasificar pares usando features estructuradas estandarizadas. |
| KNN por similitud desde cero | `src/models/from_scratch.py` | `SimilarityKnnNaive` | `SimilarityKnnOptimized` | Estimar probabilidad positiva a partir de los k vecinos mas cercanos. |

Tambien se identificaron algoritmos de soporte:

| Algoritmo de soporte | Archivo | Funcion | Uso |
|---|---|---|---|
| Scoring heuristico y etiquetado | `src/features/engineering.py` | `_compute_heuristic_score`, `build_pairwise_dataset` | Calcula `heuristic_score` y `label = int(score >= 65)`. |
| Generacion artificial proporcional | `src/ingestion/synthetic_data.py` | `expand_with_synthetic_data` | Ajusta candidatos y vacantes para alcanzar 8000 pares. |
| Proyeccion a 6 meses | `src/evaluation/reporting.py` | `build_six_month_projection` | Estima volumen futuro con crecimiento mensual de 12%. |

### Algoritmo 1: Naive Bayes Gaussiano

Archivo: `src/models/from_scratch.py`.

Funciones o clases: `NaiveBayesNaive`, `NaiveBayesOptimized`.

Entrada: matriz `X` con features estructuradas normalizadas y vector binario `y` con etiquetas 0/1.

Proceso: calcula priors, medias y varianzas por clase; en inferencia estima log-verosimilitud gaussiana y normaliza probabilidades.

Salida: probabilidades por clase y prediccion binaria.

Diferencias:

| Aspecto | Version base | Version optimizada |
|---|---|---|
| Calculo por clase | Recorre filas y features con ciclos Python. | Filtra matrices NumPy por clase y usa `mean(axis=0)` y `var(axis=0)`. |
| Inferencia | Calcula cada probabilidad fila-clase-feature en bucles. | Usa broadcasting: `X[:, None, :] - means[None, :, :]`. |
| Estructuras | Diccionarios y listas. | Arreglos NumPy apilados. |
| Estabilidad numerica | Usa log-probabilidades y resta de maximo por fila. | Mantiene log-probabilidades y vectoriza la normalizacion. |

Complejidad estimada:

| Fase | Base | Optimizada | Comentario |
|---|---:|---:|---|
| Entrenamiento | O(c * n * d) | O(c * n * d) | Misma complejidad asintotica, menor costo constante por vectorizacion. |
| Inferencia | O(m * c * d) | O(m * c * d) | Misma asintotica, operaciones C/NumPy en bloque. |
| Espacio | O(c * d) + listas temporales | O(c * d) + tensor temporal O(m * c * d) | La optimizada usa mas memoria en inferencia para ganar velocidad. |

Justificacion de optimizacion: se considera optimizada porque desplaza ciclos interpretados de Python hacia operaciones vectorizadas de NumPy, reduce conversiones `tolist()`, almacena parametros como matrices contiguas y procesa lotes completos.

### Algoritmo 2: KNN por similitud

Archivo: `src/models/from_scratch.py`.

Funciones o clases: `SimilarityKnnNaive`, `SimilarityKnnOptimized`.

Entrada: matriz `X` con features estructuradas estandarizadas y etiquetas `y`.

Proceso: guarda el conjunto de entrenamiento; para cada consulta calcula distancias euclidianas a los registros de entrenamiento; selecciona los k vecinos y promedia sus etiquetas.

Salida: probabilidad `[P(0), P(1)]` y prediccion binaria.

Diferencias:

| Aspecto | Version base | Version optimizada |
|---|---|---|
| Distancias | Tres ciclos: consulta, fila de entrenamiento, feature. | Broadcasting NumPy sobre consultas y entrenamiento. |
| Seleccion de vecinos | `sorted(distances)[:k]`, ordenamiento completo. | `np.argpartition`, seleccion parcial. |
| Votacion | Suma manual de etiquetas. | Indexacion vectorizada y `mean(axis=1)`. |
| Costo practico | Alto en inferencia por bucles y sort completo. | Menor latencia al evitar ordenamiento total. |

Complejidad estimada:

| Fase | Base | Optimizada | Comentario |
|---|---:|---:|---|
| Entrenamiento | O(n * d) | O(n * d) | Ambas solo almacenan/copian datos. |
| Inferencia | O(m * n * d + m * n log n) | O(m * n * d + m * n) promedio | `argpartition` evita ordenar todas las distancias. |
| Espacio | O(n * d) + O(n) por consulta | O(n * d) + O(m * n * d) temporal | La optimizada intercambia memoria por velocidad. |

Justificacion de optimizacion: se considera optimizada porque elimina ciclos internos Python y sustituye ordenamiento completo por seleccion parcial de vecinos, reduciendo el tiempo de inferencia sin cambiar las metricas obtenidas.

## 4. Codigo base y codigo optimizado

### Algoritmo 1: Naive Bayes Gaussiano

Fragmento de version base:

```python
class NaiveBayesNaive:
    def fit(self, X: np.ndarray, y: np.ndarray) -> "NaiveBayesNaive":
        self.classes_ = sorted(int(label) for label in set(y.tolist()))
        total_rows = len(y)
        for class_label in self.classes_:
            class_rows = []
            for row_index, label in enumerate(y):
                if int(label) == class_label:
                    class_rows.append(X[row_index].tolist())

            self.class_priors_[class_label] = len(class_rows) / max(1, total_rows)
            feature_means = []
            feature_variances = []
            for feature_index in range(X.shape[1]):
                values = [row[feature_index] for row in class_rows]
                mean = sum(values) / max(1, len(values))
                variance = sum((value - mean) ** 2 for value in values) / max(1, len(values))
                feature_means.append(mean)
                feature_variances.append(max(variance, self.epsilon))
```

Fragmento de version optimizada:

```python
class NaiveBayesOptimized:
    def fit(self, X: np.ndarray, y: np.ndarray) -> "NaiveBayesOptimized":
        self.classes_ = np.unique(y.astype(int))
        means = []
        variances = []
        priors = []
        for class_label in self.classes_:
            class_rows = X[y.astype(int) == int(class_label)]
            priors.append(len(class_rows) / max(1, len(y)))
            means.append(class_rows.mean(axis=0))
            variances.append(np.maximum(class_rows.var(axis=0), self.epsilon))
        self.class_priors_ = np.array(priors, dtype=float)
        self.means_ = np.vstack(means)
        self.variances_ = np.vstack(variances)
        return self

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        log_priors = np.log(np.maximum(self.class_priors_, self.epsilon))
        diff = X[:, None, :] - self.means_[None, :, :]
        log_likelihood = -0.5 * np.sum(np.log(2 * np.pi * self.variances_[None, :, :]), axis=2)
        log_likelihood = log_likelihood - 0.5 * np.sum((diff**2) / self.variances_[None, :, :], axis=2)
        log_scores = log_priors[None, :] + log_likelihood
        log_scores -= np.max(log_scores, axis=1, keepdims=True)
        exp_scores = np.exp(log_scores)
        return exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
```

Explicacion por bloques:

| Bloque | Explicacion |
|---|---|
| Identificacion de clases | La base usa `set(y.tolist())`; la optimizada usa `np.unique`. |
| Parametros por clase | La base extrae filas manualmente; la optimizada aplica mascara booleana. |
| Medias y varianzas | La base recorre cada feature; la optimizada calcula columnas completas con NumPy. |
| Inferencia | La base evalua fila por fila; la optimizada calcula un tensor fila-clase-feature. |
| Normalizacion | Ambas usan estabilizacion por maximo, pero la optimizada lo hace por lote. |

### Algoritmo 2: KNN por similitud

Fragmento de version base:

```python
class SimilarityKnnNaive:
    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        probabilities = []
        for query_row in X:
            distances = []
            for train_index, train_row in enumerate(self.X_train):
                squared_distance = 0.0
                for feature_index, query_value in enumerate(query_row):
                    difference = float(query_value) - float(train_row[feature_index])
                    squared_distance += difference * difference
                distances.append((math.sqrt(squared_distance), int(self.y_train[train_index])))
            neighbors = sorted(distances, key=lambda item: item[0])[: self.k]
            positive_votes = sum(label for _, label in neighbors)
            positive_probability = positive_votes / max(1, len(neighbors))
            probabilities.append([1 - positive_probability, positive_probability])
        return np.array(probabilities, dtype=float)
```

Fragmento de version optimizada:

```python
class SimilarityKnnOptimized:
    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        diff = X[:, None, :] - self.X_train[None, :, :]
        distances = np.sqrt(np.sum(diff**2, axis=2))
        neighbor_indexes = np.argpartition(
            distances,
            kth=min(self.k, self.X_train.shape[0] - 1),
            axis=1,
        )[:, : self.k]
        neighbor_labels = self.y_train[neighbor_indexes]
        positive_probabilities = neighbor_labels.mean(axis=1)
        return np.column_stack([1 - positive_probabilities, positive_probabilities])
```

Explicacion por bloques:

| Bloque | Explicacion |
|---|---|
| Calculo de distancias | La base calcula una distancia a la vez; la optimizada calcula todas con broadcasting. |
| Seleccion de vecinos | La base ordena todas las distancias; la optimizada usa particion parcial. |
| Votacion | La base suma etiquetas manualmente; la optimizada indexa etiquetas y promedia por fila. |

## 5. Explicacion de optimizacion

La optimizacion no cambia la logica estadistica de los algoritmos, sino su forma de ejecucion. En ambos casos se reemplazan ciclos interpretados de Python por operaciones vectorizadas de NumPy. En Naive Bayes, las medias, varianzas y probabilidades se calculan por matrices; en KNN, las distancias se generan por broadcasting y los vecinos se seleccionan con `np.argpartition` en lugar de ordenar todos los elementos.

Impacto observado en los artefactos:

| Familia | Fase | Base ms | Optimizada ms | Reduccion de tiempo | Speedup reportado |
|---|---:|---:|---:|---:|---:|
| Naive Bayes | Entrenamiento | 3.0844 | 0.6313 | 79.53% | 4.8858x |
| Naive Bayes | Inferencia | 11.7149 | 0.4369 | 96.27% | 26.8137x |
| KNN similitud | Entrenamiento | 0.0180 | 0.0303 | -68.33% | 0.5941x |
| KNN similitud | Inferencia | 4386.1960 | 499.8371 | 88.61% | 8.7753x |

Interpretacion: Naive Bayes mejora tanto entrenamiento como inferencia. KNN no tiene entrenamiento real, por lo que el tiempo de `fit` es despreciable y la version optimizada aparece ligeramente mas lenta en esa fase; la mejora relevante ocurre en inferencia, donde se reduce el costo practico de seleccionar vecinos.

## 6. Pruebas encontradas o generadas

Pruebas encontradas:

| Evidencia | Ruta | Resultado |
|---|---|---|
| QA del pipeline | `artifacts/validation/qa_test_results.csv` | 8/8 pruebas con estado `passed`. |
| Benchmarks de algoritmos | `artifacts/benchmarks/algorithm_benchmarks.csv` | 4 filas: base y optimizada para Naive Bayes y KNN. |
| Validacion primeros 100 | `artifacts/validation/first_100_validation.csv` | 100 registros, todos pendientes de revision humana. |
| Proyeccion 6 meses | `artifacts/validation/six_month_projection.csv` | 6 filas, una por mes. |

Prueba generada:

| Archivo | Proposito |
|---|---|
| `tests/test_evidence_artifacts.py` | Valida que existan 8000 pares, 400 candidatos, 20 vacantes, 411 positivos, 7589 negativos, cuatro benchmarks esperados, metricas equivalentes entre base y optimizada dentro de cada familia, validacion de 100 registros y proyeccion de 6 meses. |

No se encontro una suite formal previa dentro de `tests/`; la carpeta existia pero no contenia archivos. La prueba agregada es de evidencia y no modifica el comportamiento del sistema.

Casos de prueba:

| Caso | Evidencia | Resultado esperado | Resultado obtenido |
|---|---|---|---|
| Carga candidatos | QA-001 | Al menos 1 candidato | 400, passed |
| Carga vacantes | QA-002 | Al menos 1 vacante | 20, passed |
| Conteo de pares | QA-003 | 8000 pares | 8000, passed |
| Auditoria de aspirantes | QA-004 | Al menos 100 auditados | 400, passed |
| Validacion primeros 100 | QA-005 | 100 registros | 100, passed |
| Metricas de modelos | QA-006 | accuracy, precision, recall, f1, roc_auc | columnas presentes, passed |
| Proyeccion minima | QA-007 | 6 meses | 6, passed |
| Base artificial objetivo | QA-008 | 8000 pares | 8000, passed |

Observacion importante: los benchmarks base/optimizados no se ejecutaron sobre los 8000 pares completos. El archivo `algorithm_benchmarks.csv` indica `source_train_records=6400` y `source_test_records=1600`, pero el benchmark se mide sobre una muestra deterministica de `train_records=1600` y `test_records=400`. Para cumplir estrictamente una medicion base/optimizada sobre los 8000 registros completos, se debe ejecutar `run_from_scratch_benchmarks(train_df, test_df, max_train_records=6400, max_test_records=1600)` en un entorno Python funcional.

## 7. Resultados medidos

Metricas de modelos del prototipo:

| Modelo | Accuracy | Precision | Recall | F1 | ROC AUC |
|---|---:|---:|---:|---:|---:|
| heuristic | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| mlp | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| decision_tree | 0.9975 | 0.9467 | 1.0000 | 0.9726 | 1.0000 |
| multinomial_nb | 0.8875 | 0.1955 | 0.4930 | 0.2800 | 0.7510 |

Resultados de algoritmos base/optimizados:

| Modelo | Implementacion | Train ms | Inferencia ms | ms/registro | Accuracy | Precision | Recall | F1 |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| naive_bayes_naive | naive_loops | 3.0844 | 11.7149 | 0.029287 | 0.9925 | 0.9048 | 0.9500 | 0.9268 |
| naive_bayes_optimized | optimized_numpy | 0.6313 | 0.4369 | 0.001092 | 0.9925 | 0.9048 | 0.9500 | 0.9268 |
| similarity_knn_naive | naive_loops | 0.0180 | 4386.1960 | 10.965490 | 0.9950 | 1.0000 | 0.9000 | 0.9474 |
| similarity_knn_optimized | optimized_numpy | 0.0303 | 499.8371 | 1.249593 | 0.9950 | 1.0000 | 0.9000 | 0.9474 |

## 8. Cifras control

| Archivo | Filas | Columnas | Celdas nulas | Duplicados |
|---|---:|---:|---:|---:|
| `data/processed/candidates_clean.csv` | 400 | 32 | 0 | 0 |
| `data/processed/vacancies_clean.csv` | 20 | 41 | 19 | 0 |
| `data/processed/pairwise_scores.csv` | 8000 | 41 | 0 | 0 |
| `data/processed/candidate_label_audit.csv` | 400 | 12 | 0 | 0 |
| `artifacts/validation/first_100_validation.csv` | 100 | 10 | 0 | 0 |
| `artifacts/validation/six_month_projection.csv` | 6 | 11 | 0 | 0 |
| `artifacts/validation/qa_test_results.csv` | 8 | 5 | 0 | 0 |
| `artifacts/benchmarks/algorithm_benchmarks.csv` | 4 | 18 | 0 | 0 |
| `artifacts/metrics/metrics_summary.csv` | 4 | 6 | 0 | 0 |

Cifras del dataset principal:

| Metrica | Valor |
|---|---:|
| Pares unicos | 8000 |
| Candidatos unicos | 400 |
| Vacantes unicas | 20 |
| Etiquetas positivas | 411 |
| Etiquetas negativas | 7589 |
| Tasa positiva | 0.0514 |
| Modelo final seleccionado | mlp |
| Score heuristico minimo | 0.00 |
| Score heuristico maximo | 81.14 |
| Score heuristico promedio | 22.6427 |
| `final_rank_score` promedio | 0.0526 |

Distribuciones relevantes:

| Campo | Conteos principales |
|---|---|
| `source_file` candidatos | `synthetic_generated=300`, `CV_Example.xlsx=100` |
| `source_file` vacantes | `synthetic_generated=10`, `Vacancies_Example.xlsx=10` |
| `label` en pares | `0=7589`, `1=411` |
| `assigned_label` en auditoria | `1=236`, `0=164` |
| `predicted_label` en primeros 100 | `0=80`, `1=20` |
| `validation_status` primeros 100 | `pending_human_review=100` |

## 9. Base de datos de 8000 registros

La base de 8000 registros existe y corresponde a pares candidato-vacante, no a candidatos individuales.

| Elemento | Valor |
|---|---|
| Archivo principal | `data/processed/pairwise_scores.csv` |
| Formatos disponibles | CSV y Parquet (`data/processed/pairwise_scores.parquet`) |
| Registros exactos | 8000 |
| Columnas | 41 |
| Origen | 400 candidatos x 20 vacantes |
| Artificialidad | 300 candidatos sinteticos + 10 vacantes sinteticas, conservando 100 candidatos y 10 vacantes originales |
| Manifest | `artifacts/reports/synthetic_data_manifest.csv` |

Manifest de datos sinteticos:

| Metrica | Valor |
|---|---:|
| original_candidates | 100 |
| synthetic_candidates | 300 |
| total_candidates | 400 |
| original_vacancies | 10 |
| synthetic_vacancies | 10 |
| total_vacancies | 20 |
| expected_pair_records | 8000 |
| target_pair_records | 8000 |
| random_state | 42 |

Campos principales de `pairwise_scores.csv`:

| Grupo | Campos | Proposito |
|---|---|---|
| Identificacion | `pair_id`, `candidate_id`, `vacancy_id` | Trazabilidad del par evaluado. |
| Datos del candidato | `candidate_name`, `candidate_practice_area`, `candidate_position`, `candidate_job_level`, `candidate_years_experience`, `candidate_text` | Representacion del perfil. |
| Datos de la vacante | `vacancy_title`, `vacancy_practice_area`, `vacancy_job_level`, `vacancy_years_experience`, `vacancy_text` | Representacion del puesto requerido. |
| Texto combinado | `pair_text` | Entrada textual para TF-IDF y modelos de texto. |
| Etiquetado | `heuristic_score`, `label`, `label_reason` | Pseudo-etiqueta auditable y explicacion. |
| Features | 17 columnas de coincidencia, similitud, experiencia, skills e infraestructura | Entrada estructurada para modelos. |
| Scores | `score_heuristic`, `score_decision_tree`, `score_multinomial_nb`, `score_mlp`, `final_model_name`, `final_rank_score` | Resultados por modelo y score final de ranking. |

Tipos de datos inferidos:

| Tipo | Campos principales |
|---|---|
| String | IDs, nombres, puestos, textos, razones de etiqueta, modelo final. |
| Integer | `label`. |
| Float | `heuristic_score`, features de similitud, scores de modelos y `final_rank_score`. |

Algoritmos que usan la base:

| Algoritmo | Uso |
|---|---|
| Entrenamiento sklearn | Usa `pair_df` con `STRUCTURED_FEATURES`, `pair_text` y `label`. |
| Benchmarks desde cero | Usa features estructuradas y `label` en muestra deterministica. |
| Streamlit ranking | Filtra vacantes y ordena por columna de score. |
| Auditoria de etiquetas | Agrupa por candidato y conserva mejor match. |
| Proyeccion | Usa conteo de candidatos, vacantes, pares y tasa positiva. |

## 10. Etiquetado de primeros 100 registros

El etiquetado si aplica. La regla central se encuentra en `src/features/engineering.py`: despues de calcular el score heuristico, se asigna `label = int(heuristic_score >= 65)`.

| Elemento | Valor |
|---|---|
| Algoritmo que etiqueta | Scoring heuristico en `build_pairwise_dataset`. |
| Regla | `heuristic_score >= 65` asigna etiqueta 1; en caso contrario 0. |
| Columna en pares | `label`. |
| Columna en auditoria | `assigned_label`. |
| Columna en primeros 100 | `predicted_label`. |
| Registros auditados | 400 candidatos en `candidate_label_audit.csv`. |
| Primeros 100 generados | 100 registros en `first_100_validation.csv`. |
| Etiquetados en primeros 100 | 100. |
| Pendientes de revision humana | 100. |
| Sin etiqueta en primeros 100 | 0. |

Resumen de los primeros 100:

| Etiqueta | Conteo |
|---|---:|
| 0 | 80 |
| 1 | 20 |

Muestra de registros:

| ID | Candidato | Vacante | Score | Etiqueta | Justificacion breve |
|---|---|---|---:|---:|---|
| CAND-001 | Sofia Torres | Data Engineer | 45.21 | 0 | Area 25/25, posicion 0/20, experiencia 20/20; stack compartido no detectado. |
| CAND-002 | Camila Perez | Cybersecurity Analyst | 65.00 | 1 | Area 25/25, posicion 20/20, seniority+experience 20/20. |
| CAND-003 | Juan Ramirez | Cybersecurity Analyst | 50.00 | 0 | Area y posicion coinciden, pero seniority+experience aporta 5/20. |
| CAND-004 | Ramiro Sanchez | Cloud Engineer | 65.21 | 1 | Area, posicion y experiencia alcanzan umbral. |
| CAND-005 | Rocio Fuentes | QA Engineer | 45.33 | 0 | Area y experiencia suficientes, posicion sin coincidencia fuerte. |
| CAND-006 | Carmen Morales | UI/UX Designer | 48.33 | 0 | Area y experiencia aportan, similitud de posicion parcial. |
| CAND-007 | Ana Lopez | Data Engineer | 65.21 | 1 | Area, posicion y experiencia alcanzan umbral. |
| CAND-008 | Adriana Cruz | Backend Developer | 49.18 | 0 | No alcanza el umbral de 65. |
| CAND-009 | Armando Ortiz | Data Scientist | 43.10 | 0 | Puntaje por debajo del umbral. |
| CAND-010 | Joaquin Ortega | Data Engineer | 65.21 | 1 | Area, posicion y experiencia alcanzan umbral. |

Limitacion: la validacion humana final aun no esta concluida; el estado de los 100 registros es `pending_human_review`.

## 11. Proyeccion a 6 meses

El proyecto no usa una serie historica temporal real. La proyeccion se implementa como una estimacion proporcional en `build_six_month_projection`.

Supuestos:

| Supuesto | Valor |
|---|---:|
| Candidatos base | 400 |
| Vacantes base | 20 |
| Pares base | 8000 |
| Crecimiento mensual | 12% acumulado lineal sobre el mes base |
| Tasa positiva | 0.0514 |
| Revisiones Top N por vacante | 10 |
| Minutos por revision manual | 5 |
| Precision esperada | Precision del mejor modelo, 1.0 en el artefacto |

Tabla de proyeccion:

| Mes | Candidatos esperados | Vacantes esperadas | Pares esperados | Pares positivos esperados | Revisiones manuales sin IA | Revisiones con top10 | Minutos ahorrados |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 400 | 20 | 8000 | 411 | 8000 | 200 | 39000 |
| 2 | 448 | 22 | 9856 | 506 | 9856 | 220 | 48180 |
| 3 | 496 | 25 | 12400 | 637 | 12400 | 250 | 60750 |
| 4 | 544 | 27 | 14688 | 755 | 14688 | 270 | 72090 |
| 5 | 592 | 30 | 17760 | 912 | 17760 | 300 | 87300 |
| 6 | 640 | 32 | 20480 | 1052 | 20480 | 320 | 100800 |

Limitacion: no es una prediccion estadistica avanzada, sino una proyeccion proporcional derivada del volumen actual, la tasa positiva actual y un crecimiento mensual fijo.

## 12. Resultados visibles en Streamlit

Archivo principal: `src/app/streamlit_app.py`.

Comando esperado:

```bash
streamlit run src/app/streamlit_app.py
```

El README propone:

```bash
.venv_ssp/bin/streamlit run src/app/streamlit_app.py
```

Vistas implementadas:

| Vista | Funcion | Resultados |
|---|---|---|
| Ranking | `render_ranking` | Filtros por vacante, modelo, top N, area, nivel y anos; tabla de candidatos priorizados; explicacion del score. |
| Metricas | `render_metrics` | Tabla de metricas y graficas `model_metrics.png`, `roc_curves.png`, `score_distribution.png`; descarga `benchmarks.xlsx`. |
| Auditoria | `render_audit` | Tabla `candidate_label_audit.csv`; descarga `candidate_audit.xlsx`. |
| QA / Validacion | `render_qa_validation` | KPIs de QA, pruebas, cifras control, manifest sintetico, benchmarks naive/optimizado, validacion primeros 100, proyeccion 6 meses y descargas Excel. |

Resultados mostrados:

| Requisito | Estado en Streamlit |
|---|---|
| Ejecuta algoritmos | No entrena en vivo; consume resultados del pipeline. Permite elegir score para ranking. |
| Tablas | Ranking, metricas, auditoria, QA, manifest, benchmarks, primeros 100 y proyeccion. |
| Graficas | Metricas, curvas ROC y distribucion de scores. |
| Tiempos de ejecucion | Muestra `algorithm_benchmarks.csv` en la vista QA / Validacion. |
| Cifras control | Muestra `benchmark_summary.csv` y manifest sintetico. |
| Descargas | `final_results.xlsx`, `benchmarks.xlsx`, `candidate_audit.xlsx`. |
| Proyeccion 6 meses | Si, en vista QA / Validacion. |
| Etiquetado primeros 100 | Si, en vista QA / Validacion. |

Evidencia visual existente: `artifacts/figures/dashboard_preview.png`, con top candidatos priorizados y resumen de metricas; el modelo por defecto en esa evidencia es `mlp`.

Nota de reproduccion: en esta terminal no se pudo ejecutar Streamlit porque no hay un ejecutable Python/Streamlit Windows disponible; las venv existentes usan layout tipo Unix y el stub `python` devuelve acceso denegado. La documentacion anterior se basa en codigo y artefactos ya generados.

## 13. Resultados exportables en Excel

Exportacion implementada en `src/evaluation/reporting.py`, funcion `save_excel_workbook`, usando `pd.ExcelWriter(..., engine="openpyxl")`.

Libros Excel generados:

| Archivo | Hojas reales | Contenido |
|---|---|---|
| `artifacts/exports/final_results.xlsx` | `ranking_results` A1:AO8001; `metrics` A1:F5; `benchmark_summary` A1:C10; `six_month_projection` A1:K7; `algorithm_benchmarks` A1:R5; `synthetic_manifest` A1:B10 | Ranking completo, metricas, cifras control, proyeccion, benchmarks y manifest sintetico. |
| `artifacts/exports/candidate_audit.xlsx` | `candidate_audit` A1:L401; `first_100_validation` A1:J101 | Auditoria por candidato y validacion de primeros 100. |
| `artifacts/exports/benchmarks.xlsx` | `benchmark_summary` A1:C10; `metrics` A1:F5; `qa_test_results` A1:E9; `algorithm_benchmarks` A1:R5; `synthetic_manifest` A1:B10 | Evidencia de tiempos, QA, metricas y base artificial. |

Requisitos cubiertos por Excel:

| Requisito | Archivo |
|---|---|
| Resultados de ranking | `final_results.xlsx`, hoja `ranking_results`. |
| Metricas de modelos | `final_results.xlsx` y `benchmarks.xlsx`, hoja `metrics`. |
| Tiempos base/optimizados | `final_results.xlsx` y `benchmarks.xlsx`, hoja `algorithm_benchmarks`. |
| Cifras control | `benchmark_summary`, `synthetic_manifest`, `qa_test_results`. |
| Proyeccion 6 meses | `final_results.xlsx`, hoja `six_month_projection`. |
| Etiquetado primeros 100 | `candidate_audit.xlsx`, hoja `first_100_validation`. |

## 14. Informacion lista para el reporte

### Titulo tentativo

**Prototipo reproducible de recomendacion de candidatos para reclutamiento mediante similitud estructurada, aprendizaje automatico y optimizacion vectorizada de algoritmos desde cero**

### Resumen

Este proyecto aborda el problema de priorizar candidatos frente a vacantes tecnologicas en un proceso de reclutamiento asistido por inteligencia artificial. El objetivo fue construir un prototipo reproducible que integre limpieza de datos, generacion de registros artificiales, calculo de similitud candidato-vacante, etiquetado heuristico, entrenamiento de modelos y visualizacion de resultados. La metodologia utilizo Python, pandas, NumPy, scikit-learn, matplotlib y Streamlit. La base principal contiene 8000 pares candidato-vacante generados a partir de 400 candidatos y 20 vacantes, con trazabilidad de registros originales y sinteticos. Se analizaron dos algoritmos implementados desde cero: Naive Bayes Gaussiano y KNN por similitud, ambos con version base basada en ciclos y version optimizada con operaciones vectorizadas de NumPy. Los resultados muestran que Naive Bayes optimizado redujo el tiempo de inferencia de 11.7149 ms a 0.4369 ms, mientras que KNN optimizado redujo la inferencia de 4386.1960 ms a 499.8371 ms en la muestra de benchmark. El sistema exporta resultados a Excel, presenta metricas y auditoria en Streamlit, incluye validacion de los primeros 100 registros y genera una proyeccion proporcional de seis meses. Su utilidad principal es ofrecer evidencia tecnica y academica para evaluar un prototipo de recomendacion auditable en RRHH.

### Palabras clave

Reclutamiento inteligente; recomendacion de candidatos; Naive Bayes; KNN; optimizacion vectorizada; Streamlit.

### Introduccion

Los procesos de reclutamiento en perfiles tecnologicos requieren comparar informacion heterogenea: experiencia, nivel profesional, habilidades, tecnologias, responsabilidades y requisitos de vacantes. Cuando el volumen de candidatos y puestos aumenta, la revision manual de todas las combinaciones se vuelve costosa y propensa a inconsistencias. Este prototipo aborda esa situacion mediante una canalizacion reproducible que transforma datos de candidatos y vacantes en pares evaluables y rankings priorizados.

La importancia del sistema radica en que no solo genera predicciones, sino que conserva explicaciones auditables mediante un score heuristico y una razon de etiqueta. Esto permite que el resultado pueda revisarse antes de asumirlo como decision automatizada. La necesidad de optimizacion aparece en la comparacion de algoritmos desde cero: una implementacion ingenua puede ser didactica, pero no necesariamente escalable. Por ello, el proyecto incluye versiones vectorizadas de Naive Bayes y KNN, con mediciones de tiempo.

El alcance del proyecto es academico y prototipico. No incorpora integraciones reales con bolsas de trabajo ni validacion humana terminada; las APIs externas estan definidas como stubs. La etiqueta objetivo deriva de una heuristica, por lo que las metricas deben interpretarse como evidencia preliminar, no como desempeno productivo validado en campo.

### Metodologia

La metodologia se organiza en seis etapas: ingesta, expansion artificial, construccion de pares, entrenamiento, evaluacion y visualizacion. Primero se cargan los archivos `CV_Example.xlsx`, `Vacancies_Example.xlsx` y un PDF de ejemplo. Luego, `expand_with_synthetic_data` agrega 300 candidatos sinteticos y 10 vacantes sinteticas para alcanzar 400 candidatos y 20 vacantes. La combinacion cartesiana produce 8000 pares.

En la etapa de features, `build_pairwise_dataset` calcula 17 variables estructuradas: coincidencias de area y posicion, similitud de texto, ajuste de nivel, solapamiento de experiencia, habilidades, lenguajes, frameworks, bases de datos, nube, responsabilidades, calificaciones y herramientas. Con esos valores se calcula un score heuristico ponderado y se asigna `label` si el score es mayor o igual a 65.

En entrenamiento se comparan cuatro enfoques principales: heuristica, arbol de decision, Naive Bayes multinomial y MLP. Para el apartado de optimizacion se ejecuta un benchmark separado con dos algoritmos desde cero, cada uno en version base y optimizada. Los tiempos se miden con `perf_counter` y se guardan en `algorithm_benchmarks.csv`.

Las salidas se presentan en CSV, Parquet, Excel, PNG y Streamlit. La proyeccion de seis meses se calcula proporcionalmente con crecimiento mensual de 12%, tasa positiva actual y ahorro estimado por pasar de revision total a top 10 por vacante.

### Algoritmos implementados

Pseudocodigo de Naive Bayes optimizado:

```text
Entrada: X, y
Obtener clases unicas
Para cada clase:
    seleccionar filas con mascara booleana
    calcular prior, media y varianza por feature
Para predecir:
    calcular diferencias X - medias con broadcasting
    calcular log-verosimilitud gaussiana
    sumar log-priors
    estabilizar restando maximo por fila
    normalizar exponenciales
Salida: probabilidades y clase con mayor probabilidad
```

Pseudocodigo de KNN optimizado:

```text
Entrada: X_train, y_train, X_consulta, k
Guardar X_train y y_train
Para predecir:
    calcular tensor de diferencias entre consultas y entrenamiento
    sumar cuadrados por feature y obtener distancias
    seleccionar k indices menores con argpartition
    tomar etiquetas de vecinos
    promediar etiquetas positivas
Salida: probabilidad positiva y clase binaria
```

Complejidad y justificacion se reportan en las secciones 3 y 5.

### Optimizacion del codigo

Las limitaciones de la version inicial eran el uso de bucles Python, conversiones repetidas a listas, ordenamiento completo de distancias y estructuras de datos menos eficientes para calculo numerico. La version optimizada usa arreglos NumPy, mascaras booleanas, broadcasting, sumas vectorizadas y seleccion parcial de vecinos.

El impacto en escalabilidad es especialmente visible en inferencia. Naive Bayes optimizado alcanza un speedup de 26.8137x en inferencia y KNN optimizado alcanza 8.7753x. En entrenamiento, KNN no se beneficia porque solo almacena datos; por eso la mejora importante esta en prediccion.

### Resultados

Los resultados principales son:

| Resultado | Valor |
|---|---:|
| Pares generados | 8000 |
| Candidatos | 400 |
| Vacantes | 20 |
| Etiquetas positivas en pares | 411 |
| Etiquetas negativas en pares | 7589 |
| QA aprobados | 8/8 |
| Primeros 100 validados para revision | 100 |
| Meses proyectados | 6 |
| Libros Excel generados | 3 |
| Figuras PNG generadas | 8+ |

La comparacion de tiempos muestra mejoras de inferencia sin perdida de metricas dentro de cada familia base/optimizada. La interfaz Streamlit permite revisar rankings, metricas, auditoria, benchmarks, manifest de datos sinteticos, validacion de 100 registros y proyeccion. Los libros Excel consolidan ranking, metricas, QA, benchmarks, manifest sintetico y proyeccion.

### Discusion

Los resultados sugieren que la vectorizacion es una estrategia efectiva para acelerar algoritmos numericos sin cambiar su comportamiento funcional. En Naive Bayes, la reduccion del tiempo de entrenamiento e inferencia se debe a operaciones matriciales sobre clases y features. En KNN, la ventaja aparece en inferencia porque el algoritmo base ordena todas las distancias para cada consulta, mientras la version optimizada usa seleccion parcial.

Sin embargo, el proyecto tiene limitaciones relevantes. La etiqueta objetivo proviene de una heuristica; por ello, las metricas perfectas del modelo heuristico y del MLP deben interpretarse con cautela, ya que el sistema aprende o reproduce una regla interna y no necesariamente una decision validada por expertos humanos. Ademas, gran parte de la base es artificial, lo que permite pruebas de volumen pero no reemplaza datos reales de contratacion. La proyeccion de seis meses no es un modelo estadistico, sino una extrapolacion proporcional.

### Conclusion

El proyecto logro integrar una canalizacion completa para recomendacion de candidatos, desde ingesta y expansion artificial hasta visualizacion y exportacion. Se analizaron dos algoritmos desde cero, Naive Bayes y KNN, cada uno con version base y version optimizada. Las mejoras mas importantes se observaron en inferencia: 26.8137x para Naive Bayes y 8.7753x para KNN en la muestra de benchmark.

Streamlit aporta valor al permitir explorar rankings, metricas, auditoria y evidencia QA de forma interactiva. Excel aporta trazabilidad y portabilidad para revisar resultados fuera del entorno de ejecucion. Como trabajo futuro se recomienda ejecutar benchmarks completos sobre los 8000 pares, incorporar validacion humana real, corregir codificacion de caracteres en algunos textos mostrados, ampliar pruebas automatizadas y reemplazar stubs externos por integraciones reales cuando existan credenciales y controles de seguridad.

### Disponibilidad de datos y codigo

| Elemento | Ruta |
|---|---|
| Datos crudos | `data/raw/` |
| Datos procesados | `data/processed/` |
| Base de 8000 pares | `data/processed/pairwise_scores.csv` |
| Algoritmos | `src/models/from_scratch.py`, `src/features/engineering.py`, `src/models/training.py` |
| Benchmarks | `src/evaluation/algorithm_benchmarks.py`, `artifacts/benchmarks/algorithm_benchmarks.csv` |
| Pruebas QA | `artifacts/validation/qa_test_results.csv` |
| Prueba de evidencia agregada | `tests/test_evidence_artifacts.py` |
| Streamlit | `src/app/streamlit_app.py` |
| Excel | `artifacts/exports/` |
| Figuras | `artifacts/figures/` |

## 15. Limitaciones detectadas

1. No hay suite formal de pruebas previa en `tests/`; se agrego una prueba minima de evidencia.
2. El benchmark base/optimizado usa muestra deterministica de 1600 entrenamiento y 400 prueba, no los 8000 pares completos.
3. Las etiquetas son pseudo-etiquetas heuristicas; no hay validacion humana final.
4. La validacion de primeros 100 existe, pero todos los registros estan en estado `pending_human_review`.
5. Las metricas perfectas de `heuristic` y `mlp` deben discutirse como evidencia preliminar, porque la etiqueta objetivo se deriva de la heuristica.
6. La base artificial sirve para volumen y reproducibilidad, pero no representa una distribucion real de contrataciones.
7. La proyeccion a 6 meses es proporcional, no predictiva.
8. Las APIs externas estan como stubs y no se validan contra servicios reales.
9. En algunos textos de Streamlit y reportes se observan problemas de codificacion de caracteres al leer desde consola.
10. En esta terminal no se pudo ejecutar Python/Streamlit por falta de ejecutable Windows funcional; se analizaron artefactos ya generados.

## 16. Instrucciones para reproducir resultados

Requisitos previos: Python instalado y accesible como `python`, dependencias de `requirements.txt` y herramienta `pdftotext` disponible en el sistema para la extraccion del PDF.

Comandos sugeridos:

```bash
python -m venv .venv
```

En Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python run_pipeline.py
pytest tests/test_evidence_artifacts.py
streamlit run src/app/streamlit_app.py
```

En entornos Unix:

```bash
source .venv/bin/activate
pip install -r requirements.txt
python run_pipeline.py
pytest tests/test_evidence_artifacts.py
streamlit run src/app/streamlit_app.py
```

Salidas esperadas:

| Salida | Ruta |
|---|---|
| Base principal | `data/processed/pairwise_scores.csv` |
| Metricas | `artifacts/metrics/metrics_summary.csv` |
| Benchmarks | `artifacts/benchmarks/algorithm_benchmarks.csv` |
| QA | `artifacts/validation/qa_test_results.csv` |
| Primeros 100 | `artifacts/validation/first_100_validation.csv` |
| Proyeccion | `artifacts/validation/six_month_projection.csv` |
| Excel | `artifacts/exports/final_results.xlsx`, `candidate_audit.xlsx`, `benchmarks.xlsx` |
| Streamlit | `http://localhost:8501` |

Checklist de calidad:

| Criterio | Estado |
|---|---|
| Se identificaron por lo menos dos algoritmos | Cumplido: Naive Bayes y KNN. |
| Se encontro version base | Cumplido: `NaiveBayesNaive`, `SimilarityKnnNaive`. |
| Se encontro version optimizada | Cumplido: `NaiveBayesOptimized`, `SimilarityKnnOptimized`. |
| Se usaron 8000 registros artificiales | Cumplido como 8000 pares candidato-vacante. |
| Hay pruebas | Cumplido con QA CSV y prueba de evidencia agregada. |
| Hay tiempos de ejecucion | Cumplido en `algorithm_benchmarks.csv`. |
| Hay cifras control | Cumplido en `benchmark_summary.csv`, QA y analisis de CSV. |
| Hay resultados Streamlit | Cumplido por implementacion y `dashboard_preview.png`; no ejecutado en esta terminal. |
| Hay Excel | Cumplido con tres libros en `artifacts/exports/`. |
| Se analizo etiquetado primeros 100 | Cumplido. |
| Se incluyo proyeccion 6 meses | Cumplido. |
| Estilo academico | Cumplido en seccion 14. |
| Se evitaron resultados inventados | Cumplido; donde falta medicion completa, se declara limitacion. |
