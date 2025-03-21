import json

class Securitylog:
    def __init__ (self, timestamp__, ip_adress__, threat_level__, message__):
        self.timestamp = timestamp__
        self.ip_adress = ip_adress__
        self.threat_level__ = threat_level__
        self.message__ = message__

def is_suspicious(list_of_suspicious_ip, ip_adress):
    if ip_adress in list_of_suspicious_ip:
        print("True. The level of threat: High")
    
    else:
        print("False. The level of threat: Low")

list_of_suspicious_ip = ['51.156.160.34', '46.168.135.165', '113.121.88.198', '61.246.211.251']
ip_adress = input("Podaj adres IP:")

is_suspicious(list_of_suspicious_ip, ip_adress)

class Logs:
    def __init__ (self, date__, time__, ip__, status__):
        self.date = date__
        self.time = time__
        self.ip = ip__
        self.status = status__

to_json = Logs('2025-02-16','12:01:23','192.168.1.10','FAILED')

with open("plik.json", "w") as plik:
    json_string = json.dumps(to_json.__dict__, indent=4)
    plik.write(json_string)


