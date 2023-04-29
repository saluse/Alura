import openpyxl

#Crinado uma planilha
book = openpyxl.Workbook()
# Como visualizar páginas existentes
print(book.sheetnames)
# Como criar uma página
book.create_sheet('Frutas')
#Como selecionar uma páginas 
frutas_page = book['Frutas']
