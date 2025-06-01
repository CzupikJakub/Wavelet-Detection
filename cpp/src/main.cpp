#include <opencv2/opencv.hpp>
#include <iostream>

int main() {
    std::cout << "DZIALA! Teraz dodajmy OpenCV...\n";
    cv::Mat test_image = cv::Mat::zeros(300, 300, CV_8UC3);
    cv::circle(test_image, cv::Point(150, 150), 100, cv::Scalar(0, 0, 255), 5);
    cv::imshow("Test", test_image);
    cv::waitKey(0);
    return 0;
}