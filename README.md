# **Portfolio Optimization with CVaR and Stochastic Optimization**

## **Overview**
This project implements a **portfolio optimization model** using **Conditional Value at Risk (CVaR)** to minimize potential financial losses in the worst-case scenarios. The model is built with Python, utilizes the `yfinance` API for real-world stock data, and employs the **Gurobi** solver to handle mixed-integer and stochastic programming.

The portfolio optimization problem incorporates constraints such as **cardinality limits** (maximum number of assets), **budget allocation**, and **asset selection** to reflect realistic investment scenarios.

---

## **Features**
- **Real-World Data Integration**: Fetch historical market data using `yfinance`.  
- **Risk Minimization**: Optimize the portfolio to minimize CVaR, a robust measure of tail risk.  
- **Stochastic Optimization**: Generate random scenarios for future returns based on historical data.  
- **Mixed-Integer Linear Programming (MILP)**: Solve problems with both continuous (portfolio weights) and binary (asset inclusion) variables.  
- **Customizable Constraints**: Add budget limits, cardinality constraints, and more.  

---

## **Requirements**
- Python 3.8 or later
- **Dependencies**:
  - `gurobipy`: Optimization solver library for MILP.
  - `yfinance`: API for fetching historical stock market data.
  - `numpy`: Numerical computations.
  - `pandas`: Data manipulation and analysis.

Install dependencies using:
```bash
pip install gurobipy yfinance pandas numpy
```

You also need a valid Gurobi license. Academic users can get a free license from [Gurobi Academic Program](https://www.gurobi.com/academia/academic-program-and-licenses/).

---

## **How to Run the Project**

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/your-repo-name/portfolio-optimization
cd portfolio-optimization
```

### **Step 2: Set Parameters**
Open the script file and modify the following:
- **`tickers`**: List of stock tickers (e.g., `['AAPL', 'MSFT', 'GOOGL']`).
- **`start_date` and `end_date`**: Define the date range for historical data.
- **`confidence_level`**: Confidence level for CVaR (e.g., 0.95 for 95% confidence).
- **`budget`**: Total investment amount.
- **`max_assets`**: Maximum number of assets in the portfolio.

### **Step 3: Run the Script**
Run the script using Python:
```bash
python portfolio_optimization.py
```

### **Step 4: View Results**
The script outputs:
- **Optimal Portfolio Allocation**: Portfolio weights for selected assets.  
- **Selected Assets**: List of included assets.  
- **Optimal CVaR**: Expected loss in worst-case scenarios.  

---

## **File Structure**
```
portfolio-optimization/
├── portfolio_optimization.py  # Main script
├── requirements.txt           # List of dependencies
├── README.md                  # Project documentation
```

---

## **Customization**

1. **Add Constraints**:  
   Modify the optimization model to include:
   - **Sector limits**: Ensure no sector dominates the portfolio.
   - **Transaction costs**: Model real-world trading fees.  

2. **Visualize Results**:  
   Use libraries like `matplotlib` or `seaborn` to plot the portfolio allocation or CVaR distribution.

3. **Extend Risk Measures**:  
   Replace CVaR with other measures, like Sharpe Ratio or Max Drawdown.

---

## **Example Output**
```
Optimal Portfolio Allocation:
{'AAPL': 0.4, 'MSFT': 0.35, 'GOOGL': 0.25}

Selected Assets:
['AAPL', 'MSFT', 'GOOGL']

Optimal CVaR: -0.032
```

---

## **Future Improvements**
- Integrate **real-time data** for dynamic optimization.  
- Develop a **web interface** to allow user input for parameters and view results interactively.  
- Experiment with **machine learning** to predict returns and risks.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Contact**
For questions or contributions, contact **Ryan Catullo** at **rcatullo@stanford.edu**.

--- 
