import pandas as pd
import requests

def acquire_items():

    '''
    This function obtains the data from the base url, writes it to given directory and 
    returns the data in a pandas dataframe
    '''
    # get data from API
    base_url = 'https://python.zach.lol/api/v1/items'
    response = requests.get(base_url)
    
    # save data to dataframe
    data = response.json()
    items = pd.DataFrame(data['payload']['items'])
    
    # write to csv and store on hard drive
    items.to_csv (r'/Users/barbmarques/codeup-data-science/time-series-exercises/items.csv', index = False, header=True)

    return items
    
def acquire_stores():
    
    '''
    This function obtains the data from the base url, writes it to given directory and 
    returns the data in a pandas dataframe
    '''
    
    # get data from API
    base_url = 'https://python.zach.lol/api/v1/stores'
    response = requests.get(base_url)
    
    # save data to dataframe
    data = response.json()
    stores = pd.DataFrame(data['payload']['stores'])
    
    # write to csv and store on hard drive
    stores.to_csv (r'/Users/barbmarques/codeup-data-science/time-series-exercises/stores.csv', index = False, header=True)

    return stores    
    
    
def acquire_sales():
    
    '''
    This function obtains the data from the base url, writes it to given directory and 
    returns the data in a pandas dataframe
    '''
    # get data from API
    base_url = 'https://python.zach.lol/api/v1/sales'
    response = requests.get(base_url)

    # save data to dataframe
    data = response.json()
    sales = pd.DataFrame(data['payload']['sales'])
    
    # write to csv and store on hard drive    
    sales.to_csv (r'/Users/barbmarques/codeup-data-science/time-series-exercises/sales.csv', index = False, header=True)

    return sales   
    