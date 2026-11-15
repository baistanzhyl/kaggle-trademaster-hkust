# TradeMaster Cup 2025 - 4th Place Solution

My solution for the TradeMaster Cup 2025 university Kaggle competition, where I placed **4th out of 57 teams**.

Most target values could be reconstructed from `feature_16` using future rows already present in the dataset. The final approach used this structure and handled the small unknown tail separately.

The [report](report.pdf) explains the discovery, experiments, and final results.

## Files

The Python scripts are in [notebooks/](notebooks/):

| File | Purpose |
| --- | --- |
| [generate_zero_submission.py](notebooks/generate_zero_submission.py) | Reconstruct known targets and use the sample submission's zero values for the unknown tail. Start here for the simplest version. |
| [generate_tail_variants.py](notebooks/generate_tail_variants.py) | Compare zero and historical-mean tail estimates. |
| [generate_tailvar_macro_specialist.py](notebooks/generate_tailvar_macro_specialist.py) | Estimate the tail with a ridge model. |
| [generate_tailvar_robust_anchor.py](notebooks/generate_tailvar_robust_anchor.py) | Blend the ridge model with historical means. |
| [solution.py](notebooks/solution.py) | Earlier XGBoost baseline. |
| [archival_neural_baseline.py](notebooks/archival_neural_baseline.py) | Earlier neural-network baseline. |

Supporting files:

- [trademaster_core/](trademaster_core/) — shared reconstruction and tail-model code.
- [notebooks/helper/](notebooks/helper/) — data checks and boundary backtests.
- [tests/](tests/) — regression tests using the competition data.
- [report_overleaf/](report_overleaf/) — LaTeX report source, proof scripts, saved outputs, and code listings.

## Run locally

The original environment used Python 3.13. Run these commands from the repository root:

```sh
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

Place the competition files in `data/raw/` (data is not included):

```text
data/raw/
├── train_v2.csv
├── test_v2.csv
└── sample_submission.csv
```

Generate a submission with zero values for the unknown tail:

```sh
python3 notebooks/generate_zero_submission.py
```

The CSV is saved in `submissions/`. Other models can be run directly using the scripts linked above.

To run the checks after adding the data:

```sh
python3 notebooks/helper/run_sanity_checks.py
python3 -m unittest discover -s tests -v
```
