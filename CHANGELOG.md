# Changelog

Este archivo registra los cambios relevantes del proyecto. El proyecto se encuentra en desarrollo
inicial y todavia no tiene una version publicada.

## [Unreleased]

### Estado actual - 2026-08-28

#### Implementado

- Definicion del producto como Nutrition Module de Health Professional Copilot.
- Especificacion del MVP disponible en `docs/Health_Professional_Copilot_Nutrition_Module_MVP.pdf`.
- Baseline de una sola llamada al LLM y salida estructurada.
- Prompt `nutrition-baseline-v1` con limites de alcance nutricional.
- Esquemas Pydantic estrictos para intake, dataset, rubrica y brief.
- Cliente basado en `OpenAI.responses.parse` para obtener una respuesta estructurada.
- Runner de linea de comandos con seleccion de casos y modo `--dry-run`.
- Registro por ejecucion de manifiesto, outputs, errores y metricas.
- Evaluacion lexical determinista inicial.
- Dataset bloqueado con 20 casos sinteticos, desde `case_021` hasta `case_040`.
- Cinco pruebas automatizadas para dataset, prompt, aislamiento de la rubrica y metricas basicas.
- Configuracion inicial del proyecto con `uv`, variables de entorno y documentacion de uso.

#### Verificado

- Los 20 casos cargan y validan correctamente contra sus esquemas.
- El modo `--dry-run` funciona sin realizar llamadas externas.
- Las cinco pruebas automatizadas pasan.
- La version instalada del SDK de OpenAI acepta structured outputs mediante
  `responses.parse`.

#### Limites actuales

- No se realizo todavia una ejecucion completa contra la API de OpenAI.
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
