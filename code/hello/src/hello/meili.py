from meilisearch import Client
from pydantic import BaseModel

# 带认证的连接（生产环境推荐）
client = Client(
    'http://localhost:7700',
    api_key='R5T5WDon_QrPqhFK97NgGlTVa81iuVlN44TMLiClTTg'
)

# 创建/获取索引
index = client.index('cover')

# 基础搜索
results = index.search('封面')
# print(type(results))
# print(f"result:{results.get('hits')}")
for hit in results['hits']:
    print(type(hit))
    print(f"匹配结果: uid={hit['uid']},name={hit.get('name')},(类型: {hit['category']})")

# # 高级搜索（带过滤条件）
# filtered_results = movies_index.search(
#     'inception',
#     {'filter': ['genre = sci-fi']}
# )