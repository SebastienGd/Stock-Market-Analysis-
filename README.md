# Stock-Market-Analysis

This project provides a framework for testing and comparing different trading strategies using historical market data, allowing users to analyze and refine their trading approaches in a simulated environment.

Data Handling (data.py):
This module contains functionality to fetch historical financial market data. It involves retrieving data from Polygon.io's API.

Order Execution (orders.py):
This module handles the execution of buy and sell orders in the simulated trading environment.

Trading Strategies (strategy.py):
Different trading strategies are implemented as classes. Two strategies are provided: Hammer and MovingAverageCrossover.
Each strategy class contains methods to analyze market data and generate buy/sell signals based on certain conditions defined within the strategy.

Simulation (simulation.py):
The Simulation class orchestrates the entire simulation process.
It takes a trading strategy object as input during initialization.
The run_simulation() method executes the selected strategy and evaluates its performance.
It tracks profits, win rate, and the number of trades generated by the strategy during the simulation.

## Usage/Examples

```python
Simulation(
    Hammer(
        Data( #See Poligon.io API
            ticker="NIO",
            timespan="minute",
            start_date="2022-02-01",
            end_date="2022-03-01",
            multiplier=5,
            sort="asc",
            limit=50000,
        ),
        0.5 / 100, #Percentage gain
        2, #Risk/Reward ratio
    ),
).run_simulation()

Simulation.write_CSV("file_name.csv", "2022-03-13", "2022-04-13", 0.5/100, 2, "NIO")

```
