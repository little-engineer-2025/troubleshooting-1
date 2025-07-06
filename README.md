# malware issue

- Detected a weird URL at: `https://www.vodafones.es/t-Dunsine-Deuill-our-hee-arts-The-hums-a-deight-`
  at the `https://www.vodafone.es/`

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

