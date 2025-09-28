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

## 15-jul-2025

- Today I get the below for traceroute to the public IP:

```raw
traceroute -I -n $(public-ip)
traceroute to 176.85.0.4 (176.85.0.4), 30 hops max, 60 byte packets
 1  192.168.50.1  0.819 ms  0.766 ms  0.757 ms
 2  176.85.0.4  1.673 ms  1.663 ms  2.152 ms
 ```

## 25-jul-2025

Check the www.vodafone.es and compare with www.movistar.es

```raw
openssl s_client -connect www.vodafone.es:443
Connecting to 45.60.74.53
CONNECTED(00000003)
depth=2 OU=GlobalSign Root CA - R3, O=GlobalSign, CN=GlobalSign
verify return:1
depth=1 C=BE, O=GlobalSign nv-sa, CN=GlobalSign Atlas R3 DV TLS CA 2025 Q2
verify return:1
depth=0 CN=imperva.com
verify return:1
---
Certificate chain
 0 s:CN=imperva.com
   i:C=BE, O=GlobalSign nv-sa, CN=GlobalSign Atlas R3 DV TLS CA 2025 Q2
   a:PKEY: RSA, 2048 (bit); sigalg: sha256WithRSAEncryption
   v:NotBefore: Jun 13 12:11:40 2025 GMT; NotAfter: Dec 10 12:11:40 2025 GMT
 1 s:C=BE, O=GlobalSign nv-sa, CN=GlobalSign Atlas R3 DV TLS CA 2025 Q2
   i:OU=GlobalSign Root CA - R3, O=GlobalSign, CN=GlobalSign
   a:PKEY: RSA, 2048 (bit); sigalg: sha256WithRSAEncryption
   v:NotBefore: Jan 22 04:06:27 2025 GMT; NotAfter: Jan 22 00:00:00 2027 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIINRjCCDC6gAwIBAgIQAa6yDQolqKTtiaVoxTDITDANBgkqhkiG9w0BAQsFADBY
MQswCQYDVQQGEwJCRTEZMBcGA1UEChMQR2xvYmFsU2lnbiBudi1zYTEuMCwGA1UE
AxMlR2xvYmFsU2lnbiBBdGxhcyBSMyBEViBUTFMgQ0EgMjAyNSBRMjAeFw0yNTA2
MTMxMjExNDBaFw0yNTEyMTAxMjExNDBaMBYxFDASBgNVBAMMC2ltcGVydmEuY29t
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArtcFV2SChR9HzDLV9AVO
Gj6F6hvJvPysyqJL7cSYx94w8uRI8gz9zLh69S/1PvhC6TCAnKb2Zgnp7NJXXNHi
qDffy4lrdy7aFekNuc2nBR4o7bCQLqnxMYjIzQ+/TDdnToHEfaMBO4e5HR70QpWz
5qW2lHSADjjEb1gHC/NSpBvmcWsb48qmOiju9fI+53bWpBnyRENFiV15s/oDgQRu
RwPXiAw4YImsO+ijpW4S5pBVxJrFLFjlKpcxar7dWUKWwL9vDm+hI6EkoC6Zxtn/
47zXYdE8XJS1VnF/QSrFznKFPrsoj8lbyWojqMuOIzcPskkaNun9pODANKJSRFOz
AQIDAQABo4IKTDCCCkgwggb/BgNVHREEggb2MIIG8oIUc2VydmljZXMudm9kYWZv
bmUuZXOCC2ItcGxhbmV0LmVzgg1tLnZvZGFmb25lLmVzghh3d3cuZnVuZGFjaW9u
dm9kYWZvbmUuZXOCEG15YnVpbGRpbmd2Zi5jb22CGWV1cm9wZWFuaWIuc3Audm9k
YWZvbmUuZXOCEGF4aXMudm9kYWZvbmUuZXOCEHdpZmkudm9kYWZvbmUuZXOCHHRl
c3QtdnR2LmRldi50NGMudm9kYWZvbmUuZGWCFnJlY29naWRhZXF1aXBvLmxvd2ku
ZXOCFHZmLXByZXAxLnZvZGFmb25lLmVzgiR2b2RhZm9uZWZpY2hhamV0ZXN0LmNo
ZWNraW5ncGxhbi5jb22CHnNyc29uZW5ldGdyYWJhY2lvbi52b2RhZm9uZS5lc4IY
d3d3LmVtcHJlc2FzLnZvZGFmb25lLmVzgg93d3cudm9kYWZvbmUuZXOCDSouZmlu
Z2VydGkucHOCFGZ1bmRhY2lvbnZvZGFmb25lLmVzghBzZXJ2aWNpb3Mub25vLmVz
giNvbmVuZXRncmFiYWNpb25sbGFtYWRhcy52b2RhZm9uZS5lc4Igc29sdWNpb24t
cHJvZmVzaW9uYWwudm9kYWZvbmUuZXOCFnZlZ2EtdmYuc2F0ZWNncm91cC5jb22C
GWFyZWFyZXNlbGxlcnN2b2RhZm9uZS5jb22CG3JhaWZmZWlzZW4tdnBieC52b2Rh
Zm9uZS5yb4IXdmYtc2l0MS1henUudm9kYWZvbmUuZXOCHHd3dy5zYWxhZGVwcmVu
c2Eudm9kYWZvbmUuZXOCEGF5dWRhdm9kYWZvbmUuZXOCEnZvZGFmb25lZW1wcmVz
YS5lc4IVc2VydmljaW9zLnZvZGFmb25lLmVzghxkaXN0cmlidWNpb24tbmFzLnZv
ZGFmb25lLmVzghx2Zm5vdGlmaWNhY2lvbmVzLnZvZGFmb25lLmVzghZ3cy1wcmVw
YWdvLnZvZGFmb25lLmVzghF0b29scy52b2RhZm9uZS5lc4IRKi5kZS52b2RhZm9u
ZS5jb22CFnNlcnZpY2lvczIudm9kYWZvbmUuZXOCE3ZmLXNpdDIudm9kYWZvbmUu
ZXOCDSoudm9kYWZvbmUuZXOCDnl1LnZvZGFmb25lLmVzghlzZXJ2aWNlc3RhdHVz
LnZvZGFmb25lLmVzghBkYXRhLnZvZGFmb25lLmVzghh3d3cubWVkaWFsYWIudm9k
YWZvbmUuZXOCE3hjYXAtcHMudm9kYWZvbmUuZXOCEWZvYm9zLnZvZGFmb25lLmVz
ghdzY2hhbWFuLXByZS52b2RhZm9uZS5lc4IRZmF4b3Yudm9kYWZvbmUuZXOCF3Zm
LXNpdDItYXp1LnZvZGFmb25lLmVzghVhbmFseXRpY3Mudm9kYWZvbmUuZXOCD3d3
dy5iLXBsYW5ldC5lc4IWd3d3Lm9uZW5ldC52b2RhZm9uZS5ncoITdmYtc2l0My52
b2RhZm9uZS5lc4Idd3d3LmFyZWFyZXNlbGxlcnN2b2RhZm9uZS5jb22CGHZmLXBy
ZXAxLWF6dS52b2RhZm9uZS5lc4IZd3d3LmFjdHVhbGl6YXZvZGFmb25lLmNvbYIW
ZGlzZnJ1dGF0dXNvcnByZXNhLmNvbYIZdG9ub3Nlc3BlcmFmZS52b2RhZm9uZS5l
c4ISdGllbmRhLnZvZGFmb25lLmVzghhzZXJ2aWNlc3Rlc3Qudm9kYWZvbmUuZXOC
C3ZvZGFmb25lLmVzgiJzcnNvbmVuZXRncmFiYWNpb250ZXN0LnZvZGFmb25lLmVz
ggtpbXBlcnZhLmNvbYIeKi5lbnRpdHktYXVkaXQuZGUudm9kYWZvbmUuY29tghN3
ZWJpaWdnLnZvZGFmb25lLmVzggtmaW5nZXJ0aS5wc4ISdmlzaW9uLnZvZGFmb25l
LmVzgg93d3cuZmluZ2VydGkucHOCFHd3dy5heXVkYXZvZGFmb25lLmVzgg0qLnZv
ZGFmb25lLmRlghp3d3cuZGlzZnJ1dGF0dXNvcnByZXNhLmNvbYIqdm9kYWZvbmUt
Y2hlY2tvdXQtc3RhZ2UudGVyYW9uZS1wcmV2aWV3LmRlghR3d3cubXlidWlsZGlu
Z3ZmLmNvbYIWc21hcnR2b2ljZS52b2RhZm9uZS5pZYITc2NoYW1hbi52b2RhZm9u
ZS5lc4IVYWN0dWFsaXphdm9kYWZvbmUuY29tghl2b2RhZm9uZXNtYXJ0YnVpbGRp
bmcuY29tgh13d3cudm9kYWZvbmVzbWFydGJ1aWxkaW5nLmNvbYISd3MtdHBoLnZv
ZGFmb25lLmVzghZ3d3cudm9kYWZvbmVlbXByZXNhLmVzMA4GA1UdDwEB/wQEAwIF
oDAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHQYDVR0OBBYEFFwhqi5n
kNzqVHIm0vODDpJRUoRoMFcGA1UdIARQME4wCAYGZ4EMAQIBMEIGCisGAQQBoDIK
AQMwNDAyBggrBgEFBQcCARYmaHR0cHM6Ly93d3cuZ2xvYmFsc2lnbi5jb20vcmVw
b3NpdG9yeS8wDAYDVR0TAQH/BAIwADCBngYIKwYBBQUHAQEEgZEwgY4wQAYIKwYB
BQUHMAGGNGh0dHA6Ly9vY3NwLmdsb2JhbHNpZ24uY29tL2NhL2dzYXRsYXNyM2R2
dGxzY2EyMDI1cTIwSgYIKwYBBQUHMAKGPmh0dHA6Ly9zZWN1cmUuZ2xvYmFsc2ln
bi5jb20vY2FjZXJ0L2dzYXRsYXNyM2R2dGxzY2EyMDI1cTIuY3J0MB8GA1UdIwQY
MBaAFJz7VREQQKI/RXndXC6CY5NAFkfKMEgGA1UdHwRBMD8wPaA7oDmGN2h0dHA6
Ly9jcmwuZ2xvYmFsc2lnbi5jb20vY2EvZ3NhdGxhc3IzZHZ0bHNjYTIwMjVxMi5j
cmwwggGABgorBgEEAdZ5AgQCBIIBcASCAWwBagB2ABLxTjS9U3JMhAYZw48/ehP4
57Vih4icbTAFhOvlhiY6AAABl2k0AfEAAAQDAEcwRQIhAOPcQyzsQaLrkqj5Li6E
jI82EQfRitiIDpacjbvB3pjqAiAq37V6ojaJNK6DEFBqHFmvmvf0P2kbkX9B+SGg
abYPXQB3AH1ZHhLheCp7HGFnfF79+NCHXBSgTpWeuQMv2Q6MLnm4AAABl2k0AqUA
AAQDAEgwRgIhAPiHIFK/0VaS0oWsQZ0LLkMuuOB1kNEw8rtHjOGNdrEFAiEA018K
7PnES+aHd+4aSHiY7rj7cGkt7/Aa/8jjFJ3QRnMAdwAN4fIwK9MNwUBiEgnqVS78
R3R8sdfpMO8OQh60fk6qNAAAAZdpNAO0AAAEAwBIMEYCIQD/h/TIs2KsSsbyzPzQ
iHaqrcdWM9Cxkl1LrEosOMQpUgIhAIRhKb6maFkODLTD+V/ju/oCpG47XCt60QAv
sGXV1h7lMA0GCSqGSIb3DQEBCwUAA4IBAQAceNHWLz7k4Y0CfFbJZvxWZ3EYY5PR
qS3KAK/HEJX8BF6S9tBMYL1FLRlho7QXnSPf+Ky3qBD9Z6wqhFHF09NLHOFG56ZO
A2pI/ZRyF9j8upI9HX5XgXsO02+X/2XxwMjDJI3fSSH6T2UIRJnV69UYhJPcQm4G
wI3DnBwubreJH6hwAPe1gGVhUaXKBUXOT4a7n/+OiBx/F7e9BOQUSFKEt7vz+Hue
CsClIICcuLrc5tc7G/qXp3b4W1/QXVFeFRKAOMgQm9FGVVOy+MnhtXsf8O7SxPMM
bnaWvzFsY14FN+bewXAVUWkisma2pMTvADZ686/pfDx+D8lk5vVZWX3h
-----END CERTIFICATE-----
subject=CN=imperva.com
issuer=C=BE, O=GlobalSign nv-sa, CN=GlobalSign Atlas R3 DV TLS CA 2025 Q2
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: rsa_pss_rsae_sha256
Peer Temp Key: X25519, 253 bits
---
SSL handshake has read 5123 bytes and written 1612 bytes
Verification: OK
---
New, TLSv1.3, Cipher is TLS_AES_128_GCM_SHA256
Protocol: TLSv1.3
Server public key is 2048 bit
This TLS version forbids renegotiation.
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 0 (ok)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_128_GCM_SHA256
    Session-ID: 78AAB57965BDB1DCA5C1FB69482237A38D4DB212959A758375010A670A607077
    Session-ID-ctx: 
    Resumption PSK: 156D8FB809006C35BAAD837EEECAA3341624426BAC2BA7DD3D0DA50EB5DB2004
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - fa d5 79 09 a3 29 59 e1-e3 68 7c 07 ad 64 f8 77   ..y..)Y..h|..d.w
    0010 - 19 b9 a4 7d 3e 49 59 37-bb c3 cb f5 d1 e5 f2 27   ...}>IY7.......'
    0020 - 0a 53 61 3b 8d 4b 0b cb-e7 1f d2 7c b4 d3 d3 35   .Sa;.K.....|...5
    0030 - dc 90 10 34 8c ed 53 e7-59 13 11 7f 4d 4b 10 e3   ...4..S.Y...MK..
    0040 - 48 51 22 df 46 c0 c9 a9-3c dc cb e0 61 5e 65 e0   HQ".F...<...a^e.
    0050 - a6 c0 8a 18 b2 1a 47 09-e5 56 8b 98 dd ac 0d e1   ......G..V......
    0060 - a0 fe 7e 9c 8d 9e b6 0c-35 f6 bd 43 37 31 a9 05   ..~.....5..C71..
    0070 - 6d b5 04 43 db 6e 10 ff-a5 13 d3 b8 1c c9 ee 98   m..C.n..........
    0080 - ff ab 16 73 e2 2e 04 2b-33 3a d4 fd 3b 09 15 fd   ...s...+3:..;...
    0090 - 19 38 c2 82 9b af 70 70-93 5a 52 bb 55 28 3a 2b   .8....pp.ZR.U(:+
    00a0 - 9d c2 99 0c aa e2 41 ea-7d 0f bf 6f ae 3b da 54   ......A.}..o.;.T
    00b0 - 9b 78 a9 36 64 27 ca ad-01 a3 e5 dd 2f 72 15 d8   .x.6d'....../r..
    00c0 - eb 03 ca 5d cd 8f f0 61-0d 0f 7e 38 0d 7b b8 35   ...]...a..~8.{.5

    Start Time: 1753432758
    Timeout   : 7200 (sec)
    Verify return code: 0 (ok)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_128_GCM_SHA256
    Session-ID: AA470B587005E37AA5A57EA15E316EDC371DFCA6150CC56207F81C7401A59FA4
    Session-ID-ctx: 
    Resumption PSK: 11FA584F643A9F9B27B841AA0910B166853664A59AA217F54BD043AD5BA15A44
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - fa d5 79 09 a3 29 59 e1-e3 68 7c 07 ad 64 f8 77   ..y..)Y..h|..d.w
    0010 - 85 74 1a db e0 4e da f2-39 81 95 88 18 33 b6 ff   .t...N..9....3..
    0020 - c7 16 38 7a d6 c1 c1 13-68 3b f0 73 24 6f e0 69   ..8z....h;.s$o.i
    0030 - 22 74 1d d0 42 bf ad b9-a2 57 36 76 6d 11 ca 5a   "t..B....W6vm..Z
    0040 - 31 d4 37 3d de be b1 5e-28 d5 e4 3b c0 0b cb 1b   1.7=...^(..;....
    0050 - 2b 65 77 88 ec 83 8f e9-05 33 74 27 65 9b 0d 75   +ew......3t'e..u
    0060 - fb b4 b7 b3 23 b6 9f 9f-2b 4b 42 cd 6c 14 ac 99   ....#...+KB.l...
    0070 - 0e d3 c8 cb 21 dc 10 b4-4d a1 f3 1c c8 ba 68 16   ....!...M.....h.
    0080 - 1e 45 7e 2d df 53 ac ca-36 b9 46 ed 7a 37 7b 17   .E~-.S..6.F.z7{.
    0090 - 44 7f ef 29 db 0e 0b c4-7e d6 16 2b 4c 59 4d 4b   D..)....~..+LYMK
    00a0 - 03 60 56 2f 51 59 21 f8-75 1b eb 76 3e fe d9 0c   .`V/QY!.u..v>...
    00b0 - 82 95 6a 1f 0c cb c8 41-57 c9 8c b1 d5 88 c5 21   ..j....AW......!
    00c0 - 23 6b e2 af de d4 1c e5-f0 64 62 bb cb fe a6 15   #k.......db.....

    Start Time: 1753432758
    Timeout   : 7200 (sec)
    Verify return code: 0 (ok)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
