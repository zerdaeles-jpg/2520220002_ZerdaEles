from jinja2 import Template
from datetime import datetime

def rapor_olustur(hedef_ip, nmap_sonuc, header_sonuc, ai_sonuc):
    print("[*] HTML rapor oluşturuluyor...")
    
    template = Template("""
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Güvenlik Tarama Raporu</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
        h1 { color: #d32f2f; }
        h2 { color: #1565c0; border-bottom: 2px solid #1565c0; }
        table { width: 100%; border-collapse: collapse; background: white; }
        th { background: #1565c0; color: white; padding: 10px; }
        td { padding: 8px; border: 1px solid #ddd; }
        .eksik { color: red; font-weight: bold; }
        .var { color: green; }
        .ai-analiz { background: white; padding: 20px; border-left: 4px solid #d32f2f; }
        .bilgi { background: #e3f2fd; padding: 10px; border-radius: 5px; }
    </style>
</head>
<body>
    <h1>🔒 Siber Güvenlik Tarama Raporu</h1>
    <div class="bilgi">
        <b>Hedef IP:</b> {{ hedef_ip }}<br>
        <b>Tarih:</b> {{ tarih }}
    </div>

    <h2>📡 Nmap Port Tarama Sonuçları</h2>
    <table>
        <tr><th>Port</th><th>Protokol</th><th>Servis</th><th>Versiyon</th></tr>
        {% for port in nmap_sonuc %}
        <tr>
            <td>{{ port.port }}</td>
            <td>{{ port.protokol }}</td>
            <td>{{ port.servis }}</td>
            <td>{{ port.versiyon }}</td>
        </tr>
        {% endfor %}
    </table>

    <h2>🌐 Web Header Analizi</h2>
    {% for sonuc in header_sonuc %}
    <h3>{{ sonuc.url }} - HTTP {{ sonuc.durum_kodu }}</h3>
    <table>
        <tr><th>Başlık</th><th>Durum</th><th>Değer</th></tr>
        {% for baslik in sonuc.eksik_basliklar %}
        <tr>
            <td>{{ baslik }}</td>
            <td class="eksik">✗ EKSİK</td>
            <td>-</td>
        </tr>
        {% endfor %}
        {% for baslik, deger in sonuc.bulunan_basliklar.items() %}
        <tr>
            <td>{{ baslik }}</td>
            <td class="var">✓ VAR</td>
            <td>{{ deger }}</td>
        </tr>
        {% endfor %}
    </table>
    {% endfor %}

    <h2>🤖 AI Risk Analizi</h2>
    <div class="ai-analiz">
        <pre>{{ ai_sonuc }}</pre>
    </div>
</body>
</html>
    """)
    
    html = template.render(
        hedef_ip=hedef_ip,
        tarih=datetime.now().strftime("%d/%m/%Y %H:%M"),
        nmap_sonuc=nmap_sonuc,
        header_sonuc=header_sonuc,
        ai_sonuc=ai_sonuc
    )
    
    with open("rapor.html", "w", encoding="utf-8") as f:
        f.write(html)
