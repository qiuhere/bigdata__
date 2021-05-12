Bot 和 Crawler
===================================

Bot目录下是修改后的聊天机器人

Crawler目录下是我们使用的简单的爬虫

===================================

#Bot使用：

在datapreprocess.py中修改数据集的设置
对语料库进行预处理，产生corpus.pth （已经上传好corpus.pth, 可跳过）

可修改参数:

datapreprocess.py
corpus_file = 'clean_chat_corpus/qingyun.tsv' #未处理的对话数据集
save_path = 'corpus.pth' #已处理的对话数据集保存路径

运行数据处理
- python3 datapreprocess.py

运行数据训练（已经训练过模型，可跳过）
- python3 train_eval.py train

可修改参数:
config.py
model_ckpt='checkpoints/chatbot_0509_1437' #模型路径

实际运行聊天
- python3 main.py chat

====================================

# Crawler使用：

testbs.py是爬虫

可修改参数:
URL_PATH='' #爬取链接存放位置
TITLE_PATH='' #爬取标题存放位置
FILE_PATH='' #结果位置

process.py是数据处理

可修改参数:
SRC_PATH #爬虫结果位置
MID_PATH #清理结果
DST_PATH #扩大结果