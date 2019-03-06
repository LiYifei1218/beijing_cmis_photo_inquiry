import xlrd
#f = open('school_id.dat', 'w')
def get_data(filename,sheetnum):
	dir_case = "data.xlsx"
	data = xlrd.open_workbook(dir_case)
	table = data.sheets()[sheetnum]
	nor = table.nrows
	nol = table.ncols
	dict = {}
	for i in range(1,nor):
		for j in range(nol):
			title = table.cell_value(0,j)
			value = table.cell_value(i,j)
			dict[title] = value
		yield dict
 
if __name__ == '__main__':
	for i in get_data('add_user',0):
		print(i)

#with open('school_id.dat', 'r') as f:
#   f.write(dict)