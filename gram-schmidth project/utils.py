import numpy as np

def gram_schmidt(vectors):
    n = len(vectors)
    ortho = []

    for i in range(n):
        v = vectors[i]
        for j in range(i):
            proj = np.dot(v, ortho[j]) * ortho[j]
            v = v - proj
        v_norm = np.linalg.norm(v)
        if v_norm == 0:
            raise ValueError("Vectors are linearly dependent.")
        ortho.append(v / v_norm)

    return np.array(ortho)
