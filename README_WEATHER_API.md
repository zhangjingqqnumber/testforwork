# 天气查询 API

一个基于 Flask 的天气查询接口，使用 Open-Meteo 免费天气 API（无需 API key）。

## 功能特性

- 查询当前位置天气信息
- 获取未来 5 天天气预报
- 支持经纬度定位
- 中文天气描述
- 健康检查端点

## 安装依赖

```bash
pip install -r requirements.txt
```

## 运行服务

```bash
python weather_api.py
```

服务将在 `http://localhost:5001` 启动。

## API 端点

### 1. 查询天气 (GET /api/weather)

**参数:**
- `latitude` (必需): 纬度
- `longitude` (必需): 经度
- `city` (可选): 城市名称，用于显示
- `units` (可选): 单位制，metric(摄氏度) 或 imperial(华氏度)，默认 metric

**示例:**
```bash
curl "http://localhost:5001/api/weather?latitude=39.9042&longitude=116.4074&city=Beijing"
```

**响应示例:**
```json
{
  "success": true,
  "data": {
    "location": {
      "city": "Beijing",
      "latitude": "39.9042",
      "longitude": "116.4074"
    },
    "current": {
      "temperature": 31.2,
      "humidity": 54,
      "weather_code": 3,
      "weather_description": "阴天",
      "wind_speed": 5.1,
      "wind_direction": 6,
      "time": "2026-07-14T11:45"
    },
    "forecast": [
      {
        "date": "2026-07-14",
        "weather_code": 3,
        "weather_description": "阴天",
        "temp_max": 32.6,
        "temp_min": 25.6,
        "precipitation_probability": 0
      }
    ]
  }
}
```

### 2. 通过城市名称查询 (GET /api/weather/city/<city_name>)

支持的城市：beijing, shanghai, guangzhou, shenzhen, chengdu, hangzhou, newyork, london, tokyo

**示例:**
```bash
curl "http://localhost:5001/api/weather/city/beijing"
```

### 3. 健康检查 (GET /api/health)

**示例:**
```bash
curl "http://localhost:5001/api/health"
```

**响应:**
```json
{
  "status": "healthy",
  "timestamp": "2026-07-14T03:49:56.310135",
  "service": "Weather API"
}
```

## 天气代码说明

| 代码 | 描述 |
|------|------|
| 0 | 晴朗 |
| 1 | 主要晴朗 |
| 2 | 多云 |
| 3 | 阴天 |
| 45-48 | 雾 |
| 51-55 | 毛毛雨 |
| 61-65 | 雨 |
| 71-77 | 雪 |
| 80-86 | 阵雨 |
| 95-99 | 雷雨 |

## 注意事项

- 本服务使用 Open-Meteo API，无需 API key
- 生产环境请关闭 debug 模式
- 可以根据需要修改端口号
