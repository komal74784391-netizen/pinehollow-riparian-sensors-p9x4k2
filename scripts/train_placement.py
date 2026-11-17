import argparse, yaml, numpy as np
from src.sensor_placement import covariance_from_radius, greedy_placement

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', required=True)
    args = parser.parse_args()
    cfg = yaml.safe_load(open(args.config))
    n = cfg['n_candidates']
    cov = covariance_from_radius(np.arange(n)[:, None] + 0.0, cfg['sill'], cfg['range_m'])
    weights = np.array(cfg['shade_weights'][:n])
    chosen = greedy_placement(list(range(n)), cfg['budget'], cov, weights)
    print('selected sensors:', chosen)

if __name__ == '__main__':
    main()
