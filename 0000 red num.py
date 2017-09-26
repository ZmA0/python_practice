#coding:utf-8
'''
将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
'''
from PIL import Image,ImageDraw,ImageFont
def add_num(img):
    draw=ImageDraw.Draw(img)
    myfont=ImageFont.truetype('C:/windows/fonts/Arial.ttf',size=40)#windows中默认的字体设置
    fillcolor="#ff0000"#纯红色
    width,height=img.size
    draw.text((width-40,0),'1',font=myfont,fill=fillcolor)
    img.save('1.png','png')#保存为同名文件
    return 0
if __name__=='__main__':
    image=Image.open('1.png')
    add_num(image)
