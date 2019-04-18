#-*-coding:utf-8-*-


from PIL import Image
import os
import sys
"""使用Py2，在Liunx中"""

def parser_image(input_image):
    try:
        image = Image.open(input_image)
    except AttributeError:
        print ('输入错误'+'\n'+'程序退出!')
        sys.exit()
    except FileNotFoundError:
        print ('输入路径错误'+'\n'+'程序退出!')
        sys.exit()
    else :
        L_image = image.convert('L')
        width,height = L_image.size
        print (width,height)
        image_resize = L_image.resize((int(width*0.5),int(height*0.5*0.5)))
        width,height = image_resize.size
        return width,height,image_resize

def to_asc(width,height,image_resize):
    str_asc = "@%#*+=-:. "
    result = ""
    print (width,height)
    for row in range(height):
        for col in range(width):
            print ('正在转换中*************')
            gray = image_resize.getpixel((col,row))
            result += str_asc[int(gray/255*9)]
        result += '\n'
    return result

def asc_to_file(input_name,result):
    with open(input_name+'.txt','w') as f:
        f.write(result)
        f.close()

def main():
    print ('E.g: /root/sb.jpg')
    input_image = input('input image Absolute address:')
    input_name = input('E.g: sb'+'\n'+'Please input image name:')
    width,height,image_resize = parser_image(input_image)
    result_file = to_asc(width,height,image_resize)
    asc_to_file(input_name,result_file)
    print ('转换成功!')
if __name__ == '__main__':
    main()
