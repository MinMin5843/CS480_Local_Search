from experiments import (
    ensure_directories,
    run_eggholder,
    eggholder_results_to_CSV,
    plot_eggholder_results,
    run_n_queens,
    nqueens_results_to_CSV,
    plot_nqueens_success
)

if __name__ == "__main__":
    ensure_directories()
    
    print("Running Eggholder experiment...")
    eggholder_results = run_eggholder()
    eggholder_results_to_CSV(eggholder_results)
    plot_eggholder_results(eggholder_results)

    print("\nRunning N-Queens experiments...")
    results_8 = run_n_queens(8)
    results_16 = run_n_queens(16)
    results_32 = run_n_queens(32)

    nqueens_results_to_CSV(8, results_8)
    nqueens_results_to_CSV(16, results_16)
    nqueens_results_to_CSV(32, results_32)

    success_8 = sum(1 for _, _, sol in results_8 if sol)
    success_16 = sum(1 for _, _, sol in results_16 if sol)
    success_32 = sum(1 for _, _, sol in results_32 if sol)

    plot_nqueens_success(success_8, success_16, success_32)

    print("\nAll experiments completed.")
    print("CSV files are located in the 'results/' folder.")
    print("Plots are located in the 'plots/' folder.")
