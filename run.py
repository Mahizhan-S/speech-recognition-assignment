from src.load_model import load_everything
from src.inference import run_inference
from src.metrics import calculate_metrics
from src.save_results import create_results_folder
from src.save_results import save_predictions
from src.save_results import save_metrics

def main():

    create_results_folder()

    processor, model, dataset = load_everything()

    ids, gt, pred, latency = run_inference(
        processor,
        model,
        dataset
    )

    save_predictions(ids, gt, pred, latency)

    metrics = calculate_metrics(gt, pred, latency)

    save_metrics(metrics)

    print("Finished Successfully!")

if __name__ == "__main__":
    main()