from prettytable import PrettyTable

x = PrettyTable()
x.field_names = ["Name", "Type"]
x.add_row(["Quilladin", "Grass"])
x.add_row(["Fennekin", "Fire"])
x.add_row(["Zigzagoon", "Normal"])
x.add_row(["Fletchinder", "Flying"])

print(x)