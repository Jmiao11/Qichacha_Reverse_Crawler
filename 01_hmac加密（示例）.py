import hmac
import hashlib

# 函数：生成 HMAC 签名
def generate_hmac(message, secret_key, algorithm=hashlib.sha256):
    # 注意：Python 中 message 和 secret_key 需转为 bytes 类型
    message_bytes = message.encode('utf-8')
    secret_key_bytes = secret_key.encode('utf-8')
    # 创建 HMAC 实例并计算
    hmac_obj = hmac.new(secret_key_bytes, message_bytes, digestmod=algorithm)
    # 输出 16 进制格式
    return hmac_obj.hexdigest()

# 测试
message = "Hello, HMAC!"
secret_key = "my-secret-key-456"
print(generate_hmac(message, secret_key))
# 输出与 JavaScript 示例一致（相同消息+密钥+算法，结果相同）
