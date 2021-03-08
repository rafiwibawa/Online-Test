<?php
$n=5;
for( $a=$n;$a>0;$a--){
    for($i=1; $i<=$a; $i++){
        echo " ";
    }
    for($j=$n;$j>=$a;$j--){
        echo"* ";
    }
    echo"\n";
}