"""Exercise 02: while, break and continue."""

remaining = 5

# TODO: count down to 1 and update remaining on every pass.
import time

remaining = 5

print("Bắt đầu đếm ngược...")
while remaining >= 1:
    print(f"Còn lại: {remaining}")
    
    remaining -= 1
    
    time.sleep(1)

print("Hết giờ!")

# TODO: loop through 1..10, skip multiples of 3 and stop after 8.
for i in range(1, 11):
    if i > 8:
        break
        
    if i % 3 == 0:
        continue
        
    print(i)
print(remaining)
