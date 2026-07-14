from flask import Flask, jsonify, request
import requests
from datetime import datetime

app = Flask(__name__)

# 使用 Open-Meteo 免费天气 API（无需 API key）
WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast"

@app.route('/api/weather', methods=['GET'])
def get_weather():
    """
    查询天气信息
    
    参数:
    - city: 城市名称（可选，用于显示）
    - latitude: 纬度（必需）
    - longitude: 经度（必需）
    - units: 单位制，metric(摄氏度) 或 imperial(华氏度)，默认 metric
    
    返回:
    - 当前天气信息和未来几天的预报
    """
    try:
        # 获取请求参数
        latitude = request.args.get('latitude')
        longitude = request.args.get('longitude')
        city = request.args.get('city', 'Unknown')
        units = request.args.get('units', 'metric')
        
        # 验证必需参数
        if not latitude or not longitude:
            return jsonify({
                'success': False,
                'error': '缺少必需参数：latitude 和 longitude'
            }), 400
        
        # 构建 API 请求参数
        params = {
            'latitude': latitude,
            'longitude': longitude,
            'current': 'temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m,wind_direction_10m',
            'daily': 'weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max',
            'timezone': 'auto',
            'forecast_days': 5
        }
        
        # 调用天气 API
        response = requests.get(WEATHER_API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # 解析并格式化返回数据
        current = data.get('current', {})
        daily = data.get('daily', {})
        
        weather_info = {
            'success': True,
            'data': {
                'location': {
                    'city': city,
                    'latitude': latitude,
                    'longitude': longitude
                },
                'current': {
                    'temperature': current.get('temperature_2m'),
                    'humidity': current.get('relative_humidity_2m'),
                    'weather_code': current.get('weather_code'),
                    'weather_description': get_weather_description(current.get('weather_code')),
                    'wind_speed': current.get('wind_speed_10m'),
                    'wind_direction': current.get('wind_direction_10m'),
                    'time': current.get('time')
                },
                'forecast': []
            }
        }
        
        # 添加天气预报
        if daily:
            for i in range(len(daily.get('time', []))):
                forecast_day = {
                    'date': daily['time'][i],
                    'weather_code': daily['weather_code'][i],
                    'weather_description': get_weather_description(daily['weather_code'][i]),
                    'temp_max': daily['temperature_2m_max'][i],
                    'temp_min': daily['temperature_2m_min'][i],
                    'precipitation_probability': daily['precipitation_probability_max'][i]
                }
                weather_info['data']['forecast'].append(forecast_day)
        
        return jsonify(weather_info), 200
        
    except requests.exceptions.RequestException as e:
        return jsonify({
            'success': False,
            'error': f'天气 API 请求失败: {str(e)}'
        }), 503
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'服务器错误: {str(e)}'
        }), 500


def get_weather_description(code):
    """根据 WMO 天气代码返回天气描述"""
    weather_codes = {
        0: '晴朗',
        1: '主要晴朗',
        2: '多云',
        3: '阴天',
        45: '雾',
        48: '沉积雾凇',
        51: '轻度毛毛雨',
        53: '中度毛毛雨',
        55: '重度毛毛雨',
        61: '轻度雨',
        63: '中度雨',
        65: '大雨',
        71: '轻度雪',
        73: '中度雪',
        75: '大雪',
        77: '雪粒',
        80: '轻度阵雨',
        81: '中度阵雨',
        82: '强阵雨',
        85: '轻度雪阵',
        86: '大雪阵',
        95: '雷雨',
        96: '雷暴伴轻度冰雹',
        99: '雷暴伴重度冰雹'
    }
    return weather_codes.get(code, '未知')


@app.route('/api/weather/city/<city_name>', methods=['GET'])
def get_weather_by_city(city_name):
    """
    通过城市名称查询天气（需要地理编码）
    
    注意：此端点需要地理编码服务将城市名转换为经纬度
    这里使用一个简单的示例实现
    """
    # 简单的城市坐标映射（实际应用中应使用地理编码 API）
    city_coordinates = {
        'beijing': {'lat': 39.9042, 'lon': 116.4074},
        'shanghai': {'lat': 31.2304, 'lon': 121.4737},
        'guangzhou': {'lat': 23.1291, 'lon': 113.2644},
        'shenzhen': {'lat': 22.5431, 'lon': 114.0579},
        'chengdu': {'lat': 30.5728, 'lon': 104.0668},
        'hangzhou': {'lat': 30.2741, 'lon': 120.1551},
        'newyork': {'lat': 40.7128, 'lon': -74.0060},
        'london': {'lat': 51.5074, 'lon': -0.1278},
        'tokyo': {'lat': 35.6762, 'lon': 139.6503}
    }
    
    city_lower = city_name.lower().replace(' ', '')
    
    if city_lower in city_coordinates:
        coords = city_coordinates[city_lower]
        # 重定向到主天气接口
        return get_weather()
    else:
        return jsonify({
            'success': False,
            'error': f'未找到城市: {city_name}，请使用 latitude 和 longitude 参数'
        }), 404


@app.route('/api/health', methods=['GET'])
def health_check():
    """健康检查端点"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'Weather API'
    }), 200


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5001)
