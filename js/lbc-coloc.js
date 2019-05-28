cities=[] // only for 1st page
document.querySelectorAll('._2qeuk').forEach(function(element) {
    city = {
        'name': element.innerHTML
    }
    cities.push(city)
})

JSON.stringify(cities)