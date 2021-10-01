import pandas as pd
import  os
from Robo_inv_managment.settings import TEMPLATE_DIR

def readsheet():
    sheet = pd.read_excel('ROBO INV.xlsx', index_col=0,skiprows=1)
    PATH = os.path.join(TEMPLATE_DIR,'test.html')
    print(PATH)

    sheet.to_html(PATH)
    print(len(sheet))
    print(sheet)
    print(sheet.STATUS)
    print(sheet)


    return sheet
readsheet()
