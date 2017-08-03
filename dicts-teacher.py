def num_teachers(dict):
    return len(dict.keys())

def num_courses(dict):
	count = 0
	
	
	for length in list(dict.values()):

		count += len(list(dict.values())[list(dict.values()).index(length)]) 
	
	

	return count

def most_courses(dict):
    max_count = 0
    for i in dict:
        
        if len(dict[i]) > max_count:
            max_count = len(dict[i])
            winner = i
    print(winner)
    print("Test")

def stats(dict):
	stats_list = []
	for i in dict:
		stats_list += [[i, len(dict[i]) ]]
	print("Terst")
	print(stats_list)
	return [stats_list]

stats({'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'], 'Kenneth Love': ['Python Basics', 'Python Collections']})