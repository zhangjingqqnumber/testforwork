#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用SVG生成圆柱体
通过Python代码生成SVG格式的圆柱体图像
"""

def generate_cylinder_svg(width=400, height=300, radius=80, cylinder_height=200):
    """
    生成圆柱体的SVG内容
    
    参数:
        width: SVG画布宽度
        height: SVG画布高度
        radius: 圆柱体半径
        cylinder_height: 圆柱体高度
    """
    
    # 计算圆柱体中心位置
    cx = width / 2
    cy = (height - cylinder_height) / 2
    
    # 椭圆顶部和底部中心
    top_ellipse_center_y = cy
    bottom_ellipse_center_y = cy + cylinder_height
    
    # 创建SVG内容
    svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" 
     width="{width}" height="{height}" 
     viewBox="0 0 {width} {height}">
  
  <!-- 定义渐变 -->
  <defs>
    <linearGradient id="cylinderGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#b0c4de;stop-opacity:1" />
      <stop offset="50%" style="stop-color:#e8f4f8;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#b0c4de;stop-opacity:1" />
    </linearGradient>
    
    <linearGradient id="topGradient" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#f0f8ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#d0e8f0;stop-opacity:1" />
    </linearGradient>
  </defs>
  
  <!-- 圆柱体背景（可选） -->
  <rect width="{width}" height="{height}" fill="#f5f5f5"/>
  
  <!-- 圆柱体后部（底部椭圆的后半部分） -->
  <ellipse cx="{cx}" cy="{bottom_ellipse_center_y}" 
           rx="{radius}" ry="{radius * 0.3}" 
           fill="#a0b4c8" />
  
  <!-- 圆柱体侧面 -->
  <rect x="{cx - radius}" y="{top_ellipse_center_y}" 
        width="{radius * 2}" height="{cylinder_height}" 
        fill="url(#cylinderGradient)" />
  
  <!-- 圆柱体顶部椭圆 -->
  <ellipse cx="{cx}" cy="{top_ellipse_center_y}" 
           rx="{radius}" ry="{radius * 0.3}" 
           fill="url(#topGradient)" 
           stroke="#88a0b8" stroke-width="1" />
  
  <!-- 圆柱体底部椭圆的前半部分（可见部分） -->
  <path d="M {cx - radius},{bottom_ellipse_center_y} 
           A {radius},{radius * 0.3} 0 0,1 {cx + radius},{bottom_ellipse_center_y}" 
        fill="none" stroke="#88a0b8" stroke-width="1" />
  
  <!-- 侧面轮廓线 -->
  <line x1="{cx - radius}" y1="{top_ellipse_center_y}" 
        x2="{cx - radius}" y2="{bottom_ellipse_center_y}" 
        stroke="#88a0b8" stroke-width="1" />
  <line x1="{cx + radius}" y1="{top_ellipse_center_y}" 
        x2="{cx + radius}" y2="{bottom_ellipse_center_y}" 
        stroke="#88a0b8" stroke-width="1" />
  
  <!-- 标题 -->
  <text x="{width/2}" y="30" text-anchor="middle" 
        font-family="Arial, sans-serif" font-size="18" fill="#333">
    圆柱体 (Cylinder)
  </text>
  
  <!-- 标注尺寸 -->
  <text x="{width/2}" y="{height - 20}" text-anchor="middle" 
        font-family="Arial, sans-serif" font-size="12" fill="#666">
    SVG Generated Cylinder
  </text>
  
</svg>'''
    
    return svg_content


def main():
    # 生成SVG内容
    svg_content = generate_cylinder_svg(
        width=500,
        height=400,
        radius=100,
        cylinder_height=250
    )
    
    # 保存到文件
    with open('cylinder.svg', 'w', encoding='utf-8') as f:
        f.write(svg_content)
    
    print("圆柱体SVG图像已保存为 cylinder.svg")
    
    # 也可以打印SVG内容到控制台
    # print(svg_content)


if __name__ == '__main__':
    main()
