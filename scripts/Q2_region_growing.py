
import cv2
import numpy as np
import matplotlib.pyplot as plt
from collections import deque

mean = 0
std_dev = 15
img = np.zeros((100, 100), dtype=np.uint8)
img[20:40, 20:40] = 85   
img[60:80, 60:80] = 170

def region_growing(img, seeds, threshold=15):
    height, width = img.shape
    segmented = np.zeros((height,width), dtype=np.uint8)
    visited = np.zeros((height,width), dtype=bool)
    for seed in seeds:
        queue = deque([seed])
        seed_value = img[seed]
        while queue:
            x, y = queue.popleft()
            if visited[x, y]:
                continue
            visited[x, y] = True
            pixel_value = img[x, y]
            if abs(int(pixel_value) - int(seed_value)) < threshold:
                segmented[x, y] = 255
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < height and 0 <= ny < width and not visited[nx, ny]:
                            queue.append((nx, ny))
    return segmented

seeds = [(25, 25), (65, 65)]

region_result = region_growing(img, seeds, threshold=20)

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.title("Noisy Image")
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.title("Region Growing Result")
plt.imshow(region_result, cmap='gray')
plt.axis('off')
plt.tight_layout()
plt.show()