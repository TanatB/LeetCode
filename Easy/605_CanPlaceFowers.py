def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    e_flowerbed = [0] + flowerbed + [0]
    
    for i in range(1, len(e_flowerbed) - 1):
        if e_flowerbed[i - 1] == 0 and e_flowerbed[i] == 0 and e_flowerbed[i + 1] == 0:
            e_flowerbed[i] = 1
            n -= 1
    return n <= 0
    
        

if __name__ == '__main__':
    print(canPlaceFlowers([1,0,0,0,0,1], 2))