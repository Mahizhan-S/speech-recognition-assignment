import time
import torch


def run_inference(processor, model, dataset):

    audio_ids = []
    ground_truths = []
    predictions = []
    latencies = []

    for i in range(30):

        sample = dataset[i]

        audio = sample["audio"]["array"]
        audio_id = sample["id"]
        ground_truth = sample["text"]

        start = time.time()

        inputs = processor(
            audio,
            sampling_rate=16000,
            return_tensors="pt"
        ).input_features

        with torch.no_grad():
            output = model.generate(inputs)

        prediction = processor.batch_decode(
            output,
            skip_special_tokens=True
        )[0]

        end = time.time()

        prediction = prediction.upper()

        audio_ids.append(audio_id)
        ground_truths.append(ground_truth)
        predictions.append(prediction)
        latencies.append(end - start)

        print("Completed sample", i + 1)

    return audio_ids, ground_truths, predictions, latencies
