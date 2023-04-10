from config import *

English = {

    "hello_word": "Hello!\n"
                  "You can send me a photo with a question or just text, and I will return the solution to this question or task to you.\n"
                  "For further instructions, use the commands:\n"
                  "/commands - to get a list of available commands\n"
                  "/menu - to open the menu",

    "commands": "🛠 Available commands:\n"
                "/commands - List of all commands\n"
                "/menu - Active menu\n"
                "/lang - Switch interface language\n"
                "/id - Supported languages ID\n"
                "/a - Get an answer to a text question\n",

    "sry_private": "Sorry, but I only work in private messages.",

    "send_p": "📷 Send Photo",
    "send_t": "💬 Send Text",
    "get_t": "📝 Get Text",
    "mbal": "💰 My Balance",
    "menu_active": "☑️ Menu buttons activated ☑️",

    "sup_lang_list": "🔘 Supported languages ID 🔘\n"
                     "ID - Description\n"
                     "_________________\n"
                     "eng - English 🇬🇧\n"
                     "deu - German 🇩🇪\n"
                     "fra - French 🇫🇷\n"
                     "rus - Russian 🇷🇺\n"
                     "ukr - Ukrainian 🇺🇦",

    "lang1": "🇬🇧English",
    "lang2": "🇷🇺Russian",
    "lang3": "🇺🇦Ukrainian",
    "lang4": "🇩🇪German",
    "lang5": "🇫🇷French",

    "c_lang": "Choose your language: 🇬🇧🇷🇺🇺🇦🇩🇪🇫🇷",
    "lang_switch1": "Language switch to English",
    "lang_switch2": "Language switch to Russian",
    "lang_switch3": "Language switch to Ukrainian",
    "lang_switch4": "Language switch to German",
    "lang_switch5": "Language switch to French",

    "pls_wait": "⏱ Please wait while processing... ⏱",

    "error_tlim": "⛔️ERROR⛔️\n"
                  "Your text has exceeded the allowed word limit.\n"
                  f"Set limit is {token_limit} words/per query.",
    "error_stext": "⛔️ERROR⛔️\n"
                   "You sent an empty message to the request.\n"
                   "Example:\n"
                   "/a <your text>",

    "reactivate_menu": "Reactivate your menu.\nPress this command: /menu",

    "sp_desc": "🔹 Send a photo with a clear text of the task on it to the chat ⬇️\n"
               "For high-quality text detection on an image - use the language id (/lang) in caption to photo.",
    "st_desc": "🔹 Send the text of your request to the chat below.\n"
               "Example (<> - brackets are optional):\n"
               "/a <your text>",
    "gt_desc": "🔹 Send a photo with the caption '/t <lang id>' to the chat (<> - brackets are optional).\n"
               "Caption example:\n"
               "/t ukr",

    "gb_check": "💰 My Balance:\n🔘 {} $TKN",

    "pay_token_suc": "🟢 Payment successful. 🟢\nPrice: 1 $TKN.",
    "pay_token_decl": "🔴 Payment declined. 🔴\nInsufficient balance. Top up your balance.",

    "post_text": "🔸ANSWER🔸\n",

    "error_too_big_img": f"⛔️ERROR⛔️\nYou have sent a file that is too large.\nThe file size limit is {allow_img_size/1_000_000} MB.",

}

