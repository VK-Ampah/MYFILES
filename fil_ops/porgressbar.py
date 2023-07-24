import time
from tqdm import tqdm

print()
print()
print("Saving data - please wait")
# Processing bar
for _ in tqdm(range(20), desc="Processing", unit="ticks", ncols=100, bar_format="{desc}  {bar}"):
    time.sleep(.1)
print("Data successfully saved ...")
time.sleep(1)