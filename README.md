# csci-567-group-project



## About the project

An analysis of different model in predicting the bitcoin.
- ARIMA
- LRs
- GAN
- LSTM
We compare these model performances.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With
Writen by the python
- sklearn
- keras

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Getting Started

We have analysised couples of model. They are showed in different jupyternotebook.
### Prerequisites

This are the softwares needed and how to install them.
* install packages
  ```sh
  pip install tensorflow
  pip install numpy
  pip install pandas
  pip install numpy
  pip install keras
  pip install sklearn
  pip install matplotlib
  ```



### Source of Data
S&P 500 Index: 
https://fred.stlouisfed.org/series/SP500

Dow Jones Industrial Average: 
https://fred.stlouisfed.org/series/DJIA

VIX(Chicago Board Options Exchange Market Volatility Index):
https://www.cboe.com/tradable_products/vix/vix_historical_data/

US CPI monthly: 
https://fred.stlouisfed.org/series/CPIAUCSL

10-Year Breakeven Inflation Rate: 
https://fred.stlouisfed.org/series/T10YIEM

Sticky Price Consumer Price Index less Food and Energy:
https://fred.stlouisfed.org/series/CORESTICKM159SFRBATL

Bitcoin, BNB, Cardano, Ethereum, Litecoin, XRP:
https://www.kaggle.com/datasets/kapturovalexander/bitcoin-and-other-14-most-significant-cryptos/data


### Project_Bitcoin_Predict_lstm.ipynb LSTM model
File name:Project_Bitcoin_Predict_lstm.ipynb
It shows the works in the LSTM
This the jupyter notebook for building the LSTM model to predict bitcoin.

Data preparetion
read the clean data
Feature procese
remove rows
Modeling
Building a basic LSTM model
Experiments finding the best structure design of the LSTM(Automation programe to find best LSTM model for the target)
Result
Calculate the RMSE and Plot the real vs predict graph
