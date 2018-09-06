mkdir Temperaturas
cd Temperaturas
wget https://climate.nasa.gov/system/internal_resources/details/original/647_Global_Temperature_Data_File.txt

cd ..
cp tempdata.txt Temperaturas
cd Temperaturas

awk '{ if(($2 < -30.0 && $2 != "") || ($3 < -30.0 && $3 != "") || ($4 < -30.0 && $4 != "") || ($5 < -30.0 && $5 != "") || ($6 < -30.0 && $6 != "") || ($7 < -30.0  && $7 != "") || ($8 < -30.0 && $8 != "") || ($9 < -30.0 && $9 != "") ||  ($10 < -30.0 && $10 != "") || ($11 < -30.0 && $11 != "") || ($12 < -30.0 && $12 != "") || ($13 < -30.0 && $13 != "" && $13 != "-15.7*" && $13 != "-16.8*")) print ($1) }' tempdata.txt > menoresque30.txt

awk '{ if(($2 < -6.0 && $2 != "") || ($3 < -6.0 && $3 != "") || ($4 < -6.0 && $4 != "") || ($5 < -6.0 && $5 != "") || ($6 < -6.0 && $6 != "") || ($7 < -6.0  && $7 != "") || ($8 < -6.0 && $8 != "") || ($9 < -6.0 && $9 != "") ||  ($10 < -6.0 && $10 != "") || ($11 < -6.0 && $11 != "") || ($12 < -6.0 && $12 != "") || ($13 < -6.0 && $13 != "" )) print ($1) }' tempdata.txt > menoresque6.txt

awk '{m=0 ; i=1 ; while (i<15){if($i != "")m++;i++;if($i == "")i++} {print ($1, S2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14, m)}}' tempdata.txt > listaDeApoyo.txt
awk '{if($NF == 14 || $NF == 13)print $7;if($NF == 10)print $4;if($NF == 9)print $3;if($NF == 11)print $5;if($NF == 7)print $2}'  listaDeApoyo.txt > junio.txt

rm -rf listaDeApoyo.txt

awk '{m=0;if($NF != "" && $NF > -15.0)m++;if($NF == "" && (($1+$2+$3+$4+$5+$6+$7+$8+$9+$10+$11+$12+$13+$14)/(0.1*($(NF +1))) > -15.0))m++;print($1, m)}'  tempdata.txt | awk '{SUM += $2; print(SUM-1) }' | awk 'BEGIN{a=0}{if ($1>0+a) a=$1} END{print a}' 

rm tempdata.txt
cd ..
mv MartinezDiego_temp.py Temperaturas
cd Temperaturas
python MartinezDiego_temp.py
