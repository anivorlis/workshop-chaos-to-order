from ex02.generate_data import generate_data
from ex02.fit import fit
from ex02.evaluate import evaluate
from ex02.visualize import visualize


def run_pipeline():
    print("--- Stage 1: Generate Data ---")
    generate_data()

    print("\n--- Stage 2: Fit ---")
    fit()

    print("\n--- Stage 3: Evaluate ---")
    evaluate()

    print("\n--- Stage 4: Visualize ---")
    visualize()


if __name__ == "__main__":
    run_pipeline()