import xlrd
def read_xlsx(file):
    l = []
    wb =xlrd.open_workbook(filename=file)
    sheet1 = wb.sheet_by_index(0)
    for i in range (1,sheet1.nrows):
        d = []
        d = sheet1.row_values(i)
        l.append(d)
    return l


if __name__ == '__main__':
    pratice_xlsx = read_xlsx('jbk.xlsx')
    print(pratice_xlsx)
