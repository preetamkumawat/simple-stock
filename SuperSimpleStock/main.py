from simple_stock import SimpleStock, validate_params


def main():
    while True:
        try:
            input_params = raw_input("Please input details in format: "
                                     "[Stock(tea/pop/ale/gin/joe)] [Quantity] [MarketPrice] [TransactionType(buy/sell)] "
                                     ">>> ")
            input_params = input_params.split(" ")

            is_valid_input, msg = validate_params(input_params)

            if not is_valid_input:
                print(msg)
                continue

            simple_stock_obj = SimpleStock(
                input_params[0].upper(),
                int(input_params[1]),
                float(input_params[2]),
                input_params[3]
            )

            dy = simple_stock_obj.calculate_divident_yield()
            print("Divident Yield: {}".format(dy))

            pe_ratio = simple_stock_obj.calculate_divident_yield()
            print("PE Ratio: {}".format(pe_ratio))

            last_stock_numbers = simple_stock_obj.check_previous_stocks()
            print("Volume Weighted Stock Price: {}".format(last_stock_numbers["weighted_stock_price"]))
            print("GBCE All Share Index: {}".format(last_stock_numbers["all_share_index"]))
        except Exception:
            print("Good Bye!")
            break


if __name__ == '__main__':
    try:
        main()
    except:
        print("Good Bye!")
