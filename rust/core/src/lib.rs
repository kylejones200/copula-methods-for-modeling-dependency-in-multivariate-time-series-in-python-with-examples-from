//! Rank-based Gaussian copula correlation matrix from pseudo-observations.

pub fn rank_correlation_matrix(data: &[f64], n_rows: usize, n_cols: usize) -> Vec<f64> {
    assert_eq!(data.len(), n_rows * n_cols);
    let mut corr = vec![0.0; n_cols * n_cols];
    if n_rows < 2 {
        return corr;
    }
    for i in 0..n_cols {
        for j in 0..n_cols {
            let mut xi = Vec::with_capacity(n_rows);
            let mut xj = Vec::with_capacity(n_rows);
            for r in 0..n_rows {
                xi.push(data[r * n_cols + i]);
                xj.push(data[r * n_cols + j]);
            }
            corr[i * n_cols + j] = pearson(&xi, &xj);
        }
    }
    corr
}

fn pearson(x: &[f64], y: &[f64]) -> f64 {
    let n = x.len() as f64;
    let mx = x.iter().sum::<f64>() / n;
    let my = y.iter().sum::<f64>() / n;
    let mut num = 0.0;
    let mut dx = 0.0;
    let mut dy = 0.0;
    for i in 0..x.len() {
        let a = x[i] - mx;
        let b = y[i] - my;
        num += a * b;
        dx += a * a;
        dy += b * b;
    }
    if dx <= 1e-18 || dy <= 1e-18 {
        0.0
    } else {
        num / (dx * dy).sqrt()
    }
}
