import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create synthetic image (2 objects + background)
image = np.zeros((200, 200), dtype=np.uint8)
image[50:100, 50:100] = 100  # Object 1
image[120:180, 120:180] = 200 # Object 2

# Add Gaussian noise
noisy_image = image + np.random.normal(0, 30, image.shape).astype(np.uint8)

# Apply Otsu's thresholding
_, otsu_thresh = cv2.threshold(noisy_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Save results
cv2.imwrite("output/noisy_image.jpg", noisy_image)
cv2.imwrite("output/otsu_thresh.jpg", otsu_thresh)

# Display all three images in one figure
plt.figure(figsize=(12, 4))

# Original Image
plt.subplot(131), plt.imshow(image, cmap='gray', vmin=0, vmax=255)
plt.title("Original Image"), plt.axis('off')

# Noisy Image
plt.subplot(132), plt.imshow(noisy_image, cmap='gray', vmin=0, vmax=255)
plt.title("Noisy Image"), plt.axis('off')

# Otsu's Thresholding
plt.subplot(133), plt.imshow(otsu_thresh, cmap='gray', vmin=0, vmax=255)
plt.title("Otsu's Thresholding"), plt.axis('off')

plt.tight_layout()
plt.show()