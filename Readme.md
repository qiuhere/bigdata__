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

====================================

# 笨蛋使用：

根目录下有baka.py

该程序是我手写的使用数据集直接查找的Python程序
主要是为了实现我这个项目的目标——看点嘴臭

可以修改的参数是一个，就是数据集的位置
data_path=''
此处建议用上述Crawler中MID_PATH的位置
因为单纯复制扩大的结果只会消耗更多内存而没有任何其他效果

运行方式
python3 baka.py

====================================

- 备注：
此项目为大数据专题课程作业，希望老师能够对此作业不足之处进行指正

后续添加计算问题相似度选择答案的对话机器人，
也就是以爬虫结果为总数据进行很容易牛头不对马嘴的问答查询
如果张老师您只能看到第一次提交的pdf，希望您能用一下我这里写的笨蛋程序
虽然整体程序挺笨蛋的，但是你如果和它聊时事，还是可以看到不少魔怔发言的