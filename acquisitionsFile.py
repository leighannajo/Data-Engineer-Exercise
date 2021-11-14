

import pandas as pd


def makeAcquisitionFile():
    # Read in previously created people file.
    
    df_final = pd.read_csv('produced_files/people.csv')
    
    df_final['created_dt']= pd.to_datetime(df_final['created_dt'])
    df_final['updated_dt']= pd.to_datetime(df_final['updated_dt'])
    
    # Create the acquisitions file by grouping on date of the created_dt 
    # column and counting all instances of constituents acquired on that date.

    

    df_acquistions = df_final.groupby(pd.Grouper(key='created_dt', axis=0, 
                      freq='2D', sort=True)).count()



    # Create the final acquistion file by resetting the index of the 
    # grouped data, creating an empty dateframe and then creating 
    # the columns needed.




    df_acquistions.reset_index(inplace=True)





    df_acq_final = pd.DataFrame()





    df_acq_final[['acquisition_date', 
              'acquistions']] = df_acquistions[['created_dt', 'email']]





    return df_acq_final.to_csv('produced_files/acquisition_facts.csv', 
                                                           index=False)

makeAcquisitionFile()
