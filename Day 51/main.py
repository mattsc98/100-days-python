from internet_speed_x_bot import InternetSpeedTwitterBot


PROMISED_UP = 10
PROMISED_DOWN = 150
CHROME_DRIVER_PATH = r'C:\Users\matthew.schembri\OneDrive - Gain Changer\Documents\Automation\chromedriver-win64\chromedriver-win64\chromedriver.exe'
X_EMAIL = 'mattsc298@gmail.com'
X_PASS = 'MarkRussoMyLove69!'

internet_speed_x_bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)

internet_speed_x_bot.get_internet_speed()
internet_speed_x_bot.tweet_at_provider(X_EMAIL, X_PASS)

