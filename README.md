# Spoonacular API demonstration

## Running the application

### Step1: Get an API key

In order to run the application you need to create an account on https://spoonacular.com/ and get you API key [here](https://spoonacular.com/food-api/console#Profile).

After you got your API key, create `config.py` file in root of this repo. It must look like this:
```python
API_KEY = '8b6b8cf047014c24b31861c69629598c'
```
### Step2: Install dependencies

Install dependencies with `pip install -r requirements.txt` in your command line

### Step3: Run the application

Run the application with `python main.py` in your command line

## Restrictions of API free plan

* Only 1 request per second is allowed
* Only 150 requests per day are allowed