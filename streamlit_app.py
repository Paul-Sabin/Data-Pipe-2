import gspread
import pandas as pd

def get_data():
    gc = gspread.service_account(filename="C:\Asus WebStorage\psabin@gmail.com\MySyncFolder\Data Science Course\_offline\service_account.json")
    wks = gc.open("CAB DataPipeline Tesla Stock Price").sheet1
    full_list_of_lists = wks.get_all_values()
    list_of_lists = full_list_of_lists[1:]
    df = pd.DataFrame(list_of_lists, columns = ['date', 'price'])
    return df

get_data()