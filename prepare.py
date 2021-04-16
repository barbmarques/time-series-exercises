import pandas as pd
import matplotlib.pyplot as plt

def get_sales_data():
    '''
    This function reads the sales_data.csv and returns the data from all three databases into a single pandas dataframe.
    '''
    df = pd.read_csv('sales_data.csv')
    return df

df = get_sales_data()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def prep_sales_data(df):
    '''
    This function takes in a dataframe and returns the dataframe with the index reset to the given column as a datetime variable, adds a column for total amount of sale and adds a column for month and weekday, and drops the item_upc14 column (because it is a duplicate of item_upc12).  
    '''
    # change data type of column to a datetime variable
    df['sale_date'] = pd.to_datetime(df.sale_date, format='%a, %d %b %Y %H:%M:%S %Z')
    
    # change datetime format
    
    #set column as the df index
    df = df.set_index('sale_date').sort_index()
    
    #add a column for total amount of sale in dollars
    df['sale_total'] = df.sale_amount * df.item_price
    
    #add a column for month and day of week
    df['month'] = df.index.month
    df['day_of_week'] = df.index.day_name()
    
    #drops the item_upc14 column because it is a duplicate of item_upc12
    df.drop(columns = ['item_upc14'])

    return df
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def plot_sales_items():
    '''
    This function plots distribution of sale_amount and item_price
    '''
    #set figure size
    plt.figure(figsize=(20, 5))
    
    #create first subplot (sales amounts)
    plt.subplot(121)
    df['sale_amount'].plot.hist(color = 'lightgreen', edgecolor = 'darkblue')
    plt.title('Distribution of Sale Amounts')
    plt.xlabel('Number of Items Sold')
    
    #create second subplot (item prices)
    plt.subplot (122)
    df['item_price'].plot.hist(color = 'lightgreen', edgecolor = 'darkblue')
    plt.title('Distribution of Item Prices')
    plt.xlabel('Price in Dollars')
    plt.show()
    return



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def datetime(df, col):
    '''
    This function takes in a dataframe and column name. It returns the dataframe with the index reset to the given column as a datetime variable.  
    '''
    # change data type of column to a datetime variable
    df[col] = pd.to_datetime(df[col])
    
    #set column as the df index
    data = df.set_index(col).sort_index()
    
    return data
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def month_day():
    '''
    This function adds a column specifying month and weekday based on the index value.
    '''
    df['month'] = df.index.month
    df['day_of_week'] = df.index.day_name()
    return df


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def add_total():
    
    '''
    This function adds a column for total amount of sale. 
    '''
    df['sale_total'] = df.sale_amount * df.item_price
    return df


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def plot_dist():
    
    '''
    This function plots distribution of consumption, wind, solar and wind+solar."
    '''
    #set figure size
    plt.figure(figsize=(15, 10))
    plt.subplots_adjust(left=0.125, bottom=0.01, right=0.9, top=0.9, wspace=0.2, hspace=0.3)
    

    #create first subplot (consumption)
    plt.subplot(221)
    ops['Consumption'].plot.hist(color = 'lightgreen', edgecolor = 'darkblue')
    plt.title('Distribution of Consumption')
    plt.xlabel('Consumption')
    
    #create second subplot (wind)
    plt.subplot (222)
    ops['Wind'].plot.hist(color = 'lightgreen', edgecolor = 'darkblue')
    plt.title('Distribution of Wind')
    plt.xlabel('Wind')
    
    #create third subplot (solar)
    plt.subplot(223)
    ops['Solar'].plot.hist(color = 'lightgreen', edgecolor = 'darkblue')
    plt.title('Distribution of Solar')
    plt.xlabel('Solar')
    
    #create second subplot (wind)
    plt.subplot (224)
    ops['Wind+Solar'].plot.hist(color = 'lightgreen', edgecolor = 'darkblue')
    plt.title('Distribution of Wind+Solar')
    plt.xlabel('Wind+Solar')
          
    plt.show()
    return
 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def month_yr():
    '''
    This function adds a column specifying month and year based on the index value.
    '''
    ops['Month'] = ops.index.month
    ops['Year'] = ops.index.year
    return ops


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

