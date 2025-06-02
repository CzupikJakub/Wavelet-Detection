import cv2
import pywt
import matplotlib.pyplot as plt

image_path = r"C:\Users\Asus\Documents\GitHub\Wavelet-Detection\python\data\0000.png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print(f"Błąd: Nie można wczytać pliku z ścieżki: {image_path}")
else:
    # Transformacja falkowa (Haar) - 2 poziomy
    coeffs = pywt.wavedec2(image, 'haar', level=2)

    cA2, (cH2, cV2, cD2), (cH1, cV1, cD1) = coeffs
    # cA2 - aproksymacja poziom 2
    # cH2, cV2, cD2 - detale poziom 2
    # cH1, cV1, cD1 - detale poziom 1

    # Wizualizacja
    plt.figure(figsize=(12, 8))

    plt.subplot(241), plt.imshow(image, cmap='gray'), plt.title('Oryginalny')
    plt.subplot(242), plt.imshow(cA2, cmap='gray'), plt.title('Aproksymacja L2')
    plt.subplot(243), plt.imshow(cH2, cmap='jet'), plt.title('Detale poziome L2')
    plt.subplot(244), plt.imshow(cV2, cmap='jet'), plt.title('Detale pionowe L2')
    plt.subplot(245), plt.imshow(cD2, cmap='jet'), plt.title('Detale przekątne L2')
    plt.subplot(246), plt.imshow(cH1, cmap='jet'), plt.title('Detale poziome L1')
    plt.subplot(247), plt.imshow(cV1, cmap='jet'), plt.title('Detale pionowe L1')
    plt.subplot(248), plt.imshow(cD1, cmap='jet'), plt.title('Detale przekątne L1')

    plt.tight_layout()
    plt.show()