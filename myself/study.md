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
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzMTQ1NDAyNjAsMTc4OTc0NjM0MywtOT
c1NDA1Njg3LDEwNjgwNTE3MDksLTY1ODAwMjQ0MiwtMTY2MTY3
MDczNCw0OTkwNDczMTYsLTYxOTYyNTgxNywtMTAxOTA0NDMyMy
w1MjU4MzQxMjMsMTMyMDYxODQ0MiwtMTAzODkwNTc4LDExNTE0
NTEyNjEsLTE1Njk2OTMzMzEsLTE2NjQzNDY3MzksLTIwODg3ND
Y2MTJdfQ==
-->