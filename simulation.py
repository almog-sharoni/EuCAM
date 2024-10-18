from cam_memory import CAMMemory
from query_masker import QueryMasker
from cam_searcher import CAMSearcher
import matplotlib.pyplot as plt

def create_cam_memory():
    cam_memory = CAMMemory()
    # Add all possible 8-bit patterns to the memory
    for i in range(256):
        binary_pattern = f"{i:08b}"
        cam_memory.add_pattern(binary_pattern)
    return cam_memory


def run_exhaustive_simulation(mask_bits=2):
    cam_memory = create_cam_memory()
    masker = QueryMasker(mask_bits=mask_bits)
    searcher = CAMSearcher(cam_memory, masker)
    results = {}
    error_metrics = []

    # Run the search for every possible 8-bit query
    for i in range(256):
        query = f"{i:08b}"
        cam_matches = searcher.search(query)

        # For now, we'll assume the Euclidean distance matches the query exactly.
        # In a real setup, replace this with the actual Euclidean distance-based search logic.
        euclidean_matches = [query]  # Placeholder for actual Euclidean-based results

        precision, recall, f1 = calculate_error_metrics(query, cam_matches, euclidean_matches)
        error_metrics.append((query, precision, recall, f1))

    return results, error_metrics


from sklearn.metrics import precision_score, recall_score, f1_score
import numpy as np


def calculate_error_metrics(query, cam_matches, euclidean_matches, total_patterns=256):
    """
    Calculate precision, recall, and F1-score between CAM-based matches and Euclidean distance-based matches.
    """
    # Create binary vectors representing matches (1 if a pattern matches, 0 otherwise)
    cam_match_vector = np.zeros(total_patterns, dtype=int)
    euclidean_match_vector = np.zeros(total_patterns, dtype=int)

    # Mark matched patterns as 1
    for match in cam_matches:
        cam_match_vector[int(match, 2)] = 1

    for match in euclidean_matches:
        euclidean_match_vector[int(match, 2)] = 1

    # Calculate precision, recall, and F1-score
    precision = precision_score(euclidean_match_vector, cam_match_vector, zero_division=0)
    recall = recall_score(euclidean_match_vector, cam_match_vector, zero_division=0)
    f1 = f1_score(euclidean_match_vector, cam_match_vector, zero_division=0)

    # Print or log the query and its metrics for debugging
    print(f"Query: {query}, Precision: {precision}, Recall: {recall}, F1: {f1}")

    return precision, recall, f1


if __name__ == "__main__":
    mask_bits = 2
    results, error_metrics = run_exhaustive_simulation(mask_bits=mask_bits)

    # Display a few results
    print("Exhaustive Simulation Results (first 10 queries):")
    for query, matches in list(results.items())[:10]:
        print(f"Query: {query}, Matches: {matches}")

    # Analyze and plot the error distribution
    from analysis import plot_error_distribution

    # plot_error_distribution(error_metrics)

