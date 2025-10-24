
import random, math, heapq, statistics
from typing import List, Tuple
import matplotlib.pyplot as plt

DATAFILE = "datapoints.txt"  # given file, do not modify
K = 10
TRAIN_PER_CLASS = 50
TEST_PER_CLASS = 25

Point = Tuple[float, float, int]  # (width, height, label 0/1)

def load_points(path: str = DATAFILE) -> List[Point]:
    """Load datapoints from file. Ignores empty/malformed lines gracefully."""
    pts: List[Point] = []
    with open(path, "r", encoding="utf-8") as f:
        # Skip header if present
        first = f.readline()
        header_like = ("width" in first.lower() and "height" in first.lower() and "label" in first.lower())
        if not header_like:
            # first line was actually data
            parts = first.strip().split(",")
            if len(parts) == 3:
                try:
                    w, h, l = float(parts[0]), float(parts[1]), int(parts[2])
                    pts.append((w, h, l))
                except:
                    pass
        for line in f:
            parts = line.strip().split(",")
            if len(parts) != 3:
                continue
            try:
                w, h, l = float(parts[0]), float(parts[1]), int(parts[2])
                if l not in (0, 1):
                    continue
                pts.append((w, h, l))
            except:
                continue
    return pts

def euclidean(a: Tuple[float, float], b: Tuple[float, float]) -> float:
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return (dx*dx + dy*dy) ** 0.5

def k_nearest(points: List[Point], query: Tuple[float, float], k: int = K):
    dists = ((euclidean((w, h), query), lbl) for (w, h, lbl) in points)
    # nsmallest returns in ascending order by distance
    return heapq.nsmallest(k, dists, key=lambda t: t[0])

def vote(neighbors):
    k = len(neighbors)
    ones = sum(lbl for _, lbl in neighbors)
    if ones > k/2:
        return 1
    if ones < k/2:
        return 0
    # tie -> nearest neighbor's label (neighbors already sorted by distance)
    return neighbors[0][1]

def predict(train: List[Point], query: Tuple[float, float]) -> int:
    nns = k_nearest(train, query, K)
    return vote(nns)

def stratified_split(points: List[Point], train_per_class: int, test_per_class: int, seed: int):
    rng = random.Random(seed)
    c0 = [p for p in points if p[2] == 0]
    c1 = [p for p in points if p[2] == 1]
    if len(c0) < train_per_class + test_per_class or len(c1) < train_per_class + test_per_class:
        raise ValueError(f"Not enough data per class. Need at least {train_per_class + test_per_class} of each.")
    train0 = rng.sample(c0, train_per_class)
    remain0 = [p for p in c0 if p not in train0]
    test0 = rng.sample(remain0, test_per_class)

    train1 = rng.sample(c1, train_per_class)
    remain1 = [p for p in c1 if p not in train1]
    test1 = rng.sample(remain1, test_per_class)

    train = train0 + train1
    test = test0 + test1
    rng.shuffle(train)
    rng.shuffle(test)
    return train, test

def confusion_on_split(train: List[Point], test: List[Point]):
    # Define positive=1 (Pikachu), negative=0 (Pichu)
    TP = TN = FP = FN = 0
    for (w, h, true_lbl) in test:
        pred = predict(train, (w, h))
        if true_lbl == 1 and pred == 1:
            TP += 1
        elif true_lbl == 0 and pred == 0:
            TN += 1
        elif true_lbl == 0 and pred == 1:
            FP += 1
        elif true_lbl == 1 and pred == 0:
            FN += 1
    total = len(test)
    acc = (TP + TN) / total if total else 0.0
    return acc, (TP, TN, FP, FN)

def run_experiments(points: List[Point], runs: int = 10, seed_base: int = 1337):
    accuracies = []
    confusions = []
    for i in range(runs):
        seed = seed_base + i
        train, test = stratified_split(points, TRAIN_PER_CLASS, TEST_PER_CLASS, seed)
        acc, cm = confusion_on_split(train, test)
        accuracies.append(acc)
        confusions.append(cm)
    return accuracies, confusions

def main(save_plot_path: str = "bonus_accuracy.png"):
    pts = load_points(DATAFILE)
    accuracies, confusions = run_experiments(pts, runs=10, seed_base=1337)

    # Print results
    for i, (acc, (TP, TN, FP, FN)) in enumerate(zip(accuracies, confusions), start=1):
        print(f"Run {i:2d}: accuracy={acc:.4f} | TP={TP:2d} TN={TN:2d} FP={FP:2d} FN={FN:2d}")
    mean_acc = statistics.mean(accuracies) if accuracies else 0.0
    print(f"\nMean accuracy over 10 runs: {mean_acc:.4f}")

    # Plot accuracies
    plt.figure()
    plt.plot(range(1, len(accuracies)+1), accuracies, marker="o")
    plt.xlabel("Run")
    plt.ylabel("Accuracy")
    plt.title("KNN (K=10) Accuracy over 10 Stratified Splits")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(save_plot_path, dpi=150)
    print(f"Saved accuracy chart to: {save_plot_path}")

if __name__ == "__main__":
    main()
