function Q12(n) {
    let hasil = '';
    for (let i=1;i<=n;i++){
        for (let j=i;j<=n;j++){
            hasil+=' ';
        }
        for (let k=1;k<=i;k++){
            hasil+='*';
        }
        for (let l=1;l<=i-1;l++){
            hasil+='*';;
        }
        hasil+='\n';
    }
    return hasil;
}
console.log(Q12(5));