print("Günlük Görev Kaydediciye Hoş Geldin :)")

tarih = input("Bugün günlerden ne ? Kendi önerilerimle sana yardımcı olmak isterim. :)")


if tarih in ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"]:
    print( "Hafta içi yoğun olacağın için kendine çok yüklenme ve işlerini öncelik sırasına göre planla kısa sürede daha çok iş bitirebilmek için verimli çalış.\nUmarım senin için dolu dolu geçer.")
elif tarih in ["Cumartesi"  , "Pazar"]:
    print("Ooo tatil demek ama biz boş durmayalım çalışmaya devam . Daha çok vaktini alan işleri bu gün için planlayabilirsin. Tabii dinlenmeyi de unutma.\nGününü hem çalışma hem dinlenme açısından dolu dolu geçirmen dileğiyle...")

 
sabah1 = input("Sabah 08.00 - 12.00 arası planların neler?")
ogle1 = input("Öğlen 12.00 - 14.00 arası planların neler?")
ikindi1 = input("İkindi 14.00 - 18.00 arası planların neler?")
akşam1 = input("Akşam 18.00 - 22.00 arası planların neler?")

zaman = input("Şuan hangi görevlerini bilmek istersin ?(sabah/öğle/ikindi/akşam)")

if zaman in ["sabah" , "SABAH" ]:
    print(sabah1)
elif zaman in ["Öğlen" , "ÖĞLEN"]:
    print(ogle1)
elif zaman in ["ikindi" , "İKİNDİ"]:
    print(ikindi1)
elif zaman in ["akşam" , "AKŞAM"]:
    print(akşam1)

print("Programın bur şekildeydi. Sıkı çalışmaya devam...")
