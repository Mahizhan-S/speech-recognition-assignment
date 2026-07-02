# Research Summary: Whisper

## Why I Chose Whisper

I chose Whisper instead of Wav2Vec2 and HuBERT because it gives good speech recognition results without needing extra training for many tasks. It was trained on about 680,000 hours of speech data from many languages, so it works well with different accents, languages, and noisy audio. It can also perform speech recognition and speech translation using the same model.

## What Problem Does Whisper Solve?

Whisper solves the Automatic Speech Recognition (ASR) problem by converting speech into text. It is designed to recognize speech from different speakers, languages, and recording conditions.

## How Does the Architecture Work?

Whisper uses a Transformer encoder-decoder architecture. First, the input audio is converted into a log-Mel spectrogram. The encoder learns useful features from the audio, and the decoder converts those features into text one token at a time.

## Why Is It Better Than Previous Approaches?

- It was trained on a large amount of speech data.
- It supports many languages.
- It works well even when there is background noise.
- It gives good results without much additional training.
- It can perform both speech recognition and speech translation.

## What Datasets Were Used?

Whisper was trained on about 680,000 hours of supervised speech data collected from the internet. The data includes English speech recognition, multilingual speech recognition, and speech translation in 96 languages.

## What Are Its Limitations?

- Large models need more memory and computing power.
- It is slower than smaller speech recognition models.
- Accuracy may reduce if the audio quality is very poor.
- The internet data used for training may contain some bias.

## Comparison with Wav2Vec2 and HuBERT

| Feature | Wav2Vec2 | HuBERT | Whisper |
|---------|----------|---------|----------|
| Fine-tuning Required | Yes | Yes | No (for many tasks) |
| Multilingual Support | Limited | Limited | Excellent |
| Noise Handling | Good | Good | Excellent |
| Speech Translation | No | No | Yes |

Overall, I selected Whisper because it is easy to use, gives good accuracy, supports many languages, and performs well even without additional fine-tuning.

---

# Project Implementation

## Model Used

- openai/whisper-small

## Dataset Used

- LibriSpeech ASR (Validation - Clean)

## Evaluation Metrics

- Word Error Rate (WER)
- Character Error Rate (CER)
- Average Inference Latency
- Number of Processed Samples

---

# Part 3 – Project Structure

```text
project/
│
├── README.md
├── requirements.txt
├── run.py
├── src/
└── results/
```

---

# Part 4 – How to Run

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python run.py
```

---

# Output Files

After running the project, the following files are generated inside the `results/` folder.

- predictions.csv
- metrics.json

---

# References

- Whisper: Robust Speech Recognition via Large-Scale Weak Supervision
- Hugging Face Transformers
- LibriSpeech ASR Dataset
