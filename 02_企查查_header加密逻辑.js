e = {
    "url": "/api/search/searchMulti",
    "method": "post",
    "data": {
        "searchKey": "小米",
        "pageIndex": 1,
        "pageSize": 20
    },
    "headers": {
        "common": {
            "Accept": "application/json, text/plain, */*"
        },
        "delete": {},
        "get": {},
        "head": {},
        "post": {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        "put": {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        "patch": {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        "X-Requested-With": "XMLHttpRequest",
        "x-pid": "55b6cda73a07961c6e829b6190a6a6b6"
    },
    "baseURL": "https://www.qcc.com",
    "transformRequest": [
        null
    ],
    "transformResponse": [
        null
    ],
    "timeout": 0,
    "xsrfCookieName": "XSRF-TOKEN",
    "xsrfHeaderName": "X-XSRF-TOKEN",
    "maxContentLength": -1,
    "maxBodyLength": -1,
    "transitional": {
        "silentJSONParsing": true,
        "forcedJSONParsing": true,
        "clarifyTimeoutError": false
    },
    "withCredentials": true
};

a = {
    "default": {
        "options": {
            "allowPrototypes": true,
            "encodeValuesOnly": true,
            "allowDots": true,
            "arrayFormat": "brackets"
        }
    },
    "options": {
        "allowPrototypes": true,
        "encodeValuesOnly": true,
        "allowDots": true,
        "arrayFormat": "brackets"
    }
};


const crypto = require('crypto');
// 改写 _createHmacHelper 函数
_createHmacHelper = function(data, secret) {
        // 使用 crypto 模块创建 HMAC 实例
        const hmac = crypto.createHmac(algorithm = 'sha512', secret);
        // 更新要加密的数据（支持字符串或 Buffer）
        hmac.update(data);
        // 计算最终结果，返回十六进制字符串（可根据需要改为 'base64' 等）
        return hmac.digest('hex');
};

mapping = {
    "0": "W",
    "1": "l",
    "2": "k",
    "3": "B",
    "4": "Q",
    "5": "g",
    "6": "f",
    "7": "i",
    "8": "i",
    "9": "r",
    "10": "v",
    "11": "6",
    "12": "A",
    "13": "K",
    "14": "N",
    "15": "k",
    "16": "4",
    "17": "L",
    "18": "1",
    "19": "8"
}
dd = function() {
                for (var e = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase(), t = e + e, n = "", i = 0; i < t.length; ++i) {
                    var o = t[i].charCodeAt() % 20;
                    n += mapping[o]
                }
                return n
            };

cc = function(e, t) {
                return _createHmacHelper(e, t).toString()
            };

bb = function() {
                var e = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
                  , t = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase()
                  , n = JSON.stringify(e).toLowerCase();
                console.log("即将进入sha512加密：",t + n, dd(t))
                global.secret =  dd(t)
                return cc(t + n, dd(t)).toLowerCase().substr(8, 20)
            };



r_default = function() {
                var e = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
                  , t = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : ""
                  , n = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase()
                  , i = JSON.stringify(e).toLowerCase();
                console.log(n + "pathString" + i + t, global.secret)
                return _createHmacHelper(n + "pathString" + i + t, global.secret)
            };

global.tid = '2c8e87c32acd95c7bf177a47f1d6a6a2'
aa = function(e) {
                var t = e.url.replace(e.baseURL, "")
                  , n = '';
                n && (t += (-1 === t.indexOf("?") ? "?" : a.default.options.delimiter || "&") + n),
                t = t.toLowerCase();
                var i = bb(t, e.data)
                console.log("最终i:",i)
                console.log()
                , u = r_default(t, e.data, global.tid);
                e.headers[i] = u
                console.log(i,u)
                return {i,u}
            };



//a.default = i.default = cc;
// o.default = i.default =dd;
// a.default.codes = mapping

function main (e){return aa(e)}





