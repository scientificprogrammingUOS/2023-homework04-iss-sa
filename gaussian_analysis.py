import numpy as np

# implement the function gaussian_analysis
def gaussian_analysis(loc, scale, lower_bound, upper_bound):  
    
    if isinstance(loc, (int, float)) and isinstance(scale, (int, float)) and isinstance(lower_bound, (int, float)) and isinstance(upper_bound, (int, float)) and lower_bound < upper_bound:
        # 100 samples of gaussian distribution in respect to loc and scale
        sample = np.random.normal(loc, scale, size=(100))
        
        # lower_bound, upper_bound filtered out
        sample_filtered = np.clip(sample, lower_bound, upper_bound)

        # calculate mean
        mean = np.mean(sample_filtered)
        
        #calculate std
        std = np.std(sample_filtered)

        ret_tuple = (mean, std)
        return ret_tuple
    else:
        raise Exception("You might have input an invalid argument. Only integers and floats and lower_bound < upper_bound")


if __name__ == "__main__":
    # use this for your own testing!
    tup = gaussian_analysis(0, 3, 1, 3)
    print(tup)
    pass
