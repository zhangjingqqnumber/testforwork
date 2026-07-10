# 图形生成项目

本项目包含两个 Python 脚本，分别用于生成正弦波图像和 SVG 格式的圆柱体。

## 文件说明

### 1. generate_sine_wave.py
使用 matplotlib 库生成正弦波图像。

**功能特点：**
- 生成从 0 到 2π 的正弦波
- 使用 1000 个采样点确保曲线平滑
- x 轴刻度标记为 π 的倍数（0, π/2, π, 3π/2, 2π）
- 添加网格线和图例
- 输出高分辨率 PNG 图像（300 DPI）

**使用方法：**
```bash
python generate_sine_wave.py
```

**输出文件：**
- `sine_wave.png` - 正弦波图像

**依赖库：**
```bash
pip install numpy matplotlib
```

---

### 2. generate_cylinder_svg.py
使用 Python 生成 SVG 格式的圆柱体图像。

**功能特点：**
- 纯代码生成 SVG 矢量图形
- 使用渐变填充模拟光照效果
- 包含顶部椭圆、侧面和底部轮廓
- 可自定义尺寸参数（宽度、高度、半径等）

**使用方法：**
```bash
python generate_cylinder_svg.py
```

**输出文件：**
- `cylinder.svg` - 圆柱体 SVG 图像

**依赖库：**
- 仅需 Python 标准库，无需额外安装

---

## 运行环境

- Python 3.6+
- 对于正弦波生成：numpy, matplotlib
- 对于 SVG 圆柱体：无额外依赖

## 示例输出

运行脚本后，将在当前目录生成以下文件：
- `sine_wave.png` - 正弦波 PNG 图像
- `cylinder.svg` - 圆柱体 SVG 矢量图

SVG 文件可以用浏览器或任何支持 SVG 的查看器打开。

## 许可证

MIT License