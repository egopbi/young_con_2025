import heapq

worker_nums, car_nums = map(int, input().split())
events = []
price_list = [0] * worker_nums

for i in range(worker_nums):
    l, r, c = map(int, input().split())
    price_list[i] = c
    events.append((l, 1, i))
    events.append((r + 1, -1, i))

events.sort()
total_events = len(events)

top_heap = []
garbage_heap = []
loc = [0] * worker_nums
sum_top = 0
size_top = 0


def clean_top():
    while top_heap:
        c0, w0 = top_heap[0]
        if loc[w0] != 1:
            heapq.heappop(top_heap)
        else:
            break


def clean_garbage():
    while garbage_heap:
        negc0, w0 = garbage_heap[0]
        if loc[w0] != 2:
            heapq.heappop(garbage_heap)
        else:
            break


event_num = 0
current_day = events[0][0]
profit = 0

while event_num < total_events:
    day, typ, wid = events[event_num]
    if day > current_day:
        delta = day - current_day
        profit += sum_top * delta
        current_day = day

    while event_num < total_events and events[event_num][0] == day:
        _, t, idx = events[event_num]
        if t == 1:
            c = price_list[idx]
            if size_top < car_nums:
                heapq.heappush(top_heap, (c, idx))
                loc[idx] = 1
                size_top += 1
                sum_top += c
            else:
                clean_top()
                if top_heap:
                    c0, w0 = top_heap[0]
                    if c > c0:
                        heapq.heappop(top_heap)
                        sum_top -= c0
                        loc[w0] = 2
                        heapq.heappush(garbage_heap, (-c0, w0))
                        heapq.heappush(top_heap, (c, idx))
                        loc[idx] = 1
                        sum_top += c
                        event_num += 1
                        continue
                loc[idx] = 2
                heapq.heappush(garbage_heap, (-c, idx))
        else:
            if loc[idx] == 1:
                sum_top -= price_list[idx]
                size_top -= 1
                loc[idx] = 0
                while size_top < car_nums:
                    clean_garbage()
                    if not garbage_heap:
                        break
                    negc0, w0 = heapq.heappop(garbage_heap)
                    if loc[w0] != 2:
                        continue
                    c0 = -negc0
                    heapq.heappush(top_heap, (c0, w0))
                    loc[w0] = 1
                    sum_top += c0
                    size_top += 1
            elif loc[idx] == 2:
                loc[idx] = 0
        event_num += 1

print(profit)
