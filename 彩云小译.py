import requests
import json

def translate_text(source_text):
    url = "https://api.interpreter.caiyunai.com/v1/dict"
    data = {
        'trans_type': 'zh2en' if is_chinese(source_text) else 'en2zh',
        'source': source_text,
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json;charset=UTF-8',
        'origin': 'https://fanyi.caiyunapp.com',
        'Referer': 'https://fanyi.caiyunapp.com/',
        'x-authorization': 'token:qgemv4jr1y38jyq6vhvi'
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

def is_chinese(text):
    return any('\u4e00' <= char <= '\u9fff' for char in text)

def display_result(result, source_text):
    if result.get('rc') == 0:
        if is_chinese(source_text):
            entry = result['dictionary'].get('entry', '未知')
            explanations = result['dictionary'].get('explanations', ['无解释'])
            print(f"翻译: {entry}")
            print("解释: " + ", ".join(explanations))
        else:
            explanations = result['dictionary'].get('explanations', ['无解释'])
            print(f"翻译: {', '.join(explanations)}")
    else:
        print("翻译失败:", result.get('message', '未知错误'))

def main():
    print("请输入要翻译的文本（词语或一个字），输入'退出'结束:")
    while True:
        source_text = input()
        if source_text.strip().lower() == '退出':
            print("程序结束。")
            break
        
        result = translate_text(source_text)
        display_result(result, source_text)
        print("\n请输入要翻译的文本（词语或一个字），输入'退出'结束:")  # 重新提示用户

if __name__ == "__main__":
    main()
