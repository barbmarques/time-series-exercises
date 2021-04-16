import pandas as pd
import requests

stores = pd.read_csv('stores.csv', index_col=0)

def get_items_df():

    '''
    This function downloads the 'items' data from https://python.zach.lol/api/v1/items
    and returns the data in a pandas data frame.
    '''
    
    items_list = []
    url = "https://python.zach.lol/api/v1/items"
    response = requests.get(url)
    data = response.json()
    n = data['payload']['max_page']
    
    for i in range(1, n+1):
        new_url = url+"?page="+str(i)
        response = requests.get(new_url)
        data = response.json()
        page_items = data['payload']['items']
        items_list += page_items
        
    items = pd.DataFrame(items_list)
    
    items.to_csv (r'/Users/barbmarques/codeup-data-science/time-series-exercises/items.csv', index = False, header=True)
    
    return items

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_stores_df():
    
    '''
    This function downloads the 'stores' data from https://python.zach.lol/api/v1/stores
    and returns the data in a pandas data frame.
    '''
    
    stores_list = []
    url = "https://python.zach.lol/api/v1/stores"
    response = requests.get(url)
    data = response.json()
    n = data['payload']['max_page']
    
    for i in range(1, n+1):
        new_url = url+"?page="+str(i)
        response = requests.get(new_url)
        data = response.json()
        page_stores = data['payload']['stores']
        stores_list += page_stores
        
    stores = pd.DataFrame(stores_list)
    
    stores.to_csv (r'/Users/barbmarques/codeup-data-science/time-series-exercises/stores.csv', index = False, header=True)
    
    
    return stores


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_sales_df():
    
    
    '''
    This function downloads the 'sales' data from https://python.zach.lol/api/v1/sales
    and returns the data in a pandas data frame. This function may take a few minutes to run
    and it results in a data frame of ~913,000 records
  
    '''
    
    sales_list = []
    url = "https://python.zach.lol/api/v1/sales"
    response = requests.get(url)
    data = response.json()
    n = data['payload']['max_page']
    
    for i in range(1, n+1):
        new_url = url+"?page="+str(i)
        response = requests.get(new_url)
        data = response.json()
        page_sales = data['payload']['sales']
        sales_list += page_sales
        
    sales = pd.DataFrame(sales_list)
    
    sales.to_csv (r'/Users/barbmarques/codeup-data-science/time-series-exercises/sales.csv', index = False, header=True)
    
    
    return sales



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def combine_data_df():    
    
    '''
    This function takes in the three data frames (items, stores, sales), joins them and returns one
    combined data frame with 913,000 records and 14 attributes. 
    '''
    
    # join sales and stores on store_id
    sales_stores_items = pd.merge(sales, stores, left_on='store', right_on='store_id').drop(columns={'store'})
     
    # now join the above dataframe to items on item
    sales_stores_items(df, items, left_on='item', right_on='item_id').drop(columns={'item'})
    
    df.to_csv (r'/Users/barbmarques/codeup-data-science/time-series-exercises/combined_data.csv', index = False, header=True)
    
    
    return df
    
    
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_ops():
    '''
    This function retrieves the Open Power Systems Data for Germany in .csv and returns the data in 
    a pandas data frame.
    '''

    # get data from csv
    base_url = 'https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv'

    # write to df
    ops = pd.read_csv(base_url)
    
    return ops

