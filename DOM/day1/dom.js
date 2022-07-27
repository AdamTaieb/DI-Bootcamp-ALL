let a = document.getElementsByTagName('div')
console.log(a)

let b = document.getElementsByClassName ('list')
b[0].lastElementChild.textContent="Richard"

let c= document.getElementsByClassName ('list')
c[0].firstElementChild.textContent="Adam"

let d= document.getElementsByClassName ('list')
d[1].firstElementChild.textContent="Adam"

let e = document.getElementsByClassName ('list')

let f = e[1].children[1]
e[1].removeChild(f)