import os 
import csv 
import matplotlib.pyplot as plt

from eggholder import hill_climb_eggholder
from n_queens import hill_climb_nqueens

def ensure_directories():
    """
    Makes sure the necessary directories exist otherwise creates them to put the 
    results and plots in.

    Yields: 
        New results/ and plots/ directories if they do not already exist.
    """
    os.makedirs("results", exist_ok=True)
    os.makedirs("plots", exist_ok=True)

def run_eggholder():
    """
    Runs 100 instances of hill-climbing runs on the Eggholder function.

    Yields:
        A list of 100 minima found.
    """
    results = []
    for _ in range(100):
        _, _, best_val = hill_climb_eggholder()
        results.append(best_val)
    return results

def eggholder_results_to_CSV(results):
    """
    Saves Eggholder results into a CSV file under a results/ directory.
    
    Args:
        results: the list of minima from the 100 runs.

    Yields:
        A CSV file containing the results from the 100 runs saved in a results/ 
        directory.
    """
    csv_path = "results/eggholder_results.csv"
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Run", "Minimum Value"])
        for i, val in enumerate(results):
            writer.writerow([i + 1, val])

    print(f"[Eggholder] Results saved to: {csv_path}")

def plot_eggholder_results(results):
    """
    Creates a histogram of Eggholder minima and saves it to a plots/ directory.
    
    Args:
        results: the list of minima from the 100 runs.

    Yields:
        A histogram under a plots/ directory.
    """
    plt.figure(figsize=(8, 5))
    plt.hist(results, bins=20, color="skyblue", edgecolor="black")
    plt.title("Distribution of Eggholder Minima (100 Runs)")
    plt.xlabel("Minimum Value")
    plt.ylabel("Frequency")
    plt.grid(True, linestyle="--", alpha=0.5)

    plot_path = "plots/eggholder_hist.png"
    plt.savefig(plot_path)
    plt.close()

    print(f"[Eggholder] Plot saved to: {plot_path}")

def run_n_queens(N):
    """
    Runs 100 instances of hill-climbing runs for the N-Queens function.

    Args:
        N: the board size.

    Yields:
        A list of tuples containing the run number, attacks, and whether a solution has
        been found.
    """
    results = []
    for run in range(100):
        final_board, attacks, is_solution = hill_climb_nqueens(N)
        results.append((run + 1, attacks, is_solution))
    return results

def nqueens_results_to_CSV(N, results):
    """
    Saves the N-Queens results into a CSV files under the results/ directory.
    
    Args: 
        N: the board size.
        results: the list of tuples containing the run number, attacks, and whether a 
        solution has been found.
    
    Yields:
        A CSV file containing the results from the 100 runs saved in a results/ 
        directory.
    """
    csv_path = f"results/nqueens_results_N{N}.csv"
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Run", "Attacks", "Is Solution"])
        for row in results:
            writer.writerow(row)

    print(f"[N-Queens N={N}] Results saved to: {csv_path}")

def plot_nqueens_success(success_8, success_16, success_32):
    """
    Creates a bar chart of the success rate for the different board sizes (8, 16, 32) 
        and saves it to a plots/ directory.
    
    Args:
        success_8: the success rate for board size 8.
        success_16: the success rate for board size 16.
        success_32: the success rate for board size 32.

    Yields:
        A bar chart under a plots/ directory.
    """
    plt.figure(figsize=(8, 5))
    Ns = [8, 16, 32]
    successes = [success_8, success_16, success_32]

    plt.bar(Ns, successes, color=["green", "orange", "red"])
    plt.title("N-Queens Hill-Climbing Success Rates (100 Runs Each)")
    plt.xlabel("N")
    plt.ylabel("Number of Solutions Found")
    plt.ylim(0, 100)
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plot_path = "plots/nqueens_success.png"
    plt.savefig(plot_path)
    plt.close()

    print(f"[N-Queens] Success rate plot saved to: {plot_path}")
