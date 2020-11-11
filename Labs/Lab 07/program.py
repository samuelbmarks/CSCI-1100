items = [chr(i) for i in range(0x30a1, 0x30ff + 1)]
for i in range(1,11):
    items.append(str(i))
import time,random
for i in range(1000):
    s = ''
    random.shuffle(items)
    for j in range(30):
        ri = random.randrange(len(items))
        s += items[j]
    print(s)
    time.sleep(0.1)
