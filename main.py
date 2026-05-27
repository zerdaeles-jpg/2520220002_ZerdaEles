import os
from dotenv import load_dotenv
from groq import Groq
from modul1_nmap import nmap_tara
from secmeli_modul import web_header_analiz
from rapor import rapor_olustur

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ai_analiz(nmap_sonuc, header_sonuc):
    print("[*] AI analizi yapılıyor...")
    
    prompt = f"""
    Aşağıdaki siber güvenlik tarama sonuçlarını Türkçe olarak analiz et.
    Risk seviyelerini belirt ve öneriler sun.
    
    NMAP SONUÇLARI:
    {nmap_sonuc}
    
    WEB HEADER SONUÇLARI:
    {header_sonuc}
    
    Analiz formatı:
    1. Genel Risk Değerlendirmesi
    2. Kritik Bulgular
    3. Öneriler
    """
    
    yanit = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return yanit.choices[0].message.content

def main():
    hedef_ip = input("Hedef IP adresini girin: ")
    
    print("\n=== TARAMA BAŞLIYOR ===\n")
    
    nmap_sonuc = nmap_tara(hedef_ip)
    header_sonuc = web_header_analiz(hedef_ip)
    ai_sonuc = ai_analiz(nmap_sonuc, header_sonuc)
    
    print("\n=== AI ANALİZİ ===")
    print(ai_sonuc)
    
    rapor_olustur(hedef_ip, nmap_sonuc, header_sonuc, ai_sonuc)
    
    print("\n[✓] Rapor oluşturuldu: rapor.html")

if __name__ == "__main__":
    main()
