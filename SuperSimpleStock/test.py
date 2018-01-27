import itertools
import json
import time

from simple_stock import SimpleStock, validate_params

# These are our inputs
stocks = ["TEA", "POP", "ALE", "GIN", "JOE", 0, -1, "TEST"]
quantities = ["TEST"] + range(-10, 100, 10)
market_prices = ["TEST"] + range(-50, 1000, 50)
transaction_type = ["buy", "sell", "0", 0, -1]

# This is to hold the script for a certain number of seconds (to check how it behaves with past 15 minutes transactions)
WAIT_TIME_IN_SECONDS = 0

# This is used to check whether to print the input and out of invalid values
PRINT_ERROR_INPUTS = False

# Output file name
OUT_FILE_NAME = "out.txt"


def main():
    # This will provide us all the possible combinations of our inputs
    inputs = list(itertools.product(stocks, quantities, market_prices, transaction_type))
    test_dump = []
    for input_params in inputs:
        temp_out_dict = {
            "Input": {},
            "Output": {}
        }
        input_params = list(input_params)
        input_params = [str(input_params[0]), str(input_params[1]), str(input_params[2]), str(input_params[3])]
        temp_out_dict["Input"] = {
            "Stock": input_params[0],
            "Quantity": input_params[1],
            "MarketPrice": input_params[2],
            "TransactionType": input_params[3]
        }

        is_valid_input, msg = validate_params(input_params)

        if not is_valid_input:
            temp_out_dict["Output"] = msg

            if PRINT_ERROR_INPUTS:
                test_dump.append(json.dumps(temp_out_dict))

            continue

        simple_stock_obj = SimpleStock(
            str(input_params[0].upper()),
            int(input_params[1]),
            float(input_params[2]),
            str(input_params[3])
        )

        dy = simple_stock_obj.calculate_divident_yield()
        temp_out_dict["Output"]["DividentYield"] = dy

        pe_ratio = simple_stock_obj.calculate_divident_yield()
        temp_out_dict["Output"]["PE_Ratio"] = pe_ratio

        last_stock_numbers = simple_stock_obj.check_previous_stocks()
        temp_out_dict["Output"]["VolumeWeightedStockPrice"] = last_stock_numbers["weighted_stock_price"]
        temp_out_dict["Output"]["GBCE_AllShareIndex"] = last_stock_numbers["all_share_index"]

        test_dump.append(json.dumps(temp_out_dict))

        time.sleep(WAIT_TIME_IN_SECONDS)

    try:
        with open(OUT_FILE_NAME, "w") as out_file:
            out_file.write(", \n".join(test_dump))

        print("File Written with output: {}".format(OUT_FILE_NAME))
    except:
        print("Couldn't write output to a file!")


if __name__ == '__main__':
    main()
