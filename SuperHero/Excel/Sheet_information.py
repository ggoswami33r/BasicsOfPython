# Sheets
# Getting the title of a sheet
sheet.title

# Setting the title of a sheet
sheet.title = 'Employees'

# Renaming the default sheet to 'Employees'
sheet = workbook['Sheet']

sheet.title = 'Employees'

# Seeing all the available sheet operations
dir(sheet)

# Getting the active cell
sheet.active_cell

# Getting the dimensions of the sheet (the array populated with data)
sheet.dimensions

# Getting basic parameters about the sheet
sheet.sheet_format

# Getting the basic properties of the sheet
sheet.sheet_properties

# Getting the sheet state (visible/hidden)
sheet.sheet_state

# Getting other general information about a sheet
sheet.sheet_view

# Getting the number of rows in the sheet
sheet.max_row

# Getting the number of columns in the sheet
sheet.max_column

# Returning the rows in a sheet as tuples
for i in sheet.values:
    print(i)


#there are two way to get calue from a cell
sheet = workbook["EmployeeData"];

sheet['B7'].value
sheet.cell(row = 6, column = 2).value

# cell cen be defined in the below as well
cell = sheet['B9']
cell.row provides row numbers
cell.column provides column numbers
cell.coordinate provides  coordinate which is B9
cell.encoding
-->'utf-8'

# to change any value we could do the below thing
cell  = sheet['B9']
cell.value = "GG"
workbook.save("F:\Python\Basic Practices\BasicsOfPython\SuperHero\Excel\Employees.xlsx")
#while doing this job need to save close the detailed xlsx if there is any present
cell.parent
<Worksheet "EmployeeData">
>>>


'''

Cell information

sheet = workbook['EmployeeData']
sheet['B10'].value
 
#or
 
sheet.cell(row = 10, column = 2).value
 
#Selecting a cell in the sheet
cell = sheet['B10']
 
#Getting the row number of the cell
cell.row
 
#Getting the column number of the cell
cell.column
 
#Getting the coordinates of a cell
cell.coordinate
 
#Getting the data type for a cell
'''
TYPE_STRING = 's'
    TYPE_FORMULA = 'f'
    TYPE_NUMERIC = 'n'
    TYPE_BOOL = 'b'
    TYPE_NULL = 'n'
    TYPE_INLINE = 'inlineStr'
    TYPE_ERROR = 'e'
    TYPE_FORMULA_CACHE_STRING = 'str'
'''
cell.data_type
 
#Getting the encoding format for a cell
cell.encoding
 
#Setting a value for a cell
cell = sheet['B10']
cell.value = 'Test'
workbook.save("D:\Employees.xlsx") #Saving the workbook
 
#Getting the parent worksheet for a cell
cell.parent
'''