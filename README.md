# Financial Modeling API

## Project Description
The Financial Modeling API is designed to automate the extraction of financial ratios for the stock symbol 'AAPL' from an external API, store the data in a PostgreSQL database, and use it to train a regression model. This system uses a Flask API to trigger model training upon a GET request and outputs a 'completed' response once the process is finished. The aim is to predict stock prices using financial ratios as features.

## Installation
1. **Clone the repository:**
git clone https://github.com/shubhammachal/financial_modeling_api.git
2. **Set up a virtual environment:** <br>
python -m venv venv<br>
source venv/bin/activate

## Usage
### ratios_api.py 
This script is used to fetch financial ratios from financial modeling prep api and store them in the database.

### db_query.py
This script fetches the stored data, constructs a DataFrame, and saves the data in data.csv file.

### app.py
This script sets up the Flask API, and should be kept running to listen for GET requests to trigger model training. It uses data from data.csv file, train a regression model to predict stock prices and evaluate the model using R square and RMSE value.


## Contributing
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the [MIT License](LICENSE).

## Exploring Language Model Pipelines for Stock Forecasting
This script uses traditional Machine Learning i.e. regression to predict the stock prices. However, language model pipelines, such as those provided by OpenAI, offer an innovative alternative. These models can be trained on large datasets of textual information (e.g., news articles, financial reports) to capture nuances and sentiments that might impact stock prices. Unlike traditional models that directly map features to outputs, language models can generate intermediate representations, which can then be decoded into predictions. This approach allows for a more flexible and nuanced understanding of how various factors might influence stock movements.

For more information, feel free to check out https://site.financialmodelingprep.com/developer/docs.

