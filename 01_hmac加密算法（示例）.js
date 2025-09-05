const crypto = require('crypto');

// 函数：生成 HMAC 签名
function generateHMAC(message, secretKey, algorithm = 'sha256') {
  // 创建 HMAC 实例（算法 + 密钥）
  const hmac = crypto.createHmac(algorithm, secretKey);
  // 传入消息并计算（更新数据）
  hmac.update(message, 'utf8');
  // 输出 16 进制格式的结果
  return hmac.digest('hex');
}

// 测试
const message = "Hello, HMAC!";
const secretKey = "my-secret-key-456";
console.log(generateHMAC(message, secretKey));
// 输出：sha256 对应的 16 进制 HMAC（64 位字符）