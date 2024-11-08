![彩云小译logo](https://cdn-web.caiyunapp.com/xiaoyi-assets/logo/xiaoyi-logo.png)
# 彩云小译(py)
## 简介
这是一个简单的 Python 项目，通过抓取彩云小译提供的 API 实现中文和英文之间的词汇翻译。用户可以输入要翻译的文本，程序将返回翻译结果及相关解释。

## 功能
- 支持中文和英文之间的翻译
- 显示翻译结果及相关解释
- 通过命令行界面与用户交互

## 依赖
该项目依赖于 `requests` 库。可以使用以下命令安装依赖：

```bash
pip install requests
```


## 示例
```
请输入要翻译的文本（词语或一个字），输入'退出'结束:
你好
翻译: 你好
解释: how do you do; how are you; hello

请输入要翻译的文本（词语或一个字），输入'退出'结束:
exit
翻译: vi.(戏剧)退场, n.出口;离去;(演员)退场, vt.离开,退出(舞台);退 场

请输入要翻译的文本（词语或一个字），输入'退出'结束:
退出
程序结束。

[按回车键退出]
```

## 注意事项
- 请确保网络连接正常，因为程序需要访问外部 API 进行翻译。
- 使用时请遵守 API 的使用规范，以免造成不必要的流量。
- 建议打开彩云小译的官网找到"dict"更换为自己的token.
```bash
        'x-authorization': 'token:qgemv4jr1y38jyq6vhvi'
```
