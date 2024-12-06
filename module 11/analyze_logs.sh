#!/bin/bash

#Добавляем заголовок отчета
echo "Отчет о логе веб-сервера" >> report.txt

#Добавляем разделитель заголовка
echo "=========================" >> report.txt

#Cчитаем общее количество строк в файле
cnt_lines=$(wc -l < access.log)
echo "Общее количество запросов: $cnt_lines " >> report.txt

#Считаем уникальное количество IP адресов
cnt_uniq_ip=$(awk '{ips[$1]++} END {print length(ips)}' access.log)
echo "Количество уникальных IP адресов: $cnt_uniq_ip">> report.txt

#Считаем количество запросов по методам
grp_query=$(awk '{method = $6; gsub(/"/, "", method); if (method != "") methods[method]++} END {for (method in methods) print method, methods[method]}' access.log)
echo "Количество запросов по методам: " >> report.txt
echo $grp_query >> report.txt 

#Самый популярный URL
top_url=$(awk '{urls[$7]++} END {max=0; for (url in urls) {if (urls[url] > max) {max = urls[url]; popular = url}} print popular}' access.log)
count_url=$(awk '{urls[$7]++} END {max=0; for (url in urls) {if (urls[url] > max) {max = urls[url]}} print max}' access.log)
echo "Самый популярный URL: $count_url $top_url" >> report.txt
