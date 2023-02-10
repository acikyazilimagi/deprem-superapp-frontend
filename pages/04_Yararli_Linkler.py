import streamlit as st
import pandas as pd

st.markdown("""## Kalacak Yerler (Places to Stay Free of Charge):
- Kalacak Yer: 

    https://kalacakyer.org/ 

- After Harita: 

    https://afetharita.com/  

- Sığınma Yerleri (Shelters):

    https://docs.google.com/spreadsheets/d/1Aj-GWFlt8ZTxQCRjrRPME9f1TBmzqcuLDh_GTCBm7-w/edit#gid=0

- Misafir Ol:
    
    https://misafirol.org/ 

- Türk Hava Yolları (Turkish Airlines):

    https://www.turkishairlinesholidays.com/tr-tr/depremzedeler-icin-oteller 

- Gençlik ve Spor Bakanlığı:

    https://gsb.gov.tr/haber-detay.html/968 

- Ahbap:

    https://www.google.com/maps/d/u/1/viewer?mid=1aQ0TJi4q_46XAZiSLggkbTjPzLGkTzQ&ll=37.06301742072887%2C37.28739713964324&z=8 

- Hepsi Emlak:
    https://www.hepsiemlak.com/emlak-yasam/genel/dostluk-catisi 

- Otelz:
    
    https://www.otelz.com/tr/gecmisolsunturkiyem

- Barınma Alanları (Housing Areas):
    
    https://www.afetbilgi.com/G%C3%BCvenli%20Toplanma%20Alanlar%C4%B1 


## Ücretsiz Veteriner ve Kedi Evleri Adresleri (Free Vet and Cat House Addresses)
- Veteriner Listesi (Vet List):

    https://www.google.com/maps/d/u/0/viewer?mid=1quGS8qonhKrGMr0aqfrNvLi9GzvYE0I&ll=38.90781588955668%2C34.55183079999997&z=6

- Kan Bağışı (Blood Donation) / Kanver Adresi: 

    https://kanver.org/KanHizmetleri/KanBagisiNoktalari

## Deprem Alışverişi (Earthquake Shopping Donation):
-  Trendyol:
    
    https://www.trendyol.com/sr?cid=619322&pi=3 

- Hepsi Burada:

    https://www.hepsiburada.com/deprem-seferberligi 

- Amazon:
    
    https://www.amazon.com.tr/hz/wishlist/ls/1EBJ7MY9SZPZ4/ 

- N11:

    https://www.n11.com/promosyon/deprem-yardimlasma-seferberligi-1600359 

- PTTAvm:
    
    https://www.pttavm.com/arama/yardim 

- LC Waikiki:
    
    https://www.lcwaikiki.com/tr-TR/TR/etiket/deprem-seferberligi 

- Migros:
    
    https://www.migros.com.tr/ 

- Carrefoursa:
    
    https://www.carrefoursa.com/yardimlasmaseferberligi 
""")


st.markdown("## Kripto ve IBAN Para Bağışı (Crypto and IBAN Money Donation):")

dict = {
    "Organization / Charity":[],
    "Bank Info":[],
    "IBAN (EUR)":[],
    "IBAN (USD)":[],
    "Account No / Routing No":[],
    "SWIFT":[],
    "Extra Info":[]
}
iban_bagis_df =pd.DataFrame().from_dict({})