Russian = {

    "hello_word": "Здравствуйте!\n"
                  "Вы можете прислать мне фото с вопросом или просто текст, и я верну вам решение этого вопроса или задачи.\n"
                  "Для получения дальнейших инструкций используйте команды:\n"
                  "/commands - чтобы получить список доступных команд\n"
                  "/menu - чтобы открыть меню",

    "commands": "🛠 Доступные команды:\n"
                "/commands - Список всех команд\n"
                "/menu - Активное меню\n"
                "/lang - Переключить язык интерфейса\n"
                "/id - ID Поддерживаемых языков\n"
                "/a - Получить ответ на текстовый вопрос",

    "sry_private": "Извините, но я работаю только в личных сообщениях.",

    "send_p": "📷 Отправить фото",
    "send_t": "💬 Послать текст",
    "get_t": "📝 Распознать текст",
    "mbal": "💰 Мой баланс",
    "menu_active": "☑️ Кнопки меню активированы ☑️",

    "sup_lang_list": "🔘 ID Поддерживаемых языков 🔘\n"
                     "ID - Описание\n"
                     "_________________\n"
                     "eng - Английский 🇬🇧\n"
                     "deu - Немецкий 🇩🇪\n"
                     "fra - Французский 🇫🇷\n"
                     "rus - Русский 🇷🇺\n"
                     "ukr - Украинский 🇺🇦",

    "lang1": "🇬🇧Английский",
    "lang2": "🇷🇺Русский",
    "lang3": "🇺🇦Украинский",
    "lang4": "🇩🇪Немецкий",
    "lang5": "🇫🇷Французский",

    "c_lang": "Выберите ваш язык: 🇬🇧🇷🇺🇺🇦🇩🇪🇫🇷",
    "lang_switch1": "Переключение языка на Английский",
    "lang_switch2": "Переключение языка на Русский",
    "lang_switch3": "Переключение языка на Украинский",
    "lang_switch4": "Переключение языка на Немецкий",
    "lang_switch5": "Переключение языка на Французский",

    "pls_wait": "⏱ Подождите, идет обработка... ⏱",

    "error_tlim": "⛔️ОШИБКА⛔️\n"
                  "В вашем тексте превышен допустимый лимит слов.\n"
                  f"Установленный лимит: {token_limit} слов/за запрос.",
    "error_stext": "⛔️ОШИБКА⛔️\n"
                   "Вы отправили пустое сообщение на запрос.\n"
                   "Пример (<> - скобки необязательны):\n"
                   "/a <ваш текст>",

    "reactivate_menu": "Повторно активируйте свое меню.\nНажмите на эту команду: /menu",

    "sp_desc": "🔹 Отправьте фото с четко видимым и различимым текстом задачи в чат ⬇️\n"
               "Для качественного определения текста на изображении используйте ID языка в подписи к фото.",
    "st_desc": "🔹 Отправьте текст вашего запроса в чат ниже.\n"
               "Пример (<> - скобки необязательны):\n"
               "/a <ваш текст>",
    "gt_desc": "🔹 Отправьте в чат фото с подписью '/t <lang id>' (<> - скобки необязательны).\n"
               "Пример подписи:\n"
               "/t ukr",

    "gb_check": "💰 Мой баланс:\n🔘 {} $TKN",

    "pay_token_suc": "🟢 Оплата прошла успешно. 🟢\nЦена: 1 $TKN.",
    "pay_token_decl": "🔴 Платеж отклонен. 🔴\nНедостаточный баланс. Пополните свой баланс.",

    "post_text": "🔸ОТВЕТ🔸\n",
    "error_too_big_img": f"⛔️ОШИБКА⛔️\nВы отправили слишком большой файл.\nОграничение на размер файла: {allow_img_size / 1_000_000} MB."

}

