from xlrd import open_workbook

#from openpyxl import load_workbook#, get_highest_row, get_highest_column, letter_to_index

def xl2ls(max_row):
	book = open_workbook("merge.xlsx")
	sheet = book.sheet_by_index(0) #If your data is on sheet 1
	
	q = []
	ans = []
	qlen=0
	qslen=0
	
	for row in range(1, max_row): #start from 1, to leave out row 0, put max_row as 230
	    q.append((str(sheet.cell(row, 0))[6:], str(sheet.cell(row, 1))[6:])) #extract from first col
		
	return q

print(xl2ls(231))
print(xl2ls(231))
print(len(xl2ls(231)))
print(len(xl2ls(231)))
#print("{}, {}".format(len(xl2ls(230)[0]), len(xl2ls(230)[1])))