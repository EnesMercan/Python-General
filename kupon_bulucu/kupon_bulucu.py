import requests, urllib, json, colorama          #pip install requests
from bs4 import BeautifulSoup                   #pip install bs4
from colorama import init, Fore, Style          #pip install colorama

init(autoreset=True)

sorgu = "inurl:udemy.com/course/ \"inurl:couponCode"
# Bu kısımda Google'da arama yapıyoruz.
tbs = "d"
URL = f"https://google.com/search?q={sorgu}&tbs=qdr:{tbs}"

# Sanal tarayıcı oluşturuyoruz.
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
ACCEPT_ENCODING = "gzip, deflate, br"

headers = {'User-Agent': USER_AGENT, 'Content-Type': "text/plain"}

resp = requests.get(URL, headers=headers)
try:
    # Bağlantı sorunsuz olursa yani dönüş kodumuz 200 olursa BeatufiulSoup ile sayfayı parçalıyoruz.
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")

    link, title, coupon = [], [], []
    for g in soup.find_all('div', class_='r'):
        anchors = g.find_all('a')
        if anchors:
            title.append(g.find('h3').text)
            link.append(anchors[0]['href'])
            coupon.append((anchors[0]['href']).partition("?couponCode=")[2])

    results = [{"Title": t, "Link": l, "Coupon": c} for t, l, c in zip(title, link, coupon)]

    for i in range(len(results)):

        resp = requests.get(results[i]["Link"], headers=headers)

        if resp.status_code == 200:
            course_code = BeautifulSoup(resp.content, "html.parser").body['data-clp-course-id']

            CodeCheck_URL = f"https://www.udemy.com/api-2.0/course-landing-components/{course_code}/me/?components=buy_button,purchase,redeem_coupon,discount_expiration,gift_this_course&discountCode=" + \
                            results[i]["Coupon"]

            resp = requests.request("GET", CodeCheck_URL, headers=headers).json()

            # Kuponları ekrana yazdırıyoruz.
            if (resp)["purchase"]["data"]["pricing_result"]["price"]["amount"] == 0:
                print(f"\n[{Fore.GREEN}*{Style.RESET_ALL}]")
                print(f"\t{Fore.GREEN}Başlık: {Style.RESET_ALL}" + results[i]["Title"], sep='\n')
                print(f"\t{Fore.GREEN}Adres: {Style.RESET_ALL}" + results[i]["Link"], sep='\n')
                print(f"\t{Fore.GREEN}Kupon: {Style.RESET_ALL}" + results[i]["Coupon"] +
                      f"\t\t{Fore.GREEN}Tahmini Kalan Kupon: {Style.RESET_ALL}" + str(
                    (resp)["purchase"]["data"]["pricing_result"]["campaign"]["uses_remaining"])
                      + str(f"\t\t{Fore.GREEN}Kupon Bitiş Zamanı:: {Style.RESET_ALL}" + str(
                    (resp)["purchase"]["data"]["pricing_result"]["campaign"]["end_time"])[:-9]))

except KeyError:
    pass
