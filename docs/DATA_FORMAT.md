# Data format

The Python tools accept CSV recordings with a timestamp column and optional sensor columns.

## Recording columns

- `timestamp_s`: seconds from the beginning of the recording (required).
- `red`, `ir`: raw MAX30102 optical channels (optional).
- `spo2_pct`: peripheral SpO2 estimate from a separately validated upstream estimator (optional).
- `heart_rate_bpm`: heart-rate estimate (optional).
- `ax_g`, `ay_g`, `az_g`: accelerometer axes in g (optional).
- `bio_raw`: raw ADC/biopotential sample. This is not labelled EEG.
- `reference_event`: optional reference label for evaluation; 1 means event-labelled, 0 means not event-labelled.

## Evaluation CSV

Evaluation additionally accepts:
- `y_true`: reference binary labels.
- `y_pred`: binary predictions from an experimental model.

Do not mix synthetic examples with clinical recordings. Keep provenance, annotation definitions, sampling rates, units, device versions, and data-use permissions alongside each real dataset. This scaffold does not provide a clinical annotation standard.
