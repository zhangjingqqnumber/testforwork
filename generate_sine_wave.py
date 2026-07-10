#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成正弦波图像
使用matplotlib库绘制正弦波
"""

import numpy as np
import matplotlib.pyplot as plt

# 生成数据
x = np.linspace(0, 2 * np.pi, 1000)  # 从0到2π，1000个点
y = np.sin(x)  # 计算正弦值

# 创建图形
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label='sin(x)')

# 设置标题和标签
plt.title('正弦波 (Sine Wave)', fontsize=16, fontproperties='SimHei')
plt.xlabel('x (弧度)', fontsize=12, fontproperties='SimHei')
plt.ylabel('sin(x)', fontsize=12, fontproperties='SimHei')

# 添加网格
plt.grid(True, alpha=0.3)

# 添加图例
plt.legend(prop={'family': 'SimHei', 'size': 12})

# 设置x轴刻度为π的倍数
plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
           ['0', 'π/2', 'π', '3π/2', '2π'])

# 调整布局
plt.tight_layout()

# 保存图像
plt.savefig('sine_wave.png', dpi=300, bbox_inches='tight')
print("正弦波图像已保存为 sine_wave.png")

# 显示图像（如果在有GUI的环境中运行）
# plt.show()
