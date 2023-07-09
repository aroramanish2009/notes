###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    #Open file in read only as sample_file
    with open(filename, 'r') as sample_file:
        #Read lines into List called data_lines with items split at newline
        data_lines=sample_file.read().splitlines()
    #Initialize an empty dict
    mydict = {}
    #Iterate over data_lines
    for item in data_lines:
        #Split item on comma and assign left half to key and right half to value
        k = item.split(',')[0]
        v = item.split(',')[1]
        #Append key/value pair to dictionary
        mydict[k] = v
    #Return mydict 
    return mydict

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    {'Betsy': '9', 'Henrietta': '9', 'Herman': '7', 'Oreo': '6', 'Millie': '5', 'Maggie': '3', 'Moo Moo': '3', 'Milkshake': '2', 'Lola': '2', 'Florence': '2'}
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    #Sort cows dict based on the value in reverse order i.e. high value first.
    sorted_cows = {k: v for k, v in sorted(cows.items(), key=lambda item: item[1], reverse=True)}
    full_trips = []
    each_trip = []
    weight_per_trip = 0
    #create a copy of sorted dict
    copy_sorted_cows = sorted_cows.copy()
    #Loop until elements in copy_sorted_cows dict, this is done as making changes dict with loop is not permitted
    while len(copy_sorted_cows) > 0:
        #Loop over original sorted list
        for cow, weight in sorted_cows.items():
            #If item is still in copy_sorted_cows and weight is less than equal to 10 
            if cow in copy_sorted_cows and weight_per_trip + int(weight) <= 10:
                #apped item to trip and increase wait
                each_trip.append(cow)
                weight_per_trip = weight_per_trip + int(weight)
                #delete that item from copy_sorted_cows
                del copy_sorted_cows[cow]
            elif cow in copy_sorted_cows and weight_per_trip + int(weight) > 10:
                pass
        full_trips.append(each_trip)
        weight_per_trip = 0
        each_trip = []
                
    return full_trips

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    [['Moo Moo', 'Henrietta', 'Millie'], ['Betsy', 'Oreo', 'Milkshake', 'Herman'], ['Florence'], ['Maggie', 'Lola']]
    [['Moo Moo', 'Henrietta', 'Millie'], ['Betsy', 'Oreo', 'Milkshake', 'Herman'], ['Florence'], ['Lola'], ['Maggie']]
    [['Moo Moo', 'Henrietta', 'Millie'], ['Lola', 'Maggie', 'Betsy', 'Oreo', 'Milkshake'], ['Florence', 'Herman']]
    """
    cows_dict = cows.copy()
    cows_weight_list = [ k for k,v in cows_dict.items() ]
    optimal_answer = []
    shortest_trip = 100
    for partition in get_partitions(cows_weight_list):
        num_trips = len(partition)
        if num_trips < shortest_trip:
            limitation = True
            for part in partition:
                sum_part = 0
                for pa in part:
                    sum_part = sum_part + int(cows_dict[pa])
                if sum_part > 10:
                    limitation = False
                    break
            if limitation == True:
                shortest_trip = num_trips
                optimal_answer = partition
    return (optimal_answer)
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    start_time = time.time()
    greedy_algo = greedy_cow_transport(load_cows("ps1_cow_data.txt"))
    stop_time = time.time()
    time_delta = stop_time - start_time
    print ("Time to process Greedy Algo:", time_delta , greedy_algo)
    newstart_time = time.time()
    brute_algo = brute_force_cow_transport(load_cows("ps1_cow_data.txt"))
    newstop_time = time.time()
    newtime_delta = newstop_time - newstart_time
    print ("Time to process Brute Force Algo:", newtime_delta, brute_algo)

    
compare_cow_transport_algorithms()
