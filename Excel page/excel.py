import xlsxwriter


data = [
    {
        'names':"jefferai",
        'Contributions':"4053",
    },
    {
        'names':"vishalnayak",
        'Contributions':"1312",
    },
    {
        'names':"armon",
        'Contributions':"653",
    },
    {
        'names':"briankassouf",
        'Contributions': "621",
    },
    {
        'names':"ncabatoff",
        'Contributions': "533",
    },
    {
        'names':"mitchellh",
        'Contributions': "526",
    }
]

workbook = xlsxwriter.Workbook("AllAboutPythonExcel.xlsx")
worksheet = workbook.add_worksheet("firstsheet")

worksheet.write(0, 0, "#")
worksheet.write(0, 1, "names")
worksheet.write(0, 2, "Contributions")

for index, entry in enumerate(data):
    worksheet.write(index+1, 0, str(index))
    worksheet.write(index+1, 1, entry["names"])
    worksheet.write(index+1, 2, entry["Contributions"])
    

workbook.close()
