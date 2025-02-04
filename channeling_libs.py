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
