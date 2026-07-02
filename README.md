# Speech Recognition Evaluation Pipeline

A lightweight and reproducible pipeline for evaluating Automatic Speech Recognition (ASR) models. The project performs speech transcription, computes evaluation metrics, and saves both predictions and performance results in a structured format.

---

## Model

This project uses **OpenAI Whisper Small** for speech recognition.

| Attribute | Value |
|----------|-------|
| Model | `openai/whisper-small` |
| Framework | Hugging Face Transformers |
| Architecture | Encoder–Decoder Transformer |
| Task | Automatic Speech Recognition (ASR) |
| Parameters | ~244 Million |

---

## Dataset

The evaluation is performed on the **LibriSpeech ASR Demo** dataset provided by Hugging Face.

| Attribute | Value |
|----------|-------|
| Dataset | `hf-internal-testing/librispeech_asr_demo` |
| Configuration | `clean` |
| Split | `validation` |
| Source | Hugging Face Datasets |

---

## Project Structure

```text
project/
│
├── README.md
├── requirements.txt
├── run.py
├── src/
│   ├── __init__.py          # Marks src as a Python package
│   ├── load_model.py        # Loads the ASR model
│   ├── inference.py         # Generates transcriptions
│   ├── metrics.py           # Computes evaluation metrics
│   └── save_results.py      # Saves predictions and metrics
│
└── results/
    ├── predictions.csv
    └── metrics.json
```

---

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the evaluation pipeline:

```bash
python run.py
```

The pipeline will:
- Load the speech recognition model
- Perform inference on the evaluation dataset
- Compute evaluation metrics
- Save the results in the `results/` directory

---

## Output

After execution, the following files are generated inside the `results/` folder:

| File | Description |
|------|-------------|
| `predictions.csv` | Ground truth and predicted transcriptions |
| `metrics.json` | Evaluation metrics (e.g., WER, CER, and other reported metrics) |

---

## Notes

- Install all dependencies before running the project.
- The `results/` directory will be created automatically if it does not already exist.
- The modules inside `src/` can be modified independently to use different ASR models, datasets, or evaluation metrics.