closed
```

```raw
openssl s_client -connect www.movistar.es:443
Connecting to 81.47.192.13
CONNECTED(00000003)
depth=2 C=US, O=DigiCert Inc, OU=www.digicert.com, CN=DigiCert Global Root G2
verify return:1
depth=1 C=US, O=DigiCert Inc, OU=www.digicert.com, CN=GeoTrust TLS RSA CA G1
verify return:1
depth=0 C=ES, L=Madrid, O=TELEFONICA DE ESPAÑA SA, CN=www.movistar.es
verify return:1
---
Certificate chain
 0 s:C=ES, L=Madrid, O=TELEFONICA DE ESPAÑA SA, CN=www.movistar.es
   i:C=US, O=DigiCert Inc, OU=www.digicert.com, CN=GeoTrust TLS RSA CA G1
   a:PKEY: RSA, 2048 (bit); sigalg: sha256WithRSAEncryption
   v:NotBefore: Apr 21 00:00:00 2025 GMT; NotAfter: May 21 23:59:59 2026 GMT
 1 s:C=US, O=DigiCert Inc, OU=www.digicert.com, CN=GeoTrust TLS RSA CA G1
   i:C=US, O=DigiCert Inc, OU=www.digicert.com, CN=DigiCert Global Root G2
   a:PKEY: RSA, 2048 (bit); sigalg: sha256WithRSAEncryption
   v:NotBefore: Nov  2 12:23:37 2017 GMT; NotAfter: Nov  2 12:23:37 2027 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
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
7YpunTx4Du4256K4m19tZD7Q
-----END CERTIFICATE-----
subject=C=ES, L=Madrid, O=TELEFONICA DE ESPAÑA SA, CN=www.movistar.es
issuer=C=US, O=DigiCert Inc, OU=www.digicert.com, CN=GeoTrust TLS RSA CA G1
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: rsa_pkcs1_sha256
Peer Temp Key: ECDH, prime256v1, 256 bits
---
SSL handshake has read 3333 bytes and written 1674 bytes
Verification: OK
---
New, TLSv1.2, Cipher is ECDHE-RSA-AES256-GCM-SHA384
Protocol: TLSv1.2
Server public key is 2048 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-RSA-AES256-GCM-SHA384
    Session-ID: 709313FD9AEC3F4EC4BE0D0923282B7CF3B3F4B908874980E78D09E5C83CF3E8
    Session-ID-ctx: 
    Master-Key: EBA1B55DEE0229B58EECFF3F6D37FF57751DFF2D1868277D138F92283DDCD3C72B551968C6729BDE81544291ACCE88CC
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    Start Time: 1753433095
    Timeout   : 7200 (sec)
    Verify return code: 0 (ok)
    Extended master secret: no
