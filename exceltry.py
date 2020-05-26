import openpyxl

wb = openpyxl.load_workbook('test.xlsx')

print(wb.sheetnames)

sheet1 = wb.get_sheet_by_name('Sheet1')