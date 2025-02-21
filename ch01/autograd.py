
import tensorflow as tf


# 创建4个张量
a = tf.constant(1.)
b = tf.constant(2.)
c = tf.constant(3.)
w = tf.constant(4.)


with tf.GradientTape() as tape:# 构建梯度环境
    # 将w加入梯度跟踪列表，只有添加到梯度跟踪列表才可以调用TensorFlow中自动求梯度的过程
    tape.watch([w])
    # 构建计算过程
    y = a * w**2 + b * w + c
# 求导
[dy_dw] = tape.gradient(y, [w])
print(dy_dw)