---
```

The CN for www.vodafone.es it was expected to be `www.vodafone.es` instead of
`imperva.com`

I run whois imperva.com

```raw
whois imperva.com
   Domain Name: IMPERVA.COM
   Registry Domain ID: 108851426_DOMAIN_COM-VRSN
   Registrar WHOIS Server: whois.markmonitor.com
   Registrar URL: http://www.markmonitor.com
   Updated Date: 2024-11-23T10:47:28Z
   Creation Date: 2003-12-25T11:55:03Z
   Registry Expiry Date: 2026-12-25T11:55:03Z
   Registrar: MarkMonitor Inc.
   Registrar IANA ID: 292
   Registrar Abuse Contact Email: abusecomplaints@markmonitor.com
   Registrar Abuse Contact Phone: +1.2086851750
   Domain Status: clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited
   Domain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited
   Domain Status: clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited
   Domain Status: serverDeleteProhibited https://icann.org/epp#serverDeleteProhibited
   Domain Status: serverTransferProhibited https://icann.org/epp#serverTransferProhibited
   Domain Status: serverUpdateProhibited https://icann.org/epp#serverUpdateProhibited
   Name Server: NS-122.AWSDNS-15.COM
   Name Server: NS-1341.AWSDNS-39.ORG
   Name Server: NS-1956.AWSDNS-52.CO.UK
   Name Server: NS-687.AWSDNS-21.NET
   DNSSEC: unsigned
   URL of the ICANN Whois Inaccuracy Complaint Form: https://www.icann.org/wicf/
