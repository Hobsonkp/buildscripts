#!/bin/bash

option=$1

case $option in
-g)
# read api key from file
apikey=$(cat ~/bin/ipgeoapi.txt) 
# get ip address from command line
ip=$2                            

curl 'https://api.ipgeolocation.io/ipgeo?apiKey='"$apikey"'&ip='"$ip"
;;
-r)
# get report file command line
repFile=$2
#get the list of ip addresses from the failed login report
cut -d ',' -f3 ~/bin/$repFile | uniq | tail -n+2
;;
*)
exit 1
;;
esac