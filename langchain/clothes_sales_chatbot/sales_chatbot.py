import gradio as gr

from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
import openai

import os

# 更换为自己的 Serp API KEY
os.environ["OPENAI_API_KEY"] = "sk-38rkK0xdFDDMClm688CbCb0204F64d3d874066CbEf2fE608"
os.environ['OPENAI_BASE_URL'] = 'https://api.xiaoai.plus/v1'

def initialize_sales_bot(vector_store_dir: str="real_estates_sale"):
    # 读取向量数据库
    with open("real_estate_sales_data.txt",encoding='utf-8') as f:
     real_estate_sales = f.read()
    # 使用 CharacterTextSplitter 来进行文本分割
    text_splitter = CharacterTextSplitter(        
    separator = r'\d+\.',
    chunk_size = 100,
    chunk_overlap  = 0,
    length_function = len,
    is_separator_regex = True,)
    docs = text_splitter.create_documents([real_estate_sales])
    # 使用 Faiss 作为向量数据库，持久化存储衣服销售问答对（QA-Pair）
    db = FAISS.from_documents(docs, OpenAIEmbeddings())
    db.save_local("real_estates_sale")
    # 加载 FAISS 向量数据库已有结果
    db = FAISS.load_local(vector_store_dir, OpenAIEmbeddings(),allow_dangerous_deserialization=True)
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    
    global SALES_BOT    
    SALES_BOT = RetrievalQA.from_chain_type(llm,
                                           retriever=db.as_retriever(search_type="similarity_score_threshold",
                                                                     search_kwargs={"score_threshold": 0.8}))
    # 返回向量数据库的检索结果
    SALES_BOT.return_source_documents = True

    return SALES_BOT

def sales_chat(message, history):
    print(f"[message]{message}")
    print(f"[history]{history}")

    ans = SALES_BOT({"query": message})

    # 如果检索出结果
    # 返回 RetrievalQA combine_documents_chain 整合的结果
    if ans["source_documents"]:
        print(f"[result]{ans['result']}")
        print(f"[source_documents]{ans['source_documents']}")
        return ans["result"]
    # 否则就重新調用ChatOpenAI大语言模型進行回答
    else:
        # 创建 system prompt
        chat_input = [
        {"role": "system", "content": "You are a knowledgeable salesperson for clothes. Please answer the questions as if you are talking to a customer and maintain the persona of a human sales assistant throughout the conversation."},
        {"role": "user", "content": message}]

        # 使用模型生成回答
        chat_response = openai.chat.completions.create(model="gpt-3.5-turbo", messages=chat_input)
        print(chat_response)
      
        personalized_response = chat_response.choices[0].message.content

        return personalized_response
    

def launch_gradio():
    demo = gr.ChatInterface(
        fn=sales_chat,
        title="衣服销售",
        # retry_btn=None,
        # undo_btn=None,
        chatbot=gr.Chatbot(height=600),
    )

    demo.launch(share=True, server_name="0.0.0.0")

if __name__ == "__main__":
    # 初始化衣服销售机器人
    initialize_sales_bot()
    # 启动 Gradio 服务
    launch_gradio()
