import requests

def web_header_analiz(hedef_ip):
    print(f"[*] Web header analizi başlıyor: {hedef_ip}")
    
    sonuclar = []
    
    for protokol in ["http", "https"]:
        try:
            url = f"{protokol}://{hedef_ip}"
            yanit = requests.get(url, timeout=5, verify=False)
            
            print(f"  [+] {url} - Durum: {yanit.status_code}")
            
            guvenlik_basliklar = [
                "X-Frame-Options",
                "X-XSS-Protection", 
                "X-Content-Type-Options",
                "Strict-Transport-Security",
                "Content-Security-Policy",
                "Referrer-Policy"
            ]
            
            bulunan = {}
            eksik = []
            
            for baslik in guvenlik_basliklar:
                if baslik in yanit.headers:
                    bulunan[baslik] = yanit.headers[baslik]
                    print(f"    [✓] {baslik}: {yanit.headers[baslik]}")
                else:
                    eksik.append(baslik)
                    print(f"    [✗] {baslik}: EKSİK")
            
            sonuclar.append({
                "url": url,
                "durum_kodu": yanit.status_code,
                "bulunan_basliklar": bulunan,
                "eksik_basliklar": eksik,
                "tum_basliklar": dict(yanit.headers)
            })
            
        except Exception as e:
            print(f"  [-] {protokol} bağlantı hatası: {e}")
    
    return sonuclar
