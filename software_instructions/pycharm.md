# Pycharm 使用帮助

## 1. pycharm 文档翻译

如果你需要阅读英文源码、翻译变量名，或者将中文注释翻译成英文，最强大的工具是 "Translation" 插件。

    1.1. 安装步骤
        1. 打开 PyCharm，点击左上角的 File (macOS 为 PyCharm) > Settings (macOS 为 Preferences)。

        2. 在左侧菜单栏选择 Plugins (插件)。
        3. 在顶部搜索栏输入 Translation。
        4. 找到下载量最高、名字就叫 Translation 的插件（作者通常显示为 Yii.Guxing），点击 Install。
        5. 安装完成后，点击 Restart IDE 重启 PyCharm。

    1.2. 如何使用
    划词翻译： 选中代码中的单词或句子，按下快捷键 Ctrl + Shift + Y (Windows/Linux) 或 Cmd + Shift + Y (macOS)。

    右键菜单： 选中内容后点击鼠标右键，选择 Translate。

    文档翻译： 鼠标悬停在类或函数上显示文档弹窗时，点击弹窗右上角的翻译图标即可。

    1.3 进阶配置
    该插件默认使用 Google 翻译（通常无需配置即可使用）。如果遇到网络问题，你可以在 Settings > Tools > Translation 中切换翻译引擎