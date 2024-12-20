![Frame 2](https://github.com/user-attachments/assets/edba04b2-d54b-4228-b6d0-a6b832cee304)

# Imputing Daily Gas Prices

## Overview

This project investigates efficient data collection methods for time-series data, specifically focusing on inferring daily gas price values from weekly records. By comparing Linear Approximation and a quadratic Taylor Series, the project aims to achieve accurate daily imputations with minimized data demands, making it a valuable approach for data efficiency in forecasting and reducing storage and processing needs.

## Project Structure

- **main.ipynb**: Contains the full code and analysis for the project, including data loading, imputation methods, comparisons, and visualizations of results.
- **gas_price_data.txt**: Source data file containing weekly gas prices (ensure this is placed in the same directory for seamless execution).

## Methods

### 1. Linear Approximation
The Linear Approximation approach leverages a straightforward linear regression model to estimate daily values between weekly data points. This method prioritizes simplicity and computational efficiency.

### 2. Quadratic Taylor Series
The Taylor Series method expands upon the linear approach by incorporating a second-order term, allowing for curvature in the estimated data. This approach is particularly useful in markets with high variability.

## Results

The analysis demonstrates:
- **Accuracy**: Taylor Series shows higher accuracy in fluctuating markets, while Linear Approximation provides a good balance of speed and simplicity.
- **Application in Extrapolation**: Both methods have been tested for interpolation and extrapolation, with Taylor Series performing well in both contexts.

## Getting Started

### Prerequisites
- Python 3.x
- Required libraries: `pandas`, `numpy`, `matplotlib`, `sklearn`

Install any missing packages using:
```bash
pip install pandas numpy matplotlib scikit-learn
```

## Usage

1. Clone the repository

```bash
git clone <repository_url>
cd <repository_name>
```

2. Run the Jupyter notebook (main.ipynb) to see the complete analysis. The notebook will:
   
- Load the data
- Apply both Linear Approximation and Taylor Series methods
- Generate visual comparisons of the imputation methods

## Visualizations

Several plots illustrate the effectiveness of each method, particularly highlighting Taylor Series’ strength in capturing variability. Ensure matplotlib is installed to view these.

## Repository

The full code, analysis, and results are available in this repository. Contributions are welcome to explore additional imputation methods or expand on the findings.

## License

This project is open-source under the MIT License.
