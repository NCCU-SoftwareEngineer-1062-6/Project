軟工專案設定筆記
===
## 新設定步驟
1. 使用windows cmd 切換至工作資料夾上層目錄
2. `git clone https://github.com/NCCU-SoftwareEngineer-1062-6/Project.git`
3. `cd Project\` 切換進入工作根目錄
2. `virtualenv .env` 設立virtulenv
3. `.env\Scripts\activate.bat` 啟動 virtualenv
4. 確認成功啟動venv後，於cmd中鍵入 `pip install -r requirements.txt`
5. 進入次資料夾`cd nccu_course_query`, run `python manage.py migrate` 建立local database
6. run `python manage.py createsuperuser --username=joe --email=joe@example.com` 建立管理員帳號
7. run `python manage.py runserver` 啟動測試伺服器
10. I have configed all recommend VScode extension，just install all recommend extension

## 環境說明
1. 已經設定好gitignore
2. ~~有windos的自動化環境設定~~ 有問題 待fix

### superuser
`python manage.py createsuperuser --username=joe --email=joe@example.com`
### 注意事項

1. 資料夾路徑中不要有中文字元


### Install Package
- django
- pylint
- pylint-django
- autopep8

## 參考連結
https://www.jianshu.com/p/46df032e9ade

### 學習資源
- http://djangobook.py3k.cn/2.0/
- http://dokelung-blog.logdown.com/posts/235592-django-notes-table-of-contents
- https://docs.djangoproject.com/zh-hans/2.0/
- https://github.com/haiiiiiyun/awesome-django-cn
- https://developer.mozilla.org/zh-CN/docs/Learn/Server-side/Django

## 開發筆記

### Model diagram

![](https://i.imgur.com/TwA6jvj.png)

#### 資料庫匯入順序

1. Teacher,Time,Department
2. Course