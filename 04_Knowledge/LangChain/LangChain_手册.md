# LangChain 手册（工程实践版）

> 版本：v1.0  
> 编写日期：2026-03-28  
> 适用对象：希望用 LangChain 构建 LLM 应用（问答、Agent、RAG、工作流）的工程师

---

## 1. LangChain 是什么

LangChain 是一个面向 LLM 应用开发的框架，核心价值是：

- 统一模型调用接口（不同模型厂商可替换）
- 提供 Prompt、Chain、Tool、Agent、Memory、Retriever 等常用抽象
- 方便把“模型 + 知识库 + 业务逻辑 + 外部工具”编排成可运行系统

一句话理解：
**LangChain 不是模型本身，而是“把模型变成工程应用”的中间层。**

---

## 2. 适用场景

LangChain 常见落地场景：

1. **企业知识库问答（RAG）**
2. **客服/助手机器人**
3. **多工具调用 Agent（查库、调用 API、执行流程）**
4. **文档处理流水线（抽取、总结、分类、改写）**
5. **多步骤推理工作流（带状态和分支）**

不太适合的情况：

- 只做一次性 Prompt 实验（直接 SDK 更轻）
- 对延迟极端敏感且流程很简单（框架抽象可能增加复杂度）

---

## 3. 核心组件地图

理解 LangChain 的关键是分层：

1. **Models**：大模型与嵌入模型
2. **Prompts**：提示词模板
3. **Output Parsers**：把模型输出解析成结构化数据
4. **Retrievers / Vector Stores**：检索上下文（RAG）
5. **Tools**：模型可调用的外部能力
6. **Agents**：让模型决定“下一步调用哪个工具”
7. **Memory / State**：跨轮会话状态
8. **Callbacks / Tracing**：观测、调试、评估

工程上建议：

- **先做固定流程（Chain）**，稳定后再升级为 Agent
- **先做可解释的 RAG**，再追求复杂推理

---

## 4. 快速开始（Python）

### 4.1 安装

```bash
pip install -U langchain langchain-openai langchain-community
```

可选（RAG 常用）：

```bash
pip install -U faiss-cpu chromadb tiktoken pypdf
```

### 4.2 环境变量

```bash
export OPENAI_API_KEY="your_api_key"
```

### 4.3 最小调用示例

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
resp = llm.invoke("请用一句话解释什么是 RAG")
print(resp.content)
```

---

## 5. Prompt 设计规范（强烈建议）

高质量 Prompt 至少包含：

1. **角色**：你是谁（如“资深后端工程师”）
2. **任务**：要做什么
3. **约束**：格式、长度、禁用项
4. **上下文**：输入资料
5. **输出格式**：JSON/Markdown 表格等

模板化示例：

```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是企业知识库问答助手，回答必须基于提供的上下文。"),
    ("human", "问题：{question}\n\n上下文：{context}\n\n请给出结论和依据。")
])
```

建议：

- 对生产系统统一使用模板文件，避免散落在代码里
- 输出尽可能结构化（JSON schema）

---

## 6. RAG 实战标准流程

RAG（Retrieval-Augmented Generation）是 LangChain 最常见用法。

### 6.1 五步法

1. 文档加载（Loader）
2. 文档切分（Text Splitter）
3. 向量化（Embeddings）
4. 建索引（Vector Store）
5. 检索 + 生成（Retriever + LLM）

### 6.2 参考代码（精简）

```python
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

loader = PyPDFLoader("company_policy.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=120)
chunks = splitter.split_documents(docs)

emb = OpenAIEmbeddings(model="text-embedding-3-large")
vs = FAISS.from_documents(chunks, emb)
retriever = vs.as_retriever(search_kwargs={"k": 4})

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

print(qa.invoke({"query": "请总结该制度中的审批流程"}))
```

### 6.3 RAG 调参经验

- `chunk_size` 常见 400~1200，按文档类型调
- `chunk_overlap` 常见 10%~20%
- `k`（召回条数）建议从 3~6 起步
- 对召回结果做重排（rerank）通常提升明显

---

## 7. Agent 使用指南

Agent 适合“步骤不固定、需要调用多个工具”的任务。

### 7.1 什么时候用 Agent

用 Agent：

- 查询 + 计算 + 外部 API 混合任务
- 用户问题类型多变

不用 Agent：

- 固定业务流程（直接 Chain 更稳定、更快）

### 7.2 Tool 设计原则

1. 工具粒度小、职责单一
2. 入参明确（最好有 schema）
3. 错误可解释（返回可读错误信息）
4. 设置超时与重试

### 7.3 安全建议

- 对高风险工具（写数据库、发邮件、转账）增加人工确认
- 对 Agent 输出做白名单校验
- 记录每次工具调用日志（入参、出参、耗时）

---

## 8. 记忆与会话状态

短期记忆通常用于多轮对话上下文；长期记忆通常用于用户画像或历史偏好。

实践建议：

- 短期上下文放在会话状态，设置 token 上限
- 长期偏好存数据库，不要只依赖上下文窗口
- 关键业务状态（订单号、审批单号）必须结构化存储

---

## 9. 可观测性与评估

生产可用的 LLM 系统必须可观测：

1. **链路追踪**：每次调用的步骤、耗时、token 用量
2. **质量评估**：正确率、引用命中率、拒答准确性
3. **失败分析**：检索失败 / 提示词失败 / 工具失败

建议建立最小评估集（20~50 条真实问题），每次发版回归。

---

## 10. 常见问题与排查

### 10.1 回答“看起来对但其实错”

可能原因：

- 检索不到关键片段
- Prompt 没要求“必须引用依据”
- 模型温度过高

排查顺序：

1. 先看召回文档是否正确
2. 再看 Prompt 约束是否足够
3. 最后调模型与参数

### 10.2 成本过高

优化路径：

- 先降上下文长度
- 再换便宜模型处理简单步骤
- 使用缓存（Embedding 缓存、结果缓存）

### 10.3 响应慢

优化路径：

- 并行工具调用
- 降低检索规模
- 将“非实时步骤”改异步批处理

---

## 11. 生产落地清单（Checklist）

上线前至少确认：

- [ ] Prompt 已模板化并版本管理
- [ ] RAG 有离线评估集与基线结果
- [ ] Tool 有超时、重试、权限控制
- [ ] 核心链路可追踪（日志 + trace）
- [ ] 失败时有兜底回复
- [ ] 敏感信息已脱敏
- [ ] 成本预算和告警阈值已设置

---

## 12. 推荐学习路径（7 天）

- Day 1：跑通最小 LLM 调用
- Day 2：掌握 Prompt 模板与结构化输出
- Day 3：搭建一个 PDF-RAG Demo
- Day 4：接入 1~2 个工具，做简单 Agent
- Day 5：加入日志、评估、错误处理
- Day 6：做性能与成本优化
- Day 7：整理为可复用项目模板

---

## 13. 术语速查

- **LLM**：大语言模型
- **Embedding**：文本向量表示
- **RAG**：检索增强生成
- **Retriever**：从知识库检索相关片段
- **Tool**：可被模型调用的函数或外部能力
- **Agent**：可自主选择工具和步骤的执行体
- **Chain**：固定步骤的调用链

---

## 14. 在项目中的推荐落地策略

1. 第一阶段：只做 RAG + 固定流程（保证可控）
2. 第二阶段：局部引入 Agent（仅在必要环节）
3. 第三阶段：建立评估、监控、成本治理闭环

核心原则：
**先可用，再可靠，后智能。**

