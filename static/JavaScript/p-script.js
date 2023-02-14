
let i

id1.addEventListener('click', function(e){
   i=first
   alert("first function")
   const req=new XMLHttpRequest()
   request.open('POST',`/ProcessUserinfo/${JSON.stringify(i)}`)
   request.send()
})

id2.addEventListener('click',function(e){
   alert("second function")
   i=2
   console.log("present "+i)
})