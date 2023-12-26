import requests as rq
import pandas as pd
from io import StringIO


response = rq.get("https://en.wikipedia.org/wiki/G20")

io = StringIO(response.text)
raw_data = pd.read_html(io)

table = raw_data[3]

g20_df = table.to_csv("g20_data.csv")
