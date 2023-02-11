import base64
import io
import os
import pandas as pd
import streamlit as st

from helpers.http_helpers import http_helper

st.markdown("""
## KVKK:

Kişisel Verilerin İşlenmesine İlişkin Aydınlatma: 

Bu uygulama, 6 Şubat 2023 tarihinde Türkiye’de meydana gelen büyük deprem felaketinde, arama kurtarma çalışmaları ile yardım ve destek taleplerini ortak bir veri tabanında toplayarak yetkili kurum ve kuruluşlara aktarmak amacı ile bilişim teknolojileri alanında çalışan gönüllüler tarafından oluşturulmuştur.
Yardım ya da desteğe ihtiyacı olduğunu belirttiğiniz kişilerin kişisel verileri ‘’Fiili imkânsızlık nedeniyle rızasını açıklayamayacak durumda bulunan veya rızasına hukuki geçerlilik tanınmayan kişinin kendisinin ya da bir başkasının hayatı veya beden bütünlüğünün korunması için zorunlu olması’’ hukuki sebebine dayanarak, otomatik yollarla işlenecektir. Tarafınıza ait kişisel veriler, ‘’Bir hakkın tesisi, kullanılması veya korunması için veri işlemenin zorunlu olması’’ hukuki sebebine dayanarak işlenecektir.

Paylaşacağınız yardım, destek taleplerinde yer alan isim, soy isim, telefon ve adres gibi kişisel veriler, veli, vasi, temsilci bilgisi, medeni durum ve sağlık bilgileri tarafımızca oluşturulan ve sunucuları yurtiçi ve yurtdışında bulunan veri tabanında toplanarak, Afad, Akut, Kızılay gibi yetkili arama kurtarma kuruluşlarının yanı sıra destek ve yardım taleplerini karşılayabilecek sivil toplum kuruluşları ile kişisel veri işleme amacı ile sınırlı olarak paylaşılacaktır.


Bu platform kar amacı gütmeden imece usulu bilgi paylaşımı için geliştirildi, hiçbir kurum ve kuruluşla ilişiği yoktur.

Gerektiğinde yetkili merci ve kurumlara bilgi sağlanabilir ve işbirliği yapılabilir.

© 2023
KVKK

""")
