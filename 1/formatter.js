let arguments = process.argv.slice(2)

if(arguments.lenght < 2){
    console.log(```let's try this.
    node formatter.js [number] [format]
    [number] is number string which you want to format.
    [format] is patter style.```)
}else{
    let inputNumber = arguments[0]
    let format = arguments[1]
    let output = ''
    count = 0
    for(let i=0;i<format.length;i++){
        if(format[i] === '-'){
            output = output+'-'
        }else{
            output = output+inputNumber[count]
            count = count+1
        }
    }
    console.log(output)
}