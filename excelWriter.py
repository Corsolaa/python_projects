import xlsxwriter

# Insert the path of .xlsx file
path = "excelSheet.xlsx"

# Set everything ready
workbook = xlsxwriter.Workbook(path)
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})
row = 0
column = 0

# Settings the content that you want to put in the excel-sheet
content = {
        "name": ["Sebas", "Bruno", "Ferry", "Samantha", "Nick"],
        "age": [19, 19, 47, 21, 20]
}

# So I have all the keys of the dictionary
dictKeys = content.keys()

for key in dictKeys:
    # For every key in de dictionary it will write it
    # and then capitalize it and give it a bold attribute
    worksheet.write(row, column, key.capitalize(), bold)
    for item in content[key]:
        row += 1
        worksheet.write(row, column, item)
    column += 1
    row = 0

workbook.close()
