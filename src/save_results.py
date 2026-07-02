import os
import json
import pandas as pd


def create_results_folder():

    if not os.path.exists("results"):
        os.makedirs("results")


def save_predictions(ids, gt, pred, latency):

    table = pd.DataFrame({
        "audio_id": ids,
        "ground_truth": gt,
        "prediction": pred,
        "latency": latency
    })

    table.to_csv(
        "results/predictions.csv",
        index=False
    )


def save_metrics(metrics):

    with open(
        "results/metrics.json",
        "w"
    ) as file:

        json.dump(
            metrics,
            file,
            indent=4
        )

