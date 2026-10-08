import math

def softmax(scores: list[float]) -> list[float]:
    sum = 0
    out =[]
    maxx = max(scores)
    for i in range(len(scores)):
        sum += math.exp(scores[i] - maxx)
    for i in range(len(scores)):
        out.append(math.exp(scores[i]-maxx)/sum)
    return out
    pass