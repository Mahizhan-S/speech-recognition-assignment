import jiwer


def calculate_metrics(ground_truths, predictions, latencies):

    metrics = {}

    metrics["num_processed_samples"] = len(ground_truths)

    metrics["word_error_rate_wer"] = round(
        jiwer.wer(ground_truths, predictions),
        4
    )

    metrics["character_error_rate_cer"] = round(
        jiwer.cer(ground_truths, predictions),
        4
    )

    metrics["average_latency_seconds"] = round(
        sum(latencies) / len(latencies),
        4
    )

    return metrics
