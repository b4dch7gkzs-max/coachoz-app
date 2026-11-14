"""Coach Oz Stats yasal sayfaları: stats/privacy.html, stats/terms.html, stats/support.html (TR + EN).
Basketball sayfalarıyla aynı görünüm. Çalıştır: python3 scripts/stats_legal.py"""
import html, os

DATE = '14.11.2026'
MAIL = 'coachoz@coachozperformance.com'
STYLE = """<style>:root{--bg:#F2F4F9;--card:#fff;--ink:#0F1B33;--mute:#56607A;--line:#DDE3EE;--accent:#C41E3A}
@media (prefers-color-scheme:dark){:root{--bg:#070E1C;--card:#101A2F;--ink:#EAF0FA;--mute:#A6B2C8;--line:#22304D;--accent:#FF5A70}}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
main{max-width:720px;margin:0 auto;padding:32px 16px 48px}h1{font-size:28px;line-height:1.2;margin:0 0 4px}h2{margin:36px 0 8px;font-size:22px}
h3{margin:20px 0 4px;font-size:17px}p{margin:0;color:var(--ink)}.k{color:var(--accent);font-weight:700;letter-spacing:.06em;text-transform:uppercase;font-size:13px}
.m{color:var(--mute);font-size:14px;margin-bottom:12px}nav a{color:var(--accent);margin-right:16px}section{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:20px;margin-top:16px}a{color:var(--accent)}</style>"""

PRIVACY = {
 'tr': ('Gizlilik politikası', [
  ('Kısaca', 'Coach Oz Stats hiçbir kişisel veri toplamaz. Hesap açman gerekmez. Uygulamaya girdiğin her şey (oyuncu profili, fotoğraf, maç istatistikleri) yalnızca senin cihazında ve kendi iCloud hesabında saklanır; biz bu verilere erişemeyiz.'),
  ('Cihazında saklananlar', 'Oyuncunun adı, forma numarası, pozisyonu, doğum tarihi, boyu, kilosu, kullandığı el, takımı, isteğe bağlı fotoğrafı, maç videosu linki, iletişim bilgisi ve hedef notları; maç tarihleri, rakip adları ve maç istatistikleri. Bu bilgiler bize ya da üçüncü kişilere gönderilmez. Uygulama bu verileri otomatik olarak cihazındaki uygulama klasörüne ve iCloud açıksa kendi iCloud hesabına yedekler; uygulamayı yeniden yüklediğinde ya da yeni telefona geçtiğinde veriler geri gelir.'),
  ('Çocukların bilgileri', 'Uygulama veliler, oyuncular ve antrenörler içindir; 18 yaşından küçük bir oyuncunun bilgileri velisi tarafından girilmelidir. Girilen bilgiler hiçbir sunucuya gönderilmez ve yalnızca cihazda kalır. Bu bilgileri içeren PDF raporu ya da Instagram kartı yalnızca sen oluşturup paylaşmayı seçtiğinde cihazdan çıkar; kiminle paylaşacağına sen karar verirsin.'),
  ('Kamera ve fotoğraflar', 'Fotoğraf yalnızca sen oyuncu profili için seçtiğinde ya da çektiğinde kullanılır. Küçültülmüş bir kopyası cihazda saklanır; başka hiçbir yere gönderilmez.'),
  ('Ödemeler', 'Coach Oz Stats Pro tek seferlik bir satın alımdır ve ödemesi Apple tarafından App Store üzerinden alınır. Kart bilgilerin bizimle paylaşılmaz. Satın alımın geçerli olup olmadığı Apple\'dan cihazında kontrol edilir.'),
  ('Analiz, reklam, izleme', 'Uygulamada analiz aracı, reklam ve izleme yoktur. Kullanımın hakkında veri toplanmaz.'),
  ('Silme', 'Oyuncuyu uygulamada "Oyuncuyu sil" ile silebilirsin. Uygulamayı silmek cihazdaki verileri de siler; iCloud kopyasını iPhone Ayarlar > adın > iCloud > Depolama Alanını Yönet bölümünden silebilirsin.'),
  ('Değişiklikler ve iletişim', 'Bu politika değişirse güncel hali bu sayfada yayımlanır. Soruların için: ' + MAIL),
 ]),
 'en': ('Privacy policy', [
  ('In short', 'Coach Oz Stats does not collect any personal data. You don\'t need an account. Everything you enter (player profile, photo, game stats) is stored only on your device and in your own iCloud account; we cannot access it.'),
  ('Stored on your device', 'The player\'s name, jersey number, position, date of birth, height, weight, shooting hand, team, optional photo, game video link, contact details and goal notes; game dates, opponent names and game statistics. None of this is sent to us or to third parties. The app automatically backs it up to the app folder on your device and, if iCloud is on, to your own iCloud account; it comes back when you reinstall the app or move to a new phone.'),
  ('Children\'s information', 'The app is made for parents, players and coaches; information about a player under 18 should be entered by their parent or guardian. Nothing entered is sent to any server; it stays on the device. A PDF report or Instagram card containing this information leaves the device only when you create and choose to share it; you decide who receives it.'),
  ('Camera and photos', 'A photo is used only when you pick or take one for a player profile. A reduced copy is stored on the device and is not sent anywhere else.'),
  ('Payments', 'Coach Oz Stats Pro is a one-time purchase paid through Apple on the App Store. Your card details are never shared with us. Whether your purchase is valid is checked with Apple on your device.'),
  ('Analytics, ads, tracking', 'The app has no analytics, no ads and no tracking. No data about your usage is collected.'),
  ('Deleting', 'You can delete a player in the app with "Delete player". Deleting the app removes the data on the device; you can delete the iCloud copy in iPhone Settings > your name > iCloud > Manage Storage.'),
  ('Changes and contact', 'If this policy changes, the current version is published on this page. Questions: ' + MAIL),
 ]),
}

