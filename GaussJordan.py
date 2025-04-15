import numpy as np

def gauss_jordan():
    
    print("Enter the coefisien and constant values:")
    A = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(float(input(f"Enter the coefisien a{i+1}{j+1}: ")))
        const = float(input(f"Enter the constant b{i+1}: "))
        row.append(const)
        A.append(row)
    
    A = np.array(A, dtype=float)

    n = len(A)
    
    for i in range(n):
        if A[i][i] == 0.0:
            print("Invalid! (Can't divided by 0)")
            return
        
        for j in range(n):
            if i != j:
                ratio = A[j][i] / A[i][i]
                for k in range(n + 1):
                    A[j][k] = A[j][k] - ratio * A[i][k]
    
    solution = [0] * n
    for i in range(n):
        solution[i] = round(A[i][n] / A[i][i], 8) 
    
    print("\nThe solution is:")
    for i, sol in enumerate(solution):
        print(f"Variable {chr(120 + i)} = {sol}")

gauss_jordan()
