from collections import Counter

#Pair up the smallest number in the left list with the 
#smallest number in the right list, then the second-smallest left 
#number with the second-smallest right number, and so on.

def compare_lists(puzzleinput):
    if not puzzleinput:
        raise ValueError("input list is empty or invalid")
    result = []
    #sort both lists 
    list1 ,list2 = zip(*puzzleinput)
    list1, list2 = list(list1), list(list2)
    
    list1.sort()
    list2.sort()
    # pair the lists and subtract 
    for (left, right) in zip(list1, list2):
        distace = abs(left - right)
        result.append(distace)
        #print(f"{left} - {right} = {distace}") #OPTINAL check 
    return result
#eaxmple usage        
FILENMAE = "data.txt"
split_data =  []
with open(FILENMAE , 'r') as file:
    reader =  file.readlines()
    for row in reader:
        row = row.strip().split()
        if len(row) == 2:
            try:
                split_data.append([int(x) for x in row])
            except ValueError as e:
                print(f"skipping row {row} due to error {e}")
        else:
            print(f"skipping {row} due to incorrect number of values")
#Calculate a total similarity score by adding up each number in the left list 
#after multiplying it by the number of times that number appears in the right list.    
def calculate_similarity_score(list1, list2):
    count_right = Counter(list2)
    sim_score=  0
    for num in list1:
        sim_score += num *count_right[num]
    return sim_score
        
if split_data:
    result = compare_lists(split_data)
    #print("result", result)
    total_sum = sum(result)
    print("Sum of all elements in result:", total_sum)
    
    # Calculate the similarity score
    list1, list2 = zip(*split_data)
    list1, list2 = list(list1), list(list2)
    similarity_score = calculate_similarity_score(list1, list2)
    print("Similarity score:", similarity_score)
else:
    print("No valid data to process")