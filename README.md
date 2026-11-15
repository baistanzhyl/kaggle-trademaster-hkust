# TradeMaster Cup 2025 - 4th Place Solution

My solution for the TradeMaster Cup 2025 university Kaggle competition, where I placed **4th out of 57 teams**.

Most target values could be reconstructed from `feature_16` using future rows already present in the dataset. The final approach used this structure and handled the small unknown tail separately.

The [report](report.pdf) explains the discovery, experiments, and final results.

## Files

The Python scripts are in [scripts/](scripts/):

| File | Purpose |
| --- | --- |
| [submit_zero.py](scripts/submit_zero.py) | Reconstruct known targets and use the sample submission's zero values for the unknown tail. Start here for the simplest version. |
| [submit_variants.py](scripts/submit_variants.py) | Compare zero and historical-mean tail estimates. |
| [submit_ridge.py](scripts/submit_ridge.py) | Estimate the tail with a ridge model. |
| [submit_blend.py](scripts/submit_blend.py) | Blend the ridge model with historical means. |
| [baseline_xgboost.py](scripts/baseline_xgboost.py) | Earlier XGBoost baseline. |
| [baseline_neural.py](scripts/baseline_neural.py) | Earlier neural-network baseline. |

Supporting files:

- [core/](core/) — shared reconstruction and tail-model code.
- [scripts/checks/](scripts/checks/) — data checks and boundary backtests.
- [tests/](tests/) — regression tests using the competition data.
- [report/](report/) — LaTeX report source, proof scripts, saved outputs, and code listings.

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
python3 scripts/submit_zero.py
```

The CSV is saved in `submissions/`. Other models can be run directly using the scripts linked above.

To run the checks after adding the data:

```sh
python3 scripts/checks/check_data.py
python3 -m unittest discover -s tests -v
```
