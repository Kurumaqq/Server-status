import psutil

class Server():
    @property
    def cpu_used(self):
        return psutil.cpu_percent(interval=1)

    @property
    def memory_used(self):
        mem = psutil.virtual_memory()
        return self.to_GB(mem.used)
    
    @property
    def memory_free(self):
        mem = psutil.virtual_memory()
        return self.to_GB(mem.free)

    @property
    def memory_percent(self):
        mem = psutil.virtual_memory()
        used = self.to_GB(mem.used)
        total = self.to_GB(mem.total)
        return round((used / total * 100), 2)

    def to_GB(self, value, dec=2):
        return round(value / (1024 ** 3), dec)
