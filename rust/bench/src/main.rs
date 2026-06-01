use copula_methods_for_modeling_dependency_in_multivariate_time_series_in_python_with_examples_from_core::rank_correlation_matrix;

fn main() {
    let n_rows = 200usize;
    let n_cols = 5usize;
    let data: Vec<f64> = (0..n_rows * n_cols)
        .map(|i| ((i % 17) as f64 * 0.1).sin())
        .collect();
    for _ in 0..200 {
        let _ = rank_correlation_matrix(&data, n_rows, n_cols);
    }
}
