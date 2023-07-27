from scraper.scarper import amazon
import time 
import openpyxl
from prettytable import PrettyTable 
from bs4 import BeautifulSoup as bs
bot=amazon(headless=True)
try:
    with bot:
        data=bot.search_items()
        table=PrettyTable(
            field_names=["Et_live","Et_mop","bb_seller_p","bb_seller_name","et_cost"]
        )
        table.add_rows(data)
        print(table)



        existing_file = r"C:\Users\kaifk\lpth\selenium\project\amazon\scraper\Philps BB Tracker_12.07.xlsx"
        book = openpyxl.load_workbook(existing_file)

        sheet = book['Sheet1']

        # Determine the start row and column to write the data
        start_row = 45
        start_column = 9

        for i, row_data in enumerate(data):
            for j, value in enumerate(row_data):
                sheet.cell(row=start_row + i, column=start_column + j, value=value)

        book.save(existing_file)

except Exception as e:
    print("Error Occured hello : =",e)
    
time.sleep(100)


