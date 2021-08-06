从这里开启新的篇章，逐渐掌握技能，平时去研究。
1. 30天初步掌握django和electron，并搭建一个网站。
网站主题：参开[TL官网](https://www.teng-lee.com/)
首页 产品 新闻 资源 关于我们 联系我们

第一天
web入门
安装基础软件：

- 文本编辑器   vscode
- web 浏览器 chrome firefox
- 图形编辑器 GIMP
- 版本控制系统 Git
- ftp客户端 filezilla
- 自动化系统 webpack 用于自动执行重复性任务，例如缩小代码和运行测试。
-  库、框架等，以加快编写常用功能。库往往是现有的 JavaScript 或 CSS 文件，它提供现成的功能供您在代码中使用。一个框架倾向于更进一步，提供一个完整的系统，其中包含一些自定义语法，供您在其上编写 Web 应用程序。

勾画网站草图：001
首页链接
个人简介文字说明   个人图片

一个网站由许多文件组成：文本内容、代码、样式表、媒体内容等。在构建网站时，您需要将这些文件组合成一个合理的结构，并确保它们可以相互通信。
大致结构如下：
└─test-site
    │  index.html
    ├─images
    │      child.jpg│
    ├─scripts
    └─styles

**HTML 基础知识**
HTML 是一种_标记语言_，用于定义内容的结构。
```
<p>My cat is very grumpy</p>
```

这里不再说明各种标签，可以参考[html参考](https://www.runoob.com/html/html-tutorial.html)

**CSS基础**
CSS（层叠样式表）是为网页内容设计样式的代码。
与 HTML 一样，CSS 不是一种编程语言。它也不是一种标记语言。**CSS 是一种样式表语言。**CSS 是您用来有选择地设置 HTML 元素样式的工具。

这个 CSS 选择段落文本，将颜色设置为红色：
```
p {
  color: red;
}
```
**JavaScript 基础**
JavaScript 是一种编程语言，可为您的网站增加交互性。

**发布网站**
[参考地址](https://www.codecademy.com/learn/deploy-a-website)

暂未找到理想方式

第二天
HTML简介
**head和metadata**
HTML 文档的头部是页面加载时未在 Web 浏览器中显示的部分。它包含页面`<title>`,CSS链接,自定义收藏夹图标的链接和其他元数据.

html简单示例
```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My test page</title>
  </head>
  <body>
    <p>This is my page</p>
  </body>
</html>
```

**HTML文本基础**

```
# 段落 标题
<p>I am a paragraph, oh yes I am.</p>
<h1>I am the title of the story.</h1>
```
### span
这是一个`<span>`元素。它没有语义。当您想对其应用 CSS（或使用 JavaScript 对其执行某些操作）时，您可以使用它来包装内容，而无需赋予它任何额外的含义。
```
<span style="font-size: 32px; margin: 21px 0; display: block;">Is this a top level heading?</span>
```

### 无序列表
```
<ul>
milk
eggs
bread
hummus
</ul>
```

### 有序列表
```
<ol>
  <li>Drive to the end of the road</li>
  <li>Turn right</li>
  <li>Go straight across the first two roundabouts</li>
  <li>Turn left at the third roundabout</li>
  <li>The school is on your right, 300 meters up the road</li>
</ol>
```

### 嵌套列表
```
<ol>
  <li>Remove the skin from the garlic, and chop coarsely.</li>
  <li>Remove all the seeds and stalk from the pepper, and chop coarsely.</li>
  <li>Add all the ingredients into a food processor.</li>
  <li>Process all the ingredients into a paste.
    <ul>
      <li>If you want a coarse "chunky" hummus, process it for a short time.</li>
      <li>If you want a smooth hummus, process it for a longer time.</li>
    </ul>
  </li>
</ol>
```

### 文本重点

```
# em为斜体
<p>I am <em>glad</em> you weren't <em>late</em>.</p>
# strong 为粗体
<p>This liquid is <strong>highly toxic</strong>.</p>
<p>I am counting on you. <strong>Do not</strong> be late!</p>
```

**超链接**
```
<p>I'm creating a link to
<a href="https://www.mozilla.org/en-US/">the Mozilla homepage</a>.
</p>
```
title属性--指向链接时的提示信息
```
<p>I'm creating a link to
<a href="https://www.mozilla.org/en-US/"
   title="The best place to find more information about Mozilla's
          mission and how to contribute">the Mozilla homepage</a>.
</p>
```

图片链接
```
<a href="https://www.mozilla.org/en-US/">
  <img src="mozilla-image.png" alt="mozilla logo that links to the mozilla homepage">
</a>
```

**高级文本格式**

```
<dl>
  <dt>soliloquy</dt>
  <dd>In drama, where a character speaks to themselves, representing their inner thoughts or feelings and in the process relaying them to the audience (but not to other characters.)</dd>
  <dt>monologue</dt>
  <dd>In drama, where a character speaks their thoughts out loud to share them with the audience and any other characters present.</dd>
  <dt>aside</dt>
  <dd>In drama, where a character shares a comment only with the audience for humorous or dramatic effect. This is usually a feeling, thought, or piece of additional background information.</dd>
</dl>
```

```
<dl>
  <dt>aside</dt>
  <dd>In drama, where a character shares a comment only with the audience for humorous or dramatic effect. This is usually a feeling, thought, or piece of additional background information.</dd>
  <dd>In writing, a section of content that is related to the current topic, but doesn't fit directly into the main flow of content so is presented nearby (often in a box off to the side.)</dd>
</dl>
```
### 标记联系方式
```
<address>
  <p>
    Chris Mills<br>
    Manchester<br>
    The Grim North<br>
    UK
  </p>

  <ul>
    <li>Tel: 01234 567 890</li>
    <li>Email: me@grim-north.co.uk</li>
  </ul>
</address>
```

### 上标和下标
```
<p>My birthday is on the 25<sup>th</sup> of May 2001.</p>
<p>Caffeine's chemical formula is C<sub>8</sub>H<sub>10</sub>N<sub>4</sub>O<sub>2</sub>.</p>
<p>If x<sup>2</sup> is 9, x must equal 3 or -3.</p>
```

**文档和网站结构**

### 文档的基本部分

标题：

通常在顶部有一个大条带，上面有一个大标题、标志，也许还有一个标语。这通常从一个网页到另一个网页保持不变。

导航栏：

网站主要部分的链接；通常由菜单按钮、链接或选项卡表示。

主要内容：
中心的一个大区域，包含给定网页的大部分独特内容，

侧边栏：

一些外围信息、链接、引用、广告等。通常，这与主要内容中包含的内容相关（例如，在新闻文章页面上，侧边栏可能包含作者的简历或相关文章的链接），但也有在某些情况下，您还会发现一些重复出现的元素，例如辅助导航系统。

页脚：

页面底部的条带，通常包含精美的印刷品、版权声明或联系信息。

### 用于构建内容的html
-   **标题：**`<header>`
-   **导航栏：**`<nav>`
-   **主要内容是：**`<main> <section> <div>`
-   **侧边栏：**`<aside>`
-   **页脚：**`<footer>`

# 多媒体和嵌入

### 嵌入图像
```
<img src="dinosaur.jpg">
```

替换文字，当图片无法显示时，使用文字替换，属性alt
指定大小时，使用width和height属性
```
<img src="images/dinosaur.jpg"
     alt="The head and torso of a dinosaur skeleton;
          it has a large head with long sharp teeth"
     width="400"
     height="341">
```

```
<figure>
  <img src="images/dinosaur.jpg"
       alt="The head and torso of a dinosaur skeleton;
            it has a large head with long sharp teeth"
       width="400"
       height="341">

  <figcaption>A T-Rex on display in the Manchester University Museum.</figcaption>
</figure>
```

### 视频处理
```
<video src="rabbit320.webm" controls>
  <p>Your browser doesn't support HTML5 video. Here is a <a href="rabbit320.webm">link to the video</a> instead.</p>
</video>
```

# CSS
CSS（层叠样式表）允许您创建漂亮的网页

# Javascript
JavaScript 是一种脚本或编程语言，它允许您在网页上实现复杂的功能——每次网页所做的不仅仅是停留在那里并显示静态信息供您查看——显示及时的内容更新、交互式地图、动画 2D/ 3D 图形、滚动视频点唱机等

第四天
今天主要学习一下，教程中的实例

第五天
今天主要学习一下，教程中的js实例



1. Document 获取文档中的内容，接口如下
https://developer.mozilla.org/zh-CN/docs/Web/API/Document

2. ## Window 对象
3. prompt alert confirm
alert() 弹出个提示框 （确定）  
confirm() 弹出个确认框 （确定，取消）  
prompt() 弹出个输入框 让你输入东西

警告消息框  
alert 方法有一个参数，即希望对用户显示的文本字符串。该字符串不是 HTML 格式。该消息框提供了一个“确定”按钮让用户关闭该消息框，并且该消息框是模式对话框，也就是说，用户必须先关闭该消息框然后才能继续进行操作。

var truthBeTold = confirm("单击“确定”继续。单击“取消”停止。");  
if (truthBeTold) {  
window.alert("欢迎访问我们的 Web 页！");  
} else window.alert("再见啦！");  


提示消息框  
提示消息框提供了一个文本字段，用户可以在此字段输入一个答案来响应您的提示。该消息框有一个“确定”按钮和一个“取消”按钮。如果您提供了一个辅助字符串参数，则提示消息框将在文本字段显示该辅助字符串作为默认响应。否则，默认文本为 "<undefined>"。




<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2NzExOTg1OTcsLTE5NDI4Njk5MTIsLT
E1NzkxMjE0MjIsLTExODk0MzU4MTgsNjUyMjcwODM1LC05MDQx
MDk3NDgsMjA0MjUyMDY1OSwxOTQ3Mjg0NDYxLC0xMzM4NDYwMD
M5LC0xNjgwNzUxMDc1LC0xMzgyNTM3ODIzLDEyNjcxNTE2Mzks
LTIwODgxNDE1NzAsLTE3NDM2MTQ5NjcsLTE1NzIxNDY5NzUsLT
c2MzI1Njk5OCwxNDQwODM0OTk4LDE3ODk3NDYzNDMsLTk3NTQw
NTY4NywxMDY4MDUxNzA5XX0=
-->