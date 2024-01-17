from main import get_data
import gspread

def save_data():
    data = get_data()
    gc = gspread.service_account(filename="C:\Asus WebStorage\psabin@gmail.com\MySyncFolder\Data Science Course\_offline\service_account.json")
    

    wks = gc.open("CAB DataPipeline Tesla Stock Price").sheet1

    wks.append_row([data["date"],
                    data["close"]])
save_data()