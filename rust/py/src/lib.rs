use copula_methods_for_modeling_dependency_in_multivariate_time_series_in_python_with_examples_from_core::rank_correlation_matrix;
use numpy::{PyArray1, PyReadonlyArray1, IntoPyArray};
use pyo3::prelude::*;

#[pyfunction]
fn rank_correlation_matrix_py<'py>(
    py: Python<'py>,
    data: PyReadonlyArray1<f64>,
    n_rows: usize,
    n_cols: usize,
) -> PyResult<Bound<'py, PyArray1<f64>>> {
    Ok(rank_correlation_matrix(data.as_slice()?, n_rows, n_cols).into_pyarray(py))
}

#[pyfunction]
#[pyo3(signature = (data, n_rows, n_cols, iterations=200))]
fn bench_kernel_py(
    data: PyReadonlyArray1<f64>,
    n_rows: usize,
    n_cols: usize,
    iterations: usize,
) -> PyResult<f64> {
    let d = data.as_slice()?.to_vec();
    let start = std::time::Instant::now();
    for _ in 0..iterations {
        let _ = rank_correlation_matrix(&d, n_rows, n_cols);
    }
    Ok(start.elapsed().as_secs_f64())
}

#[pymodule]
fn copula_methods_for_modeling_dependency_in_multivariate_time_series_in_python_with_examples_from_rs(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(rank_correlation_matrix_py, m)?)?;
    m.add_function(wrap_pyfunction!(bench_kernel_py, m)?)?;
    Ok(())
}
