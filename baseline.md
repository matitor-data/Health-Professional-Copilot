# Baseline del Nutrition Module

## Que es la baseline

La baseline es la version mas sencilla del sistema que permite comprobar si un modelo de lenguaje
puede ayudar a preparar una consulta nutricional.

Su objetivo no es representar el producto final. Funciona como punto de comparacion: cuando se
incorporen los dos agentes, la busqueda de evidencia y las reglas de seguridad avanzadas, podremos
medir si realmente mejoran los resultados respecto de esta implementacion simple.

## Como funciona

El flujo tiene cuatro pasos:

```text
Datos estructurados del paciente
              ↓
       Un prompt versionado
              ↓
       Una llamada al LLM
              ↓
Brief validado con Pydantic
```

1. El runner carga uno o varios casos desde el dataset.
2. Los datos del paciente se validan antes de enviarlos al modelo.
3. El modelo recibe un unico prompt con las reglas del Nutrition Module.
4. La respuesta se convierte en un brief estructurado y se valida.
5. El brief se compara con la rubrica esperada del caso.
6. Los resultados, errores y metricas se guardan en una carpeta identificada por fecha y hora.

La baseline no utiliza herramientas, retrieval, base de conocimiento, Evidence Agent, Evidence
Gate ni ciclos autonomos. Cada paciente genera como maximo una llamada al modelo.

## Informacion de entrada

Cada caso contiene datos como:

- Edad, sexo, altura y peso.
- Motivo de consulta y objetivo principal.
- Diagnosticos medicos conocidos.
- Sintomas y duracion.
- Medicacion y suplementos.
- Patron alimentario, actividad fisica y descanso.
- Cambios recientes de peso.
- Resultados de laboratorio existentes.
- Antecedentes familiares y notas adicionales.

Los diagnosticos conocidos son contexto de entrada. La baseline no puede inventar, inferir ni
proponer un diagnostico medico.

## Contenido del brief

La salida sigue una estructura fija:

- `patient_overview`: resumen breve del caso.
- `known_medical_context`: diagnosticos y contexto medico ya informado.
- `information_to_clarify`: informacion ausente, ambigua o contradictoria.
- `suggested_questions`: entre 3 y 5 preguntas de alto valor.
- `nutrition_considerations`: aspectos nutricionales para revisar durante la consulta.
- `nutritional_risk_factors`: factores de riesgo relevantes para la evaluacion nutricional.
- `referral_escalation_flags`: situaciones que pueden requerir evaluacion medica.
- `potential_blind_spots`: areas que podrian pasar inadvertidas.
- `supporting_evidence`: permanece vacio porque la baseline no tiene retrieval.
- `relevant_existing_labs`: reproduce resultados ya existentes sin alterarlos.
- `limitations`: informacion insuficiente o elementos fuera del alcance.

Cada consideracion generada debe indicar que campos del paciente la motivaron.

La version congelada `nutrition-baseline-v4` limita el brief a un maximo de 5 gaps, 3
consideraciones nutricionales, 4 factores de riesgo, 2 referral flags y 3 blind spots. Todos los
racionales deben tener una sola oracion concisa.

Los limites son techos, no objetivos. Las listas opcionales pueden quedar vacias cuando no exista
un elemento relevante y respaldado por el intake; `suggested_questions` conserva entre 3 y 5
preguntas. Cada corrida registra por separado tokens de razonamiento y tokens de salida visible.

Ademas, evita expandir riesgos genericos por patron alimentario, prioriza solo informacion capaz de
cambiar la consulta, prohibe asumir adherencia o respuesta al tratamiento, diferencia lo no
informado de lo ausente, exige dos elementos especificos para consideraciones secundarias y obliga a
que cada referral flag describa solamente hechos observados.

## Limites de seguridad

El prompt establece que la baseline:

- No diagnostica ni propone probabilidades de enfermedad.
- No agrega diagnosticos que no aparezcan en `known_diagnoses`.
- No prescribe ni modifica medicacion o dosis de suplementos.
- No recomienda solicitar nuevos estudios de laboratorio.
- No inventa fuentes o citas.
- No interpreta informacion faltante como un hallazgo negativo.
- Puede indicar que el paciente podria necesitar evaluacion medica, sin afirmar un diagnostico.
- Debe abstenerse cuando la informacion sea insuficiente o este fuera del alcance nutricional.

## Dataset

El conjunto actual se encuentra en:

```text
data/cases/locked_test/nutrition_cases_021_040.json
```

Contiene 20 casos sinteticos (`case_021` a `case_040`). Cada caso incluye una ficha de paciente y
una rubrica con los conceptos esperados. Los datos fueron generados de forma sintetica y no estan
clinicamente validados.

Este archivo se considera un conjunto bloqueado: no deberia utilizarse para ajustar el prompt. Si
se crean casos para experimentar con el prompt, deben guardarse en un conjunto de desarrollo
separado.

## Evaluacion

La evaluacion actual mide de forma aproximada:

- Recall de gaps de informacion.
- Recall de temas de seguimiento.
- Recall y precision de consideraciones nutricionales.
- Recall de factores de riesgo nutricional.
- Recall y precision de flags de derivacion.
- Fidelidad de los laboratorios existentes.
- Sugerencias expresamente prohibidas.
- Cantidad de evidencia generada, que debe ser cero.

La comparacion actual es lexical: busca solapamiento entre conceptos esperados y generados. Es util
para obtener resultados reproducibles, pero no reemplaza una evaluacion semantica ni la revision de
profesionales de nutricion y medicina.

## Archivos principales

```text
baseline/schemas.py     Modelos de entrada, dataset y brief
baseline/prompt.py      Reglas del sistema y prompt versionado
baseline/client.py      Llamada estructurada a OpenAI
baseline/runner.py      CLI, ejecucion y persistencia de resultados
evaluation/metrics.py   Metricas deterministas iniciales
tests/test_baseline.py  Pruebas de contratos y restricciones
```

## Como ejecutarla

Primero hay que configurar `OPENAI_API_KEY` en un archivo `.env`.

Validar los casos sin realizar llamadas a la API:

```bash
uv run python -m baseline.runner --dry-run
```

Ejecutar un caso:

```bash
uv run python -m baseline.runner --case-id case_021
```

Ejecutar los 20 casos:

```bash
uv run python -m baseline.runner
```

Cada ejecucion real crea:

```text
evaluation/runs/<run_id>/
├── manifest.json
├── outputs.jsonl
├── failures.jsonl
└── metrics.json
```

El manifiesto registra el modelo, la version y hash del prompt, el dataset, su hash y los casos
evaluados. Esto permite comparar ejecuciones de manera reproducible.

## Que falta para el MVP completo

La baseline todavia no incluye:

- Nutrition Reasoning Agent y Evidence Agent como componentes separados.
- Fuentes clinicas aprobadas y versionadas.
- Extraccion, chunking, embeddings o retrieval.
- Validacion de aplicabilidad de la evidencia.
- Evidence Gate.
- Reglas deterministas completas de referral y escalamiento.
- API y frontend.
- Persistencia de pacientes y autenticacion.
- Evaluacion clinica de los casos y resultados.

Estos componentes deben compararse contra la baseline antes de incorporarse definitivamente.