Ukrainian = {

    "hello_word": "Вітаю!\n"
                  "Ви можете надіслати мені фото з питанням або просто текст, і я поверну вам вирішення цього питання або завдання.\n"
                  "Для подальших інструкцій використовуйте команди:\n"
                  "/commands - щоб отримати список доступних команд\n"
                  "/menu - щоб відкрити меню",

    "commands": "🛠 Доступні команди:\n"
                "/commands - Список усіх команд\n"
                "/menu - Активне меню\n"
                "/lang - Переключити мову інтерфейсу\n"
                "/id - ID мов, що підтримуються\n"
                "/a - Отримати відповідь на текстове запитання",

    "sry_private": "Вибачте, але я працюю лише в особистих повідомленнях.",

    "send_p": "📷 Відправити фото",
    "send_t": "💬 Надіслати текст",
    "get_t": "📝 Розпізнати текст",
    "mbal": "💰 Мій баланс",
    "menu_active": "☑️ Кнопки меню активовані ☑️",

    "sup_lang_list": "🔘 ID мов, що підтримуються 🔘\n"
                     "ID - Опис\n"
                     "_________________\n"
                     "eng - Англійська 🇬🇧\n"
                     "deu - Німецька 🇩🇪\n"
                     "fra - Французька 🇫🇷\n"
                     "rus - Російська 🇷🇺\n"
                     "ukr - Українська 🇺🇦",

    "lang1": "🇬🇧Англійська",
    "lang2": "🇷🇺Російська",
    "lang3": "🇺🇦Українська",
    "lang4": "🇩🇪Німецька",
    "lang5": "🇫🇷Французька",

    "c_lang": "Виберіть вашу мову: 🇬🇧🇷🇺🇺🇦🇩🇪🇫🇷",
    "lang_switch1": "Перемикання мови на Англійську",
    "lang_switch2": "Перемикання мови на Російську",
    "lang_switch3": "Перемикання мови на Українську",
    "lang_switch4": "Перемикання мови на Німецьку",
    "lang_switch5": "Перемикання мови на Французьку",

    "pls_wait": "⏱ Зачекайте, йде обробка... ⏱",

    "error_tlim": "⛔️ПОМИЛКА⛔️\n"
                  "У тексті перевищено допустимий ліміт слів.\n"
                  f"Встановлений ліміт: {token_limit} слів/за запит.",
    "error_stext": "⛔️ПОМИЛКА⛔️\n"
                   "Ви надіслали порожнє повідомлення на запит.\n"
                   "Приклад (<> - дужки необов'язкові):\n"
                   "/a <ваш текст>",

    "reactivate_menu": "Повторно активуйте своє меню.\nНатисніть на цю команду: /menu",

    "sp_desc": "🔹 Надішліть фото з чітко видимим і помітним текстом завдання в чат ⬇️\n"
               "Для якісного визначення тексту на зображенні використовуйте ID мови підпису до фото.",
    "st_desc": "🔹 Надішліть текст вашого запиту в чат нижче.\n"
               "Приклад (<> - дужки необов'язкові):\n"
               "/a <ваш текст>",
    "gt_desc": "🔹 Надішліть у чат фото з підписом '/t <lang id>' (<> - дужки необов'язкові).\n"
               "Приклад підпису:\n"
               "/t ukr",

    "gb_check": "💰 Мій баланс:\n🔘 {} $TKN",

    "pay_token_suc": "🟢 Оплата пройшла успішно. 🟢\nЦіна: 1 $TKN.",
    "pay_token_decl": "🔴 Платіж відхилений. 🔴\nНедостатній баланс. Поповніть свій баланс.",

    "post_text": "🔸ВІДПОВІДЬ🔸\n",
    "error_too_big_img": f"⛔️ПОМИЛКА⛔️\nВи надіслали надто великий файл.\nОбмеження на розмір файлу: {allow_img_size / 1_000_000} MB."

}


