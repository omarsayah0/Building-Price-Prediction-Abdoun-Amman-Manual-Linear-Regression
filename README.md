# Manual Linear Regression (Simple & Multiple)

## About
In this repository, I implemented **two regression models from scratch (without using scikit-learn)** to demonstrate how linear regression works mathematically and programmatically.  
It includes:

1. **Simple Manual Linear Regression** – implemented using the basic linear equation `y = b0 + b1*x`.
2. **Multiple Manual Linear Regression** – implemented using two approaches chosen by the user:
   - **Normal Equation** (analytical solution)
   - **Gradient Descent** (iterative optimization)

These models predict the **price of a building located in Abdoun, Amman, Jordan**, based on parameters such as:
- Building area (m²)
- Building age (years)
- Number of rooms

---

## Files in the Repository

| File Name | Description |
|------------|-------------|
| `Simple_Manual_Linear-Regression.py` | Implements a simple linear regression model using manual formulas for mean, variance, covariance, and coefficient estimation. |
| `Multiple_Manual_Linear-Regression.py` | Implements a multiple linear regression model with two selectable solving methods: Normal Equation or Gradient Descent. |

---

## How It Works

### Simple Linear Regression
The program:
1. Calculates the regression coefficients **(b₀, b₁)** manually using:
   \[
   b_1 = \frac{\text{Cov}(x, y)}{\text{Var}(x)} \quad,\quad b_0 = \bar{y} - b_1 \bar{x}
   \]
2. Predicts prices for new building areas.
3. Evaluates performance using:
   - **Mean Squared Error (MSE)**
   - **Mean Absolute Error (MAE)**
   - **R² Score**

### Multiple Linear Regression
The user selects one of two methods:

#### 1️⃣ Normal Equation
Uses the closed-form solution:
`θ = (X^T * X)^(-1) * X^T * y` 
This directly computes the optimal weights analytically.

#### 2️⃣ Gradient Descent
Uses an iterative approach to minimize the cost function:
`J(θ) = (1/m) * Σ(h_θ(xᵢ) - yᵢ)²`
It updates weights according to:
`θⱼ := θⱼ - α * (∂J(θ) / ∂θⱼ)`
where `α` is the learning rate.

---

## How to Run

1. Install Dependencies  (**only for multiple **):
   ```bash
   pip install numpy
   
2. Run the simple linear regression:
   ```bash
   python Simple_Manual_Linear-Regression.py

3. Run the multiple linear regression:
   ```bash
   python Multiple_Manual_Linear-Regression.py

4. Provide User Inputst , The script will ask you for:
   ```bash
   Add the size of the building in m^2:
   Add the age of the building:
   Add how many rooms in the building:

5. Run the multiple linear regression:
   ```bash
   python Multiple_Manual_Linear-Regression.py

6. Example Output:
   
- Simple Linear Regression:
   ```bash
   Add the size of the building in m^2: 250
   The expected price in JD is : 255,000 JD
   The Mean Squared Error is:  3456789.12
   The R^2 Score is:  0.987
   The Mean Absolute Error is:  1105.45
   
 - Multiple Linear Regression:
   ```bash
   Choose a method to solve this: (1) Normal Equation or (2) Gradient Descent: 1
   Add the size of the building in m^2: 300
   Add the age of the building: 3
   Add how many rooms in the building: 5
   The expected price in JD is : 495,000 JD
   The Mean Squared Error is:  2765432.88
   The R^2 Score is:  0.992
   The Mean Absolute Error is:  970.23

## Author

Omar Alethamat

LinkedIn : https://www.linkedin.com/in/omar-alethamat-8a4757314/

## License

This project is licensed under the MIT License — feel free to use, modify, and share with attribution.
