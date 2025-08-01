#!/bin/bash

# db_list="Arade,Bimbo,CityMaxCapita,CMSprovider,CommonGovernment,Corporations,Eixo,Euro2016,Food,Generico,HashTags,Hatred,IGlocations1,IGlocations2,IUBLibrary,Medicare1,Medicare2,Medicare3,MedPayment1,MedPayment2,MLB,Motos,MulheresMil,NYC,PanCreactomy1,PanCreactomy2,Physicians,Provider,RealEstate1,RealEstate2,Redfin1,Redfin2,Redfin3,Redfin4,Rentabilidad,Romance,SalariesFrance,TableroSistemaPenal,Taxpayer,Telco,TrainsUK1,TrainsUK2,Uberlandia,USCensus,Wins,YaleLanguages"

db_list="Arade,Bimbo"
dst_dir="/home/saeed/Downloads/tmp/myTemp/"

./runAll.sh $db_list $dst_dir
