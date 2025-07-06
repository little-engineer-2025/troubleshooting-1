#!/bin/bash

# I try to retrieve the sample using different User-Agents to verify if it changes depending on it

# curl
curl --noproxy "www.vodafone.es" -o data/payload-curl.js -L "https://www.vodafone.es/t-Dunsine-Deuill-our-hee-arts-The-hums-a-deight-"

# firefox-win
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0"
curl --noproxy "www.vodafone.es" -o data/payload-firefox-win.js -L "https://www.vodafone.es/t-Dunsine-Deuill-our-hee-arts-The-hums-a-deight-" -H "User-Agent: ${UA}"

# firefox-linux-fedora
UA="Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0"
curl --noproxy "www.vodafone.es" -o data/payload-firefox-linux.js -L "https://www.vodafone.es/t-Dunsine-Deuill-our-hee-arts-The-hums-a-deight-" -H "User-Agent: ${UA}"

# firefox-macos
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 15.5; rv:140.0) Gecko/20100101 Firefox/140.0"
curl --noproxy "www.vodafones.es" -o data/payload-firefox-macos.js -L "https://www.vodafone.es/t-Dunsine-Deuill-our-hee-arts-The-hums-a-deight-" -H "User-Agent: ${UA}"

