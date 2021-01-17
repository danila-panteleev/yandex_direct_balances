import gspread

gc = gspread.oauth()

sh = gc.open("Задачи")

worksheet = sh.worksheet("Балансы G")

print(worksheet.get(''))