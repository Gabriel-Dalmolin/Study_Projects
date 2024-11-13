def get_fibbonaci_sequence(times):
    actual_value = 1
    last_value = 0
    sequence = [0, 1]
    for _ in range(times):
        last_value, actual_value = actual_value, actual_value+last_value
        sequence.append(actual_value)
    return sequence

print(" ".join(str(num) for num in get_fibbonaci_sequence(100)))
        
        