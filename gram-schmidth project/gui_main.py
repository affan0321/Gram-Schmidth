import tkinter as tk
from tkinter import messagebox
import numpy as np
from utils import gram_schmidt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class GramSchmidtApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gram-Schmidt Process")
        self.vectors = []

        self.instructions = tk.Label(root, text="Enter a vector (space-separated):")
        self.instructions.pack()

        self.entry = tk.Entry(root, width=40)
        self.entry.pack()

        self.add_button = tk.Button(root, text="Add Vector", command=self.add_vector)
        self.add_button.pack()

        self.calc_button = tk.Button(root, text="Compute Orthonormal Vectors", command=self.compute)
        self.calc_button.pack()

        self.display = tk.Text(root, height=10, width=50)
        self.display.pack()

    def add_vector(self):
        vec_text = self.entry.get()
        try:
            vector = np.array([float(x) for x in vec_text.split()])
            if self.vectors and len(vector) != len(self.vectors[0]):
                raise ValueError("All vectors must have the same dimension.")
            self.vectors.append(vector)
            self.display.insert(tk.END, f"Added: {vector}\n")
            self.entry.delete(0, tk.END)
        except:
            messagebox.showerror("Error", "Invalid vector format!")

    def compute(self):
        if not self.vectors:
            messagebox.showwarning("Warning", "No vectors entered.")
            return
        try:
            mat = np.array(self.vectors)
            ortho = gram_schmidt(mat)
            self.display.insert(tk.END, "\nOrthonormal Vectors:\n")
            for i, vec in enumerate(ortho):
                self.display.insert(tk.END, f"{i+1}: {np.round(vec, 4)}\n")
            self.plot_vectors(self.vectors, ortho)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def plot_vectors(self, original, orthonormal):
        dim = len(original[0])
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d' if dim == 3 else None)

        colors = ['r', 'g', 'b', 'c', 'm', 'y']
        for i, vec in enumerate(original):
            ax.quiver(0, 0, 0, *vec, color=colors[i % len(colors)], label=f"Original {i+1}")

        for i, vec in enumerate(orthonormal):
            ax.quiver(0, 0, 0, *vec, color=colors[i % len(colors)], linestyle='dashed', label=f"Orthonormal {i+1}")

        ax.set_xlim([-2, 2])
        ax.set_ylim([-2, 2])
        if dim == 3:
            ax.set_zlim([-2, 2])
        ax.set_title("Vector Visualization")
        ax.legend()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = GramSchmidtApp(root)
    root.mainloop()
