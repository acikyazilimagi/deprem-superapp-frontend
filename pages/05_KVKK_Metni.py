import base64
import io
import os
import pandas as pd
import streamlit as st

from helpers.http_helpers import http_helper
url = os.getenv("API_BASE_ENDPOINT") + os.getenv("API_GET_CALL_MAP_DATA_ENDPOINT")
response = http_helper.send_request(url, method="POST", body_params={})

data = response.json()
df = pd.DataFrame(data)
csv_string = df.to_csv(index=False)
actual_data = data["detail"]
csv_strings = pd.DataFrame(actual_data)
csv_strings = csv_strings.drop(columns=['_id'])
csv_strings['gereksinimler'] = csv_strings['gereksinimler'].apply(lambda x: ','.join(map(str, x)))
csv = io.StringIO(csv_strings.to_csv(index=False))
b64 = base64.b64encode(csv.getvalue().encode()).decode()
href = f'<a href="data:file/csv;base64,{b64}" download="myfilename.csv">Yardım İhityaçları Verisini İndir</a>'
st.markdown(href, unsafe_allow_html=True)

url2 = os.getenv("API_BASE_ENDPOINT") + os.getenv("API_GET_HELPER_MAP_DATA_ENDPOINT")
response2 = http_helper.send_request(url2, method="POST", body_params={})

data2 = response2.json()
df2 = pd.DataFrame(data2)
csv_string2 = df2.to_csv(index=False)
actual_data2 = data2["detail"]
csv_strings2 = pd.DataFrame(actual_data2)
csv_strings2 = csv_strings2.drop(columns=['_id'])
csv_strings2['servis'] = csv_strings2['servis'].apply(lambda x: ','.join(map(str, x)))
csv2 = io.StringIO(csv_strings2.to_csv(index=False))
b642 = base64.b64encode(csv2.getvalue().encode()).decode()
href2 = f'<a href="data:file/csv;base64,{b642}" download="myfilename.csv">Yardım Noktaları Verisini İndir</a>'
st.markdown(href2, unsafe_allow_html=True)
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

url = os.getenv("API_BASE_ENDPOINT") + os.getenv("API_GET_CALL_MAP_DATA_ENDPOINT")
response = http_helper.send_request(url, method="POST", body_params={})
