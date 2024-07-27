# Day1

## ChatGPT 最朴素的 Prompt技巧：将大模型当做你的工作伙伴 实践作业

本次作业的目标是练习使用ChatGPT进行文本生成。作业内容是生成一份学习日报，让chatgpt解读上传的课程pdf文件，总结课程学习内容。

作业link如下，可直接打开查看：
https://chatgpt.com/share/e44047e7-079d-4659-94fb-a00a2e9a3b5a

# Day2

## GPT-4V/translator/langchain chains实践作业

1.上传自己手写的图片到images文件夹，可命名为gpt-4v.jpg；
2.修改query_base64_image_description的方法描述，分析gpt-4v.jpg图片；
3.输出分析结果，并使用函数对输出进行渲染，渲染成Markdown格式使结果更易读；。

### 作业结果如下图：
### 手写图片
![](./openai_api/images/handwriting_2.jpg)
### 分析结果
![](./homework_results/gpt-4v-0.png)
### 格式化结果
![](./homework_results/gpt-4v-1.png)


ai translator中，添加2种以上的其他语言对翻译
### 作业结果如下图，具体可看translator的readme文件：
### 英翻中
![](./homework_results/英翻中.png)
### 英翻韩
![](./homework_results/英翻韩.png)


扩展chains，使其支持生物、计算机和汉语文学老师等学科的提示词模板及对应 Chains问答

### 作业结果如下图：
### 提示词模板
![](./homework_results/langchain-0.png)
### Chains问答
![](./homework_results/langchain-1.png)

# Day3

## GPT-4V 实践作业

1.自行生成一个新的产品介绍知识库，可搜索使用一个产品的行业数据，也可自建一个产品的真实数据。参考“房产销售聊天机器人”，开发一个“**销售聊天机器人”；
2.在"**销售聊天机器人"中，使用向量数据库进行检索回答，如果向量数据库检索不到问题答案时，能够通过一个prompt来回答这个问题，而不是直接告诉用户我是一个AI机器人。

### 作业结果如下图：
![](./homework_results/clothes_sales_chatbot.png)