German = {

    "hello_word": "Hallo!\n"
                  "Sie können mir ein Foto mit einer Frage oder einfach nur einem Text schicken, und ich werde Ihnen die Lösung zu dieser Frage oder Aufgabe zurücksenden.\n"
                  "Verwenden Sie für weitere Anweisungen die Befehle:\n"
                  "/commands - um eine Liste der verfügbaren Befehle zu erhalten\n"
                  "/menu - um das Menü zu öffnen",

    "commands": "🛠 Verfügbare Befehle:\n"
                "/commands - Liste aller Befehle\n"
                "/menu - Aktives Menü\n"
                "/lang - Sprache der Benutzeroberfläche wechseln\n"
                "/id - Unterstützte Sprachen-ID\n"
                "/a - Erhalten Sie eine Antwort auf eine Textfrage\n",

    "sry_private": "Tut mir leid, aber ich arbeite nur in privaten Nachrichten.",

    "send_p": "📷 Foto senden",
    "send_t": "💬 Text senden",
    "get_t": "📝 Text erhalten",
    "mbal": "💰 Mein Gleichgewicht",
    "menu_active": "☑️ Menütasten aktiviert ☑️",

    "sup_lang_list": "🔘 Unterstützte Sprachen-ID 🔘\n"
                     "ID - Beschreibung\n"
                     "_________________\n"
                     "eng - Englisch 🇬🇧\n"
                     "deu - Deutsch 🇩🇪\n"
                     "fra - Französisch 🇫🇷\n"
                     "rus - Russisch 🇷🇺\n"
                     "ukr - Ukrainisch 🇺🇦",

    "lang1": "🇬🇧Englisch",
    "lang2": "🇷🇺Russisch",
    "lang3": "🇺🇦Ukrainisch",
    "lang4": "🇩🇪Deutsch",
    "lang5": "🇫🇷Französisch",

    "c_lang": "Wähle deine Sprache: 🇬🇧🇷🇺🇺🇦🇩🇪🇫🇷",
    "lang_switch1": "Sprachumschaltung auf Englisch",
    "lang_switch2": "Sprachumschaltung auf Russisch",
    "lang_switch3": "Sprachumschaltung auf Ukrainisch",
    "lang_switch4": "Sprachumschaltung auf Deutsch",
    "lang_switch5": "Sprachumschaltung auf Französisch",

    "pls_wait": "⏱ Bitte warten Sie während der Bearbeitung... ⏱",

    "error_tlim": "⛔️FEHLER⛔️\n"
                  "Ihr Text hat die zulässige Wortgrenze überschritten.\n"
                  f"Limit gesetzt ist {token_limit} Wörter/pro Abfrage.",
    "error_stext": "⛔️FEHLER⛔️\n"
                   "Sie haben eine leere Nachricht an die Anfrage gesendet.\n"
                   "Beispiel (<> - Klammern sind optional):\n"
                   "/a <dein text>",

    "reactivate_menu": "Reaktivieren Sie Ihr Menü.\nKlicken Sie auf diesen Befehl: /menu",

    "sp_desc": "🔹 Senden Sie ein Foto mit einem klaren Text der Aufgabe an den Chat ⬇️\n"
               "Verwenden Sie für eine qualitativ hochwertige Texterkennung auf einem Bild die Sprach-ID (/lang) in der Bildunterschrift.",
    "st_desc": "🔹 Senden Sie den Text Ihrer Anfrage an den Chat unten.\n"
               "Beispiel (<> - Klammern sind optional):\n"
               "/a <your text>",
    "gt_desc": "🔹 Senden Sie ein Foto mit der Beschriftung '/t <lang id>' an den Chat (<> - Klammern sind optional).\n"
               "Beschriftungsbeispiel:\n"
               "/t ger",

    "gb_check": "💰 Mein Gleichgewicht:\n🔘 {} $TKN",

    "pay_token_suc": "🟢 Bezahlung erfolgreich. 🟢\nPreis: 1 $TKN.",
    "pay_token_decl": "🔴 Zahlung abgelehnt. 🔴\nMangelhaftes Gleichgewicht. Laden Sie Ihr Guthaben auf.",

    "post_text": "🔸ANTWORTEN🔸\n",

    "error_too_big_img": f"⛔️FEHLER⛔️\nYSie haben eine zu große Datei gesendet.\nDie maximale Dateigröße beträgt {allow_img_size/1_000_000} MB.",

}


