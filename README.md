# malware issue

- Detected a weird URL at: `https://www.vodafones.es/t-Dunsine-Deuill-our-hee-arts-The-hums-a-deight-`
  at the `https://www.vodafone.es/`

## 6-jun-2025

- It was detected on [traceroute](./data/traceroute-8-8-8-8.txt) something
  weird:
  - After the router (192.168.1.1) there are a hop to 192.168.144.1 which is a
    private network (some additional device installed?).
  - After that address there are two additional IPs:
    - 

- A quick nmap on the IP 192.168.144.1 show the content at [nmap](./data/nmap-192.168.144.1).

- 

## 6-jul-2025

- Retrieve html where the URL of the script is found by: `curl -L "https://www.vodafone.es" | head -n 10`

```raw
curl -L "https://www.vodafone.es" | head -n 10
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100  3056    0  3056    0     0   5950      0 --:--:-- --:--:-- --:--:--  5950
<!-- (es1231yr)-->
<!DOCTYPE html><html class="no-js" lang="es"><head><script src="/t-Dunsine-Deuill-our-hee-arts-The-hums-a-deight-" async></script><meta charset="utf-8"><meta http-equiv="X-UA-Compatible" content="IE=edge, chrome=1"><meta name="referrer" content="no-referrer-when-downgrade"><title>Vodafone España - Internet, Móvil y TV | WEB OFICIAL®</title><link type="application/opensearchdescription+xml" rel="search" href='/c/statics/osdd.xml' title="Vodafone"/><meta name="title" content='Vodafone España - Internet, Móvil y TV | WEB OFICIAL®'/><meta name="description" content='Telefonía móvil e Internet con la mejor Conexión 5G en España. Internet, Fibra óptica, Móvil y Televisión ¡Con ofertas a tu medida!'/><meta name="keywords" content=''/>
	<!-- SOCIAL META TAGS -->
	<meta property="og:url" content="https://www.vodafone.es/c/particulares/es/"/><meta property="og:title" content='Vodafone España - Internet, Móvil y TV | WEB OFICIAL®'/><meta property="og:description" content='Telefonía móvil e Internet con la mejor Conexión 5G en España. Internet, Fibra óptica, Móvil y Televisión ¡Con ofertas a tu medida!'/><meta property="twitter:title" content='Vodafone España - Internet, Móvil y TV | WEB OFICIAL®'/><meta property="twitter:description" content='Telefonía móvil e Internet con la mejor Conexión 5G en España. Internet, Fibra óptica, Móvil y Televisión ¡Con ofertas a tu medida!'/><meta property="og:image" content='https://www.vodafone.es/c/statics/imagen/ogg-vodafone.jpg'/><meta name="twitter:image" content='https://www.vodafone.es/c/statics/imagen/ogg-vodafone.jpg'/>
	<!-- ROBOTS META TAG -->
	<link rel="canonical" href='https://www.vodafone.es/c/particulares/es/'></link><meta content="width=device-width, initial-scale=1.0, minimum-scale=1.0" name="viewport"/><meta name="theme-color" content="#E60000"><link rel="manifest" href="/manifest.json"/><script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "WebSite",
100 16367    0 16367    0     0  29251      0 --:--:-- --:--:-- --:--:--  288k
curl: (23) Failure writing output to destination, passed 1436 returned 17
```

- Retrieve payload by: `./download.sh`

```raw
ll data/
total 1096
-rw-r--r--. 1 avisiedo avisiedo 275626 Jul  6 18:21 payload-curl.js
-rw-r--r--. 1 avisiedo avisiedo 275626 Jul  6 18:21 payload-firefox-linux.js
-rw-r--r--. 1 avisiedo avisiedo 275626 Jul  6 18:21 payload-firefox-macos.js
-rw-r--r--. 1 avisiedo avisiedo 275626 Jul  6 18:21 payload-firefox-win.js
-rw-r--r--. 1 avisiedo avisiedo   7820 Jul  6 18:17 ua-firefox.txt
```

- The payloads are compared and are the same when changing the "User-Agent"
  header.
- Analyzed the `payload-firefox-win.js` at VirusTotal at:
  [Virus Total Report](https://www.virustotal.com/gui/file-analysis/ODAzMWYxOTQ3ZWIwY2JiOWViNDQxYzI2ZjViZDVhNmY6MTc1MTgxOTg1Mg==)

  - [CAPE Sandbox report](https://www.virustotal.com/ui/file_behaviours/54653bfd567c9d6633296bc8c2e9f929c3e589e56811caf683642f73764c2e81_CAPE%20Sandbox/html)
  - [Zenbox report](https://www.virustotal.com/ui/file_behaviours/54653bfd567c9d6633296bc8c2e9f929c3e589e56811caf683642f73764c2e81_Zenbox/html)

## 7-jul-2025

- After indenting the content for `payload-curl.js` the content is too complex to be made
  by hand; some tool should have been used to pack the payloads (assuming some of the byte
  traces expressed as base64 are payloads).

## 13-jul-2025

- I do traceroute to 8.8.8.8 and I got:

```raw
$ traceroute -I -n 8.8.8.8
traceroute to 8.8.8.8 (8.8.8.8), 30 hops max, 60 byte packets
 1  192.168.50.1  0.580 ms * *                       >>>> My personal router
 2  192.168.1.1  1.365 ms * *                        >>>> The ISP router
 3  192.168.144.1  7.345 ms  7.343 ms  7.342 ms      >>>> ??? Another private IP???
 4  217.11.109.136  32.444 ms  32.445 ms  32.444 ms  >>>> Which address is this??
 5  217.11.109.106  32.910 ms  32.909 ms  32.908 ms  >>>> And this other one???
 6  80.58.106.109  32.438 ms  32.366 ms  31.564 ms
 7  * * *
 8  176.52.253.102  25.552 ms  25.546 ms *
 9  108.170.252.253  25.528 ms * *
10  * 142.250.46.165  16.882 ms *
11  * * *
12  * * *
13  8.8.8.8  15.963 ms  15.935 ms  15.452 ms
```

> BTW too many hops to reach out 8.8.8.8

- I retrieve the public IP and I got:

```raw
$ curl -s 'https://api.ipify.org?format=json' | jq -r '.ip'
79.145.194.226
```

- The weather service in the console indicate the public IP is from ?Barcelona?

- If I try traceroute the IP directly I got the below:

```raw
$ traceroute -I -n 79.145.194.226
traceroute to 79.145.194.226 (79.145.194.226), 30 hops max, 60 byte packets
 1  192.168.50.1  0.558 ms  0.530 ms  0.523 ms
 2  79.145.194.226  1.054 ms  1.333 ms  1.331 ms     >>>> The PUBLIC IP is inside my home network!??
```

- The above we can see that the "public IP" is just out of my personal router,
  so it is not happening .

## 14-jul-2025

A regression situation happened because the mitigation stopped working for some
period of time.

See: [2025-07-15-fix-unknown.txt](data/2025-07-15-fix-unknown.txt) for the list of
rpm packages installed from unknown source. From this list are removed the
firefox browser and the chromium browser which where uninstalled as soon as the
situation was discovered.

