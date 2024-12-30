import time

start = time.time()

total = 0
for i in range(1, 10001):
    for j in range(1, 10001):
        total = i + j

print(f"The total is {total}")
end = time.time()
print(f"It takes {end-start:.2f} seconds to compute the total.")
