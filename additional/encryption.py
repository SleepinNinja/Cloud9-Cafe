#import string
import random, itertools
import re


class Encryption:
    def __init__(self, message):
        self._message = message

    def _substution_cipher(self):
        """
        Substuite each letter with some other predefined letter
        this one is very easy to predict thats why not using it.
        eg: hello will become ykcch
        """
        key = random.randint(1,100)
        letters = string.ascii_lowercase
        mapping_dict = {letters[i]:letters[(i + key) % 26] for i in range(26)}
        mapping_dict[" "] = " "

        encrypted_message = "".join([mapping_dict[let] for let in message])
        encrypted_key = self._encrypt_key(str(key))

        return encrypted_message, encrypted_key

    def _transposition_cipher(self):
        """
        Don't do substution but changes the order in which the letter of a
        word exists.
        eg: hello will become oelhl
        """
        indices = random.sample(list(range(len(self._message))), k = len(self._message))
        #print("indices", indices)
        message_list = [None] * len(self._message)

        for i in range(len(self._message)):
            message_list[indices[i]] = self._message[i]

        #print(message_list)
        #"".join(message[index] for index in indices)
        encrypted_message = "".join(message_list)
        #print("enc_message", encrypted_message)
        encrypted_key = self._encrypt_key(list(map(str, indices)))


        return encrypted_message, encrypted_key

    def _encrypt_key(cls, key):
        #print(key)
        num_replacement = {
        "1": "╤", "2": "╡", "3": "┴", "4": "╔", "5": "╪",
        "6": "╘", "7": "╬", "8": "■", "9": "Œ", "0": "¤"
        }

        encrypted_key = map(lambda number: "".join([num_replacement[num] for num in number]), key)
        return list(encrypted_key)


    def encrypt(self):
        #print(message)
        #message = message.lower()
        encryption_algo_list = [self._transposition_cipher, self._substution_cipher]
        algo_selection = random.randint(0, len(encryption_algo_list) - 1)
        #print(algo_selection)
        encrypted_message, encrypted_key = encryption_algo_list[0]()

        #print(encrypted_message, encrypted_key, sep = "\n")

        """"
        if len(encrypted_key) == 1:
            random_index = random.randint(0, len(encrypted_message) - 1)
            print(random_index)
            return encrypted_message[:random_index] + encrypted_key[0] + encrypted_message[random_index:]

        """
        inserting_indices = random.sample(list(range(len(encrypted_message))), k = 4)
        #print(inserting_indices)
        message = list(zip(encrypted_key, encrypted_message))
        #print("message", message)

        return "".join(itertools.chain(*message))

        #for index in inserting_indices:
            #encrypted_message.insert()



class Decryption:
    def __init__(self, encrypted_message):
        self._encrypted_message = encrypted_message

    def _find_key_message(self):
        symbol_to_num = {
            "╤": "1", "╡": "2", "┴": "3", "╔": "4", "╪": "5",
            "╘": "6", "╬": "7", "■": "8", "Œ": "9", "¤": "0"
        }

        key_find = re.compile(r"[╤╡┴╔╪╘╬■Œ¤]+")
        message_find = re.compile(r"[^╤╡┴╔╪╘╬■Œ¤]+")
        symbol_indices = re.findall(key_find, self._encrypted_message)
        enc_message = "".join(re.findall(message_find, self._encrypted_message))
        num_indices = []

        for symbols in symbol_indices:
            to_num = int("".join([symbol_to_num[symbol] for symbol in symbols]))
            num_indices.append(to_num)

        return num_indices, enc_message


    def _decrypt_message(self):
        key, enc_message = self._find_key_message()
        #print(key, enc_message, sep = "\n")

        original_message = [enc_message[k] for k in key]
        #print("originl message", "".join(original_message))

        return "".join(original_message)

    def decrypt(self):
        return self._decrypt_message()



