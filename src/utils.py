from src.server import Server
from pathlib import Path

server = Server()

def get_status_server():
    return f'''
CPU: {server.cpu_used} %
Memory used: {server.memory_used}GB ({server.memory_percent}%)
 '''

def get_services():
    services_path = Path('/etc/systemd/system/')
    services_list = []
    for service in services_path.glob('*.service'):
        name = str(service).split('/')[-1]
        if name.count('.') == 1:
            services_list.append(name.split('.')[0])
    return services_list