TERMS = {
 'tr': ('Kullanım koşulları', [
  ('Hizmet', 'Coach Oz Stats, basketbol oyuncularının maç istatistiklerini kaydetmek, verimlilik ve ortalamaları hesaplamak ve PDF oyuncu raporu oluşturmak için bir uygulamadır. Uygulamanın kullanımı Apple\'ın standart son kullanıcı lisans sözleşmesine (EULA) tabidir.'),
  ('Ücretsiz sürüm ve Pro', 'Uygulama ücretsiz indirilir; ücretsiz sürümde 1 oyuncu ve oyuncu başına 3 maç kaydedilir. Coach Oz Stats Pro, tek seferlik ödemeyle sınırsız maç, birden fazla oyuncu ve PDF raporunu açar. Abonelik değildir, yenilenmez. Satın alım Apple kimliğine bağlıdır; aynı Apple kimliğiyle başka cihazda "Satın alımı geri yükle" ile açılır.'),
  ('İstatistiklerin niteliği', 'İstatistikler kullanıcı tarafından girilir; resmi lig ya da federasyon istatistiği değildir. Raporlar bu nedenle "kullanıcı tarafından kaydedilmiştir" notunu taşır. Uygulama bir kulübe, okula ya da burs programına kabul, seçilme ya da transfer garantisi vermez; oyuncu temsilciliği ya da aracılık hizmeti sunmaz.'),
  ('Kullanıcının sorumluluğu', '18 yaşından küçük oyunculara ait bilgilerin ve fotoğrafların girilmesi ve paylaşılması velinin izni ve sorumluluğundadır. Başkasına ait fotoğrafları ya da bilgileri izinsiz kullanmamalısın.'),
  ('Fikri haklar', 'Uygulamanın tasarımı, metinleri ve rapor şablonları Coach Oz\'a aittir. Oluşturduğun raporları ve kartları kendi amaçların için serbestçe kullanabilir ve paylaşabilirsin.'),
  ('İletişim', MAIL),
 ]),
 'en': ('Terms of use', [
  ('Service', 'Coach Oz Stats is an app for recording a basketball player\'s game statistics, calculating efficiency and averages, and creating a PDF player report. Use of the app is governed by Apple\'s standard End User License Agreement (EULA).'),
  ('Free version and Pro', 'The app is free to download; the free version records 1 player and 3 games per player. Coach Oz Stats Pro is a one-time payment that unlocks unlimited games, multiple players and the PDF report. It is not a subscription and does not renew. The purchase is tied to your Apple ID; on another device with the same Apple ID, use "Restore purchase".'),
  ('Nature of the statistics', 'Statistics are entered by the user and are not official league or federation statistics. Reports therefore carry a "recorded by the user" note. The app does not guarantee admission, selection or a transfer to any club, school or scholarship program, and does not provide player representation or agency services.'),
  ('Your responsibility', 'Entering and sharing information and photos of players under 18 is subject to the parent\'s or guardian\'s consent and responsibility. Do not use other people\'s photos or information without permission.'),
  ('Intellectual property', 'The app\'s design, texts and report templates belong to Coach Oz. You may freely use and share the reports and cards you create for your own purposes.'),
  ('Contact', MAIL),
 ]),
}