stringg = """

Jump to navigation
Jump to search
Welcome to Wikipedia,
the free encyclopedia that anyone can edit.
6,416,084 articles in English

    The arts
    Biography
    Geography
    History
    Mathematics
    Science
    Society
    Technology
    All portals

From today's featured article
Cleveland Centennial half dollar

The Cleveland Centennial half dollar is a commemorative United States half dollar, dated 1936, issued to mark the 100th anniversary of Cleveland, Ohio, as an incorporated city, and in commemoration of the Great Lakes Exposition, held in Cleveland that year. In the mid-1930s, commemorative coins were increasing in value, and Cincinnati businessman Thomas G. Melish, a coin collector, lobbied Congress to authorize several new issues, for which he would be the sole distributor. He was successful with the Cincinnati Musical Center half dollar and the Cleveland piece, and profited from both. Brenda Putnam designed the Cleveland coin, which was approved by the Commission of Fine Arts after suggestions by sculptor Lee Lawrie. Melish distributed the Cleveland coins through the exposition, at local banks, and by mail order from his office in Cincinnati. Sales were good, and the full authorized mintage of 50,000 was struck at the Philadelphia Mint. (Full article...)
Recently featured:

    John McGraw Jaguar British logistics in the Falklands War

    Archive By email More featured articles

Did you know ...
Thromidia catalai
Thromidia catalai

    ... that the starfish Thromidia catalai (pictured) can weigh as much as 6 kilograms (13 lb)?
    ... that the first exhibit of the West Virginia Music Hall of Fame came from founder Michael Lipton's record collection?
    ... that the senior Burmese princes could not attend the funeral of King Mindon since they had all been arrested?
    ... that in 1958, New Jersey assemblyman Carmine Savino proposed cutting property taxes in half by imposing a three-percent state sales tax that would be used to cover public school costs?
    ... that the Greenlandic novel Homo Sapienne was written in only one month?
    ... that when the Marquis Theatre was completed, some Broadway performers boycotted it because of a controversy over the construction of the hotel above it?
    ... that magma travelling through dykes usually solidifies before it gets to the Earth's surface?
    ... that Jonathan Weiner explains in his book how Time, Love, [and] Memory became associated with specific fly genes?

    Archive Start a new article Nominate an article


In the news
Magdalena Andersson
Magdalena Andersson

    Magdalena Andersson (pictured), who resigned a week earlier after one day as designate, is re-elected as Prime Minister of Sweden.
    Barbados becomes a republic, with Sandra Mason replacing Queen Elizabeth II as the head of state.
    In baseball, the Tokyo Yakult Swallows defeat the Orix Buffaloes to win the Japan Series.
    American musical theatre composer and lyricist Stephen Sondheim dies at the age of 91.

Ongoing:

    COVID-19 pandemic

Recent deaths:

    Ray Kennedy Aron Atabek Hermann Bausinger Norodom Ranariddh Virgil Abloh Mārtiņš Brauns

    Nominate an article

On this day

December 1: World AIDS Day; Great Union Day in Romania (1918)
Francis Walsingham
Francis Walsingham

    1577 – Francis Walsingham (pictured), Elizabeth I of England's principal secretary and spymaster, was knighted.
    1821 – On the island of Hispaniola, General José Núñez de Cáceres established the Republic of Spanish Haiti, which only lasted three months.
    1941 – The Civil Air Patrol, the civilian auxiliary of the United States Air Force, was founded.
    1971 – A period of political and economic reforms known as the Croatian Spring came to an end as the League of Communists of Yugoslavia decided to purge the reformist leadership of Croatia.
    1991 – More than 92 percent of voters approved the independence of Ukraine as declared on 24 August.

    Archie MacLaren (b. 1871)Zhu De (b. 1886)Anna Roosevelt Halsted (d. 1975)

More anniversaries:

    November 30 December 1 December 2

    Archive By email List of days of the year

Today's featured picture
Northern royal albatross

The northern royal albatross (Diomedea sanfordi) is a large seabird in the albatross family, Diomedeidae. It nests only on the Chatham Islands, on Enderby Island, and at Taiaroa Head on the Otago Peninsula of New Zealand. It spends the rest of the year away from land, in circumpolar flights over the Southern Ocean, feeding on squid, fish, crustaceans, salps and carrion. The species is listed on the IUCN Red List as endangered, but predators have been eliminated from the islands where it breeds, and conservation efforts have proved successful at the Taiaroa Head colony. This northern royal albatross was photographed off the southeastern coast of Tasmania, Australia.

Photograph credit: John Harrison
Recently featured:

    Henry Taube Walchensee Hydroelectric Power Station A Meeting in the Royal Danish Academy of Sciences and Letters

    Archive More featured pictures

Other areas of Wikipedia

    Community portal – Bulletin board, projects, resources and activities covering a wide range of Wikipedia areas.
    Help desk – Ask questions about using Wikipedia.
    Reference desk – Serving as virtual librarians, Wikipedia volunteers tackle your questions on a wide range of subjects.
    Site news – Announcements, updates, articles and press releases on Wikipedia and the Wikimedia Foundation.
    Teahouse – To ask your first basic questions about contributing to Wikipedia.
    Village pump – For discussions about Wikipedia itself, including areas for technical issues and policies.

Wikipedia's sister projects

Wikipedia is hosted by the Wikimedia Foundation, a non-profit organization that also hosts a range of other projects:

    Commons logo
    Commons
    Free media repository
    MediaWiki logo
    MediaWiki
    Wiki software development
    Meta-Wiki logo
    Meta-Wiki
    Wikimedia project coordination
    Wikibooks logo
    Wikibooks
    Free textbooks and manuals
    Wikidata logo
    Wikidata
    Free knowledge base
    Wikinews logo
    Wikinews
    Free-content news
    Wikiquote logo
    Wikiquote
    Collection of quotations
    Wikisource logo
    Wikisource
    Free-content library
    Wikispecies logo
    Wikispecies
    Directory of species
    Wikiversity logo
    Wikiversity
    Free learning tools
    Wikivoyage logo
    Wikivoyage
    Free travel guide
    Wiktionary logo
    Wiktionary
    Dictionary and thesaurus

Wikipedia languages

This Wikipedia is written in English. Many other Wikipedias are available; some of the largest are listed below.

    1,000,000+ articles
        العربية Deutsch Español Français Italiano Nederlands 日本語 Polski Português Русский Svenska Українська Tiếng Việt 中文
    250,000+ articles
        Bahasa Indonesia Bahasa Melayu Bân-lâm-gú Български Català Čeština Dansk Esperanto Euskara فارسی‎ עברית 한국어 Magyar Norsk Bokmål Română Srpski Srpskohrvatski Suomi Türkçe
    50,000+ articles
        Asturianu Bosanski Eesti Ελληνικά Simple English Galego Hrvatski Latviešu Lietuvių മലയാളം Македонски Norsk nynorsk Shqip Slovenčina Slovenščina ไทย

Navigation menu

    Not logged in
    Talk
    Contributions
    Create account
    Log in

    Main Page
    Talk

    Read
    View source
    View history

Search

    Main page
    Contents
    Current events
    Random article
    About Wikipedia
    Contact us
    Donate

Contribute

    Help
    Learn to edit
    Community portal
    Recent changes
    Upload file

Tools

    What links here
    Related changes
    Special pages
    Permanent link
    Page information
    Wikidata item

Print/export

    Download as PDF
    Printable version

In other projects

    Wikimedia Commons
    MediaWiki
    Meta-Wiki
    Multilingual Wikisource
    Wikispecies
    Wikibooks
    Wikidata
    Wikimania
    Wikinews
    Wikiquote
    Wikisource
    Wikiversity
    Wikivoyage
    Wiktionary

Languages

    العربية
    বাংলা
    Български
    Bosanski
    Català
    Čeština
    Dansk
    Deutsch
    Eesti
    Ελληνικά
    Español
    Esperanto
    Euskara
    فارسی
    Français
    Galego
    한국어
    Hrvatski
    Bahasa Indonesia
    Italiano
    עברית
    ქართული
    Latviešu
    Lietuvių
    Magyar
    Македонски
    Bahasa Melayu
    Nederlands
    日本語
    Norsk bokmål
    Norsk nynorsk
    Polski
    Português
    Română
    Русский
    Simple English
    Slovenčina
    Slovenščina
    Српски / srpski
    Srpskohrvatski / српскохрватски
    Suomi
    Svenska
    ไทย
    Türkçe
    Українська
    Tiếng Việt
    中文
    Complete list

    Text is available under the Creative Commons Attribution-ShareAlike License; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. Wikipedia® is a registered trademark of the Wikimedia Foundation, Inc., a non-profit organization.

    Privacy policy
    About Wikipedia
    Disclaimers
    Contact Wikipedia
    Mobile view
    Developers
    Statistics
    Cookie statement

    Wikimedia Foundation
    Powered by MediaWiki


Jump to navigation
Jump to search
Welcome to Wikipedia,
the free encyclopedia that anyone can edit.
6,416,084 articles in English

    The arts
    Biography
    Geography
    History
    Mathematics
    Science
    Society
    Technology
    All portals

From today's featured article
Cleveland Centennial half dollar

The Cleveland Centennial half dollar is a commemorative United States half dollar, dated 1936, issued to mark the 100th anniversary of Cleveland, Ohio, as an incorporated city, and in commemoration of the Great Lakes Exposition, held in Cleveland that year. In the mid-1930s, commemorative coins were increasing in value, and Cincinnati businessman Thomas G. Melish, a coin collector, lobbied Congress to authorize several new issues, for which he would be the sole distributor. He was successful with the Cincinnati Musical Center half dollar and the Cleveland piece, and profited from both. Brenda Putnam designed the Cleveland coin, which was approved by the Commission of Fine Arts after suggestions by sculptor Lee Lawrie. Melish distributed the Cleveland coins through the exposition, at local banks, and by mail order from his office in Cincinnati. Sales were good, and the full authorized mintage of 50,000 was struck at the Philadelphia Mint. (Full article...)
Recently featured:

    John McGraw Jaguar British logistics in the Falklands War

    Archive By email More featured articles

Did you know ...
Thromidia catalai
Thromidia catalai

    ... that the starfish Thromidia catalai (pictured) can weigh as much as 6 kilograms (13 lb)?
    ... that the first exhibit of the West Virginia Music Hall of Fame came from founder Michael Lipton's record collection?
    ... that the senior Burmese princes could not attend the funeral of King Mindon since they had all been arrested?
    ... that in 1958, New Jersey assemblyman Carmine Savino proposed cutting property taxes in half by imposing a three-percent state sales tax that would be used to cover public school costs?
    ... that the Greenlandic novel Homo Sapienne was written in only one month?
    ... that when the Marquis Theatre was completed, some Broadway performers boycotted it because of a controversy over the construction of the hotel above it?
    ... that magma travelling through dykes usually solidifies before it gets to the Earth's surface?
    ... that Jonathan Weiner explains in his book how Time, Love, [and] Memory became associated with specific fly genes?

    Archive Start a new article Nominate an article


In the news
Magdalena Andersson
Magdalena Andersson

    Magdalena Andersson (pictured), who resigned a week earlier after one day as designate, is re-elected as Prime Minister of Sweden.
    Barbados becomes a republic, with Sandra Mason replacing Queen Elizabeth II as the head of state.
    In baseball, the Tokyo Yakult Swallows defeat the Orix Buffaloes to win the Japan Series.
    American musical theatre composer and lyricist Stephen Sondheim dies at the age of 91.

Ongoing:

    COVID-19 pandemic

Recent deaths:

    Ray Kennedy Aron Atabek Hermann Bausinger Norodom Ranariddh Virgil Abloh Mārtiņš Brauns

    Nominate an article

On this day

December 1: World AIDS Day; Great Union Day in Romania (1918)
Francis Walsingham
Francis Walsingham

    1577 – Francis Walsingham (pictured), Elizabeth I of England's principal secretary and spymaster, was knighted.
    1821 – On the island of Hispaniola, General José Núñez de Cáceres established the Republic of Spanish Haiti, which only lasted three months.
    1941 – The Civil Air Patrol, the civilian auxiliary of the United States Air Force, was founded.
    1971 – A period of political and economic reforms known as the Croatian Spring came to an end as the League of Communists of Yugoslavia decided to purge the reformist leadership of Croatia.
    1991 – More than 92 percent of voters approved the independence of Ukraine as declared on 24 August.

    Archie MacLaren (b. 1871)Zhu De (b. 1886)Anna Roosevelt Halsted (d. 1975)

More anniversaries:

    November 30 December 1 December 2

    Archive By email List of days of the year

Today's featured picture
Northern royal albatross

The northern royal albatross (Diomedea sanfordi) is a large seabird in the albatross family, Diomedeidae. It nests only on the Chatham Islands, on Enderby Island, and at Taiaroa Head on the Otago Peninsula of New Zealand. It spends the rest of the year away from land, in circumpolar flights over the Southern Ocean, feeding on squid, fish, crustaceans, salps and carrion. The species is listed on the IUCN Red List as endangered, but predators have been eliminated from the islands where it breeds, and conservation efforts have proved successful at the Taiaroa Head colony. This northern royal albatross was photographed off the southeastern coast of Tasmania, Australia.

Photograph credit: John Harrison
Recently featured:

    Henry Taube Walchensee Hydroelectric Power Station A Meeting in the Royal Danish Academy of Sciences and Letters

    Archive More featured pictures

Other areas of Wikipedia

    Community portal – Bulletin board, projects, resources and activities covering a wide range of Wikipedia areas.
    Help desk – Ask questions about using Wikipedia.
    Reference desk – Serving as virtual librarians, Wikipedia volunteers tackle your questions on a wide range of subjects.
    Site news – Announcements, updates, articles and press releases on Wikipedia and the Wikimedia Foundation.
    Teahouse – To ask your first basic questions about contributing to Wikipedia.
    Village pump – For discussions about Wikipedia itself, including areas for technical issues and policies.

Wikipedia's sister projects

Wikipedia is hosted by the Wikimedia Foundation, a non-profit organization that also hosts a range of other projects:

    Commons logo
    Commons
    Free media repository
    MediaWiki logo
    MediaWiki
    Wiki software development
    Meta-Wiki logo
    Meta-Wiki
    Wikimedia project coordination
    Wikibooks logo
    Wikibooks
    Free textbooks and manuals
    Wikidata logo
    Wikidata
    Free knowledge base
    Wikinews logo
    Wikinews
    Free-content news
    Wikiquote logo
    Wikiquote
    Collection of quotations
    Wikisource logo
    Wikisource
    Free-content library
    Wikispecies logo
    Wikispecies
    Directory of species
    Wikiversity logo
    Wikiversity
    Free learning tools
    Wikivoyage logo
    Wikivoyage
    Free travel guide
    Wiktionary logo
    Wiktionary
    Dictionary and thesaurus

Wikipedia languages

This Wikipedia is written in English. Many other Wikipedias are available; some of the largest are listed below.

    1,000,000+ articles
        العربية Deutsch Español Français Italiano Nederlands 日本語 Polski Português Русский Svenska Українська Tiếng Việt 中文
    250,000+ articles
        Bahasa Indonesia Bahasa Melayu Bân-lâm-gú Български Català Čeština Dansk Esperanto Euskara فارسی‎ עברית 한국어 Magyar Norsk Bokmål Română Srpski Srpskohrvatski Suomi Türkçe
    50,000+ articles
        Asturianu Bosanski Eesti Ελληνικά Simple English Galego Hrvatski Latviešu Lietuvių മലയാളം Македонски Norsk nynorsk Shqip Slovenčina Slovenščina ไทย

Navigation menu

    Not logged in
    Talk
    Contributions
    Create account
    Log in

    Main Page
    Talk

    Read
    View source
    View history

Search

    Main page
    Contents
    Current events
    Random article
    About Wikipedia
    Contact us
    Donate

Contribute

    Help
    Learn to edit
    Community portal
    Recent changes
    Upload file

Tools

    What links here
    Related changes
    Special pages
    Permanent link
    Page information
    Wikidata item

Print/export

    Download as PDF
    Printable version

In other projects

    Wikimedia Commons
    MediaWiki
    Meta-Wiki
    Multilingual Wikisource
    Wikispecies
    Wikibooks
    Wikidata
    Wikimania
    Wikinews
    Wikiquote
    Wikisource
    Wikiversity
    Wikivoyage
    Wiktionary

Languages

    العربية
    বাংলা
    Български
    Bosanski
    Català
    Čeština
    Dansk
    Deutsch
    Eesti
    Ελληνικά
    Español
    Esperanto
    Euskara
    فارسی
    Français
    Galego
    한국어
    Hrvatski
    Bahasa Indonesia
    Italiano
    עברית
    ქართული
    Latviešu
    Lietuvių
    Magyar
    Македонски
    Bahasa Melayu
    Nederlands
    日本語
    Norsk bokmål
    Norsk nynorsk
    Polski
    Português
    Română
    Русский
    Simple English
    Slovenčina
    Slovenščina
    Српски / srpski
    Srpskohrvatski / српскохрватски
    Suomi
    Svenska
    ไทย
    Türkçe
    Українська
    Tiếng Việt
    中文
    Complete list

    Text is available under the Creative Commons Attribution-ShareAlike License; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. Wikipedia® is a registered trademark of the Wikimedia Foundation, Inc., a non-profit organization.

    Privacy policy
    About Wikipedia
    Disclaimers
    Contact Wikipedia
    Mobile view
    Developers
    Statistics
    Cookie statement

    Wikimedia Foundation
    Powered by MediaWiki


Jump to navigation
Jump to search
Welcome to Wikipedia,
the free encyclopedia that anyone can edit.
6,416,084 articles in English

    The arts
    Biography
    Geography
    History
    Mathematics
    Science
    Society
    Technology
    All portals

From today's featured article
Cleveland Centennial half dollar

The Cleveland Centennial half dollar is a commemorative United States half dollar, dated 1936, issued to mark the 100th anniversary of Cleveland, Ohio, as an incorporated city, and in commemoration of the Great Lakes Exposition, held in Cleveland that year. In the mid-1930s, commemorative coins were increasing in value, and Cincinnati businessman Thomas G. Melish, a coin collector, lobbied Congress to authorize several new issues, for which he would be the sole distributor. He was successful with the Cincinnati Musical Center half dollar and the Cleveland piece, and profited from both. Brenda Putnam designed the Cleveland coin, which was approved by the Commission of Fine Arts after suggestions by sculptor Lee Lawrie. Melish distributed the Cleveland coins through the exposition, at local banks, and by mail order from his office in Cincinnati. Sales were good, and the full authorized mintage of 50,000 was struck at the Philadelphia Mint. (Full article...)
Recently featured:

    John McGraw Jaguar British logistics in the Falklands War

    Archive By email More featured articles

Did you know ...
Thromidia catalai
Thromidia catalai

    ... that the starfish Thromidia catalai (pictured) can weigh as much as 6 kilograms (13 lb)?
    ... that the first exhibit of the West Virginia Music Hall of Fame came from founder Michael Lipton's record collection?
    ... that the senior Burmese princes could not attend the funeral of King Mindon since they had all been arrested?
    ... that in 1958, New Jersey assemblyman Carmine Savino proposed cutting property taxes in half by imposing a three-percent state sales tax that would be used to cover public school costs?
    ... that the Greenlandic novel Homo Sapienne was written in only one month?
    ... that when the Marquis Theatre was completed, some Broadway performers boycotted it because of a controversy over the construction of the hotel above it?
    ... that magma travelling through dykes usually solidifies before it gets to the Earth's surface?
    ... that Jonathan Weiner explains in his book how Time, Love, [and] Memory became associated with specific fly genes?

    Archive Start a new article Nominate an article


In the news
Magdalena Andersson
Magdalena Andersson

    Magdalena Andersson (pictured), who resigned a week earlier after one day as designate, is re-elected as Prime Minister of Sweden.
    Barbados becomes a republic, with Sandra Mason replacing Queen Elizabeth II as the head of state.
    In baseball, the Tokyo Yakult Swallows defeat the Orix Buffaloes to win the Japan Series.
    American musical theatre composer and lyricist Stephen Sondheim dies at the age of 91.

Ongoing:

    COVID-19 pandemic

Recent deaths:

    Ray Kennedy Aron Atabek Hermann Bausinger Norodom Ranariddh Virgil Abloh Mārtiņš Brauns

    Nominate an article

On this day

December 1: World AIDS Day; Great Union Day in Romania (1918)
Francis Walsingham
Francis Walsingham

    1577 – Francis Walsingham (pictured), Elizabeth I of England's principal secretary and spymaster, was knighted.
    1821 – On the island of Hispaniola, General José Núñez de Cáceres established the Republic of Spanish Haiti, which only lasted three months.
    1941 – The Civil Air Patrol, the civilian auxiliary of the United States Air Force, was founded.
    1971 – A period of political and economic reforms known as the Croatian Spring came to an end as the League of Communists of Yugoslavia decided to purge the reformist leadership of Croatia.
    1991 – More than 92 percent of voters approved the independence of Ukraine as declared on 24 August.

    Archie MacLaren (b. 1871)Zhu De (b. 1886)Anna Roosevelt Halsted (d. 1975)

More anniversaries:

    November 30 December 1 December 2

    Archive By email List of days of the year

Today's featured picture
Northern royal albatross

The northern royal albatross (Diomedea sanfordi) is a large seabird in the albatross family, Diomedeidae. It nests only on the Chatham Islands, on Enderby Island, and at Taiaroa Head on the Otago Peninsula of New Zealand. It spends the rest of the year away from land, in circumpolar flights over the Southern Ocean, feeding on squid, fish, crustaceans, salps and carrion. The species is listed on the IUCN Red List as endangered, but predators have been eliminated from the islands where it breeds, and conservation efforts have proved successful at the Taiaroa Head colony. This northern royal albatross was photographed off the southeastern coast of Tasmania, Australia.

Photograph credit: John Harrison
Recently featured:

    Henry Taube Walchensee Hydroelectric Power Station A Meeting in the Royal Danish Academy of Sciences and Letters

    Archive More featured pictures

Other areas of Wikipedia

    Community portal – Bulletin board, projects, resources and activities covering a wide range of Wikipedia areas.
    Help desk – Ask questions about using Wikipedia.
    Reference desk – Serving as virtual librarians, Wikipedia volunteers tackle your questions on a wide range of subjects.
    Site news – Announcements, updates, articles and press releases on Wikipedia and the Wikimedia Foundation.
    Teahouse – To ask your first basic questions about contributing to Wikipedia.
    Village pump – For discussions about Wikipedia itself, including areas for technical issues and policies.

Wikipedia's sister projects

Wikipedia is hosted by the Wikimedia Foundation, a non-profit organization that also hosts a range of other projects:

    Commons logo
    Commons
    Free media repository
    MediaWiki logo
    MediaWiki
    Wiki software development
    Meta-Wiki logo
    Meta-Wiki
    Wikimedia project coordination
    Wikibooks logo
    Wikibooks
    Free textbooks and manuals
    Wikidata logo
    Wikidata
    Free knowledge base
    Wikinews logo
    Wikinews
    Free-content news
    Wikiquote logo
    Wikiquote
    Collection of quotations
    Wikisource logo
    Wikisource
    Free-content library
    Wikispecies logo
    Wikispecies
    Directory of species
    Wikiversity logo
    Wikiversity
    Free learning tools
    Wikivoyage logo
    Wikivoyage
    Free travel guide
    Wiktionary logo
    Wiktionary
    Dictionary and thesaurus

Wikipedia languages

This Wikipedia is written in English. Many other Wikipedias are available; some of the largest are listed below.

    1,000,000+ articles
        العربية Deutsch Español Français Italiano Nederlands 日本語 Polski Português Русский Svenska Українська Tiếng Việt 中文
    250,000+ articles
        Bahasa Indonesia Bahasa Melayu Bân-lâm-gú Български Català Čeština Dansk Esperanto Euskara فارسی‎ עברית 한국어 Magyar Norsk Bokmål Română Srpski Srpskohrvatski Suomi Türkçe
    50,000+ articles
        Asturianu Bosanski Eesti Ελληνικά Simple English Galego Hrvatski Latviešu Lietuvių മലയാളം Македонски Norsk nynorsk Shqip Slovenčina Slovenščina ไทย

Navigation menu

    Not logged in
    Talk
    Contributions
    Create account
    Log in

    Main Page
    Talk

    Read
    View source
    View history

Search

    Main page
    Contents
    Current events
    Random article
    About Wikipedia
    Contact us
    Donate

Contribute

    Help
    Learn to edit
    Community portal
    Recent changes
    Upload file

Tools

    What links here
    Related changes
    Special pages
    Permanent link
    Page information
    Wikidata item

Print/export

    Download as PDF
    Printable version

In other projects

    Wikimedia Commons
    MediaWiki
    Meta-Wiki
    Multilingual Wikisource
    Wikispecies
    Wikibooks
    Wikidata
    Wikimania
    Wikinews
    Wikiquote
    Wikisource
    Wikiversity
    Wikivoyage
    Wiktionary

Languages

    العربية
    বাংলা
    Български
    Bosanski
    Català
    Čeština
    Dansk
    Deutsch
    Eesti
    Ελληνικά
    Español
    Esperanto
    Euskara
    فارسی
    Français
    Galego
    한국어
    Hrvatski
    Bahasa Indonesia
    Italiano
    עברית
    ქართული
    Latviešu
    Lietuvių
    Magyar
    Македонски
    Bahasa Melayu
    Nederlands
    日本語
    Norsk bokmål
    Norsk nynorsk
    Polski
    Português
    Română
    Русский
    Simple English
    Slovenčina
    Slovenščina
    Српски / srpski
    Srpskohrvatski / српскохрватски
    Suomi
    Svenska
    ไทย
    Türkçe
    Українська
    Tiếng Việt
    中文
    Complete list

    Text is available under the Creative Commons Attribution-ShareAlike License; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. Wikipedia® is a registered trademark of the Wikimedia Foundation, Inc., a non-profit organization.

    Privacy policy
    About Wikipedia
    Disclaimers
    Contact Wikipedia
    Mobile view
    Developers
    Statistics
    Cookie statement

    Wikimedia Foundation
    Powered by MediaWiki


Jump to navigation
Jump to search
Welcome to Wikipedia,
the free encyclopedia that anyone can edit.
6,416,084 articles in English

    The arts
    Biography
    Geography
    History
    Mathematics
    Science
    Society
    Technology
    All portals

From today's featured article
Cleveland Centennial half dollar

The Cleveland Centennial half dollar is a commemorative United States half dollar, dated 1936, issued to mark the 100th anniversary of Cleveland, Ohio, as an incorporated city, and in commemoration of the Great Lakes Exposition, held in Cleveland that year. In the mid-1930s, commemorative coins were increasing in value, and Cincinnati businessman Thomas G. Melish, a coin collector, lobbied Congress to authorize several new issues, for which he would be the sole distributor. He was successful with the Cincinnati Musical Center half dollar and the Cleveland piece, and profited from both. Brenda Putnam designed the Cleveland coin, which was approved by the Commission of Fine Arts after suggestions by sculptor Lee Lawrie. Melish distributed the Cleveland coins through the exposition, at local banks, and by mail order from his office in Cincinnati. Sales were good, and the full authorized mintage of 50,000 was struck at the Philadelphia Mint. (Full article...)
Recently featured:

    John McGraw Jaguar British logistics in the Falklands War

    Archive By email More featured articles

Did you know ...
Thromidia catalai
Thromidia catalai

    ... that the starfish Thromidia catalai (pictured) can weigh as much as 6 kilograms (13 lb)?
    ... that the first exhibit of the West Virginia Music Hall of Fame came from founder Michael Lipton's record collection?
    ... that the senior Burmese princes could not attend the funeral of King Mindon since they had all been arrested?
    ... that in 1958, New Jersey assemblyman Carmine Savino proposed cutting property taxes in half by imposing a three-percent state sales tax that would be used to cover public school costs?
    ... that the Greenlandic novel Homo Sapienne was written in only one month?
    ... that when the Marquis Theatre was completed, some Broadway performers boycotted it because of a controversy over the construction of the hotel above it?
    ... that magma travelling through dykes usually solidifies before it gets to the Earth's surface?
    ... that Jonathan Weiner explains in his book how Time, Love, [and] Memory became associated with specific fly genes?

    Archive Start a new article Nominate an article


In the news
Magdalena Andersson
Magdalena Andersson

    Magdalena Andersson (pictured), who resigned a week earlier after one day as designate, is re-elected as Prime Minister of Sweden.
    Barbados becomes a republic, with Sandra Mason replacing Queen Elizabeth II as the head of state.
    In baseball, the Tokyo Yakult Swallows defeat the Orix Buffaloes to win the Japan Series.
    American musical theatre composer and lyricist Stephen Sondheim dies at the age of 91.

Ongoing:

    COVID-19 pandemic

Recent deaths:

    Ray Kennedy Aron Atabek Hermann Bausinger Norodom Ranariddh Virgil Abloh Mārtiņš Brauns

    Nominate an article

On this day

December 1: World AIDS Day; Great Union Day in Romania (1918)
Francis Walsingham
Francis Walsingham

    1577 – Francis Walsingham (pictured), Elizabeth I of England's principal secretary and spymaster, was knighted.
    1821 – On the island of Hispaniola, General José Núñez de Cáceres established the Republic of Spanish Haiti, which only lasted three months.
    1941 – The Civil Air Patrol, the civilian auxiliary of the United States Air Force, was founded.
    1971 – A period of political and economic reforms known as the Croatian Spring came to an end as the League of Communists of Yugoslavia decided to purge the reformist leadership of Croatia.
    1991 – More than 92 percent of voters approved the independence of Ukraine as declared on 24 August.

    Archie MacLaren (b. 1871)Zhu De (b. 1886)Anna Roosevelt Halsted (d. 1975)

More anniversaries:

    November 30 December 1 December 2

    Archive By email List of days of the year

Today's featured picture
Northern royal albatross

The northern royal albatross (Diomedea sanfordi) is a large seabird in the albatross family, Diomedeidae. It nests only on the Chatham Islands, on Enderby Island, and at Taiaroa Head on the Otago Peninsula of New Zealand. It spends the rest of the year away from land, in circumpolar flights over the Southern Ocean, feeding on squid, fish, crustaceans, salps and carrion. The species is listed on the IUCN Red List as endangered, but predators have been eliminated from the islands where it breeds, and conservation efforts have proved successful at the Taiaroa Head colony. This northern royal albatross was photographed off the southeastern coast of Tasmania, Australia.

Photograph credit: John Harrison
Recently featured:

    Henry Taube Walchensee Hydroelectric Power Station A Meeting in the Royal Danish Academy of Sciences and Letters

    Archive More featured pictures

Other areas of Wikipedia

    Community portal – Bulletin board, projects, resources and activities covering a wide range of Wikipedia areas.
    Help desk – Ask questions about using Wikipedia.
    Reference desk – Serving as virtual librarians, Wikipedia volunteers tackle your questions on a wide range of subjects.
    Site news – Announcements, updates, articles and press releases on Wikipedia and the Wikimedia Foundation.
    Teahouse – To ask your first basic questions about contributing to Wikipedia.
    Village pump – For discussions about Wikipedia itself, including areas for technical issues and policies.

Wikipedia's sister projects

Wikipedia is hosted by the Wikimedia Foundation, a non-profit organization that also hosts a range of other projects:

    Commons logo
    Commons
    Free media repository
    MediaWiki logo
    MediaWiki
    Wiki software development
    Meta-Wiki logo
    Meta-Wiki
    Wikimedia project coordination
    Wikibooks logo
    Wikibooks
    Free textbooks and manuals
    Wikidata logo
    Wikidata
    Free knowledge base
    Wikinews logo
    Wikinews
    Free-content news
    Wikiquote logo
    Wikiquote
    Collection of quotations
    Wikisource logo
    Wikisource
    Free-content library
    Wikispecies logo
    Wikispecies
    Directory of species
    Wikiversity logo
    Wikiversity
    Free learning tools
    Wikivoyage logo
    Wikivoyage
    Free travel guide
    Wiktionary logo
    Wiktionary
    Dictionary and thesaurus

Wikipedia languages

This Wikipedia is written in English. Many other Wikipedias are available; some of the largest are listed below.

    1,000,000+ articles
        العربية Deutsch Español Français Italiano Nederlands 日本語 Polski Português Русский Svenska Українська Tiếng Việt 中文
    250,000+ articles
        Bahasa Indonesia Bahasa Melayu Bân-lâm-gú Български Català Čeština Dansk Esperanto Euskara فارسی‎ עברית 한국어 Magyar Norsk Bokmål Română Srpski Srpskohrvatski Suomi Türkçe
    50,000+ articles
        Asturianu Bosanski Eesti Ελληνικά Simple English Galego Hrvatski Latviešu Lietuvių മലയാളം Македонски Norsk nynorsk Shqip Slovenčina Slovenščina ไทย

Navigation menu

    Not logged in
    Talk
    Contributions
    Create account
    Log in

    Main Page
    Talk

    Read
    View source
    View history

Search

    Main page
    Contents
    Current events
    Random article
    About Wikipedia
    Contact us
    Donate

Contribute

    Help
    Learn to edit
    Community portal
    Recent changes
    Upload file

Tools

    What links here
    Related changes
    Special pages
    Permanent link
    Page information
    Wikidata item

Print/export

    Download as PDF
    Printable version

In other projects

    Wikimedia Commons
    MediaWiki
    Meta-Wiki
    Multilingual Wikisource
    Wikispecies
    Wikibooks
    Wikidata
    Wikimania
    Wikinews
    Wikiquote
    Wikisource
    Wikiversity
    Wikivoyage
    Wiktionary

Languages

    العربية
    বাংলা
    Български
    Bosanski
    Català
    Čeština
    Dansk
    Deutsch
    Eesti
    Ελληνικά
    Español
    Esperanto
    Euskara
    فارسی
    Français
    Galego
    한국어
    Hrvatski
    Bahasa Indonesia
    Italiano
    עברית
    ქართული
    Latviešu
    Lietuvių
    Magyar
    Македонски
    Bahasa Melayu
    Nederlands
    日本語
    Norsk bokmål
    Norsk nynorsk
    Polski
    Português
    Română
    Русский
    Simple English
    Slovenčina
    Slovenščina
    Српски / srpski
    Srpskohrvatski / српскохрватски
    Suomi
    Svenska
    ไทย
    Türkçe
    Українська
    Tiếng Việt
    中文
    Complete list

    Text is available under the Creative Commons Attribution-ShareAlike License; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. Wikipedia® is a registered trademark of the Wikimedia Foundation, Inc., a non-profit organization.

    Privacy policy
    About Wikipedia
    Disclaimers
    Contact Wikipedia
    Mobile view
    Developers
    Statistics
    Cookie statement

    Wikimedia Foundation
    Powered by MediaWiki


Jump to navigation
Jump to search
Welcome to Wikipedia,
the free encyclopedia that anyone can edit.
6,416,084 articles in English

    The arts
    Biography
    Geography
    History
    Mathematics
    Science
    Society
    Technology
    All portals

From today's featured article
Cleveland Centennial half dollar

The Cleveland Centennial half dollar is a commemorative United States half dollar, dated 1936, issued to mark the 100th anniversary of Cleveland, Ohio, as an incorporated city, and in commemoration of the Great Lakes Exposition, held in Cleveland that year. In the mid-1930s, commemorative coins were increasing in value, and Cincinnati businessman Thomas G. Melish, a coin collector, lobbied Congress to authorize several new issues, for which he would be the sole distributor. He was successful with the Cincinnati Musical Center half dollar and the Cleveland piece, and profited from both. Brenda Putnam designed the Cleveland coin, which was approved by the Commission of Fine Arts after suggestions by sculptor Lee Lawrie. Melish distributed the Cleveland coins through the exposition, at local banks, and by mail order from his office in Cincinnati. Sales were good, and the full authorized mintage of 50,000 was struck at the Philadelphia Mint. (Full article...)
Recently featured:

    John McGraw Jaguar British logistics in the Falklands War

    Archive By email More featured articles

Did you know ...
Thromidia catalai
Thromidia catalai

    ... that the starfish Thromidia catalai (pictured) can weigh as much as 6 kilograms (13 lb)?
    ... that the first exhibit of the West Virginia Music Hall of Fame came from founder Michael Lipton's record collection?
    ... that the senior Burmese princes could not attend the funeral of King Mindon since they had all been arrested?
    ... that in 1958, New Jersey assemblyman Carmine Savino proposed cutting property taxes in half by imposing a three-percent state sales tax that would be used to cover public school costs?
    ... that the Greenlandic novel Homo Sapienne was written in only one month?
    ... that when the Marquis Theatre was completed, some Broadway performers boycotted it because of a controversy over the construction of the hotel above it?
    ... that magma travelling through dykes usually solidifies before it gets to the Earth's surface?
    ... that Jonathan Weiner explains in his book how Time, Love, [and] Memory became associated with specific fly genes?

    Archive Start a new article Nominate an article


In the news
Magdalena Andersson
Magdalena Andersson

    Magdalena Andersson (pictured), who resigned a week earlier after one day as designate, is re-elected as Prime Minister of Sweden.
    Barbados becomes a republic, with Sandra Mason replacing Queen Elizabeth II as the head of state.
    In baseball, the Tokyo Yakult Swallows defeat the Orix Buffaloes to win the Japan Series.
    American musical theatre composer and lyricist Stephen Sondheim dies at the age of 91.

Ongoing:

    COVID-19 pandemic

Recent deaths:

    Ray Kennedy Aron Atabek Hermann Bausinger Norodom Ranariddh Virgil Abloh Mārtiņš Brauns

    Nominate an article

On this day

December 1: World AIDS Day; Great Union Day in Romania (1918)
Francis Walsingham
Francis Walsingham

    1577 – Francis Walsingham (pictured), Elizabeth I of England's principal secretary and spymaster, was knighted.
    1821 – On the island of Hispaniola, General José Núñez de Cáceres established the Republic of Spanish Haiti, which only lasted three months.
    1941 – The Civil Air Patrol, the civilian auxiliary of the United States Air Force, was founded.
    1971 – A period of political and economic reforms known as the Croatian Spring came to an end as the League of Communists of Yugoslavia decided to purge the reformist leadership of Croatia.
    1991 – More than 92 percent of voters approved the independence of Ukraine as declared on 24 August.

    Archie MacLaren (b. 1871)Zhu De (b. 1886)Anna Roosevelt Halsted (d. 1975)

More anniversaries:

    November 30 December 1 December 2

    Archive By email List of days of the year

Today's featured picture
Northern royal albatross

The northern royal albatross (Diomedea sanfordi) is a large seabird in the albatross family, Diomedeidae. It nests only on the Chatham Islands, on Enderby Island, and at Taiaroa Head on the Otago Peninsula of New Zealand. It spends the rest of the year away from land, in circumpolar flights over the Southern Ocean, feeding on squid, fish, crustaceans, salps and carrion. The species is listed on the IUCN Red List as endangered, but predators have been eliminated from the islands where it breeds, and conservation efforts have proved successful at the Taiaroa Head colony. This northern royal albatross was photographed off the southeastern coast of Tasmania, Australia.

Photograph credit: John Harrison
Recently featured:

    Henry Taube Walchensee Hydroelectric Power Station A Meeting in the Royal Danish Academy of Sciences and Letters

    Archive More featured pictures

Other areas of Wikipedia

    Community portal – Bulletin board, projects, resources and activities covering a wide range of Wikipedia areas.
    Help desk – Ask questions about using Wikipedia.
    Reference desk – Serving as virtual librarians, Wikipedia volunteers tackle your questions on a wide range of subjects.
    Site news – Announcements, updates, articles and press releases on Wikipedia and the Wikimedia Foundation.
    Teahouse – To ask your first basic questions about contributing to Wikipedia.
    Village pump – For discussions about Wikipedia itself, including areas for technical issues and policies.

Wikipedia's sister projects

Wikipedia is hosted by the Wikimedia Foundation, a non-profit organization that also hosts a range of other projects:

    Commons logo
    Commons
    Free media repository
    MediaWiki logo
    MediaWiki
    Wiki software development
    Meta-Wiki logo
    Meta-Wiki
    Wikimedia project coordination
    Wikibooks logo
    Wikibooks
    Free textbooks and manuals
    Wikidata logo
    Wikidata
    Free knowledge base
    Wikinews logo
    Wikinews
    Free-content news
    Wikiquote logo
    Wikiquote
    Collection of quotations
    Wikisource logo
    Wikisource
    Free-content library
    Wikispecies logo
    Wikispecies
    Directory of species
    Wikiversity logo
    Wikiversity
    Free learning tools
    Wikivoyage logo
    Wikivoyage
    Free travel guide
    Wiktionary logo
    Wiktionary
    Dictionary and thesaurus

Wikipedia languages

This Wikipedia is written in English. Many other Wikipedias are available; some of the largest are listed below.

    1,000,000+ articles
        العربية Deutsch Español Français Italiano Nederlands 日本語 Polski Português Русский Svenska Українська Tiếng Việt 中文
    250,000+ articles
        Bahasa Indonesia Bahasa Melayu Bân-lâm-gú Български Català Čeština Dansk Esperanto Euskara فارسی‎ עברית 한국어 Magyar Norsk Bokmål Română Srpski Srpskohrvatski Suomi Türkçe
    50,000+ articles
        Asturianu Bosanski Eesti Ελληνικά Simple English Galego Hrvatski Latviešu Lietuvių മലയാളം Македонски Norsk nynorsk Shqip Slovenčina Slovenščina ไทย

Navigation menu

    Not logged in
    Talk
    Contributions
    Create account
    Log in

    Main Page
    Talk

    Read
    View source
    View history

Search

    Main page
    Contents
    Current events
    Random article
    About Wikipedia
    Contact us
    Donate

Contribute

    Help
    Learn to edit
    Community portal
    Recent changes
    Upload file

Tools

    What links here
    Related changes
    Special pages
    Permanent link
    Page information
    Wikidata item

Print/export

    Download as PDF
    Printable version

In other projects

    Wikimedia Commons
    MediaWiki
    Meta-Wiki
    Multilingual Wikisource
    Wikispecies
    Wikibooks
    Wikidata
    Wikimania
    Wikinews
    Wikiquote
    Wikisource
    Wikiversity
    Wikivoyage
    Wiktionary

Languages

    العربية
    বাংলা
    Български
    Bosanski
    Català
    Čeština
    Dansk
    Deutsch
    Eesti
    Ελληνικά
    Español
    Esperanto
    Euskara
    فارسی
    Français
    Galego
    한국어
    Hrvatski
    Bahasa Indonesia
    Italiano
    עברית
    ქართული
    Latviešu
    Lietuvių
    Magyar
    Македонски
    Bahasa Melayu
    Nederlands
    日本語
    Norsk bokmål
    Norsk nynorsk
    Polski
    Português
    Română
    Русский
    Simple English
    Slovenčina
    Slovenščina
    Српски / srpski
    Srpskohrvatski / српскохрватски
    Suomi
    Svenska
    ไทย
    Türkçe
    Українська
    Tiếng Việt
    中文
    Complete list

    Text is available under the Creative Commons Attribution-ShareAlike License; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. Wikipedia® is a registered trademark of the Wikimedia Foundation, Inc., a non-profit organization.

    Privacy policy
    About Wikipedia
    Disclaimers
    Contact Wikipedia
    Mobile view
    Developers
    Statistics
    Cookie statement

    Wikimedia Foundation
    Powered by MediaWiki




"""

e = Encryption(stringg)

encrypted_message = e.encrypt()
print("\nencrypted_message: ", encrypted_message)
d = Decryption(encrypted_message)
decrypted_message = d.decrypt()
#print("decrypted_message: ", decrypted_message)
print(len(stringg))
