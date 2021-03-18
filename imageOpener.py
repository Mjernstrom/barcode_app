import pandas as pd 
from PIL import Image
import os

def logic(barcodeInput, dir_path):
    dir_path_db = os.path.join(dir_path, 'test.xlsx')
    df2 = pd.read_excel(dir_path_db, engine='openpyxl', usecols=[1], sheet_name='Sheet1')
    for index, row in df2.iterrows():
        if int(barcodeInput) == row.values:
            df1 = pd.read_excel(dir_path_db, engine='openpyxl', usecols=[0], sheet_name='Sheet1')
            return str(df1.iloc[index].values)
        
    print("Could not find design.")

def main():
    scan = True
    dir_path = os.path.dirname(os.path.realpath(__file__))
    while scan:
        barcodeInput = input("Scan barcode then press enter: ")
        result = logic(barcodeInput, dir_path)
        chars_to_remove = "[]''"
        final_result = result
        for char in chars_to_remove:
            final_result = final_result.replace(char, "")
        dir_path_design = os.path.join(dir_path, final_result)
        img = Image.open(dir_path_design)
        img.show()


main()