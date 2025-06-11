house_nums = int(input())
whoosh_between_house_s = list(map(int, input().split()))

cur_speed_s = 10**7
time_to_work = 0

for i in range(house_nums-1):
    cur_speed_s = (whoosh_between_house_s[i] if whoosh_between_house_s[i] < cur_speed_s else cur_speed_s)
    time_to_work += cur_speed_s

print(time_to_work)