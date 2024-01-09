brand = document.getElementById('brand')
model = document.getElementById('model')
storage = document.getElementById('storage')
ram = document.getElementById('ram')
frontCamera = document.getElementById('frontCamera')
backCamera = document.getElementById('backCamera')
color = document.getElementById('color')
price = document.getElementById('price')
os = document.getElementById('os')
isActive = document.getElementById('isActive')
image = document.getElementById('image')
submitButton = document.getElementById('submitButton')



submitButton.onclick = function () {

    let data =[ {
        "brand": brand.value,
        "model": model.value,
        "storage": storage.value,
        "ram": ram.value,
        "frontCamera": frontCamera.value,
        "backCamera": backCamera.value,
        "color": color.value,
        "price": price.value,
        "os": os.value,
        "isActive": isActive.value,
        "Email": email.value,
        "image": image.value
    } ]

    


    let jsonData = JSON.stringify(data)



    fetch("http://localhost:8000/addPhone/", {
    
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: jsonData
    
    
    }).then((res) => res.text())
        .then((data) => console.log(data))


}










