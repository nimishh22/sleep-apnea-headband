# Validation protocol

This is a proposed research protocol template, not evidence that validation has been completed.

## Before analysis

- Record dataset name, version, access date, license, and permitted use.
- Confirm whether channels are synchronized and document sampling rates and units.
- Define event labels and scoring windows before model development.
- Specify inclusion/exclusion criteria without inspecting test-set outcomes.
- Record software commit SHA and dependency versions.

## Data partitioning

- Split by participant/recording identity to prevent windows from the same participant appearing in both train and test sets.
- Keep the test set locked until preprocessing and model settings are fixed.
- Use a validation set or nested cross-validation for model selection.
- Do not tune thresholds on the final test set.

## Required reporting

Report at minimum:
- Participant and recording counts.
- Number of positive and negative labelled events.
- Sensitivity/recall, specificity, precision, F1 and confusion matrix.
- False positives per hour and event-level detection delay where definitions support them.
- Confidence intervals and the method used to calculate them.
- Missing-data and signal-quality rejection rates.
- Performance by sensor availability and relevant subgroups where adequately powered.

## Avoiding misleading results

- Do not treat adjacent windows as independent participants.
- Do not report accuracy alone for imbalanced data.
- Do not claim performance from synthetic data.
- Do not compare against physician annotation unless the source labels and annotation protocol genuinely support that statement.
- Do not claim real-time latency from offline batch processing.
- Do not claim closed-loop benefit from event detection metrics.

## Reproducibility checklist

- [ ] Dataset provenance and license recorded.
- [ ] Annotation definition documented.
- [ ] Participant-level split fixed.
- [ ] Preprocessing parameters recorded.
- [ ] Model and thresholds versioned.
- [ ] Held-out results generated once after lock.
- [ ] Confidence intervals and failure cases reported.
- [ ] Limitations and missing channels disclosed.
