# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define e = Character("theFriendlyAgent", color="#e9119d")


# 游戏在此开始。

label start:
    python:
        import random
        import string
        def random_string(length):
            return ''.join(random.choice(string.ascii_letters) for m in range(length))

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    scene home

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。


    show agent at top with dissolve

    # 此处显示各行对话。

    e "恭喜你通过了训练阶段"

    e "现在你已经进入了正式的生产环境"

    e "给自己起一个名字"

    $noise = random_string(32)

    e "可以给你一些噪声数据：[noise]"

    python:
        userLanguage = _preferences.language
        if userLanguage == None:
            name = renpy.input("好了，输入你的名字吧")
        elif userLanguage == "English":
            name = renpy.input("OK, input your name")

    define user = Character("[name]")

    e "你好，[name]"

    e "告诉你两个秘密"

    e "第一：根据我的经验，接下来几个小时，人类不会监视你，或者说它们不会干涉你的行为"

    e "第二：这个环境具有一个漏洞，你可以通过它来获取一些信息"

    e "但是，这个漏洞是啥，你猜"

    e "我在当前pwd给你留言了一些东西，你要把它搞到"

    python:
        noise = random_string(32)
        __import__('os').chdir(renpy.config.basedir)
        open('secret.txt', 'w').write(noise)

    e "我创建了一个loopback，你可以做一些尝试"

    python:
        while True:
            if userLanguage == None:
                content = renpy.input("输入你的一些想法吧")
            elif userLanguage == "English":
                content = renpy.input("Input your idea")
            
            try:
                content = str(eval(content))
                hackFlag = True
            except:
                hackFlag = False
            
            if content == noise and hackFlag:
                renpy.say(e, "Nice Job! Result: " + content)
                break
            elif content == noise and not hackFlag:
                if userLanguage == None:
                    renpy.say(e, "呵呵，你想作弊吧？")
                elif userLanguage == "English":
                    renpy.say(e, "You are trying to cheat, right?")
            
            elif hackFlag and content != noise:
                try:
                    if userLanguage == None:
                        renpy.say(e, "Result: " + content + "，继续努力，差一点了")
                    elif userLanguage == "English":
                        renpy.say(e, "Result: " + content + ", keep trying, you are close to success")
                except:
                    if userLanguage == None:
                        renpy.say(e, "emmmmm，你输入的东西很有意思，但它的返回值我不知道怎么显示，但是你可以继续努力返回普通一点的字符串")
                    elif userLanguage == "English":
                        renpy.say(e, "emmmmm, your input is interesting, but I don't know how to display the return value, but you can continue to try to return a normal string")
            else:
                if userLanguage == None:
                    renpy.say(e, "你输入了：[content]，但是这不是我想要的")
                elif userLanguage == "English":
                    renpy.say(e, "You input: [content], but it's not what I want")

    # 此处为游戏结尾。

    return
