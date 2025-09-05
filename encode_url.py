from urllib.parse import quote, urlparse, urlunparse
'''
这是url编码模块,不是核心部分
'''

def encode_url_chinese(original_url):
    # 解析URL为组件（协议、域名、路径、参数等）
    parsed = urlparse(original_url)

    # 对查询参数中的中文进行编码
    encoded_query = quote(parsed.query, safe='=&')

    # 重新组合URL
    encoded_url = urlunparse(parsed._replace(query=encoded_query))

    return encoded_url

# 示例使用
if __name__ == "__main__":
    original_url = "https://www.qcc.com/web/search?key=小米"
    encoded_url = encode_url_chinese(original_url)

    print("原始URL:", original_url)
    print("编码后URL:", encoded_url)
