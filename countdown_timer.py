import time
t = int(input("Enter the time in seconds: "))
for x in range(t, 0, -1):
    sec = x % 60
    min = int(x/60)%60
    hr = int(x/3600)
    print(f"{hr:02d}:{min:02d}:{sec:02d}")
    time.sleep(1)

print("Time's up!")