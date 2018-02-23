#python 3.6      
#蔡军生       
#http://blog.csdn.net/caimouse/article/details/51749579      
#

SITE_NAME = '论坛'
AUTHOR = 'caijunsheng'

GLOBAL_PARAMS = {'site_name': SITE_NAME, 'title': SITE_NAME, 'author': AUTHOR}

##### 公共配置 #####
COOKIE_EXPIRES = 3600 # 单位s
IMG_DIR = '/static/img'
POSTS_PER_PAGE = 10 # 每页显示10篇文章

# 本地环境下的MySQL配置
DBN = 'mysql'
HOST = '127.0.0.1'
PORT = 3308
DRIVER = 'mysql.connector'
DB = 'forum'
MYSQL_USERNAME = 'root'
MYSQL_PASSWORD = '12345678'

##### email服务器配置 #####
import web
web.config.smtp_server = 'smtp.gmail.com'
web.config.smtp_port = 587
web.config.smtp_username = 'your_gmail_address'
web.config.smtp_password = 'your_gmail_password'
web.config.smtp_starttls = True

##### 调试模式 #####
web.config.debug = False
