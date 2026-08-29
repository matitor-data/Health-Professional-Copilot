# Changelog

Este archivo registra los cambios relevantes del proyecto. El proyecto se encuentra en desarrollo
inicial y todavia no tiene una version publicada.

## [Unreleased]

### Estado actual - 2026-08-29

#### Implementado

- Prompts v1, v2 y v3 almacenados como archivos independientes y seleccionables mediante
  `--prompt-version`.
- Comparador automatico de runs con salida JSON y Markdown para metricas, tokens, tamano visible,
  latencia, coste estimado y cantidad de elementos por seccion.
- Prompt `nutrition-baseline-v3` con guardrails contra riesgos genericos, hechos asumidos y referral
  flags que completen informacion ausente.
- Requisito de dos elementos especificos del intake para generar una consideracion nutricional
  secundaria.
- Distincion explicita entre informacion no reportada y evidencia de ausencia o insuficiencia.
- Prompt `nutrition-baseline-v2` con presupuestos explicitos de salida para reducir tokens,
  latencia y carga de revision profesional.
- Restricciones Pydantic para un maximo de 5 gaps, entre 3 y 5 preguntas, 3 consideraciones
  nutricionales, 4 factores de riesgo, 2 referral flags y 3 blind spots.
- Racionales definidos como una unica oracion concisa en el prompt y en la descripcion del esquema.
- Definicion del producto como Nutrition Module de Health Professional Copilot.
- Especificacion del MVP disponible en `docs/Health_Professional_Copilot_Nutrition_Module_MVP.pdf`.
- Baseline de una sola llamada al LLM y salida estructurada.
- Prompt inicial `nutrition-baseline-v1` conservado en el manifiesto de la ejecucion de referencia.
- Esquemas Pydantic estrictos para intake, dataset, rubrica y brief.
- Cliente basado en `OpenAI.responses.parse` para obtener una respuesta estructurada.
- Runner de linea de comandos con seleccion de casos y modo `--dry-run`.
- Registro por ejecucion de manifiesto, outputs, errores y metricas.
- Evaluacion lexical determinista inicial.
- Dataset bloqueado con 20 casos sinteticos, desde `case_021` hasta `case_040`.
- Cinco pruebas automatizadas para dataset, prompt, aislamiento de la rubrica y metricas basicas.
- Configuracion inicial del proyecto con `uv`, variables de entorno y documentacion de uso.

#### Verificado

- Ejecucion real de `case_021` con `nutrition-baseline-v3`: un caso exitoso y cero fallos.
- Comparacion automatica v1 vs v3 generada en `evaluation/reports/v1_vs_v3_case021/`.
- V3 redujo el brief visible de 10.658 a 6.851 caracteres y la latencia de 44,111 a 36,044
  segundos.
- V3 aumento los output tokens totales de 3.959 a 4.849 y el coste estimado de USD 0,00822 a
  USD 0,01007; la optimizacion de tokens no se considera lograda todavia.
- Los 20 casos cargan y validan correctamente contra sus esquemas.
- El modo `--dry-run` funciona sin realizar llamadas externas.
- Las ocho pruebas automatizadas pasan.
- La version instalada del SDK de OpenAI acepta structured outputs mediante
  `responses.parse`.

#### Limites actuales

- Solo se ejecutaron comparaciones reales sobre `case_021`; falta validar un conjunto representativo
  y luego los 20 casos.
- Los casos sinteticos y sus rubricas no cuentan con validacion clinica.
- Las metricas utilizan coincidencia lexical aproximada y no evaluacion semantica.
- La baseline no recupera evidencia; `supporting_evidence` debe permanecer vacio.
- No existen todavia API funcional, interfaz de usuario, autenticacion ni almacenamiento de
  pacientes.
- No estan implementados Nutrition Reasoning Agent, Evidence Agent, Evidence Gate ni la base de
  conocimiento.
- Las reglas deterministas completas de referral y escalamiento siguen pendientes.

#### Proximos pasos propuestos

- Ejecutar la baseline sobre los 20 casos y guardar el primer reporte de referencia.
- Revisar casos y rubricas con profesionales de nutricion y medicina.
- Separar un dataset de desarrollo del conjunto bloqueado.
- Incorporar evaluacion semantica y adjudicacion profesional.
- Implementar el Nutrition Reasoning Agent y compararlo contra la baseline.
- Construir el registro de fuentes aprobadas y el Evidence Agent.
- Incorporar reglas deterministas de scope, referral y escalamiento.
- Implementar Evidence Gate antes de mostrar afirmaciones respaldadas por evidencia.

## [0.1.0] - Pendiente

La version `0.1.0` declarada en `pyproject.toml` representa el identificador de desarrollo del
paquete. Todavia no corresponde a una release publicada.
