# Prototipo IA para Reclutamiento

Proyecto de Fase 2 para construir un sistema de recomendacion de candidatos en Recursos Humanos usando un pipeline local reproducible, tres modelos de `sklearn`, una app minima en Streamlit y nueve entregables en Word.

## Ejecucion rapida

```bash
.venv_ssp/bin/python run_pipeline.py
.venv_ssp/bin/python export_docs.py
.venv_ssp/bin/streamlit run src/app/streamlit_app.py
```

## Estructura

- `data/raw`: copias de los insumos originales.
- `data/processed`: tablas limpias y salidas del pipeline.
- `artifacts`: metricas, figuras y reportes auxiliares.
- `docs_src`: fuentes en Markdown de los entregables.
- `docs`: archivos `.docx` generados con Pandoc.
- `src`: codigo del prototipo.

## Flujo de trabajo

1. Se copian los archivos de entrada a `data/raw`.
2. Se limpian los datasets de candidatos y vacantes.
3. Se generan 1000 pares candidato-vacante.
4. Se calculan features, puntajes heurisiticos y pseudo-etiquetas.
5. Se entrenan tres modelos comparables.
6. Se exportan metricas, tablas, figuras y evidencias.
7. Se generan nueve entregables Word basados en los artefactos reales.

## Notas

- Las integraciones externas a bolsas de trabajo se documentan como `stubs`.
- El despliegue seguro se modela como un entorno local/containerizado.
- Las metricas son preliminares porque la etiqueta objetivo se deriva de una heuristica y no de evaluacion humana final.
- La configuracion operativa base se documenta en `.env.example`.
