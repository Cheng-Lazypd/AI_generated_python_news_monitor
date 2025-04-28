from openai import OpenAI
import requests
import os

#读取python官网的源代码
url="http://www.python.org"
headers={"User-Agent":"Mozilla/5.0"}
response=requests.get(url,headers=headers)
html=response.text

#设置调取api
client = OpenAI(api_key="sk-6f5d570098754d298d523710d4883901", base_url="https://api.deepseek.com/v1")

#用deepseek-chat提取所有latest news
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你要从网站爬虫结构中找到新闻部分并将其内容提取出来，回复所有新闻部分的content，content之间用“$”隔开,不要有任何额外多余的输出，结尾不要加$，因为我之后会根据你的回复的所有内容来整理成一个新闻的list并进行一些程序操作"},
        {"role": "user", "content":html},
    ],
    stream=False
)
content=response.choices[0].message.content

#将回复整理成list
new=''
news=[]
for char in content:
    if char!='$':
        new=new+char
    else:
        news.append(new)
        new=''
news.append(new)

#提取每个新闻的时间
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你要从网站爬虫结构中找到新闻部分并将其对应的时间提取出来，回复所有新闻时间部分的content，注意不包含upcoming events或是其他非新闻内容的时间，只包含新闻的时间，content之间用“$”隔开,不要有任何额外多余的输出，因为我之后会根据你的回复的所有内容来整理成一个新闻的list并进行一些程序操作，时间输出示例：“2024-03-03 17:17”"},
        {"role": "user", "content":html},
    ],
    stream=False
)
content=response.choices[0].message.content

#将回复整理成list
time=''
times=[]
for char in content:
    if char!='$':
        time=time+char
    else:
        times.append(time)
        time=''
times.append(time)

#把时间整合进news
for i in range(len(news)):
    news[i]='['+times[i]+'] '+news[i]

#打印所有新闻
print('Latest News:')
for new in news:
    print(new)

#正常运行情况：与上次提取内容对比并更新
if os.path.exists("news_last.txt"):
    with open("news_last.txt","r",encoding="utf-8") as f:
        content=[line.rstrip("\n") for line in f.readlines()]#将上次读取的内容转化成list
        if news==content:#无更新
            print("No new updates.")
        else:#有更新
            print("News updates available.")
            update=[]
            #将更新的news存储到update里
            for new in news:
                if new not in content:
                    update.append(new)
            #更新日志
            with open("Changelog.txt","a",encoding="utf-8") as f1:
                for i in range(len(update)):
                    f1.write(update[-i-1])
                    f1.write("\n")
                    print(update[-i-1])#展示更新内容
#第一次运行情况
else:
    with open("Changelog.txt", "a", encoding="utf-8") as f1:
        for i in range(len(news)):
            f1.write(news[-i-1])
            f1.write("\n")
#将这次提取的新闻内容覆盖存储
with open("news_last.txt","w+",encoding="utf-8") as f:
    for new in news:
        f.write(new)
        f.write("\n")
