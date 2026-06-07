import sys

def get_health_advice(query):
    """
    Simulates a very basic, local AI health assistant.
    Processes queries using a simple keyword-based knowledge base.
    All processing is done on-device, ensuring privacy.
    """
    query = query.lower()
    
    # --- Privacy-focused AI concept: Local knowledge base ---
    # In a real application, this could be a small, on-device machine learning model
    # (e.g., a quantized NLP model) or a more sophisticated rule engine.
    # The key is that it operates without sending data to external servers.
    knowledge_base = {
        "ateş": "Ateşiniz varsa bol sıvı tüketin ve dinlenin. Yüksek veya uzun süreli ateş için bir doktora danışın.",
        "baş ağrısı": "Baş ağrısı için dinlenmek, su içmek ve ağrı kesici almak yardımcı olabilir. Şiddetli veya sürekli ağrı için tıbbi yardım alın.",
        "öksürük": "Öksürük için boğazınızı nemli tutun, ballı ılık içecekler tüketin. Uzun süren veya şiddetli öksürük için doktora görünün.",
        "mide bulantısı": "Mide bulantısı için hafif yiyecekler tüketin, bol su için. Geçmeyen bulantı veya kusma durumunda doktora danışın.",
        "uyku": "Uyku düzeninizi iyileştirmek için düzenli yatma saatleri belirleyin, kafein ve ekran süresini azaltın. Kronik uyku sorunları için uzmana başvurun.",
        "stres": "Stres yönetimi için meditasyon, egzersiz ve hobiler edinebilirsiniz. Yoğun stres için profesyonel destek almayı düşünün.",
        "beslenme": "Dengeli beslenmek için çeşitli meyve, sebze, tam tahıl ve protein kaynakları tüketin. Kişiselleştirilmiş beslenme önerileri için diyetisyene danışın.",
        "egzersiz": "Düzenli egzersiz yapmak genel sağlığınız için çok önemlidir. Haftada en az 150 dakika orta yoğunlukta aktivite hedefleyin. Yeni bir egzersiz programına başlamadan önce doktorunuza danışın."
    }

    found_advice = []
    for keyword, advice in knowledge_base.items():
        if keyword in query:
            found_advice.append(advice)
    
    if found_advice:
        return "İşte size birkaç öneri:\n" + "\n".join(found_advice)
    else:
        return "Üzgünüm, bu konuda size doğrudan bir tavsiye veremiyorum. Lütfen daha fazla bilgi için bir sağlık uzmanına danışın. Unutmayın, ben sadece bir yapay zeka asistanıyım ve profesyonel tıbbi tavsiye yerine geçmem."

def display_privacy_statement():
    """
    Displays a simulated privacy statement, emphasizing local data processing.
    """
    print("\n--- Gizlilik Beyanı ---")
    print("Bu Yapay Zeka Sağlık Asistanı, gizliliğinizi en üst düzeyde tutmak üzere tasarlanmıştır.")
    print("Girdiğiniz hiçbir sağlık verisi harici sunuculara gönderilmez veya depolanmaz.")
    print("Tüm işlem, cihazınızda yerel olarak gerçekleştirilir.")
    print("Bu sayede kişisel sağlık bilgilerinizin kontrolü tamamen sizde kalır.")
    print("-----------------------\n")

def main():
    print("Gizlilik Odaklı Yapay Zeka Sağlık Asistanına Hoş Geldiniz!")
    print("Sağlık durumunuz veya genel iyilik haliniz hakkında sorular sorabilirsiniz.")
    print("Çıkmak için 'çıkış' yazın.")
    
    display_privacy_statement()

    while True:
        user_input = input("Siz: ")
        if user_input.lower() == 'çıkış':
            print("Asistan: Hoşça kalın! Sağlıklı günler dilerim.")
            break
        
        # --- Privacy-focused AI concept: Local processing of user input ---
        # The user's query is processed directly by the local `get_health_advice` function.
        # No network requests are made, ensuring sensitive data remains on the user's device.
        response = get_health_advice(user_input)
        print(f"Asistan: {response}")

if __name__ == "__main__":
    main()
