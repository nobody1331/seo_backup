import webbrowser
import time
import random

# List URL yang akan dibuka secara otomatis setiap 3 menit
urls = [
"https://www.origaminews.com/10-people-who-were-considered-stupid-but-managed-to-change-the-world/"
"https://www.origaminews.com/12-inspiring-dyslexic-individuals-who-changed-the-world/",
"https://www.origaminews.com/25-benefits-of-coconut-water-for-health/",
"https://www.origaminews.com/6-tips-to-help-you-find-a-girlfriend-and-get-out-of-singleness/",
"https://www.origaminews.com/7-surprising-benefits-of-archery-for-your-health-and-well-being/",
"https://www.origaminews.com/8-habits-of-highly-genius-that-make-them-stand-out/",
"https://www.origaminews.com/anime-as-a-lifesaver-the-benefits-of-watching-anime-for-mental-health/",
"https://www.origaminews.com/anime-recommendations-12-must-watch-hacker-themed-shows/",
"https://www.origaminews.com/anime-recommendations-angel-beats-a-thought-provoking-anime-about-life-and-its-meaning/",
"https://www.origaminews.com/anime-recommendations-mahou-shoujo-site-is-a-must-watch-for-fans-of-dark-magical-girl-anime/",
"https://www.origaminews.com/anime-recommendations-review-tasogare-otome-x-amnesia/",
"https://www.origaminews.com/anime-recommendations-tokyo-ghoul-an-anime-that-once-went-viral-in-its-time/",
"https://www.origaminews.com/anime-with-main-characters-who-die-due-to-lies/",
"https://www.origaminews.com/arena-breakout-will-be-globally-released-on-july-14th-for-ios-and-android/",
"https://www.origaminews.com/asus-zenfone-10-a-look-at-the-new-design-and-specs/",
"https://www.origaminews.com/atarashii-gakko-rising-stars-of-japans-music-scene/",
"https://www.origaminews.com/b-komachi-sign-wa-b-romanized-and-translated-english-lyrics/",
"https://www.origaminews.com/babymetal-a-kawaii-metal-band-with-iconic-songs-and-unique-collaborations/",
"https://www.origaminews.com/becoming-a-star-a-comprehensive-guide/",
"https://www.origaminews.com/blue-protocol-the-highly-anticipated-mmorpg-launches-with-server-overload-issues-in-japan/",
"https://www.origaminews.com/break-even-point-is-a-break-even-point-check-out-the-formula-and-its-functions-in-business/",
"https://www.origaminews.com/consuming-alcohol-in-the-right-amount-to-maintain-heart-health/",
"https://www.origaminews.com/could-carlo-ancelotti-become-the-coach-of-the-brazilian-national-team/",
"https://www.origaminews.com/cryptocurrency-a-revolutionary-financial-evolution/",
"https://www.origaminews.com/deeper-insights-into-dance-monkey-tones-and-is-mega-hit/",
"https://www.origaminews.com/detroit-area-city-bans-lgbt-other-political-flags-from-display-on-public-property/",
"https://www.origaminews.com/elon-musk-limits-twitter-interactions-for-free-users-an-in-depth-look/",
"https://www.origaminews.com/exciting-news-for-anime-fans-oshi-no-ko-confirmed-for-season-2/",
"https://www.origaminews.com/exploring-barongsai-the-rich-history-variations-and-performances-of-the-chinese-lion-dance/",
"https://www.origaminews.com/getting-to-know-lazarus-group/",
"https://www.origaminews.com/hackers-in-asia-discovering-the-hub-of-digital-disruption/",
"https://www.origaminews.com/hatsune-miku-the-virtual-pop-star-who-defied-reality-and-conquered-the-world/",
"https://www.origaminews.com/high-school-dxd-season-5-release-date-and-spoilers/",
"https://www.origaminews.com/how-the-internet-of-things-is-changing-the-future-of-technology/",
"https://www.origaminews.com/i-wonder-why-lyrics-by-kana-hanazawa/",
"https://www.origaminews.com/iphone-15-camera-rumored-to-compete-with-full-frame-slr-revolutionary-technology-and-improved-image-quality/",
"https://www.origaminews.com/jack-mas-return-and-current-status/",
"https://www.origaminews.com/japans-struggle-with-low-birth-rates-government-implements-new-policies-encouraging-work-life-balance-for-more-family-time/",
"https://www.origaminews.com/juneteenth-day-today-celebrating-freedom-and-remembrance-in-the-united-states/",
"https://www.origaminews.com/liverpool-secures-dominik-szoboszlai/",
"https://www.origaminews.com/manchester-city-makes-history-with-first-ever-champions-league-win/",
"https://www.origaminews.com/mar-a-lago-secrets-trump-charged-with-endangering-national-security/",
"https://www.origaminews.com/masayoshi-oishi-japanese-musician-enriching-the-anime-and-video-game-industries/",
"https://www.origaminews.com/meet-the-fascinating-characters-of-majo-no-tabitabi-wandering-witch-the-journey-of-elaina/",
"https://www.origaminews.com/mirror-mirror-f-hero-x-milli-ft-changbin-lyrics-thai-english/",
"https://www.origaminews.com/natos-largest-air-exercise-in-history-involves-asian-partners-japan-joins-to-strengthen-defense-cooperation/",
"https://www.origaminews.com/new-zealand-enters-technical-recession-due-to-typhoon-induced-economic-decline/",
"https://www.origaminews.com/north-korea-faces-severe-food-crisis-with-reports-of-starvation-and-looming-humanitarian-disaster/",
"https://www.origaminews.com/protect-your-family-this-rainy-season-importance-of-flu-vaccination-for-children-in-indonesia/",
"https://www.origaminews.com/racism-in-various-countries-a-problem-that-persists/",
"https://www.origaminews.com/reborn-as-a-vending-machine-a-refreshing-twist-in-anime/",
"https://www.origaminews.com/recognizing-the-characteristics-of-children-who-are-victims-of-bullying/",
"https://www.origaminews.com/religion-and-political-power-indonesia-is-not-a-religion-country/",
"https://www.origaminews.com/sony-bravia-xr-tv-lineup-indonesia/",
"https://www.origaminews.com/the-emotional-and-physiological-changes-when-falling-in-love/",
"https://www.origaminews.com/the-exceptional-features-of-the-japanese-education-system-a-closer-look/",
"https://www.origaminews.com/the-fascinating-evolution-of-whales-from-land-dwelling-creatures-to-majestic-ocean-giants/",
"https://www.origaminews.com/the-history-of-sake-a-journey-through-time-and-culture/",
"https://www.origaminews.com/the-importance-of-drinking-water-how-to-hydrate-your-body-properly/",
"https://www.origaminews.com/the-martyrs-of-japan-a-historical-account-of-courage-and-faith/",
"https://www.origaminews.com/the-meaning-behind-semicolon-tattoos-a-symbol-of-hope-and-support-for-mental-health/",
"https://www.origaminews.com/the-origin-of-oxygen-on-earth-its-formation-and-importance-for-life/",
"https://www.origaminews.com/the-threat-of-the-southeast-asia-golden-triangle-cartel-in-the-global-drug-trade/",
"https://www.origaminews.com/the-top-12-most-heartbreaking-anime-ever/",
"https://www.origaminews.com/ukraine-russia-crisis-a-threat-to-us-dollar-dominance-in-the-global-market/",
"https://www.origaminews.com/uncovering-the-facts-of-hatsune-miku-the-worldwide-virtual-idol/",
"https://www.origaminews.com/undead-girl-murder-farce-2023-supernatural-anime-directed-by-mamoru-hatakeyama/",
"https://www.origaminews.com/understanding-coronary-heart-disease-risk-factors-symptoms-and-prevention/",
"https://www.origaminews.com/understanding-dividend-distribution-a-guide-for-investors/",
"https://www.origaminews.com/university-of-manchester-targeted-by-hackers-student-and-staff-data-at-risk-of-breach/",
"https://www.origaminews.com/unraveling-the-mysteries-of-the-unification-church-a-journey-into-the-life-and-legacy-of-reverend-sun-myung-moon/",
"https://www.origaminews.com/us-cybersecurity-official-warns-of-potential-chinese-state-hacker-attacks-on-critical-infrastructure-in-event-of-conflict/",
"https://www.origaminews.com/warren-buffett-the-humble-philanthropist-and-successful-investor/",
"https://www.origaminews.com/what-are-mutual-funds-a-tactical-guide-to-investing-with-a-long-term-vision/",
"https://www.origaminews.com/what-is-brain-cancer-and-how-is-it-treated/",
"https://www.origaminews.com/what-is-dna-and-why-is-it-important-understanding-the-basics-of-genetics/",
"https://www.origaminews.com/when-will-eromanga-sensei-season-2-be-released-five-years-have-gone/",
"https://www.origaminews.com/who-is-psy-the-k-pop-sensation-behind-gangnam-style/",
"https://www.origaminews.com/why-are-asian-students-good-at-mathematics/",
"https://www.origaminews.com/why-are-so-many-koreans-named-kim/",
"https://www.origaminews.com/why-do-asians-eat-rice/",
"https://www.origaminews.com/why-is-earths-core-so-hot/",
"https://www.origaminews.com/why-people-with-rabies-experience-hydrophobia-exploring-the-science-behind-the-fear-of-water/",
"https://www.origaminews.com/world-plastic-bag-free-day-2023-embrace-an-eco-friendly-lifestyle/",
"https://www.origaminews.com/yoko-ono-changing-the-world-by-being-yourself/",
"https://www.origaminews.com/yousei-teikoku-an-innovative-force-in-j-metal/",
"https://www.origaminews.com/zom-100-bucket-list-of-the-dead-a-unique-and-thrilling-take-on-the-zombie-genre-in-anime/"
]

# Loop infiniti, membuka URL secara acak dengan waktu delay antara 30 detik sampai 2 menit
hitung = 0
while hitung < 20:  # Batasi jumlah URL yang dibuka
    random.shuffle(urls)  # Acak urutan URL
    for url in urls:
        webbrowser.get("firefox").open(url)
        delay = random.randint(20, 60)  # Acak waktu delay antara 30 detik sampai 2 menit
        time.sleep(delay)  # Waktu delay dalam detik
        hitung += 1
        if hitung >= 20:  # Jika sudah membuka 20 URL, keluar dari loop
            break
