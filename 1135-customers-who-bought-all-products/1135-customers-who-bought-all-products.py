import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    P_list = product.sort_values(by = 'product_key').product_key.tolist()
    data = pd.DataFrame()
    l = []

    for i in customer['customer_id'].unique():
        C_list = customer[customer['customer_id'] == i]['product_key'].sort_values().unique().tolist()
        if P_list == C_list:
            l.append(i)
    
    data['customer_id'] = l
    data.sort_values(by = 'customer_id', inplace = True)

    return data
    

    