import psutil
import datetime
from typing import Dict, Any

def bytes_to_gb(bytes_val : int) -> float:
    """Convert bytes to GB with rounded of to 2 decimal"""
    return (bytes_val / (1024 ** 3),2)

def get_cpu_metrics() -> Dict[str, Any]:
    """Get CPU usages metrics.."""
    return {
        "usage_percentage": psutil.cpu_percent(interval=1),
        "core_count": psutil.cpu_count(),
        "core_count_logical": psutil.cpu_count(logical=True),
    }

def get_memory_metrics() -> Dict[str, Any]:
    """Get memory metrics.."""
    memory = psutil.virtual_memory()
    return{
        "total_memory": bytes_to_gb(memory.total),
        "memory_availabel": bytes_to_gb(memory.available),
        "memory_usage": bytes_to_gb(memory.used),
        "usage_percent": memory.percent,
    }

def get_disk_metrics() -> Dict[str,Any]:
    """Get disk usage metrics.."""
    disk = psutil.disk_usage('/')
    return {
        "total_gb": bytes_to_gb(disk.total),
        "used_gb": bytes_to_gb(disk.used),
        "free_gb": bytes_to_gb(disk.free),
        "usage_percent": disk.percent,
    }

def get_all_metrics() -> Dict[str,Any]:
    """Get all system metrics in one call."""
    return {
        "timestamp": datetime.datetime.now().isoformat(),
        "cpu": get_cpu_metrics(),
        "memory": get_memory_metrics(),
        "disk": get_disk_metrics(),
    }
