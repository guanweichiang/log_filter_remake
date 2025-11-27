import sys
import site


# 1. 指向我們剛剛建立的虛擬環境 site-packages
site.addsitedir('/var/www/log_filter/venv/lib/python3.13/site-packages')
# 注意：上面的 python3.10 請根據您的系統版本確認 (ls /var/www/log_filter/venv/lib/ 查看是 3.x)

# 2. 將專案目錄加入系統路徑
sys.path.insert(0, '/var/www/log_filter')

# 3. 匯入 Flask app
# 假設您的主程式檔名是 myapp.py，且裡面的實例變數叫 app
from myapp import app as application
