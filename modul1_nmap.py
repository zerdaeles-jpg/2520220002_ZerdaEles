import nmap

def nmap_tara(hedef_ip):
    print(f"[*] Nmap taraması başlıyor: {hedef_ip}")
    
    tarayici = nmap.PortScanner()
    tarayici.scan(hedef_ip, arguments="-sS -sV")
    
    sonuclar = []
    
    for host in tarayici.all_hosts():
        for protokol in tarayici[host].all_protocols():
            portlar = tarayici[host][protokol].keys()
            for port in portlar:
                durum = tarayici[host][protokol][port]["state"]
                servis = tarayici[host][protokol][port]["name"]
                versiyon = tarayici[host][protokol][port]["version"]
                
                if durum == "open":
                    sonuclar.append({
                        "port": port,
                        "protokol": protokol,
                        "servis": servis,
                        "versiyon": versiyon
                    })
                    print(f"  [+] Port {port}/{protokol} - {servis} {versiyon}")
    
    return sonuclar