SUPPORT = {
 'tr': ('Türkçe', [
  ('İletişim', 'Soru, öneri ve hata bildirimleri için: <a href="mailto:%s">%s</a>. Genellikle 2 iş günü içinde yanıt veriyoruz.' % (MAIL, MAIL)),
  ('Maç nasıl kaydedilir?', 'Maç sekmesinde rakibi ve tarihi gir, "Maçı başlat"a dokun. Maç boyunca her olayda ilgili tuşa dokun; yanlış dokunuşta "Geri al". Maç bitince süreyi girip "Maçı bitir ve kaydet".'),
  ('Yanlış girilen maçı düzeltme', 'Profil sekmesinde maçlar listesinde maçın altındaki "Düzenle"ye dokun; her istatistiği + ve − ile düzeltebilir, rakip, tarih ve süreyi değiştirebilirsin.'),
  ('Verimlilik (EFF) nasıl hesaplanır?', 'EFF = sayı + ribaund + asist + top çalma + blok − kaçan saha içi atış − kaçan serbest atış − top kaybı.'),
  ('Pro\'yu yeni telefonda açma', 'Aynı Apple kimliğiyle giriş yaptığın telefonda Pro ekranını aç ve "Satın alımı geri yükle"ye dokun.'),
  ('Verilerim nerede, nasıl geri gelir?', 'Veriler otomatik olarak Dosyalar uygulamasında "Coach Oz Stats" klasörüne ve iCloud açıksa kendi iCloud hesabına yedeklenir. Uygulamayı yeniden yüklediğinde ya da aynı Apple kimliğiyle yeni telefona geçtiğinde kendiliğinden geri gelir.'),
  ('Gizlilik ve koşullar', '<a href="privacy.html">Gizlilik politikası</a> · <a href="terms.html">Kullanım koşulları</a>'),
 ]),
 'en': ('English', [
  ('Contact', 'Questions, suggestions and bug reports: <a href="mailto:%s">%s</a>. We usually reply within 2 business days.' % (MAIL, MAIL)),
  ('Language', 'The app interface is currently in Turkish; the PDF player report can be created in Turkish or English. Button names below are given in English with the Turkish label in brackets.'),
  ('How do I record a game?', 'In the Game tab enter the opponent and date and tap "Start game" (Maçı başlat). Tap the matching key for each event; tap "Undo" (Geri al) if you make a mistake. When the game ends, enter the minutes played and tap "Finish and save" (Maçı bitir ve kaydet).'),
  ('Fixing a game', 'In the Profile tab, tap "Edit" (Düzenle) under the game in the games list; adjust each stat with + and −, and change the opponent, date and minutes.'),
  ('How is efficiency (EFF) calculated?', 'EFF = points + rebounds + assists + steals + blocks − missed field goals − missed free throws − turnovers.'),
  ('Unlocking Pro on a new phone', 'On a phone signed in with the same Apple ID, open the Pro screen and tap "Restore purchase" (Satın alımı geri yükle).'),
  ('Where is my data and how does it come back?', 'Data is backed up automatically to the "Coach Oz Stats" folder in the Files app and, if iCloud is on, to your own iCloud account. It comes back on its own when you reinstall the app or move to a new phone with the same Apple ID.'),
  ('Privacy and terms', '<a href="privacy.html">Privacy policy</a> · <a href="terms.html">Terms of use</a>'),
 ]),
}

def page(title_en, h1, body):
    return ('<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{title_en} · Coach Oz Stats</title>{STYLE}</head><body><main><p class="k">Coach Oz Stats</p><h1>{h1}</h1>{body}</main></body></html>\n')

def doc(d, raw=False):
    out = f'<p class="m">Son güncelleme / Last updated: {DATE}</p><nav><a href="#tr">Türkçe</a><a href="#en">English</a></nav>'
    for lang in ('tr', 'en'):
        t, secs = d[lang]
        out += f'<section lang="{lang}" id="{lang}"><h2>{html.escape(t)}</h2>'
        for h, p in secs:
            out += f'<h3>{html.escape(h)}</h3><p>{p if raw else html.escape(p)}</p>'
        out += '</section>'
    return out

def support():
    out = ''
    for lang in ('tr', 'en'):
        t, secs = SUPPORT[lang]
        out += f'<section lang="{lang}" id="{lang}"><h2>{t}</h2>' + ''.join(f'<h3>{html.escape(h)}</h3><p>{p}</p>' for h, p in secs) + '</section>'
    return out

os.makedirs('stats', exist_ok=True)
open('stats/privacy.html', 'w').write(page('Privacy policy', 'Gizlilik politikası / Privacy policy', doc(PRIVACY)))
open('stats/terms.html', 'w').write(page('Terms of use', 'Kullanım koşulları / Terms of use', doc(TERMS)))
open('stats/support.html', 'w').write(page('Support', 'Destek / Support', support()))
open('stats/index.html', 'w').write(page('Coach Oz Stats', 'Coach Oz Stats',
    '<section><p>Basketbol oyuncuları ve veliler için maç istatistiği, verimlilik ve PDF scout raporu. / Game stats, efficiency and PDF scout reports for basketball players and parents.</p>'
    '<p style="margin-top:12px"><a href="privacy.html">Gizlilik / Privacy</a> · <a href="terms.html">Koşullar / Terms</a> · <a href="support.html">Destek / Support</a></p></section>'))
print('stats/ sayfaları yazıldı')
