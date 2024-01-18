import numpy as np


def main():
    np.random.seed(42)
    unif_distr = np.random.uniform(0, 1, 1000)
    print("Mean:", np.mean(unif_distr))


if __name__ == "__main__":
    main()
