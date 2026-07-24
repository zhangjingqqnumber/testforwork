#!/usr/bin/env python3
"""
正弦波生成器
生成正弦波数据并可选地绘制波形图
"""

import numpy as np
import matplotlib.pyplot as plt


def generate_sine_wave(frequency=1.0, amplitude=1.0, phase=0.0, duration=1.0, sample_rate=1000):
    """
    生成正弦波数据
    
    参数:
        frequency: 频率 (Hz)，默认 1.0 Hz
        amplitude: 振幅，默认 1.0
        phase: 相位 (弧度)，默认 0.0
        duration: 持续时间 (秒)，默认 1.0 秒
        sample_rate: 采样率 (Hz)，默认 1000 Hz
    
    返回:
        t: 时间数组
        y: 正弦波数据数组
    """
    # 生成时间数组
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    
    # 生成正弦波: y = A * sin(2πft + φ)
    y = amplitude * np.sin(2 * np.pi * frequency * t + phase)
    
    return t, y


def plot_sine_wave(t, y, frequency=1.0, amplitude=1.0, phase=0.0):
    """
    绘制正弦波图形
    
    参数:
        t: 时间数组
        y: 正弦波数据数组
        frequency: 频率 (Hz)
        amplitude: 振幅
        phase: 相位 (弧度)
    """
    plt.figure(figsize=(10, 6))
    plt.plot(t, y, linewidth=1.5, label=f'{frequency} Hz')
    plt.xlabel('时间 (秒)')
    plt.ylabel('振幅')
    plt.title(f'正弦波 (频率={frequency}Hz, 振幅={amplitude}, 相位={phase:.2f} rad)')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.tight_layout()
    plt.savefig('sine_wave.png', dpi=150)
    print("正弦波图像已保存为 'sine_wave.png'")
    plt.show()


def main():
    """主函数：演示正弦波生成"""
    print("=" * 50)
    print("正弦波生成器")
    print("=" * 50)
    
    # 参数设置
    frequency = 2.0      # 2 Hz
    amplitude = 1.0      # 振幅 1.0
    phase = 0.0          # 无相位偏移
    duration = 2.0       # 2 秒
    sample_rate = 1000   # 1000 Hz 采样率
    
    print(f"\n参数设置:")
    print(f"  频率: {frequency} Hz")
    print(f"  振幅: {amplitude}")
    print(f"  相位: {phase:.2f} 弧度")
    print(f"  持续时间: {duration} 秒")
    print(f"  采样率: {sample_rate} Hz")
    
    # 生成正弦波
    t, y = generate_sine_wave(
        frequency=frequency,
        amplitude=amplitude,
        phase=phase,
        duration=duration,
        sample_rate=sample_rate
    )
    
    print(f"\n生成了 {len(y)} 个采样点")
    print(f"时间范围: {t[0]:.3f} - {t[-1]:.3f} 秒")
    print(f"数据范围: {y.min():.3f} - {y.max():.3f}")
    
    # 显示前 10 个数据点
    print("\n前 10 个数据点:")
    for i in range(10):
        print(f"  t={t[i]:.4f}s, y={y[i]:.6f}")
    
    # 绘制波形
    try:
        plot_sine_wave(t, y, frequency, amplitude, phase)
    except Exception as e:
        print(f"\n注意: 无法显示图形 (可能需要 GUI 环境): {e}")
        print("但数据已成功生成，可保存为文件使用")
    
    # 保存数据到 CSV 文件
    np.savetxt('sine_wave_data.csv', np.column_stack([t, y]), 
               delimiter=',', header='time,amplitude', comments='')
    print("\n正弦波数据已保存为 'sine_wave_data.csv'")


if __name__ == "__main__":
    main()