>>> Last update of whois database: 2025-07-25T08:49:24Z <<<

For more information on Whois status codes, please visit https://icann.org/epp

NOTICE: The expiration date displayed in this record is the date the
registrar's sponsorship of the domain name registration in the registry is
currently set to expire. This date does not necessarily reflect the expiration
date of the domain name registrant's agreement with the sponsoring
registrar.  Users may consult the sponsoring registrar's Whois database to
view the registrar's reported date of expiration for this registration.

TERMS OF USE: You are not authorized to access or query our Whois
database through the use of electronic processes that are high-volume and
automated except as reasonably necessary to register domain names or
modify existing registrations; the Data in VeriSign Global Registry
Services' ("VeriSign") Whois database is provided by VeriSign for
information purposes only, and to assist persons in obtaining information
about or related to a domain name registration record. VeriSign does not
guarantee its accuracy. By submitting a Whois query, you agree to abide
by the following terms of use: You agree that you may use this Data only
for lawful purposes and that under no circumstances will you use this Data
to: (1) allow, enable, or otherwise support the transmission of mass
unsolicited, commercial advertising or solicitations via e-mail, telephone,
or facsimile; or (2) enable high volume, automated, electronic processes
that apply to VeriSign (or its computer systems). The compilation,
repackaging, dissemination or other use of this Data is expressly
prohibited without the prior written consent of VeriSign. You agree not to
use electronic processes that are automated and high-volume to access or
query the Whois database except as reasonably necessary to register
domain names or modify existing registrations. VeriSign reserves the right
to restrict your access to the Whois database in its sole discretion to ensure
operational stability.  VeriSign may restrict or terminate your access to the
Whois database for failure to abide by these terms of use. VeriSign
reserves the right to modify these terms at any time.

