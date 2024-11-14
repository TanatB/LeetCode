# Prefix Sum Questions
def largestAltitude(gain: list[int]) -> int:
    total = 0
    alt = [0]
    
    for i in range(len(gain)):
        total += gain[i]
        alt.append(total)
        
    return max(alt)


if __name__ == '__main__':
    gain = [-4,-3,-2,-1,4,3,2]
    print(largestAltitude(gain))