French = {

    "hello_word": "Bonjour!\n"
                  "Vous pouvez m'envoyer une photo avec une question ou simplement un texte, et je vous renverrai la solution à cette question ou tâche.\n"
                  "Pour plus d'instructions, utilisez les commandes:\n"
                  "/commands - pour obtenir une liste des commandes disponibles\n"
                  "/menu - pour ouvrir le menu",

    "commands": "🛠 Commandes disponibles:\n"
                "/commands - Liste de toutes les commandes\n"
                "/menu - Menu actif\n"
                "/lang - Changer la langue de l'interface\n"
                "/id - ID des langues prises en charge\n"
                "/a - Obtenir une réponse à une question textuelle\n",

    "sry_private": "Désolé, mais je ne travaille qu'en messages privés.",

    "send_p": "📷 Envoyer une photo",
    "send_t": "💬 Envoyer du texte",
    "get_t": "📝 Obtenir du texte",
    "mbal": "💰 Mon solde",
    "menu_active": "☑️ Boutons de menu activés ☑️",

    "sup_lang_list": "🔘 ID des langues prises en charge 🔘\n"
                     "ID - Description\n"
                     "_________________\n"
                     "eng - Anglais 🇬🇧\n"
                     "deu - Allemand 🇩🇪\n"
                     "fra - Français 🇫🇷\n"
                     "rus - Russe 🇷🇺\n"
                     "ukr - Ukrainien 🇺🇦",

    "lang1": "🇬🇧Anglais",
    "lang2": "🇷🇺Russe",
    "lang3": "🇺🇦Ukrainien",
    "lang4": "🇩🇪Allemand",
    "lang5": "🇫🇷Français",

    "c_lang": "Choisissez votre langue: 🇬🇧🇷🇺🇺🇦🇩🇪🇫🇷",
    "lang_switch1": "Changement de langue vers l'anglais",
    "lang_switch2": "Changement de langue vers le russe",
    "lang_switch3": "Changement de langue vers l'ukrainien",
    "lang_switch4": "Changement de langue vers l'allemand",
    "lang_switch5": "Changement de langue vers le français",

    "pls_wait": "⏱ Veuillez patienter pendant le traitement... ⏱",

    "error_tlim": "⛔️ERREUR⛔️\n"
                  "Votre texte a dépassé la limite de mots autorisée.\n"
                  f"La limite définie est {token_limit} mots/par requête.",
    "error_stext": "⛔️ERREUR⛔️\n"
                   "Vous avez envoyé un message vide à la demande.\n"
                   "Exemple:\n"
                   "/a <ton texte>",

    "reactivate_menu": "Réactivez votre menu.\nAppuyez sur cette commande: /menu",

    "sp_desc": "🔹 Envoyez une photo avec un texte clair de la tâche sur le chat ⬇️\n"
               "Pour une détection de texte de haute qualité sur une image, utilisez l'identifiant de langue (/lang) dans la légende de la photo.",
    "st_desc": "🔹 Envoyez le texte de votre demande au chat ci-dessous.\n"
               "Exemple (<> - les crochets sont facultatifs):\n"
               "/a <ton texte>",
    "gt_desc": "🔹 Envoyez une photo avec la légende '/t <lang id>' au chat (<> - les crochets sont facultatifs).\n"
               "Exemple de légende:\n"
               "/t fra",

    "gb_check": "💰 Mon solde:\n🔘 {} $TKN",

    "pay_token_suc": "🟢 Paiement réussi. 🟢\nPrix: 1 $TKN.",
    "pay_token_decl": "🔴 Paiement refusé. 🔴\nSolde insuffisant. Rechargez votre solde.",

    "post_text": "🔸RÉPONDRE🔸\n",

    "error_too_big_img": f"⛔️ERREUR⛔️\nVous avez envoyé un fichier trop volumineux.\nLa limite de taille de fichier est {allow_img_size/1_000_000} MB.",

}


language = [English, Russian, Ukrainian, German, French]
