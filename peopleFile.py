


import pandas as pd

def make_peopleFile():

    # Read in the constituent email address file.
    df_emails = pd.read_csv('data/cons_email.csv')



    # Filter dataset to primary email addresses only.
    df_emails = df_emails.loc[df_emails['is_primary']==1]






    # Read in the subscription status file and filter to statuses 
    # where chapter_id is 1 only.


    df_sub = pd.read_csv('data/cons_email_chapter_subscription.csv')
    df_sub = df_sub.loc[df_sub['chapter_id']==1]



    # Merge the email address and subscription datasets on the 
    # common column cons_email_id.




    df_subEmail = df_emails.merge(df_sub, how='inner', 
                            on='cons_email_id')



    # Change datatype of the cons_id column by replacing null 
    # values with 0 and converting to integers.




    df_subEmail.cons_id.fillna(0, inplace=True)





    df_subEmail.cons_id = df_subEmail.cons_id.astype('int')


    # Read in the constituents dataset.




    df_cons = pd.read_csv('data/cons.csv')




    # Merge the new matched dataset with the constitiuents dataset 
    # on the cons_id column.



    df_all = df_subEmail.merge(df_cons, how='inner', 
                            on='cons_id')








    # Create an empty dataframe for the final people file with 
    # the needed columns.




    df_final = pd.DataFrame()





    df_final[['email', 'code', 'is_unsub', 
          'created_dt', 'updated_dt']] = df_all[['email', 'source', 
                                                    'isunsub', 'create_dt_y', 
                                                         'create_dt_x']]


    # Convert the is_unsub column to boolean datatype and the created_dt and 
    # updated_dt columns to datetime objects.




    df_final['is_unsub'] = df_final['is_unsub'].astype('bool')
    df_final['created_dt']= pd.to_datetime(df_final['created_dt'])
    df_final['updated_dt']= pd.to_datetime(df_final['updated_dt'])

    # Save as csv file
    return df_final.to_csv('produced_files/people.csv', index=False)


make_peopleFile()





