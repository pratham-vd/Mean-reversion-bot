import yfinance as yf
import pandas as pd

class Download_data:
    def __init__(self,start,end,symbol):  
        self.start = start
        self.end = end
        self.symbol = symbol

    def download_data(self):
        df = yf.download(self.symbol, start=self.start, end=self.end)
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = ['_'.join(col).strip() for col in df.columns.values]
            close_col = f'Close_{self.symbol}'
        else:
            close_col = 'Close'
        return df

data = Download_data(start="2020-01-01", end="2024-01-01", symbol="ETH-USD")
df = data.download_data()

print(df)