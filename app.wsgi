import sys
import site


site.addsitedir('/var/www/log_filter/venv/lib/python3.13/site-packages')
# 注意：上面的 python3.10 請根據您的系統版本確認 (ls /var/www/log_filter/venv/lib/ 查看是 3.x)

sys.path.insert(0, '/var/www/log_filter')

# 假設您的主程式檔名是 myapp.py，且裡面的實例變數叫 app
from myapp import app as application
