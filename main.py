def find_longest_sequence(numbers):
    print("The longest sequence search started...")
    
    start_ends = {}
    
    for num in numbers:
        start_two = num[:2]
        if start_two not in start_ends:
            start_ends[start_two] = []
        start_ends[start_two].append(num)
    
    print(f"Unique starts: {len(start_ends)}")
    
    def find_longest_chain(current, used):
        best_chain = [current]
        
        next_start = current[-2:]
        
        for candidate in start_ends.get(next_start, []):
            if candidate not in used:
                new_used = used.copy()
                new_used.add(candidate)
                
                chain = [current] + find_longest_chain(candidate, new_used)
                
                if len(chain) > len(best_chain):
                    best_chain = chain
        
        return best_chain

    longest_sequence = []
    print("The longest chain search...")
    
    for start_num in numbers:
        sequence = find_longest_chain(start_num, {start_num})
        print(f"Current chain from {start_num}: {len(sequence)} numbers")
        
        if len(sequence) > len(longest_sequence):
            longest_sequence = sequence

    return longest_sequence

def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip().zfill(6) for line in file]

print("Reading numbers from file...")
numbers = read_numbers_from_file('text.txt')

print("The longest sequence search starts...")
result = find_longest_sequence(numbers)

print(f"\nThe longest sequence ({len(result)} numbers):")
print(result)

print("\nSequence check:")
for i in range(len(result)-1):
    current = result[i]
    next_num = result[i+1]
    is_valid = current[-2:] == next_num[:2]
    print(f"{current} -> {next_num} (Correct transition: {is_valid})")
    
