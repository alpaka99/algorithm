input_data = "SSADADAAASADAAAS"

N = int(input("어떻게 끊을지 입력해주세요"))
max_char = ""
max_num = 0
for i in range(len(input_data)-N):
    cnt = [0 for _ in range(26)]
    sample_data = input_data[i:i+N]
    for j in range(len(sample_data)):
        cnt[ord(sample_data[j])-ord("A")] += 1


    tmp_max = max(cnt)
    if max_num < tmp_max:
        for j in range(len(cnt)):
            if cnt[j] == tmp_max:
                max_char = chr(ord('A')+j)
                max_num = tmp_max
                break
print(max_char, max_num)
