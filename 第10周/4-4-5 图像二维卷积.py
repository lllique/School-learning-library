from PIL import Image  # pillow
import numpy as np
from scipy import signal, misc

# 打开图像
im = Image.open("1.jpg")
# 剪裁为480*480
box = (round(im.width / 2 - 240, 0),
       round(im.height / 2 - 240, 0),
       round(im.width / 2 + 240, 0),
       round(im.height / 2 + 240, 0))
crop_im = im.crop(box)
# 图像转为灰度
bw_crop_im = crop_im.convert('L')
print('size', crop_im.size)
# 图像转为数组
crop = np.array(bw_crop_im)
print(crop)
# 卷积核
# 低通（模糊）
filter1 = np.array([[1 / 9, 1 / 9, 1 / 9],
                    [1 / 9, 1 / 9, 1 / 9],
                    [1 / 9, 1 / 9, 1 / 9]])
# 锐化
sharpen_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
# 卷积
grad = signal.convolve2d(crop, filter1, boundary='symm', mode='same')

# 数组转为图像
new_im = Image.fromarray(np.array(grad))
# 把新旧图像拼接一下
to_image = Image.new('RGB', (480 * 2, 480))
to_image.paste(bw_crop_im, (0, 0))
to_image.paste(new_im, (481, 0))
to_image.show()

'''
mode： str {‘full’, ‘valid’, ‘same’}，可选
指示输出大小的字符串：
    full
    输出是输入的完全离散线性卷积。 (默认)
    valid
    输出仅包含那些不依赖零填充的元素。在 ‘valid’ 模式中，in1 或 in2 在每个维度上都必须至少与另一个一样大。
    same
    输出与 in1 大小相同，以 ‘full’ 输出为中心。
boundary： str {‘fill’, ‘wrap’, ‘symm’}，可选
指示如何处理边界的标志（如何填充）：
    fill
    用填充值填充输入数组。 (默认)
    wrap
    圆形边界条件。
    symm
    对称边界条件。
'''
