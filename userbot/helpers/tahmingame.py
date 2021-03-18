import random


class tahmingame:


	def __init__(self):
		pass
	def ipucu(self, kelime):
		text = "`Hmm, Bir Kelime Tuttum İşte İp Ucun:\n\n`"
		if kelime == "Kitap":
			text+="**Okulda Kullanılan Araçlardan Biridir?**"
		if kelime == "Dizi":
			text+="**Televizyonda İzlenir?**"
		if kelime == "bilgisayar":
			text+="**Günümüzün Favori Eşyalarındandır?**"
		if kelime == "masa":
			text+="**Yemek Yerken Üstüne Tabak vb. Konur Ders Calışırken Üstüne Kitap Vb Konur?**"
		if kelime == "okul":
			text+="**Sınıfların Olduğu Eğitim Görülen Yer Neresidir?**"
		if kelime == "öğrenci":
			text+="**Sınıflarda Bulunur?**"
		if kelime == "oyun":
			text+="**Şuan Bot İle Yaptığınız Şey?**"
		if kelime == "strateji":
			text+="**Clash Of Clansın Olduğu Oyun Türü?**"
		if kelime == "Eylül":
			text+="**Bir Aydır Ama İsim Olarakta Kullanılır?**"
		if kelime == "klavye":
			text+="**Telefon, Tablet, Bilgisayar v.b. de Yazı Yazmayı Sağlayan Bir Donanım/Yazılım?**"
		if kelime == "kemik":
			text+="**Kalsiyum Neyde Yararlıdır?**"
		if kelime == "koltuk":
			text+="**Oturduğumuz Yer?**"
		if kelime == "kapı":
			text+="**Biryere Girerken/Cıkarken Acıp Kapattığımız Şey?**"
		if kelime == "ev":
			text+="**Barındığımız/Yaşadığımız Bir Yer?**"
		if kelime == "köprü":
			text+="**Dere, Deniz v.b. nin Üstünden Islanmadan Geçmemizi Sağlar?**"
		if kelime == "Sarı":
			text+="**Galatasaray Ve Fenerbahcedenin Ortak Rengi?**"
		if kelime == "kaya":
			text+="**Taşın Büyüğü?**"
		if kelime == "cocuk":
			text+="**Anne İle Babanın Cinsel İlişki Sonucu Gercekleştirdiği Canlı?**"
		if kelime == "anne":
			text+="**Cocuk Doğuran Kişi?**"
		if kelime == "baba":
			text+="**Cocuğun Yapımında Emeği Gecen Kişi?**"
		if kelime == "telefon":
			text+="**Şuan Elinde Tuttuğun Cihaz?**"
		if kelime == "internet":
			text+="**İnternet Sitesi v.b. Girmenizi Sağlayan Bir Teknoloji?**"
		if kelime == "market":
			text+="**Alışveriş Yaptığımız Yer?**"
		if kelime == "avm":
			text+="**Marketin Büyüğü?**"
		if kelime == "sakız":
			text+="**Çiğnen Ve Yenen Birşey?**"
		if kelime == "yemek":
			text+="**Yediğimiz Şey?**"
		if kelime == "meyve":
			text+="**Domates Meyvemidir? Sebzemidir?**"
		if kelime == "edit":
			text+="**Fotoğrafile Oynayınca Napılmış Olur?**"
		if kelime == "sohbet":
			text+="**Telegram Gruplarında Napılır?**"
		return text