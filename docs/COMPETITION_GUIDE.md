# Competition guide

## Project summary

This project is an early-stage wearable-sensing research prototype. Its software demonstrates a modular pipeline for acquiring selected sensor channels, checking signal quality, extracting transparent features, generating exploratory candidate scores, and evaluating predictions against supplied reference labels.

## Research question

Can synchronized wearable signals provide useful information for identifying periods that merit further sleep-study review?

This repository does not establish that the signals can diagnose obstructive sleep apnea. The current candidate scorer is a software-pipeline demonstration, not a trained or validated medical model.

## System overview

1. Sensor acquisition firmware reads raw optical samples from a MAX30102, acceleration from a LIS3DH, and an uncalibrated analog input.
2. CSV ingestion validates timestamps and loads recordings.
3. Feature extraction calculates descriptive summaries over a supplied window.
4. A transparent baseline produces an exploratory score when sufficient input quality is present.
5. Evaluation compares binary predictions with reference labels and reports confusion-matrix metrics.

## What is novel or investigable

The research contribution should be framed as the evaluation of a low-cost multimodal sensing pipeline and its limitations, not as a finished diagnostic or treatment device. The team can investigate whether motion and peripheral pulse-oximetry features add information beyond either channel alone, provided the dataset has suitable synchronized channels and expert annotations.

## Current evidence

- Firmware and analysis scaffolding are present.
- Python unit tests are included.
- Synthetic CSVs demonstrate file formats and commands.
- No clinical dataset has been processed in this repository.
- No trained model or held-out clinical evaluation is included.
- No measured sensitivity, specificity, latency, or intervention benefit is claimed.

## Recommended experiment plan

1. Define the target label and event timing rule before analysis.
2. Select an appropriately licensed, de-identified dataset with relevant channels and documented expert annotations.
3. Split data by participant, not by randomly selected windows, to reduce leakage.
4. Keep a held-out test set untouched until model and thresholds are finalized.
5. Compare single-channel baselines with multimodal models.
6. Report sensitivity, specificity, precision, F1, AUROC where appropriate, false alarms per hour, confidence intervals, and missing-signal rates.
7. Include subgroup and signal-quality analyses when sample size permits.
8. Document all preprocessing, sampling rates, window sizes, thresholds, exclusions, and software versions.
9. Do not deploy haptic/audio feedback to participants as part of this software-only evaluation.

## Suggested judging demonstration

Use only the included synthetic examples. Show the serial data schema, inspect a sample CSV, explain how feature extraction works, and run the evaluation command on the synthetic labelled example. Explicitly state that this demonstrates the software workflow, not clinical performance.

## Short presentation description

"A modular research prototype exploring whether low-cost wearable signals can be synchronized and analyzed as candidate indicators for sleep-study research. The current implementation focuses on sensor acquisition, transparent signal features, reproducible evaluation, and explicit safety boundaries. Clinical validity remains an open research question."
