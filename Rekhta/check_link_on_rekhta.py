import pandas as pd
import xlwings as xw

if __name__ == "__main__":
    excel_file = "Ghazals.xlsx"
    wb = xw.Book(excel_file)
    ws = wb.sheets['Sheet1']
    ws2 = wb.sheets['Sheet2']
    rows = max(2, ws.range('B' + str(ws.cells.last_cell.row)).end('up').row, ws.range('A' + str(ws.cells.last_cell.row)).end('up').row)
    rows2 = max(2, ws2.range('B' + str(ws2.cells.last_cell.row)).end('up').row, ws2.range('A' + str(ws2.cells.last_cell.row)).end('up').row)
    youtube_list = ws[f"B2:B{rows}"].value
    rekhta_list = ws2[f"B2:B{rows2}"].value
    for i in range(0, len(youtube_list)):
        if "youtube" in youtube_list[i]:
            link = youtube_list[i].split("?v=")
            link = "https://youtube.com/watch?v=" + link[1]
            if link in rekhta_list:
                ws[f"B{i + 2}"].color = (43, 196, 64)