data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]
output_data = []

filter_data = []

for item in data:
    parts = item.split()
    nilai_filter = list(filter(str.isdigit, parts))
    filter_data.append(nilai_filter)

for values in filter_data:
    print(values)

