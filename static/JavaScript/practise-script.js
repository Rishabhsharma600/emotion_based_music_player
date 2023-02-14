let i;

id1.addEventListener('click',function(e){
    alert("hello broooooo vash")
    i="first"
    alert("first function")
    const req=new XMLHttpRequest()
    req.open('POST',`/processUserInfo/${JSON.stringify(i)}`)
    req.send()

})