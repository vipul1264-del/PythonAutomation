import openpyxl
from openpyxl import load_workbook, workbook

wb = load_workbook("path of xlsl file")

sheet = wb("sheet1")

user_id = sheet['G10'].value
password = sheet['G11'].value

