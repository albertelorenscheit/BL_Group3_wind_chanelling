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
