# encoding:utf-8
import os
from PIL import Image
import numpy as np
import imghdr


class CONF:
    input_path = "input_img"  # 待处理的图片存放的位置
    output_path = "output_img"  # 去除水印后的图片存放位置
    level_black = 108  # 用于去除水印的特征值
    level_white = 170  # 用于去除水印的特征值
    is_log = True  # 是否打印日志信息


class DocWipe:
    def __init__(self, input_path, output_path, level_black, level_white, is_log):
        self.input_path = input_path
        self.output_path = output_path
        self.level_black = level_black
        self.level_white = level_white
        self.is_log = is_log

    """ 初始化 """

    @classmethod
    def initialize(cls, config):
        input_path = config.input_path
        output_path = config.output_path
        level_black = config.level_black
        level_white = config.level_white
        is_log = config.is_log
        return cls(input_path, output_path, level_black, level_white, is_log)


""" 主流程 """


def wipe_process(self, ):
    if os.path.exists(self.input_path) and os.path.isdir(self.output_path):
        self.visit_dir_files(self.input_path, self.output_path, self.input_path)
        if self.is_log:
            print(u'完成！所有图片已保存至路径' + self.output_path)
    else:
        print(u'待处理的图片存放的位置 %s, 如果没有请新建目录 %s' % (self.input_path, self.input_path))
        print(u'去除水印后的图片存放位置 %s, 如果没有请新建目录 %s' % (self.output_path, self.output_path))


""" 图片处理 """


def img_deal(self, img_path, save_path):
    img = Image.open(img_path)
    img = self.levels_deal(img, self.level_black, self.level_white)
    img_res = Image.fromarray(img.astype('uint8'))
    if self.is_log:
        print(u'图片[' + img_path + u']处理完毕')
    img_res.save(save_path)


""" 图像矩阵处理 """


def levels_deal(self, img, black, white):
    if white > 255:
        white = 255
    if black < 0:
        black = 0
    if black >= white:
        black = white - 2
    img_array = np.array(img, dtype=int)
    c_rate = -(white - black) / 255.0 * 0.05
    rgb_diff = np.maximum(img_array - black, 0)
    img_array = np.around(rgb_diff * c_rate, 0)
    img_array = img_array.astype(int)
    return img_array


""" 创建文件夹 """


def mkdir(self, path):
    path = path.strip().rstrip("\\")
    is_exists = os.path.exists(path)
    if not is_exists:
        os.makedirs(path)
        return True
    else:
        return False


""" 递归访问文件/文件夹 """


def visit_dir_files(self, org_input_dir, org_output_dir, recursion_dir):
    single_file = False
    if os.path.isdir(recursion_dir):
        dir_list = os.listdir(recursion_dir)
    else:
        dir_list = [recursion_dir]
        single_file = True
    for i in range(0, len(dir_list)):
        path = os.path.join(recursion_dir, dir_list[i])
        if os.path.isdir(path):
            self.visit_dir_files(org_input_dir, org_output_dir, path)
        else:
            if imghdr.what(path):
                abs_output_dir = org_output_dir + recursion_dir[len(org_input_dir):]
                target_path = os.path.join(abs_output_dir, dir_list[i])
                if single_file:
                    target_path = os.path.join(org_output_dir, os.path.basename(dir_list[i]))
                target_dir_name = os.path.dirname(target_path)
                if not os.path.exists(target_dir_name):
                    self.mkdir(target_dir_name)
                self.img_deal(path, target_path)


if __name__ == '__main__':
    # 对象初始化
    doc_wipe = DocWipe.initialize(config=CONF)
    # 调用主流程
    doc_wipe.wipe_process()
