#basics
import requests
#math, plots
import pandas as pd
#API limitations
import time

#function with structure matching all cases
def getData(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data["results"][0]["values"])
        df = df[['year', 'val']]
        df = df.sort_values(by='year', ascending=False)
        
        idx_max_year = df['year'].idxmin()
        current_value = df.iloc[idx_max_year]['val']
        current_year = df.iloc[idx_max_year]['year']
        #sorting again to retun chart-ready df
        df = df.sort_values(by='year', ascending=True)

        return df, current_value, current_year