企查查搜索爬虫脚本

一、功能
爬取企查查指定关键词（如 “华为”“小米”）的企业搜索结果，支持自定义页数（非会员限前 2 页）。

二、需要安装的库
打开终端执行以下命令：
pip install requests lxml PyExecJS

三、文件说明
文件名
作用
02_逆向 header 加密.py
主脚本（核心逻辑）
02_企查查_header 加密逻辑.js
生成加密请求头，不能删 / 改
encode_url.py
处理中文关键词的 URL 编码，不能删

四、使用步骤（必看）
1. 自己拿 Cookie（关键！）
脚本需要企查查的 Cookie 才能用，步骤：
用浏览器打开 https://www.qcc.com ，登录账号；
按 F12 → 点「Application」→「Cookies」→ 选 https://www.qcc.com；
复制 QCCSESSID、qcc_did、_c_WBKFRo、acw_tc 这 4 个值，用 ;  隔开；
打开 02_逆向header加密.py，找到 cookie = "..." 这行，把复制的内容替换进去。
2. 运行脚本
终端切换到脚本所在文件夹；
执行命令：python 02_逆向header加密.py；
按提示输入：
搜索关键字（如 “华为”）；
搜索页数（非会员只能输 1 或 2）。
五、注意事项
Cookie 会过期，若报错 “身份验证失败”，重新按步骤 1 拿新 Cookie；
非会员只能爬前 2 页，会员可自己改脚本里的页数限制；
别频繁运行，避免被企查查封 IP。