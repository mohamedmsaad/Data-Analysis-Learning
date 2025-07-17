from scipy.stats import norm

def prob_in_between(mu, sigma, upper, lower):
    z_upper = (upper-mu)/sigma
    z_lower = (lower-mu)/sigma

    p_upper = norm.cdf(z_upper)
    p_lower = norm.cdf(z_lower)

    probability = p_upper - p_lower

    print(f"Z({upper}) = {z_upper:.2f} --> cumulative probability = {p_upper:.4f}")
    print(f"Z({lower}) = {z_lower:.2f} --> cumulative probability = {p_lower:.4f}")
    print(f"Probability between {lower} and {upper}: {probability:.4f} ({probability*100:.2f}%)")

    return probability

if __name__ == "__main__":
    mu = float(input("Enter the mean (mu): "))
    sigma = float(input("Enter the standard deviation (sigma): "))
    lower = float(input("Enter the lower bound: "))
    upper = float(input("Enter the upper bound: "))


    prob_in_between(mu, sigma, upper, lower)
