#-*coding:utf-8*-

#from img_ASC import main
import MaHaiTao.img_ASC
import MaHaiTao.douban_TOP250
import MaHaiTao.house_money
import MaHaiTao.WYmusic_Comment
import MaHaiTao.Maoyan

print('1:img_ASC')
print('2:爬虫-豆瓣电影top250信息排名')
print('3:爬虫-房价')
print('4:爬虫-网易云音乐歌曲评论')
print('5:爬虫-猫眼电影top250信息排名')
print ('**************************************************************************************************')

def offset(choose):
    if choose == 1:
        MaHaiTao.img_ASC.main()
    elif choose == 2:
        MaHaiTao.douban_TOP250.main()
    elif choose == 3:
        MaHaiTao.house_money.main()
    elif choose == 4:
        MaHaiTao.WYmusic_Comment.main()
    elif choose == 5:
        MaHaiTao.Maoyan.main()
    else :
        print ('暂无！')
def main():
    while True:
        try:
            choose = int(input('输入数字,执行想要的程序：'))
        except ValueError :
            print ('输入错误，重新输入：')
        else:
            offset(choose)
if __name__=="__main__":
    main()
