import numpy as np 

# implement your function to combine two numpy arrays 

def combination(np_arr1, np_arr2, axis=0):
    arr1 = np_arr1.squeeze()
    arr2 = np_arr2.squeeze()

    try:
        combined_arr = np.concatenate((arr1, arr2), axis)
        return combined_arr
    except ValueError:
        print("The two given arrays cannot be combined along the given axis")
    
    



if __name__ == "__main__":
    # use this for your own testing!
    array1 = np.array([[[1, 2, 3]]])
    array2 = np.ones(shape=(3, 2))
    comb_arr = combination(array1, array2)
    pass
