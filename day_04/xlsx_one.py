from day_04 import xlsx_pratice
import allure
import pytest

pratice_xlsx = xlsx_pratice.pratice_xlsx('jbk.xlsx')
ids = []
for i in range(len(pratice_xlsx)):
    xlsx_pop= pratice_xlsx[i].pop()
    ids.append(xlsx_pop)

