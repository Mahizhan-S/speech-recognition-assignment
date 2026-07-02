from transformers import WhisperProcessor
from transformers import WhisperForConditionalGeneration
from datasets import load_dataset


def load_everything():

    processor = WhisperProcessor.from_pretrained(
        "openai/whisper-small"
    )

    model = WhisperForConditionalGeneration.from_pretrained(
        "openai/whisper-small"
    )

    dataset = load_dataset(
        "hf-internal-testing/librispeech_asr_demo",
        "clean",
        split="validation"
    )

    return processor, model, dataset
