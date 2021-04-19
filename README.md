# automationPractice
Training automation testing

Author : Vu Quang Hiep - HiepVQ

Project : Training Automation Test

Date : 19/04/2021
1. Chạy test từ dòng lệnh từng testsuite, & chạy tổng thể toàn bộ testcases để đưa ra báo cáo:
- Chạy unittest đối với từng testcase, và được viết theo testsuite, các testsuite được để trong thư mục: ..\automationPractice\testCases\package
- Chạy toàn bộ testcases bằng cách chạy file allTestSuites.py theo đường dẫn: ..\automationPractice\testCases\testSuites\allTestSuites.py
2. Chạy trên 2 browsers Firefox và Chrome:
Chạy bằng pytest (sử dụng parameterized) theo thao tác sau:
- B1 : Sử dụng Terminal trong Pycharm để chạy lệnh
- B2 : Chạy pytest đối với file test_productDetail_parallel bằng câu lệnh "pytest testCases/package/test_productDetail_parallel.py"
![image](https://user-images.githubusercontent.com/46483616/115174585-b3dc7a00-a0f3-11eb-8ab2-d8cf2cb17d14.png)

3. Chạy song song 2 browsers, mỗi browser 5 testcases
*Chạy 4 testcases mục 11 và 1 testcases mục 12
Chạy bằng pytest (sử dụng parameterized) theo thao tác sau:
- B1 : Sử dụng Terminal trong Pycharm để chạy lệnh
- B2 : Chạy pytest đối với file test_productDetail_parallel bằng câu lệnh "pytest -n 2 testCases/package/test_productDetail_parallel.py"
![image](https://user-images.githubusercontent.com/46483616/115174548-a45d3100-a0f3-11eb-983a-2d77c32d8fbb.png)

4. Test trên 2 máy song song sử dụng Selenium Grid
Thực hiện các thao tác như sau:
- Cài đặt JDK 8 
- Tải tập tin selenium-server-standalone-3.141.59.jar
- Chạy câu lệnh "java -jar selenium-server-standalone-3.141.59.jar -role hub" để thiết lập hub trên máy chính
![image](https://user-images.githubusercontent.com/46483616/115175336-023e4880-a0f5-11eb-9763-8c04284dcf37.png)
- Chạy câu lệnh "java -Dwebdriver.chrome.driver=C:\Drivers\chromedriver_win32\chromedriver.exe -jar selenium-server-standalone-3.141.59.jar -role node -hub http://192.168.137.1:4444/grid/register/"
![image](https://user-images.githubusercontent.com/46483616/115175760-d2dc0b80-a0f5-11eb-8842-618de5b9cb34.png)
 


