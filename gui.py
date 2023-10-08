import tkinter as tk

# Chatgpt is cool


def on_entry_change(row, col, var):
    value = var.get()[:1]  # Limit the input to a single character
    if not value.isdigit():
        value = ""  # Clear the input if it's not a digit
    var.set(value)
    grid_values[row][col] = int(value) if value else 0  # Store the value in the grid or set it to 0 if empty
    # print(f"Value at row {row}, column {col}: {grid_values[row][col]}")

def on_done_button():
    root.destroy()  # Close the GUI window

# Create the main window
root = tk.Tk()
root.title("Input Grid")

# Create a 9x9 grid of entry widgets
entry_grid = []
grid_values = [[0 for _ in range(9)] for _ in range(9)]  # Initialize the 2D array
for row in range(9):
    row_entries = []
    for col in range(9):
        entry_var = tk.StringVar()  # Variable to store the input
        entry_var.trace_add("write", lambda *args, r=row, c=col, v=entry_var: on_entry_change(r, c, v))
        entry = tk.Entry(root, textvariable=entry_var, width=5)  # Adjust width as needed
        entry.grid(row=row, column=col, padx=2, pady=2)
        row_entries.append(entry)
    entry_grid.append(row_entries)

# Create a button to finalize input
done_button = tk.Button(root, text="Done", command=on_done_button)
done_button.grid(row=9, column=0, columnspan=9, pady=10)

# Start the tkinter event loop
root.mainloop()

# Print the 2D array after the GUI is closed
#print("Grid values:")
for row in grid_values:
    print(row)
#print(grid_values)
def getBoard():
    return grid_values
getBoard()
