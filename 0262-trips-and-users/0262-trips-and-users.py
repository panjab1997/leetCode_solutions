import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    trip_and_User = trips.merge(users, how = 'left', left_on ='client_id', right_on = 'users_id')
    trips_and_Users = trip_and_User.merge(users, how='left', left_on = 'driver_id', right_on = 'users_id',
    suffixes = ('_client', '_driver'))

    Unbanned = ((trips_and_Users['banned_driver'] == 'No') & (trips_and_Users['banned_client'] == 'No')
    & (trips_and_Users['request_at'] >= "2013-10-01") & (trips_and_Users['request_at'] <= "2013-10-03"))

    Cancelled = trips_and_Users['status'].isin(['cancelled_by_driver','cancelled_by_client'])

    aggregate_1 = trips_and_Users[Unbanned & Cancelled].groupby('request_at')['id'].count()
    aggregate_2 = trips_and_Users[Unbanned].groupby('request_at')['id'].count()

    cancellation_rate = round(aggregate_1 / aggregate_2, 2).fillna(0)

    Output = pd.DataFrame(cancellation_rate).reset_index()

    Output.columns = ['Day', 'Cancellation Rate']

    return Output
    
