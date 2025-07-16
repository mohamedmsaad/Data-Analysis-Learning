from scipy.stats import norm

def z_to_percentile(z):
    percentile = norm.cdf(z)
    return percentile

if __name__ == "__main__":
    z = float(input("Enter z-score : "))
    p = z_to_percentile(z)
    print(f"Z-score: {z}")
    print(f"Percentile: {p:.4f} (i.e., {p*100:.2f}%)")