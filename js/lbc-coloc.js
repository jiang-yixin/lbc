cities=[] // only for 1st page
document.querySelectorAll('._2qeuk').forEach(function(element) {
    cities.push(element.innerHTML)
})

JSON.stringify(cities)