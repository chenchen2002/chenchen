import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/94.0.4606.81 Safari/537.36',
}  # 请求头

info_list = []

for page in range(784286, 784309):
    # print(page)
    url = 'https://nce.koolearn.com/20161006/{}.html'.format(str(page))
    r = requests.get(url, headers=headers)
    soup = r.content.decode("utf-8")
    soup = BeautifulSoup(soup, "html.parser")
    recipe_list = soup.select('.xqy_core_text p')
    for i in recipe_list:
         print(i)
        try:
            recipe_url = i.select_one('a').get('href')
            soup_r = requests.get(recipe_url, headers=headers).content.decode("utf-8")
            soup_recipe = BeautifulSoup(soup_r, "html.parser")
            recipe_title = soup_recipe.select_one('.recipe_title').text
            recipe_ingredients = soup_recipe.select('.recipe_ingredients .right')
            main = [_.text.strip() for _ in recipe_ingredients[0].select('strong')]
            others = [_.text.strip() for _ in recipe_ingredients[1].select('strong')]
            info = {
                'name': recipe_title,
                'main': ' '.join(main),
                'others': ' '.join(others)
            }
            print(info)
            info_list.append(info)
        # except AttributeError:
        except Exception:
            continue

with open('recipe.txt', 'w', encoding='utf-8') as f:
    for i in info_list:
        text = '菜名：{}\n主料：{}\n辅料：{}\n\n'.format(i['name'], i['main'], i['others'])
        f.write(text)
