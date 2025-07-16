from scipy.stats import norm

def percentile_to_z(p):
    z = norm.ppf(p)
    return z

if __name__ == "__main__":
    p = float(input("Enter percentile: "))
    z = percentile_to_z(p)
    print(f"Percentile: {p}")
    print(f"Z-score: {z:.4f}")