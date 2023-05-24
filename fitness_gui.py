import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Create a Tkinter window
root = tk.Tk()clo
root.title("Heatmap Application")
root.geometry("500x400")

# Execute a Bash file on start
import subprocess

# subprocess.run("./your_bash_script.sh", shell=True)
# Replace "your_bash_script.sh" with the actual path and name of your Bash script

# Generate random data for the heatmap
data = np.random.random((10, 10))

fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)


# Create a heatmap using Seaborn
# hm = plt.imshow(
#     data,
#     cmap="hot",
# )

sns.heatmap(data, cmap="hot", annot=True, fmt=".2f", cbar=True, ax=ax)

# Create a Matplotlib figure and embed it in the Tkinter window
# fig = Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

# Run the Tkinter event loop
root.mainloop()
