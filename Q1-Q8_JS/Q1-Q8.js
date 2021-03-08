// Q1
function Q1(n) {
    let hasil = '';
    for (let i = 0; i < n; i++) {
        for (let j = n; j > i; j--) {
            hasil += '* ';
        }
        hasil += '\n';
    }
    return hasil;
}
console.log(Q1(5));
// Q2
function Q2(n) {
    let hasil = '';
    for (let i = 0; i < n; i++) {
        for (let j = 0; j <= i; j++) {
            hasil += '* ';
        }
        hasil += '\n';
    }
    return hasil;
}
console.log(Q2(5));
// Q3
function Q3(n) {
    let hasil = '';
    for (let i = 0; i < n+1; i++) {
        for (let j = 0; j <= i; j++) {
            hasil += '* ';
        }
        hasil += '\n';
    }

    for (let i = 0; i < n; i++) {
        for (let j = n; j > i; j--) {
            hasil += '* ';
        }
        hasil += '\n';
    }

    return hasil;
}
console.log(Q3(5));

// Q4

const nilai = parseInt(prompt('Masukan Nilai '));
let faktorial = 1;
for (let i = 1; i <=nilai; i++) {
    faktorial *= i;
}
console.log('Q4. Factorial 10! adalah : ',faktorial);

// Q5
const str = prompt('Masukan String ');
var replaced = str.replace(/ /g, '%20');
console.log('Q5.',replaced)

// Q6
const number = parseInt(prompt('Input : n = '));
let n1 = 0, n2 = 1, nextTerm;

for (let i = 1; i <= number; i++) {
    
    nextTerm = n1 + n2;
    n1 = n2;
    n2 = nextTerm;
}
console.log('Q6. Output :',n1);

// Q7
function is_unique(str) {
    var obj = {};
    for(var z=0;z<str.length;++z) {
      var ch = str[z];
      if(obj[ch]) return false; else obj[ch] = true;
    }
    return true;
  }
  
  console.log(is_unique("rafi2019")); // true
  console.log(is_unique("rafirafi")); // false

// Q8
let array = [2, 4, 5, 1, 8, 12, 7];
console.log('Q8')
console.log('Nilai Terbesar Adalah : ',Math.max.apply(Math, array));
console.log('Nilai Terkecil Adalah : ',Math.min.apply(Math, array));

