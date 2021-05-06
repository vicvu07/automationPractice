import unittest
import os
from HtmlTestRunner import HTMLTestRunner
import sys

# Locate the Roor directory of project
PRV1_DIR = os.path.dirname(os.path.abspath(__file__))  # cd testSuites
PRV2_DIR = os.path.dirname(os.path.abspath(PRV1_DIR))  # cd testCases
ROOT_DIR = os.path.dirname(os.path.abspath(PRV2_DIR))  # cd automationPractice
sys.path.append(ROOT_DIR)
createAccountTest_DIR = 'testCases.package.test_CreateAccount.TestCreateAccount'
home_page_DIR = 'testCases.package.test_homePage.TestHomePage'
contactUs_DIR = 'testCases.package.test_ContactUs.TestContactUs'
order_DIR = 'testCases.package.test_Order.TestOrder'
productDetail_DIR = 'testCases.package.test_productDetail.TestProductDetail'

# Locate testcase

# Tạo account/	Lỗi khi nhập 1 email adress không hợp lệ
tc1 = f'{createAccountTest_DIR}.test_CreateAccount_Error'

# Tạo account/	Tạo thành công 1 account
tc2 = f'{createAccountTest_DIR}.test_CreateAccount_Successfull'

# Newsletter/	Submit a newsletter
tc3 = f'{home_page_DIR}.test_NewsletterSubmit'

# Contact Us/	Submit a contact form
tc4 = f'{contactUs_DIR}.test_ContactUs'

# Search	/Kiểm tra khi gõ từ khóa vào ô tìm kiếm "Search"
tc5 = f'{home_page_DIR}.test_TypeSearchKeyWord'

# Search/	Kiểm tra việc hỗ trợ tự động hoàn thiện từ khóa
tc6a = f'{home_page_DIR}.test_SuggestKeyWord'

# Search /Kiểm tra sau khi lựa chọn từ khóa gợi ý
tc6b = f'{home_page_DIR}.test_SuitableProductDetail'

# /Kiểm tra hiển thị số lượng sản phẩm tìm kiếm thành công
tc6c = f'{home_page_DIR}.test_ProductQuantity'

# /Kiểm tra xem việc tìm kiếm có cung cấp thông tin về giá cả của mặt hàng
tc6d = f'{home_page_DIR}.test_ProductPrice'

# /Search	Kiểm tra hiển thị của kết quả tìm kiếm sau khi nhập sai tên sản phẩm
tc7 = f'{home_page_DIR}.test_Search_fail'

# /Mua hàng	Mua thành công
tc8 = f'{order_DIR}.test_order_successfully'

# /Mua hàng	Thay đổi thông tin mua hàng
tc9 = f'{order_DIR}.test_change_and_order_successfully'

# /Mua hàng	Mua đồ khuyến mại
tc10 = f'{order_DIR}.test_promotion_product'

# /Chi tiết sản phẩm
tc11 = f'{productDetail_DIR}.test_view_large_product_image'

# /Chi tiết sản phẩm	Share to Twitter
tc12 = f'{productDetail_DIR}.test_share_to_twitter'

# /Chi tiết sản phẩm	Write a comment
tc13 = f'{productDetail_DIR}.test_write_a_comment'

# /Chi tiết sản phẩm	Send to friend
tc14 = f'{productDetail_DIR}.test_send_to_a_friend'

allTCs = unittest.TestLoader().loadTestsFromNames([tc1, tc2, tc3, tc4, tc5, tc6a, tc6b
                                                      , tc6d, tc7, tc8, tc9, tc10, tc11, tc12, tc13, tc14])
TestCases = unittest.TestSuite(allTCs)
runner = HTMLTestRunner(output=ROOT_DIR + '/reports', combine_reports=True, report_name="Automation_Report",
                        report_title='Testing Website Result')

runner.run(TestCases)