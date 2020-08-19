import nmap3
from celery import shared_task

@shared_task
def scan_job(ip, arg):
    n = nmap3.Nmap()
    results = n.scan_top_ports(ip, args=arg)
    results['ip'] = ip
    return results
