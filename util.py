def train_test_split_evtNo(*args, **kwargs):
    """ Function that splits args into train-test based on eventNo"""
    from sklearn.utils import shuffle
    if "n" in kwargs:
        n = kwargs["n"]
    else:
        n = 3
    if "evtNo" in kwargs:
        evtNo = kwargs["evtNo"]
    else:
        print ("evtNo keyword argument not given!")
        return 0
                

    testEvents = (evtNo%n == 1)
    output =  [[arg[~testEvents], arg[testEvents]] for arg in args]
    output = [item for sublist in output for item in sublist] # idiomatic way to flatten list of lists
    return output