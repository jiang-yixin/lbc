// copy this script and use it in the console of web browser for every page
// to get a list of json format
posts=[] // only for 1st page
document.querySelectorAll('._3DFQ-').forEach(function(element) {
	let title = element.querySelector('._2tubl').getElementsByTagName('span')[0].innerHTML,
	url = 'https://www.leboncoin.fr' + element.getElementsByTagName('a')[0].getAttribute('href'),
	price = element.querySelector('._1NfL7').innerHTML.match(/>([0-9\s]+)</g)[0]
	price = price.substring(1, price.length - 1).replace(' ','')
	let cityInfos = element.querySelector('._2qeuk').innerHTML,
	cityInfosLength = cityInfos.length
	let zipCode = cityInfos.substring(cityInfosLength-6, cityInfosLength),
	city = cityInfos.substring(0, cityInfosLength - 6)
	post = {
		'title': title,
		'url': url,
		'price': price,
		'city': city,
		'zipCode': zipCode
	}

	posts.push(post)
})

JSON.stringify(posts)