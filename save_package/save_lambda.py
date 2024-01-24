from main import get_data
import gspread

def save_data(event, context):
    # data = get_data() Don't think we need to call this, because it's the get_data function that triggers save_data
    gc = gspread.service_account(filename="./service_account.json")
    

    wks = gc.open("CAB DataPipeline Tesla Stock Price").sheet1

    wks.append_row([event["date"],
                    event["close"]])
    return "Data written to Google Sheet"
