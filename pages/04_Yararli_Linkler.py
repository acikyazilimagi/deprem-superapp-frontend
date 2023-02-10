import streamlit as st
import pandas as pd

st.markdown("""### Kalacak Yerler (Places to Stay Free of Charge):

| Yer (Place) | İletişim (Contact) |
|:-----------|:------------|
| Kalacak Yer | [https://kalacakyer.org/ ](https://kalacakyer.org/ ) |
| Afet Harita | [https://afetharita.com/](https://afetharita.com/) |
| Sığınma Yerleri (Shelters) | [https://docs.google.com/spreadsheets/d/1Aj-GWFlt8ZTxQCRjrRPME9f1TBmzqcuLDh_GTCBm7-w/edit#gid=0](https://docs.google.com/spreadsheets/d/1Aj-GWFlt8ZTxQCRjrRPME9f1TBmzqcuLDh_GTCBm7-w/edit#gid=0) |
| Misafir Ol | [https://misafirol.org/](https://misafirol.org/) |
| Türk Hava Yolları (Turkish Airlines) | [https://www.turkishairlinesholidays.com/tr-tr/depremzedeler-icin-oteller](https://www.turkishairlinesholidays.com/tr-tr/depremzedeler-icin-oteller)|
| Gençlik ve Spor Bakanlığı | [https://gsb.gov.tr/haber-detay.html/968](https://gsb.gov.tr/haber-detay.html/968) |
| Ahbap | [https://www.google.com/maps/d/u/1/viewer?mid=1aQ0TJi4q_46XAZiSLggkbTjPzLGkTzQ&ll=37.06301742072887%2C37.28739713964324&z=8](https://www.google.com/maps/d/u/1/viewer?mid=1aQ0TJi4q_46XAZiSLggkbTjPzLGkTzQ&ll=37.06301742072887%2C37.28739713964324&z=8) |
| Hepsi Emlak | [https://www.hepsiemlak.com/emlak-yasam/genel/dostluk-catisi](https://www.hepsiemlak.com/emlak-yasam/genel/dostluk-catisi) |
| Otelz | [https://www.otelz.com/tr/gecmisolsunturkiyem](https://www.otelz.com/tr/gecmisolsunturkiyem) |
| Barınma Alanları (Housing Areas) | [https://www.afetbilgi.com/G%C3%BCvenli%20Toplanma%20Alanlar%C4%B1](https://www.afetbilgi.com/G%C3%BCvenli%20Toplanma%20Alanlar%C4%B1) |


### Ücretsiz Veteriner ve Kedi Evleri Adresleri (Free Vet and Cat House Addresses)

| Yer (Place) | İletişim (Contact) |
|:-----------|:------------|
| Veteriner Listesi (Vet List) | [https://www.google.com/maps/d/u/0/viewer?mid=1quGS8qonhKrGMr0aqfrNvLi9GzvYE0I&ll=38.90781588955668%2C34.55183079999997&z=6](https://www.google.com/maps/d/u/0/viewer?mid=1quGS8qonhKrGMr0aqfrNvLi9GzvYE0I&ll=38.90781588955668%2C34.55183079999997&z=6) |


### Kan Bağışı (Blood Donation)

| Yer (Place) | İletişim (Contact) |
|:-----------|:------------|
| Kanver Adresi | [https://kanver.org/KanHizmetleri/KanBagisiNoktalari](https://kanver.org/KanHizmetleri/KanBagisiNoktalari) |

### Deprem Alışverişi (Earthquake Shopping Donation)

| Yer (Place) | İletişim (Contact) |
|:-----------|:------------|
| Trendyol | [https://www.trendyol.com/sr?cid=619322&pi=3](https://www.trendyol.com/sr?cid=619322&pi=3) |
| Hepsi Burada | [https://www.hepsiburada.com/deprem-seferberligi](https://www.hepsiburada.com/deprem-seferberligi) |
| Amazon | [https://www.amazon.com.tr/hz/wishlist/ls/1EBJ7MY9SZPZ4/](https://www.amazon.com.tr/hz/wishlist/ls/1EBJ7MY9SZPZ4/) |
| N11 | [https://www.n11.com/promosyon/deprem-yardimlasma-seferberligi-1600359](https://www.n11.com/promosyon/deprem-yardimlasma-seferberligi-1600359) |
| PTTAvm | [https://www.pttavm.com/arama/yardim](https://www.pttavm.com/arama/yardim) |
| LC Waikiki | [https://www.lcwaikiki.com/tr-TR/TR/etiket/deprem-seferberligi](https://www.lcwaikiki.com/tr-TR/TR/etiket/deprem-seferberligi) |
| Migros | [https://www.migros.com.tr/](https://www.migros.com.tr/) |
| Carrefoursa| [https://www.carrefoursa.com/yardimlasmaseferberligi]() |


### Kripto ve IBAN Para Bağışı (Crypto and IBAN Money Donation)

#### A. International Accounts for Money Transfer
##### Governmental and Semi Governmental Organizations (Not Suggested)

| Organization / Charity | Bank Info | IBAN (EUR) | IBAN (USD) | Account No / Routing No | SWIFT Code | Extra Info |
|:-----------|:------------|:------------|:------------|:------------|:------------|:------------|
| [Turkish Red Crescent](https://twitter.com/RedCrescent/status/1622611174918352896) | Ziraat Bank International | DE26 5122 0700 1080 0000 01 ||| TCZBDEFF| NGO, part of International Red Cross and Red Crescent Movement, accused of being corrupt |
| [Disaster and Emergency Management Presidency](https://www.afad.gov.tr/depremkampanyasi2) | T.C. Ziraat Bankası | TR19 0001 0017 4555 5555 5552 06 | TR46 0001 0017 4555 5555 5552 05 || TCZBTR2A | Governmental Organization, widely critized for being slow and not organizing efforts to rescue |
| [Disaster and Emergency Management Presidency](https://www.afad.gov.tr/depremkampanyasi2) | Türkiye İş Bankası | TR19 0006 4000 0024 2992 5862 85 | TR09 0006 4000 0024 2992 5862 71 || ISBKTRIS | Governmental Organization, widely critized for being slow and not organizing efforts to rescue |
| [Embassy of the Republic of Turkey](https://www.instagram.com/p/CoU3aBlOM02/) | Bank of America ||| 0019 2343 0455 / ABA: 054001204 | BOFAUS3N | Governmental Organization |
||||||||

##### Non-Governmental Organizations (Suggested)

| Organization / Charity | Bank Info | IBAN (EUR) | IBAN (USD) | IBAN (GDP) | SWIFT Code | Extra Info |
|:-----------|:------------|:------------|:------------|:------------|:------------|:------------|
| [Ahbap Derneği](https://ahbap.org/bagisci-ol) | Türkiye İş Bankası | TR15 0006 4000 0021 0212 1502 77 | TR32 0006 4000 0021 0212 1502 62 | TR37 0006 4000 0021 0212 2608 49 | ISBKTRIS | NGO, focuses on humanitarian aid |
| [AKUT - Arama Kurtarma Derneği](https://www.akut.org.tr/en/about-akut) | Türkiye İş Bankası | TR12 0006 4000 0021 0806 6661 44 | TR48 0006 4000 0021 0806 6666 60 || ISBKTRIS | NGO, Search and Rescue focus |
| [AKUT - Arama Kurtarma Derneği](https://www.akut.org.tr/en/about-akut) | QNB Finansbank | TR66 0011 1000 0000 0032 4941 26 | TR82 0011 1000 0000 0032 4941 29 || FNNBTRIS | NGO, Search and Rescue focus |
| [Bündnis Entwicklung Hilft (BEH) & Aktion Deutschland Hilft (ADH)](https://www.spendenkonto-nothilfe.de/) | Commerzbank | DE53 200 400 600 200 400 600 ||| COBADEFF | NGO, see website for alternative payment options (German) |

#### B. International Funds or Organizations

| Organization / Charity | Link | Credit Card | Paypal | Alternative Payment | Info | Extra Info |
|:-----------|:------------|:------------|:------------|:------------|:------------|:------------|
| Turkish Red Crescent | [Donate to Turkish Red Crescent](https://www.kizilay.org.tr/Bagis/BagisYap/405/donations-for-earthquake-in-pazarcik) | Yes || Direct Payment, Postal Payment, In-App Payment (Android, IOS) | NGO, part of International Red Cross and Red Crescent Movement, accused of being corrupt | Turkey |
| International Red Cross and Red Crescent Movement | [Donate Now](https://donation.ifrc.org/?campaign=f3cfd66a-0ba7-ed11-a2da-005056010028) | Yes ||| NGO | Uses Swiss Francs |
| Ahbap Platform | [Official Website](https://ahbap.org/disasters-turkey) | Yes || Direct Payment | NGO, focuses on humanitarian aid | Turkey |
| Ahbap Platform | [GoFundMe](https://www.gofundme.com/f/xh8d5t-turkey-earthquake-fund) | Yes | Yes | Direct Payment | NGO, focuses on humanitarian aid | Turkey |
| Hasan Abi For Turkey | [Events Softgiving](https://events.softgiving.com/donate/HasanAbiForTurkeySyriaEarthquakesFund) | Yes | Yes || Fundraiser by Turkish-American streamer HasanAbi | Donations go to Donations go to CARE Turkey, CARE Syria, AKUT & Ahbap via Givinga Foundation |
| American Turkish Association of Washington D.C. | [Fundraiser](https://donate.tpfund.org/team/479874) | Yes | Yes || NGO, Fundraiser via Turkish Philanthropy Funds | USA |
| Association of Turkish Americans of Southern California | [Link](https://zrnv.mjt.lu/nl3/Q8y4YfF_oUhU-uoJLvHgwQ?m=AVoAAAtKlVcAAcrkfYQAAAG3SB4AAAAATbwAAEWSAAYfNgBj4piLoCUyiQo3RdmqV6ZmCLC4QgAF3JY&b=5ff13ac2&e=267b09e7&x=RVHl8MmyM-qf4j84CZW1mw) || Yes | Zelle | NGO | USA |
| British Red Cross | [Donate Red Cross](https://donate.redcross.org.uk/appeal/turkey-syria-earthquake-appeal?c_name=Turkey-Syria) | Yes | Yes || NGO, part of International Red Cross and Red Crescent Movement | UK |
| German Red Cross | [DRK](https://www.drk.de/spenden/privatperson-spenden/jetzt-spenden/) | Yes | Yes | Amazon Pay, SEPA, Sofort | NGO, part of International Red Cross and Red Crescent Movement | Germany |
| French Red Cross | [Donner Croix-Rouge](https://donner.croix-rouge.fr/seisme-moyen-orient/~mon-don) | Yes | Yes | Direct Payment | NGO, part of International Red Cross and Red Crescent Movement | France |
| Lithuanian Red Cross | [Lietuvos Raudonojo Kryžiaus](https://redcross.lt/naujienos-ir-renginiai/padekime-isgelbeti-gyvybes/) | Yes || Direct Payment, SMS | NGO, part of International Red Cross and Red Crescent Movement | Lithuania |
| Oxfam Australia | [Donate Oxfam](https://secure.oxfam.org.au/donate/turkey-syria-earthquake) | Yes ||| NGO | Australia |
||||||||
||||||||
||||||||
||||||||
||||||||
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




