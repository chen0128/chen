import requests
from bs4 import BeautifulSoup

# 假设这里有一个包含目标 HTML 结构的网页 URL
# 这里用一个占位 URL 示例，实际使用时需替换为真实有效的网页地址
url = 'https://example.com'

# 设置请求头，模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    # 发送 HTTP 请求获取网页内容
    response = requests.get(url, headers=headers)
    # 检查请求是否成功
    response.raise_for_status()

    # 使用 BeautifulSoup 解析 HTML 内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找所有 class 为 "article" 的 div 元素
    article_divs = soup.find_all('div', class_='article')

    # 遍历每个 article div 元素
    for article_div in article_divs:
        # 查找 class 为 "title" 的 h2 元素
        title_element = article_div.find('h2', class_='title')
        if title_element:
            title = title_element.text.strip()
        else:
            title = "未找到标题"

        # 查找 class 为 "content" 的 p 元素
        content_element = article_div.find('p', class_='content')
        if content_element:
            content = content_element.text.strip()
        else:
            content = "未找到内容"

        # 打印文章标题和内容
        print(f"标题: {title}")
        print(f"内容: {content}")
        print("-" * 50)

except requests.RequestException as e:
    print(f"请求出错: {e}")
except Exception as e:
    print(f"发生其他错误: {e}")