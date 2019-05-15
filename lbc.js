posts=[] // only for 1st page
document.querySelectorAll('._3DFQ-').forEach(function(element){
	let url = 'https://www.leboncoin.fr' + element.getElementsByTagName('a')[0].getAttribute('href'),
	price = element.querySelector('._1NfL7').innerHTML.match(/>([0-9\s]+)</g)[0]
	price = price.substring(1, price.length - 1).replace(' ','')
	let city = element.querySelector('._2qeuk').innerHTML
	//post = [url, price, city]

	post = {
		'url': url,
		'price': price,
		'city': city
	}

	posts.push(post)
})

JSON.stringify(posts)