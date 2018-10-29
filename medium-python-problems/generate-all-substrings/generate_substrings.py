
def generate_substrings(string):
    '''Generate all unique substrings from a string'''
    results = set()
    # create 2 indices that move and return difference slices of the string
    # set first index: max length of the string (can alter for length of substring desired)
    for substring in range(0, len(string) + 1):
        # set second index 
        for index in range(len(string)+ 1 - substring): 
            # slice using indices to generate substring
            results.add(string[index : index + substring])
    return results

print(generate_substrings('hello'))
