from urllib import request

goog_url = "https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1612275967&period2=1643811967&interval=1d&events=history&includeAdjustedClose=false"


def download_stock_data(csv_url):
    response = request.urlopen(csv_url)  # connect to the internet
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    des_url = r"goog.csv"  # r is for raw string
    fx = open(des_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()


download_stock_data(goog_url)
