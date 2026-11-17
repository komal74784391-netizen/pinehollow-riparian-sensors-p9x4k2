import numpy as np

def covariance_from_radius(radius_m, sill, range_m):
    """Exponential covariance model for the riparian microclimate field."""
    return sill * np.exp(-radius_m / range_m)

def greedy_placement(candidates, k, cov, shade_weights):
    """Greedy maximisation of a weighted log-determinant objective."""
    chosen = []
    while len(chosen) < k:
        best_idx, best_gain = None, -np.inf
        for idx in range(len(candidates)):
            if idx in chosen:
                continue
            trial = chosen + [idx]
            sub = cov[np.ix_(trial, trial)]
            sign, logdet = np.linalg.slogdet(sub + 1e-9 * np.eye(len(trial)))
            if sign <= 0:
                continue
            gain = logdet + shade_weights[idx]
            if gain > best_gain:
                best_idx, best_gain = idx, gain
        chosen.append(best_idx)
    return chosen
