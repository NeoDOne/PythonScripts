#!/bin/bash
for protocol in 'http://' 'https://'; do
    while read line;
    do
        #echo $line
        code=$(curl -L --write-out "%{http_code}\n" --connect-timeout 10 --output /dev/null --silent --insecure $protocol$line)
    if [ $code = "000" ]; then
        echo "$protocol$line: not responding."
    elif [ $code = "301" ]; then
        echo "$protocol$line: moved permanently."
    elif [ $code = "302" ]; then
        echo "$protocol$line: has been redirected to another site."
    else
        echo "$protocol$line: HTTP $code ."
    fi
    done < test_domains.txt
done
