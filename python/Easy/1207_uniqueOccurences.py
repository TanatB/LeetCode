def uniqueOccurrences(arr: list[int]) -> bool:
    unique_count = {a : 0 for a in set(arr)}
    
    for element in arr:
        unique_count[element] += 1
        
    return len(set(unique_count.values())) == len(list(unique_count.values()))
            


if __name__ == '__main__':
    print("1207 Test.")
    
    arr = [1,2,2,1,1,3]
    print(uniqueOccurrences(arr))