The Registry database contains ONLY .COM, .NET, .EDU domains and
Registrars.
Domain Name: imperva.com
Registry Domain ID: 108851426_DOMAIN_COM-VRSN
Registrar WHOIS Server: whois.markmonitor.com
Registrar URL: http://www.markmonitor.com
Updated Date: 2024-11-23T10:47:28+0000
Creation Date: 2003-12-25T11:55:03+0000
Registrar Registration Expiration Date: 2026-12-25T00:00:00+0000
Registrar: MarkMonitor, Inc.
Registrar IANA ID: 292
Registrar Abuse Contact Email: abusecomplaints@markmonitor.com
Registrar Abuse Contact Phone: +1.2086851750
Domain Status: clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)
Domain Status: clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)
Domain Status: clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)
Domain Status: serverUpdateProhibited (https://www.icann.org/epp#serverUpdateProhibited)
Domain Status: serverTransferProhibited (https://www.icann.org/epp#serverTransferProhibited)
Domain Status: serverDeleteProhibited (https://www.icann.org/epp#serverDeleteProhibited)
Registrant Organization: Imperva Inc.
Registrant Country: US
Registrant Email: Select Request Email Form at https://domains.markmonitor.com/whois/imperva.com
Tech Email: Select Request Email Form at https://domains.markmonitor.com/whois/imperva.com
Name Server: ns-1341.awsdns-39.org
Name Server: ns-1956.awsdns-52.co.uk
Name Server: ns-687.awsdns-21.net
Name Server: ns-122.awsdns-15.com
DNSSEC: unsigned
URL of the ICANN WHOIS Data Problem Reporting System: http://wdprs.internic.net/
>>> Last update of WHOIS database: 2025-07-25T08:49:43+0000 <<<

For more information on WHOIS status codes, please visit:
  https://www.icann.org/resources/pages/epp-status-codes

If you wish to contact this domain’s Registrant or Technical
contact, and such email address is not visible above, you may do so via our web
form, pursuant to ICANN’s Temporary Specification. To verify that you are not a
robot, please enter your email address to receive a link to a page that
facilitates email communication with the relevant contact(s).

Web-based WHOIS:
  https://domains.markmonitor.com/whois/contact/imperva.com

If you have a legitimate interest in viewing the non-public WHOIS details, send
your request and the reasons for your request to whoisrequest@markmonitor.com
and specify the domain name in the subject line. We will review that request and
may ask for supporting documentation and explanation.

The data in MarkMonitor’s WHOIS database is provided for information purposes,
and to assist persons in obtaining information about or related to a domain
name’s registration record. While MarkMonitor believes the data to be accurate,
the data is provided "as is" with no guarantee or warranties regarding its
accuracy.

By submitting a WHOIS query, you agree that you will use this data only for
lawful purposes and that, under no circumstances will you use this data to:
  (1) allow, enable, or otherwise support the transmission by email, telephone,
or facsimile of mass, unsolicited, commercial advertising, or spam; or
  (2) enable high volume, automated, or electronic processes that send queries,
data, or email to MarkMonitor (or its systems) or the domain name contacts (or
its systems).

MarkMonitor reserves the right to modify these terms at any time.

By submitting this query, you agree to abide by this policy.

MarkMonitor Domain Management(TM)
Protecting companies and consumers in a digital world.

Visit MarkMonitor at https://www.markmonitor.com
Contact us at +1.8007459229
In Europe, at +44.02032062220
```

Which is quite different from www.vodafone.es

No failures on the certificate chain in the system so:

- Or they are using a valid certificate.
- Or the root certificate of the system is compromised.

This is in a fresh re-installed system.

## 19-ago-2025 - detected another payload at o2online.es

I have observed a download at https://o2online.es similar to what I have observed
at the previous operator web page; /hypothesis) probably I am receiving a wrong
content that inject the payload to be executed from the Internet browser.

The file is 'output.f66d5730807c.js' and can be located at the data payloads
directory.

The analysis by VirusTotal is worried at:
https://www.virustotal.com/gui/file/b744a700db211fd330a4a9150348413eb8415615e2eb3ab12299cf9791452bd9/behavior

The analysis by VirusTotal for the ungziped version:
https://www.virustotal.com/gui/file/f66d5730807c7e3af4fbcf2470f9dd98f50213ef9c4601bc75b93ebcb9c969e9/behavior

- The payload is not detected by any antivirus engineer.
- Based on the behavior analysis it has a bootkit, which is very dangerous
  for the persistency that it provides, because some of them resist to format
  and reinstallation of the system.
- The file seems to be the jquery library, but it should not have that results
  in VirusTotal, so probably the malware is being hidden in a tempered library.
- I downloaded the official 3.5.1 jquery library version minified, and the
  files does not match; the size differ in 1 character; downloaded from:
  https://code.jquery.com/jquery-3.5.1.min.js

## 2-sep-2025

see: https://www.redhat.com/en/blog/interrupt-linux-boot-process

Stop boot sequence into initramdisk by using "rd.break=premount"

## 28-sep-2025

When I achieve to boot the system, I observe in the logs the below:

```raw
$ journalctl --no-hostname | grep NetworkManager-initrd >> README.md
ago 26 08:17:54 systemd[1]: NetworkManager-initrd.service: Two services allocated for the same bus name org.freedesktop.NetworkManager, refusing operation.
ago 26 08:17:54 systemd[1]: NetworkManager-initrd.service: Two services allocated for the same bus name org.freedesktop.NetworkManager, refusing operation.
ago 26 22:49:12 systemd[1]: NetworkManager-initrd.service: Two services allocated for the same bus name org.freedesktop.NetworkManager, refusing operation.
ago 26 22:49:12 systemd[1]: NetworkManager-initrd.service: Two services allocated for the same bus name org.freedesktop.NetworkManager, refusing operation.
sep 20 05:44:36 systemd[1]: NetworkManager-initrd.service: Two services allocated for the same bus name org.freedesktop.NetworkManager, refusing operation.
sep 20 05:44:36 systemd[1]: NetworkManager-initrd.service: Two services allocated for the same bus name org.freedesktop.NetworkManager, refusing operation.
sep 20 05:55:39 systemd[1]: NetworkManager-initrd.service: Two services allocated for the same bus name org.freedesktop.NetworkManager, refusing operation.
sep 20 05:55:39 systemd[1]: NetworkManager-initrd.service: Two services allocated for the same bus name org.freedesktop.NetworkManager, refusing operation.
sep 20 05:58:40 systemd[1]: NetworkManager-initrd.service: Two services allocated for the same bus name org.freedesktop.NetworkManager, refusing operation.
sep 20 05:58:40 systemd[1]: NetworkManager-initrd.service: Two services allocated for the same bus name org.freedesktop.NetworkManager, refusing operation.
sep 28 14:51:22 systemd[1]: NetworkManager-initrd.service: Two services allocated for the same bus name org.freedesktop.NetworkManager, refusing operation.
sep 28 14:51:22 systemd[1]: NetworkManager-initrd.service: Two services allocated for the same bus name org.freedesktop.NetworkManager, refusing operation.
```

Why is coming a NetworkManager instance coming from the initrd? Where is this service coming from? It was not found yet in the
initramdisk at `/boot/initramfs-linux-asahi.img`

Located the service at `/usr/lib/systemd/system/` directory:

```raw
$ ll /usr/lib/systemd/system/*-initrd* >> README.md
-rw-r--r-- 1 root root  877 sep 18 03:52 /usr/lib/systemd/system/NetworkManager-config-initrd.service
-rw-r--r-- 1 root root 1370 sep 18 03:52 /usr/lib/systemd/system/NetworkManager-initrd.service
-rw-r--r-- 1 root root  930 sep 18 03:52 /usr/lib/systemd/system/NetworkManager-wait-online-initrd.service
-rw-r--r-- 1 root root  909 sep  4 20:35 /usr/lib/systemd/system/systemd-pcrphase-initrd.service
```

A copy of this files uploaded at data/20250928
