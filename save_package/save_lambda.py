import gspread

def save_data(event, context):
    gc = gspread.service_account(filename="./service_account.json")
    
    wks = gc.open("CAB DataPipeline Tesla Stock Price").sheet1

    wks.append_row([event["responsePayload"]["date"],
                    event["responsePayload"]["close"]])
    return "Data written to Google Sheet"
