import matplotlib.pyplot as plt

def plot_error_distribution(error_metrics):
    queries = [q for q, _, _, _ in error_metrics]
    precision_scores = [p for _, p, _, _ in error_metrics]
    recall_scores = [r for _, _, r, _ in error_metrics]
    f1_scores = [f for _, _, _, f in error_metrics]

    # Create histograms for each metric
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.hist(precision_scores, bins=10, range=(0, 1), alpha=0.7, color='blue', edgecolor='black')
    plt.title('Precision Distribution')
    plt.xlabel('Precision')
    plt.ylabel('Frequency')

    plt.subplot(1, 3, 2)
    plt.hist(recall_scores, bins=10, range=(0, 1), alpha=0.7, color='green', edgecolor='black')
    plt.title('Recall Distribution')
    plt.xlabel('Recall')
    plt.ylabel('Frequency')

    plt.subplot(1, 3, 3)
    plt.hist(f1_scores, bins=10, range=(0, 1), alpha=0.7, color='red', edgecolor='black')
    plt.title('F1 Score Distribution')
    plt.xlabel('F1 Score')
    plt.ylabel('Frequency')

    plt.tight_layout()
    plt.show()
