def main():
    avg_1 = average(2, 20)
    avg_2 = average(4, 11)
    print(avg_1)
    print(avg_2)
    
    final = average(avg_1, avg_2)
    print("avg_1", avg_1)
    print("avg_2", avg_2)
    print("final", final)
    
    
    """
    returns the number which is half way between a and b
    """
def average(a, b):
    sum = a + b
    return sum / 2
