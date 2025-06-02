#include <opencv2/opencv.hpp>
#include <iostream>

void loadAndShowImage() {
    cv::Mat image = cv::imread("C:\\Users\\Asus\\Documents\\GitHub\\Wavelet-Detection\\data\\vehicles\\0000.png");
    if (image.empty()) {
        std::cerr << "B³¹d: Nie znaleziono pliku!" << std::endl;
        return;
    }

    // Przetwarzanie wstêpne
    cv::Mat gray;
    cv::cvtColor(image, gray, cv::COLOR_BGR2GRAY);
    cv::resize(gray, gray, cv::Size(640, 480));

    // Wyœwietl wynik
    cv::imshow("Oryginalny obraz", image);
    cv::imshow("Przetworzony obraz (szary)", gray);
    cv::waitKey(0);
}

int main() {
    loadAndShowImage();
    return 0;
}