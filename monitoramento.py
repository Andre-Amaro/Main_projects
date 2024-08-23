"""
Construi esse simples aplicação para ajudar no monitoramento da rede durante meu plantão na empresa onde trabalho usando um webhook do discord para gerar as notificações

"""

import requests as rq
import json
import subprocess as sp
import csv
import os
import threading
#discord bot
def discord_bot(name):
    bot_command = f'{name} está down!'
    #discord bot notification
    webhook_url = 'Your API Key'
     
    data = {
        'content': f'{bot_command}'
        }
    headers = {
        'Content-Type': 'application/json'
        }
    response = rq.post(webhook_url, data=json.dumps(data), headers=headers)
#subprocess checking is host is up while handler the exception 
def check_host(ip):
    try:
        sp.check_output(['ping','-n','4', ip] ,creationflags=sp.CREATE_NO_WINDOW)
        return True
    except sp.CalledProcessError:
        return False
    
#test and mixing discord with the monitoring
def monitor_hosts(hosts):
    for name, ip in hosts:
        if check_host(ip):
           pass
        else:
            discord_bot(name)


def monitoring():

    folder_path = 'YOUR DATA PATH'
    file_name = 'HOSTS.csv'
    file_path = os.path.join(folder_path, file_name)
    with open(file_path,'r')as f:
        csv_reader = csv.DictReader(f) #transforming it into dictionary
        csv_final = [(x['routers'], x['ips']) for x in csv_reader] #creating a list with hosts name and ips
        
    num_threads = 5 # Number of threads to use
    threads = []
    chunk_size = len(csv_final) // num_threads #creating a average between threads and the len of the list 

    # creating and starting threads
    for i in range(num_threads):
        start_index = i * chunk_size
        end_index = (i + 1) * chunk_size
        thread = threading.Thread(target=monitor_hosts, args=(csv_final[start_index:end_index],))
        threads.append(thread)
        thread.start()

    # waiting for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    monitoring()

