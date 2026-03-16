import os

filename = "data.txt"

if os.path.exists(filename):
    print("File already exists.")
else:
    print("Nah sorry, file not found. Creating it now...")
    with open(filename, "w") as file:
        file.write("File created successfully.\n")
    print("File created.")