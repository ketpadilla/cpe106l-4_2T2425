import tkinter.filedialog as fd

# Open a file dialog to choose a file
target = fd.askopenfilename()

# Read and print the file if a file was selected
if target:
    with open(target, 'r') as file:
        for line in file:
            print(line, end='')