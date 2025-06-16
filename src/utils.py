from src.config import Config
from src.server import Server
import subprocess

server = Server()
config = Config()

def server_status() -> str:
    cpu = server.cpu_used
    mem = server.memory_used
    mem_pct = server.memory_percent
    mem_total = server.memory_total
    disk = server.disk_used
    disk_total = server.disk_total
    disk_pct = server.disk_percent

    return (
        "🖥️ *Server status* 🖥️\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        f"⚡ CPU:   {status_bar(cpu)} {cpu}%\n"
        f"🧠 Mem:  {status_bar(mem_pct)} {mem}GB | {mem_total}GB\n"
        f"💾 DISK: {status_bar(disk_pct)} {disk}GB | {disk_total}GB\n"
        "━━━━━━━━━━━━━━━━━━━━━━"
    )

def status_bar(percent: int, max=10) -> str:
    progress_used = round(percent / 10)
    progress_free = max - progress_used

    return f'|{'█'*progress_used}{'░'*progress_free}|'

def services_status():
    text = ''
    servies =  server.services
    max_length = max(len(service) for service in servies)
    
    for service in servies:
        if service in config.ignore_service: continue 
        name = service.ljust(max_length)
        active = check_active(service)
        text += f'{name}  →  {active}\n'
    
    return f'```\n{text}\n```'  

def check_active(service_name: str, as_text=True) -> str | bool:
    result = subprocess.run(
        ['systemctl', 'is-active', service_name],
        capture_output=True,
        text=True
    ).stdout.strip() == 'active'

    if not as_text: return result
    return '🟢 Active' if result else '🔴 Inactive'

def check_perm(user_id: int): return user_id == config.own_chat
