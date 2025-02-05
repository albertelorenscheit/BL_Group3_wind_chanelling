""" 
To use this library run the following two lines, in your .ipynb file before importing functions

import sys
sys.path.append("..")

"""

def AWS_file_loader(file_name):
    import pandas as pd

    df = pd.read_csv(file_name, skiprows=1).iloc[2:]
    # read the file, skip one row that has useless info, and the first 2 rows
    # of data because they are respectively units and nans
    df.loc[:,'TIMESTAMP'] = df.TIMESTAMP.astype('datetime64[ns]')
    # Change the format of datetime
    df.set_index('TIMESTAMP', inplace=True)
    # set the time as index
    df = df.astype(float)
    # change all other collumns to float
    return df

def compute_t_stat(x,t_0=0):
    """Computs the t-statistic of a distribution and the associated p-value.
    By default, it computes the deviation from t_0 = 0, but you may specify
    another value. Eg: for a linear regression slope, you could use t_0 = 1."""

    from scipy import stats
    tstat, pval = stats.ttest_1samp(x, 0)
    return {'t_0':t_0,
            'tstat':tstat,
            'pval':pval}

def save_figure(fig, folder_path, filename, file_format='png'):
 
    import os
    # Ensure the folder exists
    os.makedirs(folder_path, exist_ok=True)

    # Create the full file path
    file_path = os.path.join(folder_path, f"{filename}.{file_format}")

    # Save the figure
    fig.savefig(file_path, format=file_format, bbox_inches='tight')

    return file_path

def load_path():
    """Automatically returns the correct path for Linux or Windows users"""
    import platform
    if platform.system() =='Linux': path='/home/clc/Desktop/AGF350_data/Data/'
    elif platform.system() =='Windows': path='../Data/'
    return path
