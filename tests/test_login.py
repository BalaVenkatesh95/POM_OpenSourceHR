from pages.login_page import LoginPage

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

loginpage = LoginPage(url)
file_path = "C:\\workspace\\orangeHR_TDD_POM\\resources\\login_details.xlsx"
sheet_name = "login"

def test_login():
    loginpage.login_user(file_path, sheet_name)


def test_shutdown():
    loginpage.shutdown()
