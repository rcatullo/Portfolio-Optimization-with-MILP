import gurobipy as gp
from gurobipy import GRB
import yfinance as yf
import numpy as np
import pandas as pd

# Parameters
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']  # Portfolio assets
start_date = '2020-01-01'
end_date = '2023-01-01'
confidence_level = 0.95  # CVaR confidence level
budget = 1.0  # Total budget for investment
max_assets = 3  # Maximum number of assets in the portfolio
scenarios = 1000  # Number of scenarios for stochastic optimization

# Fetch historical data
data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
returns = data.pct_change().dropna()

# Generate random scenarios for returns
scenario_returns = np.random.multivariate_normal(
    returns.mean(), returns.cov(), size=scenarios
)
scenario_returns_df = pd.DataFrame(scenario_returns, columns=tickers)

# Calculate expected returns and covariance matrix
expected_returns = returns.mean()
covariance_matrix = returns.cov()

# Optimization model
model = gp.Model("Portfolio_Optimization")

# Decision variables
x = model.addVars(tickers, lb=0, ub=1, vtype=GRB.CONTINUOUS, name="x")  # Portfolio weights
z = model.addVars(range(scenarios), lb=0, vtype=GRB.CONTINUOUS, name="z")  # CVaR variables
alpha = model.addVar(vtype=GRB.CONTINUOUS, name="alpha")  # VaR variable
y = model.addVars(tickers, vtype=GRB.BINARY, name="y")  # Asset inclusion variables

# Objective: Minimize CVaR
model.setObjective(
    alpha + (1 / (1 - confidence_level)) * (1 / scenarios) * gp.quicksum(z[s] for s in range(scenarios)),
    GRB.MINIMIZE
)

# Budget constraint
model.addConstr(gp.quicksum(x[t] for t in tickers) == budget, "Budget")

# Linking constraint: x[t] > 0 implies y[t] = 1
for t in tickers:
    model.addConstr(x[t] <= y[t], f"Link_{t}")

# Cardinality constraint: Limit number of assets
model.addConstr(gp.quicksum(y[t] for t in tickers) <= max_assets, "MaxAssets")

# CVaR constraints for each scenario
for s in range(scenarios):
    model.addConstr(
        gp.quicksum(scenario_returns_df.iloc[s][t] * x[t] for t in tickers) >= alpha - z[s],
        f"CVaR_Scenario_{s}"
    )

# Solve the model
model.optimize()

# Extract results
if model.status == GRB.OPTIMAL:
    portfolio_weights = {t: x[t].X for t in tickers if x[t].X > 1e-6}
    print("Optimal Portfolio Allocation:")
    print(portfolio_weights)
    print("\nSelected Assets:")
    print([t for t in tickers if y[t].X > 0.5])
    print(f"\nOptimal CVaR: {model.ObjVal}")
else:
    print("No optimal solution found.")
