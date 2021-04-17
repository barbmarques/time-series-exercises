import pandas as pd
import requests


def get_sales_data():
    '''
    This function reads the sales_data.csv and returns the data in a pandas dataframe.
    '''
    df = pd.read_csv('sales_data.csv')
    return df

df = get_sales_data()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_items_df():
    
    '''
    This function scans through all pages of the API at the given URL and returns a pandas dataframe containing the entire dataset.
    '''
    
    #creating a blank list for items
    items_list = []
    
    #define url and send request to server
    url = "https://python.zach.lol/api/v1/items"
    response = requests.get(url)
    
    # return the response text
    data = response.json()
    
    # define n as the last page ('max_page') of the data
    n = data['payload']['max_page']
    
    # loop through page urls, adding data from each page to items_list
    for i in range(1, n+1):
        new_url = url+"?page="+str(i)
        response = requests.get(new_url)
        data = response.json()
        page_items = data['payload']['items']
        items_list += page_items
        
    # create a dataframe containing data from items_list   
    items = pd.DataFrame(items_list)
    
    return items


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_stores_df():
   
    '''
    This function scans through all pages of the API at the given URL and returns a pandas dataframe containing the entire dataset.
    '''
    
    #creating a blank list for stores
    stores_list = []
    
    #define url and send request to server
    url = "https://python.zach.lol/api/v1/stores"
    response = requests.get(url)
    
    # return the response text
    data = response.json()
    
    # define n as the last page ('max_page') of the data    
    n = data['payload']['max_page']
    
    
    # loop through page urls, adding data from each page to list of stores  
    for i in range(1, n+1):
        new_url = url+"?page="+str(i)
        response = requests.get(new_url)
        data = response.json()
        page_stores = data['payload']['stores']
        stores_list += page_stores

    # create a dataframe containing data from stores_list  
    stores = pd.DataFrame(stores_list)
    
    return stores
    
    
 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_sales_df():
    
    '''
    This function scans through all pages of the API at the given URL and returns a pandas dataframe containing the entire dataset.
    '''
    
    #creating a blank list for sales    
    sales_list = []
    
    #define url and send request to server    
    url = "https://python.zach.lol/api/v1/sales"
    response = requests.get(url)
    
    # return the response text    
    data = response.json()
    
    # define n as the last page ('max_page') of the data 
    n = data['payload']['max_page']
    
    # loop through page urls, adding data from each page to list of sales
    for i in range(1, n+1):
        new_url = url+"?page="+str(i)
        response = requests.get(new_url)
        data = response.json()
        page_sales = data['payload']['sales']
        sales_list += page_sales

    # create a dataframe containing data from sales_list          
    sales = pd.DataFrame(sales_list)
    
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
    
    
    