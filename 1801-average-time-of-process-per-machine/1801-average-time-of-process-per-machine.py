import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    activity_start = activity[activity['activity_type'] == 'start']
    activity_end = activity[activity['activity_type'] == 'end']

    activity_start.rename(columns={'timestamp': 'start_time'}, inplace=True)
    activity_end.rename(columns={'timestamp': 'end_time'}, inplace=True)

    merged = pd.merge(activity_start, activity_end, on=['machine_id', 'process_id'])

    merged['processing_time'] = merged['end_time'] - merged['start_time']

    avg_time = merged.groupby('machine_id')['processing_time'].mean().round(3)

    return avg_time.to_frame('processing_time').reset_index()    