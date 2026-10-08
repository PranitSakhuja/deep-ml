import numpy as np

def log_softmax(scores: list) -> np.ndarray:
    out = []
    maxx = max(scores)
    total = sum(np.exp(s - maxx) for s in scores)   # computed once

    for i in range(len(scores)):
        out.append(scores[i] - maxx - np.log(total))
    return np.array(out)