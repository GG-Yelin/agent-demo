# 将所有工具函数放入一个字典，方便后续调用
from tool.attraction import get_attraction
from tool.weather import get_weather

available_tools = {
    "get_weather": get_weather,
    "get_attraction": get_attraction,
}
