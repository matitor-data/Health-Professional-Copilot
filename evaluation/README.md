# Evaluation Artifacts

This directory contains evaluation code, recorded trajectories, and reproducible reports. Paths
referenced by frozen manifests are intentionally preserved.

## Layout

```text
evaluation/
├── metrics.py                     Consultation-preparation metrics
├── compare.py                     Baseline and Nutrition Agent comparator
├── locked_compare.py              Final baseline and complete-module comparator
├── locked_evaluation_plan_v1.json Pre-execution locked configuration
├── locked_execution_manifest_v1.json Recorded run IDs and artifact hashes
├── runs/                          Baseline runs
├── agent_runs/                    Nutrition Agent trajectories
├── evidence_agent_runs/           End-to-end Nutrition and Evidence Agent trajectories
├── evidence_demo_runs/            Recorded video demonstration
├── evidence_fixed_runs*/          Fixed-input Evidence Agent stability runs
├── locked_runs/                   One-time final baseline and solution runs
└── reports/                       Human- and machine-readable comparisons
```

## Artifact policy

- `runs/`, `agent_runs/`, and agent-specific run directories contain raw execution artifacts.
- `reports/` contains derived summaries and comparisons.
- The locked plan was written before execution; the locked manifest records what actually ran.
- Frozen reference paths must not be renamed because tests and manifests use them for reproducibility.
- Do not rerun the locked benchmark for tuning. A future experiment requires a new versioned plan,
  dataset, and report.

The concise final result is available at [`../execution_report.md`](../execution_report.md).
