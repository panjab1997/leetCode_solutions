import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    merged_df = employee.merge(bonus, how = 'left', on = 'empId')
    df = merged_df[['name','bonus']]
    final = df.drop(df[df['bonus'] >= 1000].index)

    return final
    

    