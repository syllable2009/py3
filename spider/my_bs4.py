from bs4 import BeautifulSoup

def extract_body(response):
    if response is None:
        return None
    try:
        soup = BeautifulSoup(response.text, 'lxml')
        return soup
    except Exception as e:
        print(f"解析失败: {e}")
        return None
