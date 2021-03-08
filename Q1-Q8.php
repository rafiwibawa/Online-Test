<?php

// Q1
echo "\n===Q1===\n";
$n=5;
for($i=1; $i<=$n; $i++){
	for($j=$n; $j>=$i; $j-=1){
		echo "* ";
	}
    echo "\n";
}

// Q2
echo "\n===Q2===\n";
$n=5;
for($i=$n;$i>0;$i--){
    for($j=$n;$j>=$i;$j--){
        echo "* ";
    }
    echo "\n";
}

// Q3
echo "\n===Q3===\n";
$n=6;
for($i=$n;$i>0;$i--){
    for($j=$n;$j>=$i;$j--){
        echo "* ";
    }
    echo "\n";
}
$n=5;
for($i=1; $i<=$n; $i++){
	for($j=$n; $j>=$i; $j-=1){
		echo "* ";
	}
    echo "\n";
}

// Q4
echo "\n===Q4===\n";
$nilai = readline('Masukan Nilai : ');
$faktorial = 1;
for ($i=1; $i <=$nilai ; $i++) { 
    $faktorial *=$i;
}
echo 'Bilangan Faktorial ',$nilai,'! adalah : ',$faktorial,"\n";
// Q5
echo "\n===Q5===\n";

$string = readline('Masukan String : ');
$new = str_replace(' ', '%20', $string);
echo $new;

// Q6
echo "\n===Q6===\n";
$n = readline('Input : ');

$angka_sebelumnya=0;
$angka_sekarang=1;
 
for ($i=0; $i<$n-1; $i++)
{
  $output = $angka_sekarang + $angka_sebelumnya;

  $angka_sebelumnya = $angka_sekarang;
  $angka_sekarang = $output;
}
echo "Output : ",$output;

// Q7
echo "\n===Q7===\n";
function uniq($str) 
{
    for($i = 0; $i < strlen($str); $i++)
    {
        for($j = $i + 1; $j < strlen($str); $j++) 
        {
            if($str[$i] == $str[$j])
            {
                return false;
            }
        }
    }
    return true;
}
$str = "rafi2019";  # true
# $str = "rafirafi" #false
if(uniq($str)){
    echo "Input : ", $str,"\nOutput : true";
}
else{
    echo "Input : ", $str, "\nOutput : false";
}

// Q8
echo "\n===Q8===\n";
$array = [2, 4, 5, 1, 8, 12, 7];
echo "Nilai Terbesar Adalah : ",max($array),"\n";
echo "Nilai Terkecil Adalah : ",min($array),"\n";

