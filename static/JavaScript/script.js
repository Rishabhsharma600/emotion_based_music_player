
let songtp="";
function handleclick(type)
{
    // alert(type)
    console.log(type)
    songtp=type;
    console.log("sontp value "+songtp)

    const req=new XMLHttpRequest()
    req.open('POST',`/processUserInfo/${JSON.stringify(songtp)}`)
    req.send()

}


let langtp=""
function handleclick_2(type)
{
    // alert(type)
    console.log(type)
    langtp=type;
    console.log("sontp value "+langtp)

    const req=new XMLHttpRequest()
    req.open('POST',`/processUserInfo_2/${JSON.stringify(langtp)}`)
    req.send()

}

let langtp_3=""
function handleclick_3(type)
{
    // alert(type)
    console.log(type)
    langtp_3=type;
    console.log("sontp value "+langtp_3)

    const req=new XMLHttpRequest()
    req.open('POST',`/process_3/${JSON.stringify(langtp_3)}`)
    req.send()

}

let langtp_4=""
function handleclick_4(type)
{
    // alert(type)
    console.log(type)
    langtp_4=type;
    console.log("sontp value "+langtp_4)

    const req=new XMLHttpRequest()
    req.open('POST',`/process_4/${JSON.stringify(langtp_4)}`)
    req.send()

}

let langtp_5=""
function handleclick_5(type)
{
    // alert(type)
    console.log(type)
    langtp_5=type;
    console.log("sontp value "+langtp_5)

    const req=new XMLHttpRequest()
    req.open('POST',`/process_5/${JSON.stringify(langtp_5)}`)
    req.send()

}















// id2.addEventListener('click',function(e){
//     alert("hello broooooo vash")
//     i="first"
//     alert("first function")
//     const req=new XMLHttpRequest()
//     req.open('POST',`/processUserInfo/${JSON.stringify(i)}`)
//     req.send()

// })
// id3.addEventListener('click',function(e){
//     alert("hello broooooo vash")
//     i="first"
//     alert("first function")
//     const req=new XMLHttpRequest()
//     req.open('POST',`/processUserInfo/${JSON.stringify(i)}`)
//     req.send()

// })
// id4.addEventListener('click',function(e){
//     alert("hello broooooo vash")
//     i="first"
//     alert("first function")
//     const req=new XMLHttpRequest()
//     req.open('POST',`/processUserInfo/${JSON.stringify(i)}`)
//     req.send()

// })
// const ele=id1;
// ele.addEventListener('click',function(e){
//     console.log("hello broooooo vash")
// })