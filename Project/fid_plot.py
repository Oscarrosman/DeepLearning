import matplotlib.pyplot as plt
import numpy as np

hours = np.arange(0, 25, 1)  # Time in hours
fid_horse = [133, 110, 92, 67, 58, 50, 42, 39, 37, 36, 30, 28, 27, 26, 26, 25, 20.6, 20.1, 21.6, 20.6, 19.1, 18.6, 19.1, 20.9, 18.3]
fid_elephant = [450, 88.8, 69.9, 59.1, 54.1, 50.2, 47.4, 45.4, 39.7, 40.8, 36.9, 36.0, 34.9, 33.9, 34.2, 32.5, 33.9, 31.3, 30.6, 32.6, 31.8, 33.7, 31.4, 30.1, 32.3]

plt.figure(figsize=(8, 6))

# Plot each animal FID curve
plt.plot(hours, fid_horse, label='Horse', color='green', linewidth=2)
plt.plot(hours, fid_elephant, label='Elephant', color='blue', linewidth=2)

plt.xlabel('Hours', fontsize=12)
plt.ylabel('FID', fontsize=12)
#plt.title('FID Scores over Time for 32x32 Horse & Elephant', fontsize=14)

plt.xlim([0, 24])
plt.yticks([15, 20, 25, 30, 35, 40, 50, 75, 100])
plt.ylim([10, 100])
plt.legend()
plt.grid(True)

plt.show()
