n = int(input("몇 번째 쌍둥이소수를 찾을까요?"))

k = 2 #소수 2
twins = 0

while True:
    cnt = 0
    flag = 0

    for i in range(1, k+1):
        if k%i == 0:
            cnt += 1
    if cnt == 2:
        flag += 1
    
    cnt = 0
    
    for i in range(1, k+3):
        if (k+2)%i == 0:
            cnt += 1
    if cnt == 2:
        flag += 1

    if flag == 2:
        twins += 1
    
    if twins == n:
        print(k, k+2)
        break
    
    k += 1
