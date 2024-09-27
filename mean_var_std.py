import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("A lista deve conter 9 números para realizar o cálculo da matrix 3x3")
    matrix = np.array(list).reshape(3, 3)
    calculations = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().item()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().item()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().item()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().item()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().item()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().item()]
    }

    return calculations

def showResult(result):
    for key, value in result.items():
        print(f"{key}: {value}")

# Example usage
resultado = calculate([0, 1, 2, 3, 4, 5, 6, 7, 3])
showResult(resultado)