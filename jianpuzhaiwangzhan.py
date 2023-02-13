import requests
from bs4 import BeautifulSoup
headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69'
}
info_list=[]
for p in range (1,3):
    url ='http://www.jinbianwanbao.cn/news.html?pagesize=20&p={}'.format(str(p))
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, features='html.parser')
    recipe_list= soup.select('#right .textlist li')
    #print(recipe_list)
    for i in recipe_list:
        recipe_url = i.select_one('a').get('href')
        recipe_url='http://www.jinbianwanbao.cn/'+recipe_url
        #print(recipe_url)
        soup_r = requests.get(url=recipe_url, headers=headers).content
        soup_recipe = BeautifulSoup(soup_r, features='html.parser')
        #解析具体新闻
        recipe_title = soup_recipe.select_one('.InfoTitle').text
        recipe_content = soup_recipe.select_one('.InfoContent').text
        info = {
            'title': recipe_title,
            'content': recipe_content
        }
        info_list.append(info)
        #Test
with open('recipe.txt', 'w', encoding='utf-8') as f:
      for i in info_list:
        text = '题目：{}\n内容：{}\n\n'.format(i['title'], i['content'])
        f.write(text)






