package database

func GetFirstNames() []string {
	return []string{
		"ivan", "matvey", "vitaly",
		"artem", "alexander", "roman",
		"evgeny", "maksim", "denis",
		"alexey", "dmitry", "sergey",
		"nikolai", "konstantin", "nikita",
		"mikhail", "boris", "victor",
		"gennady", "vyacheslav", "vladimir",
		"andrei", "anatoly", "ilya",
		"kirill", "oleg", "sofia",
		"anastasia", "victoria", "ksenia",
		"arina", "elizaveta", "adelina",
		"irina", "elena", "polina",
		"daria", "natalia", "svetlana",
		"vera", "nadezhda", "galina",
		"lubov", "alexandra", "maria",
		"anna", "angelina", "marina",
		"ekaterina", "ludmila", "tatyana",
	}
}

func GetSecondNames() []string {
	return []string{
		"ivanov", "kuznetsov", "petrov",
		"smirnov", "magomedov", "popov",
		"volkov", "morozov", "novikov",
		"pavlov", "andreev", "vasilyev",
		"romanov", "makarov", "lebedev",
		"kozlov", "egorov", "zakharov",
		"stepanov", "nikitin", "orlov",
	}
}

func GetMails() []string {
	return []string{
		"gmail.com", "dvfu.ru", "mail.ru",
		"yandex.ru", "protonmail.com", "outlook.com",
	}
}

func GetDishes() [][]string {
	return [][]string{
		{
			// Завтраки
			"Каша рисовая молочная (карамель)",
			"Каша рисовая молочная (шоколад)",
			"Каша рисовая молочная (апельсин)",
			"Каша овсяная молочная (персик)",
			"Каша овсяная молочная (ананас)",
			"Завтрак рыбный с малосольным лососем и яйцом пашот на вафельном дранике",
			"Завтрак мясной с котлетой, маринованными огурчиками и яичницой глазуньей",
			"Завтрак с курицей в панировке и помидорами",
		},
		{
			// Салаты
			"Салат с курицей (аля цезарь)",
			"Салат по-гречески",
			"Поке с лососем",
			"Поке с курицей",
			"Салат с запеченной свеклой",
			"Салат с куриной печенью",
			"Баклажаны в азиатском стиле",
		},
		{
			// Супы
			"Том Ям",
			"Том Кха",
			"Сливочный грибной с сухариками",
			"Гороховый с копченостями",
			"Куриный с лапшой",
			"Уха по-фински",
			"Куриный с яйцом",
		},
		{
			// Вторые блюда
			"Фетучини карбонара",
			"Фетучини болоньез",
			"Гуляш с гарниром",
			"Язык с гарниром",
			"Курица в панировке с картофельными дольками Комбо",
			"Курица в азиатском стиле",
			"Плов",
			"Рагу в азиатском стиле",
			"Биточки из лосося с гарниром",
			"Биточки куриные с гарниром",
		},
		{
			// Выпечка
			"Пян-се",
			"Синабон",
			"Печенье Бискотти",
			"Печенье Кантучи",
			"Тарт ягодный",
			"Тарт цитрусовый",
			"Улитка",
			"Ромовая баба",
			"Кекс рождественский",
			"Кекс лимонный",
			"Овсяное печенье",
		},
		{
			// Десерты
			"Тарталетка вишня-шоколад",
			"Тарталетка фисташка-малина",
			"Тарталетка лимонная",
			"Чиа пуддинг",
			"Меренговый рулет",
			"Дамские пальчики",
			"Пироженное картошка",
			"Заварное колицо",
			"Панакота с малиной",
		},
		{
			// Пицца
			"Пепперони",
			"Три сыра",
			"Курица и грибы",
			"Маргарита",
			"Гавайская",
		},
	}
}

func GetBannerPaths() []string {
	return []string{
		"banners/рисовая каша.webp",
		"banners/рисовая каша.webp",
		"banners/рисовая каша.webp",
		"banners/овсяная каша.webp",
		"banners/овсяная каша.webp",
		"banners/завтрак рыбный.webp",
		"banners/мясной завтрак.webp",
		"banners/завтрак курица.webp",
		"banners/салат с курицей.webp",
		"banners/греческий салат.webp",
		"banners/поке с лососем.webp",
		"banners/поке с курицей.webp",
		"banners/салат с запечёной свеклойjpg.webp",
		"banners/салат с куриной печенью.webp",
		"banners/баклажаны в азиатском стиле.webp",
		"banners/том ям.webp",
		"banners/том кха.webp",
		"banners/сливочный грибной суп.webp",
		"banners/суп гороховый с копченностями.webp",
		"banners/суп куриный с лапшой.webp",
		"banners/уха по-фински.webp",
		"banners/куриный с яйцом.webp",
		"banners/фетучинни карбонара.webp",
		"banners/фетучини болоньез.webp",
		"banners/гуляш с гарниром.webp",
		"banners/язык с гарниром.webp",
		"banners/куриная панировка и картофельные дольки КОМБО .webp",
		"banners/курица в азиатском стиле.webp",
		"banners/плов.webp",
		"banners/рагу в азиатском стиле.webp",
		"banners/биточки из лосося с гарниром.webp",
		"banners/куриные биточки с гарниром.webp",
		"banners/пянсе.webp",
		"banners/синабон.webp",
		"banners/печенье бискотти.webp",
		"banners/печенье кантучи.webp",
		"banners/ягодный тарт.webp",
		"banners/цитрусовый тарт.webp",
		"banners/улитка.webp",
		"banners/ромовая баба.webp",
		"banners/кекс рождественский.webp",
		"banners/кекс лимонный.webp",
		"banners/овсяное печенье.webp",
		"banners/тарталетки вишня-шоколад.webp",
		"banners/тарталетки фисташка-малинаjpg.webp",
		"banners/тарталетка лимон.webp",
		"banners/чиа пудинг.webp",
		"banners/меренговый рулет.webp",
		"banners/дамские пальцы.webp",
		"banners/пироженное картошка.webp",
		"banners/заварное кольцо.webp",
		"banners/панакота с малиной.webp",
		"banners/пепперони.webp",
		"banners/три сыра.webp",
		"banners/курица грибы.webp",
		"banners/пицца маргарита.webp",
		"banners/пицца гавайская.webp",
	}
}

func GetDishCategories() []string {
	return []string{
		"Завтраки",
		"Салаты",
		"Супы",
		"Вторые блюда",
		"Выпечка",
		"Десерты",
		"Пицца",
	}
}
