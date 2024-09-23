import psutil
import time

# تابع برای خواندن دمای سیستم
def get_temperature():
    try:
        temps = psutil.sensors_temperatures()
        if not temps:
            print("سنسور دما یافت نشد.")
            return None
        
        # ممکن است بسته به نوع سیستم، نام سنسور متفاوت باشد. معمولاً 'coretemp' یا 'thermal_zone' استفاده می‌شود.
        for name, entries in temps.items():
            for entry in entries:
                if entry.label == '':
                    return entry.current
        return None
    except Exception as e:
        print(f"خطا در خواندن دما: {e}")
        return None

# تابع برای کنترل سیستم بر اساس دما
def control_temperature():
    # تعریف آستانه‌های دما
    MAX_TEMP = 70  # دما به سانتی‌گراد
    MIN_TEMP = 30

