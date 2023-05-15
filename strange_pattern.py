import numpy as np

# implement the function strange pattern

def strange_pattern(tuple_n_m):
    # initiate numpy array with zeros with given tuple
    np_array = np.zeros(tuple_n_m) 

    for row in range(tuple_n_m[0]):  # for row indice of array (=n)
        for col in range(tuple_n_m[1]): # for column indice of array (=m)
            # pattern rules:
            if row % 3 == 0:
                if col % 3 == 0:
                    np_array[row, col] = np_array[row, col] + 1

            elif row % 3 == 1:
                if col % 3 == 2:
                    np_array[row, col] = np_array[row, col] + 1

            elif row % 3 == 2:
                if col % 3 == 1:
                    np_array[row, col] = np_array[row, col] + 1
    
    # convert 0&1 array into boolean array
    bool_pattern_array = np.array(np_array, dtype=bool) 
    return bool_pattern_array

    


if __name__ == "__main__":
    pattern = strange_pattern((10, 10))
    print(pattern)
    pass
