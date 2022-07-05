setTimeout(function(){
    alert("hello")
},2000)

let id



setTimeout(function(){
    let div1 = document.createElement("p")
    div1.innerText = "Hello World"
    document.querySelector("div").appendChild(div1)
},2000)
let counter =0
id = setInterval(function(){
        let div2 = document.createElement("p")
    div2.innerText = "Hello World"
    document.querySelector("div").appendChild(div2)
    counter++
    if (counter>=5){
    _clear()
    }
    },2000)

function _clear(){
         clearInterval(id)
    }

let p =document.querySelectorAll("div")[0];
console.log(p)
function _clear(){
    clearInterval(id)
}

function  myMove(){
  let box = document.getElementById('animate');
  let pos = 0;
  let id = setInterval(function(){
    if(pos == 350){
      clearInterval(id)
    }
    else{
      pos++
      box.style.left = pos + "px";
    }

  },1)
}

let elem = document.getElementById("box")

elem.addEventListener("dragend",function(event){

let x = event.clientX
let y = event.clientY 
elem.style.left = x + "px"
elem.style.top= y + "px"

})

function lettersOnly(input){
    var regex=/[^a-z]/gi;
    input.value = input.value.replace(regex,"")
}

// let a = document.getElementsByTagName('h1')[0]
// console.log(a)
// let b = document.querySelector('article')
// console.log(b)
// let c = document.querySelectorAll('p')[3]
// b.removeChild(c)

// let red = document.querySelector('h2');
// red.addEventListener('click', function() {
//  red.style.backgroundColor = 'red'
// })

// let hide = document.querySelector('h3');
// hide.addEventListener('click', function(){
//  hide.style.display = 'none'
// })

// let x = document.querySelector('button')
// x.addEventListener('click', function() {
//  document.body.style.fontWeight = 'bold'
// })

// let bonus = document.querySelector('h1')
// bonus.addEventListener('mouseover', function(event) {
//  event.target.style.fontSize =  Math.random()*100 +'px'
// })

// let bonus1 = document.querySelectorAll('p')[1]
// bonus1.addEventListener('mouseover', function(event) {
//  event.target.style.animation =  'fadeIn 5s'
// })

// let allBoldItems = []
// function getBold_Items() {
//  let a = document.getElementsByTagName('strong') 
//  console.log(a)
//  for (i=0; i < a.length; i++) {
//      allBoldItems.push(a[i])
//      console.log(allBoldItems)
//  }
    
// }
// getBold_Items()

// function highlight() {

//  for (i=0; i < allBoldItems.length; i++)
//      allBoldItems[i].style.color = 'blue'
// }
// highlight()

// function return_normal() {
//  for (i=0; i < allBoldItems.length; i++) {
//      allBoldItems[i].style.color = 'black'
//  }

// }
// return_normal()

// let change = document.querySelector('p');
// console.log (change)
// change.addEventListener('mouseover', highlight)

// change.addEventListener('mouseout', return_normal)

// let anim = document.querySelector('h1');
// console.log(anim)
// anim.addEventListener('click', function (event) {
//  anim.style.color = 'blue'})
// anim.addEventListener('dblclick', function(event) {
//  document.body.style.backgroundColor = 'purple'})
// anim.addEventListener('mouseover', function(event) {
//  anim.style.fontSize =  Math.random()*100 +'px'})
// anim.addEventListener('mouseout', function(event) {
//  anim.style.opacity = '0.5'})

