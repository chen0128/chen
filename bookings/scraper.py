# import requests
# from bs4 import BeautifulSoup
#
# def scrape_jinhuyang_info():
#     url = 'https://www.1230e.com/case/59.html'  # 替换为实际的景点官网
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         soup = BeautifulSoup(response.content, 'html.parser')
#
#         # 示例：提取页面标题作为景点名称
#         name = soup.title.string if soup.title else '未找到景点名称'
#
#         # 示例：提取第一段介绍文字作为景点简介
#         intro = soup.find('p').text if soup.find('p') else '未找到景点简介'
#
#         return {
#             'name': name,
#             'intro': intro
#         }
#     except requests.RequestException as e:
#         print(f"请求出错: {e}")
#         return None