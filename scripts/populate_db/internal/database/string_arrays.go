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
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B0%D1%8F%20%D0%BA%D0%B0%D1%88%D0%B0.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B0%D1%8F%20%D0%BA%D0%B0%D1%88%D0%B0.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B0%D1%8F%20%D0%BA%D0%B0%D1%88%D0%B0.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D0%BE%D0%B2%D1%81%D1%8F%D0%BD%D0%B0%D1%8F%20%D0%BA%D0%B0%D1%88%D0%B0.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D0%BE%D0%B2%D1%81%D1%8F%D0%BD%D0%B0%D1%8F%20%D0%BA%D0%B0%D1%88%D0%B0.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D0%B7%D0%B0%D0%B2%D1%82%D1%80%D0%B0%D0%BA%20%D1%80%D1%8B%D0%B1%D0%BD%D1%8B%D0%B9.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D0%BC%D1%8F%D1%81%D0%BD%D0%BE%D0%B9%20%D0%B7%D0%B0%D0%B2%D1%82%D1%80%D0%B0%D0%BA.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D0%B7%D0%B0%D0%B2%D1%82%D1%80%D0%B0%D0%BA%20%D0%BA%D1%83%D1%80%D0%B8%D1%86%D0%B0.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D1%81%D0%B0%D0%BB%D0%B0%D1%82%20%D1%81%20%D0%BA%D1%83%D1%80%D0%B8%D1%86%D0%B5%D0%B9.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D0%B3%D1%80%D0%B5%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%B0%D0%BB%D0%B0%D1%82.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D0%BF%D0%BE%D0%BA%D0%B5%20%D1%81%20%D0%BB%D0%BE%D1%81%D0%BE%D1%81%D0%B5%D0%BC.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D0%BF%D0%BE%D0%BA%D0%B5%20%D1%81%20%D0%BA%D1%83%D1%80%D0%B8%D1%86%D0%B5%D0%B9.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D1%81%D0%B0%D0%BB%D0%B0%D1%82%20%D1%81%20%D0%B7%D0%B0%D0%BF%D0%B5%D1%87%D1%91%D0%BD%D0%BE%D0%B9%20%D1%81%D0%B2%D0%B5%D0%BA%D0%BB%D0%BE%D0%B9jpg.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D1%81%D0%B0%D0%BB%D0%B0%D1%82%20%D1%81%20%D0%BA%D1%83%D1%80%D0%B8%D0%BD%D0%BE%D0%B9%20%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D1%8C%D1%8E.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D0%B1%D0%B0%D0%BA%D0%BB%D0%B0%D0%B6%D0%B0%D0%BD%D1%8B%20%D0%B2%20%D0%B0%D0%B7%D0%B8%D0%B0%D1%82%D1%81%D0%BA%D0%BE%D0%BC%20%D1%81%D1%82%D0%B8%D0%BB%D0%B5.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D1%82%D0%BE%D0%BC%20%D1%8F%D0%BC.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D1%82%D0%BE%D0%BC%20%D0%BA%D1%85%D0%B0.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D1%81%D0%BB%D0%B8%D0%B2%D0%BE%D1%87%D0%BD%D1%8B%D0%B9%20%D0%B3%D1%80%D0%B8%D0%B1%D0%BD%D0%BE%D0%B9%20%D1%81%D1%83%D0%BF.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D1%81%D1%83%D0%BF%20%D0%B3%D0%BE%D1%80%D0%BE%D1%85%D0%BE%D0%B2%D1%8B%D0%B9%20%D1%81%20%D0%BA%D0%BE%D0%BF%D1%87%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8F%D0%BC%D0%B8.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D1%81%D1%83%D0%BF%20%D0%BA%D1%83%D1%80%D0%B8%D0%BD%D1%8B%D0%B9%20%D1%81%20%D0%BB%D0%B0%D0%BF%D1%88%D0%BE%D0%B9.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D1%81%D1%83%D0%BF%20%D0%BA%D1%83%D1%80%D0%B8%D0%BD%D1%8B%D0%B9%20%D1%81%20%D0%BB%D0%B0%D0%BF%D1%88%D0%BE%D0%B9.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D1%81%D1%83%D0%BF%20%D0%BA%D1%83%D1%80%D0%B8%D0%BD%D1%8B%D0%B9%20%D1%81%20%D0%BB%D0%B0%D0%BF%D1%88%D0%BE%D0%B9.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D1%84%D0%B5%D1%82%D1%83%D1%87%D0%B8%D0%BD%D0%BD%D0%B8%20%D0%BA%D0%B0%D1%80%D0%B1%D0%BE%D0%BD%D0%B0%D1%80%D0%B0.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D1%84%D0%B5%D1%82%D1%83%D1%87%D0%B8%D0%BD%D0%B8%20%D0%B1%D0%BE%D0%BB%D0%BE%D0%BD%D1%8C%D0%B5%D0%B7.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D0%B3%D1%83%D0%BB%D1%8F%D1%88%20%D1%81%20%D0%B3%D0%B0%D1%80%D0%BD%D0%B8%D1%80%D0%BE%D0%BC.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D1%8F%D0%B7%D1%8B%D0%BA%20%D1%81%20%D0%B3%D0%B0%D1%80%D0%BD%D0%B8%D1%80%D0%BE%D0%BC.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D0%BA%D1%83%D1%80%D0%B8%D0%BD%D0%B0%D1%8F%20%D0%BF%D0%B0%D0%BD%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0%20%D0%B8%20%D0%BA%D0%B0%D1%80%D1%82%D0%BE%D1%84%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5%20%D0%B4%D0%BE%D0%BB%D1%8C%D0%BA%D0%B8%20%D0%9A%D0%9E%D0%9C%D0%91%D0%9E%20.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D0%BA%D1%83%D1%80%D0%B8%D1%86%D0%B0%20%D0%B2%20%D0%B0%D0%B7%D0%B8%D0%B0%D1%82%D1%81%D0%BA%D0%BE%D0%BC%20%D1%81%D1%82%D0%B8%D0%BB%D0%B5.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D0%BF%D0%BB%D0%BE%D0%B2.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D1%80%D0%B0%D0%B3%D1%83%20%D0%B2%20%D0%B0%D0%B7%D0%B8%D0%B0%D1%82%D1%81%D0%BA%D0%BE%D0%BC%20%D1%81%D1%82%D0%B8%D0%BB%D0%B5.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D0%B1%D0%B8%D1%82%D0%BE%D1%87%D0%BA%D0%B8%20%D0%B8%D0%B7%20%D0%BB%D0%BE%D1%81%D0%BE%D1%81%D1%8F%20%D1%81%20%D0%B3%D0%B0%D1%80%D0%BD%D0%B8%D1%80%D0%BE%D0%BC.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D0%BA%D1%83%D1%80%D0%B8%D0%BD%D1%8B%D0%B5%20%D0%B1%D0%B8%D1%82%D0%BE%D1%87%D0%BA%D0%B8%20%D1%81%20%D0%B3%D0%B0%D1%80%D0%BD%D0%B8%D1%80%D0%BE%D0%BC.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D0%BF%D1%8F%D0%BD%D1%81%D0%B5.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D1%81%D0%B8%D0%BD%D0%B0%D0%B1%D0%BE%D0%BD.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D1%8C%D0%B5%20%D0%B1%D0%B8%D1%81%D0%BA%D0%BE%D1%82%D1%82%D0%B8.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D1%8C%D0%B5%20%D0%BA%D0%B0%D0%BD%D1%82%D1%83%D1%87%D0%B8.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D1%8F%D0%B3%D0%BE%D0%B4%D0%BD%D1%8B%D0%B9%20%D1%82%D0%B0%D1%80%D1%82.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D1%86%D0%B8%D1%82%D1%80%D1%83%D1%81%D0%BE%D0%B2%D1%8B%D0%B9%20%D1%82%D0%B0%D1%80%D1%82.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D1%83%D0%BB%D0%B8%D1%82%D0%BA%D0%B0.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D1%80%D0%BE%D0%BC%D0%BE%D0%B2%D0%B0%D1%8F%20%D0%B1%D0%B0%D0%B1%D0%B0.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D0%BA%D0%B5%D0%BA%D1%81%20%D1%80%D0%BE%D0%B6%D0%B4%D0%B5%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D0%BA%D0%B5%D0%BA%D1%81%20%D0%BB%D0%B8%D0%BC%D0%BE%D0%BD%D0%BD%D1%8B%D0%B9.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D0%BE%D0%B2%D1%81%D1%8F%D0%BD%D0%BE%D0%B5%20%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D1%8C%D0%B5.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D1%82%D0%B0%D1%80%D1%82%D0%B0%D0%BB%D0%B5%D1%82%D0%BA%D0%B8%20%D0%B2%D0%B8%D1%88%D0%BD%D1%8F-%D1%88%D0%BE%D0%BA%D0%BE%D0%BB%D0%B0%D0%B4.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D1%82%D0%B0%D1%80%D1%82%D0%B0%D0%BB%D0%B5%D1%82%D0%BA%D0%B8%20%D1%84%D0%B8%D1%81%D1%82%D0%B0%D1%88%D0%BA%D0%B0-%D0%BC%D0%B0%D0%BB%D0%B8%D0%BD%D0%B0jpg.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D1%82%D0%B0%D1%80%D1%82%D0%B0%D0%BB%D0%B5%D1%82%D0%BA%D0%B0%20%D0%BB%D0%B8%D0%BC%D0%BE%D0%BD.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D1%87%D0%B8%D0%B0%20%D0%BF%D1%83%D0%B4%D0%B8%D0%BD%D0%B3.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D0%BC%D0%B5%D1%80%D0%B5%D0%BD%D0%B3%D0%BE%D0%B2%D1%8B%D0%B9%20%D1%80%D1%83%D0%BB%D0%B5%D1%82.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D0%B4%D0%B0%D0%BC%D1%81%D0%BA%D0%B8%D0%B5%20%D0%BF%D0%B0%D0%BB%D1%8C%D1%86%D1%8B.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D0%BF%D0%B8%D1%80%D0%BE%D0%B6%D0%B5%D0%BD%D0%BD%D0%BE%D0%B5%20%D0%BA%D0%B0%D1%80%D1%82%D0%BE%D1%88%D0%BA%D0%B0.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D0%B7%D0%B0%D0%B2%D0%B0%D1%80%D0%BD%D0%BE%D0%B5%20%D0%BA%D0%BE%D0%BB%D1%8C%D1%86%D0%BE.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D0%BF%D0%B0%D0%BD%D0%B0%D0%BA%D0%BE%D1%82%D0%B0%20%D1%81%20%D0%BC%D0%B0%D0%BB%D0%B8%D0%BD%D0%BE%D0%B9.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D0%BF%D0%B5%D0%BF%D0%BF%D0%B5%D1%80%D0%BE%D0%BD%D0%B8.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D1%82%D1%80%D0%B8%20%D1%81%D1%8B%D1%80%D0%B0.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D0%BA%D1%83%D1%80%D0%B8%D1%86%D0%B0%20%D0%B3%D1%80%D0%B8%D0%B1%D1%8B.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D0%BF%D0%B8%D1%86%D1%86%D0%B0%20%D0%BC%D0%B0%D1%80%D0%B3%D0%B0%D1%80%D0%B8%D1%82%D0%B0.webp&version_id=null",
		"http://localhost:9001/api/v1/buckets/biofood/objects/download?preview=true&prefix=%D0%BF%D0%B8%D1%86%D1%86%D0%B0%20%D0%B3%D0%B0%D0%B2%D0%B0%D0%B9%D1%81%D0%BA%D0%B0%D1%8F.webp&version_id=null",
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
