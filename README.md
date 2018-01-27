# SuperSimpleStock
This code contains mainly 3 files:
1. **simple_stock.py** - This holds the code to validate the input and calculate DividentYield, PE_ratio, Volume Weighted Stock Price and All Share index
2. **main.py** - This will run the code and will keep on taking inputs and giving outputs until we forcefully quit the script with Ctrl + C
3. **test.py** - This file contains different test cases and saves their inputs and outputs to a file in the same directory where our code is.

## Running the code
Please type in the below command after navigating in terminal to directory named **SuperSimpleStock**

```
python main.py
```
The input prompt will ask for different input params as below:
 ```
 Please input in format: [Stock(tea/pop/ale/gin/joe)] [Quantity] [MarketPrice] [TransactionType(buy/sell)] >>> tea 10 1200 buy
 ```
>*The input params should be separated by spaces*


## Sample test cases:
In file **test.py** we have got few params which we can adjust to define our own test cases and run the script agains them with command:

```
python test.py
```

The parameters are displayed in order in which they are taken in **main.py** terminal:
```
stocks - holds different stock types ("TEA", "POP", "ALE", "GIN", "JOE")
quantities - Quantities to be bought or sold
market_prices - Market Prices of different stocks
transaction_type - Transaction type (buy/sell)
WAIT_TIME_IN_SECONDS - (integer) This param holds the wait time in each itiration of our loop. This is handy if we need to test the code for 15 minutes bracket
PRINT_ERROR_INPUTS - (boolean) If Set to True then input and output of test cases with wrong input values will be saved in the ouuut file.
OUT_FILE_NAME - this contains the file name to which we want to write our input and final output.
```
> The output file contains data in json format which can be formatted with online [json fomatter](http://jsonviewer.stack.hu/) for better visibility.
