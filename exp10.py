# Experiment 10: Linear Regression using Python

import numpy as np
import matplotlib.pyplot as plt

# Function to estimate coefficients
def estimate_coef(x, y):
    # Number of observations/points
    n = np.size(x)

    # Mean of x and y vector
    m_x, m_y = np.mean(x), np.mean(y)

    # Calculating cross-deviation and deviation about x
    SS_xy = np.sum(y * x) - n * m_y * m_x
    SS_xx = np.sum(x * x) - n * m_x * m_x

    # Calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x

    return (b_0, b_1)


# Function to plot regression line
def plot_regression_line(x, y, b):
    # Plotting the actual points as scatter plot
    plt.scatter(x, y, color="magenta", marker="o", s=60, label="Actual Data")

    # Predicted response vector
    y_pred = b[0] + b[1] * x

    # Plotting the regression line
    plt.plot(x, y_pred, color="green", label="Regression Line")

    # Putting labels
    plt.xlabel('X - Independent Variable')
    plt.ylabel('Y - Dependent Variable')
    plt.title("Linear Regression Line")
    plt.legend()
    plt.show()


# Main function
def main():
    # Observations / sample data
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

    # Estimating coefficients
    b = estimate_coef(x, y)
    print("Estimated coefficients:")
    print(f"b_0 (Intercept) = {b[0]:.3f}")
    print(f"b_1 (Slope) = {b[1]:.3f}")

    # Plotting regression line
    plot_regression_line(x, y, b)


# Driver code
if __name__ == "__main__":
    main()
