# CSCI-567-Fall-2023-group-project
<a name="readme-top"></a>

## About the project

The inception of this project is driven by the critical goal of enhancing the prediction accuracy of Bitcoin prices, a subject of great significance in the financial sector. Existing methodologies in this realm often falter due to the volatile nature of cryptocurrency markets, leading to predictions that are less reliable and, at times, misleading. Our approach, grounded in a comparative analysis of three important models：

- AutoRegressive Integrated Moving Average (ARIMA)
- Linear Regressions (LRs)
- Long Short-Term Memory Networks (LSTM)
- Generative Adversarial Networks (GAN)

  We try to use them to address these challenges. We observed that while individual models have been explored in isolation, a comprehensive comparative study that encapsulates the strengths and weaknesses of these models in tandem is lacking. Our solution is a careful examination of these models, assessing their accuracy, reliability, and computational efficiency in the context of Bitcoin price forecasting.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With
Writen by the python

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
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Files
- `CSCI567 Baseline Models.ipynb`: Our baseline models
- `CSCI567 GAN.ipynb` : GAN model
- `CSCI567 GRU.ipynb` : GRU model
- CSCI567 Poster.pdf` : The project poster file.
- `CSCI567 WGAN-GP.ipynb` : WGAN-GP model
- `CSCI567Project_Bitcoin_Predict_lstm.ipynb` :This the jupyter notebook for building the LSTM model to predict bitcoin.
- `merge.py` :  This py file show the detail how we process the data.
- `Merged_Data.csv` : This is our cleaned data csv file.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Authors

- Yu Du
- Yikun Chen
- Zheng Bao
- Zhiyuan Zhou
- Chao Li

**Department of Computer Science**  
University of Southern California  
Los Angeles, CA 90017, USA  

**Email**:  
- Yu Du: [ydu35952@usc.edu](mailto:ydu35952@usc.edu)
- Yikun Chen: [yikunche@usc.edu](mailto:yikunche@usc.edu)
- Zheng Bao: [baojames@usc.edu](mailto:baojames@usc.edu)
- Zhiyuan Zhou: [zzhou534@usc.edu](mailto:zzhou534@usc.edu)
- Chao Li: [cli49003@usc.edu](mailto:cli49003@usc.edu)



