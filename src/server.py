from pathlib import Path
import psutil

class Server():
    @property
    def cpu_used(self) -> str: return psutil.cpu_percent(interval=1)

    @property
    def memory_used(self) -> str:
        mem = psutil.virtual_memory()
        return self.to_GB(mem.used)
    
    @property
    def memory_total(self) -> str:
        mem = psutil.virtual_memory()
        return self.to_GB(mem.total)

    @property
    def memory_percent(self) -> str:
        mem = psutil.virtual_memory()
        used = self.to_GB(mem.used)
        total = self.to_GB(mem.total)
        return round((used / total * 100), 2)

    @property
    def disk_used(self) -> str:
        disk = psutil.disk_usage('/')
        return self.to_GB(disk.used)

    @property
    def disk_total(self) -> str:
        disk = psutil.disk_usage('/')
        return self.to_GB(disk.total)

    @property
    def disk_percent(self) -> str:
        disk = psutil.disk_usage('/')
        used =  self.to_GB(disk.used)
        total = self.to_GB(disk.total)
        return round((used / total * 100), 2)

    @property
    def services(self) -> list:
        services_path = Path('/etc/systemd/system/')
        services_list = []
        for service in services_path.glob('*.service'):
            name = str(service).split('/')[-1]
            if name.count('.') == 1:
                services_list.append(name.split('.')[0])
        return services_list   

    def to_GB(self, value, dec=2) -> float:
        return round(value / (1024 ** 3), dec)
