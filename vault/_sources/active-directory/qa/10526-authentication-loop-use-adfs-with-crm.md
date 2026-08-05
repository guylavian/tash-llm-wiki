---
title: "Authentication Loop use ADFS with CRM"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/10526/authentication-loop-use-adfs-with-crm
question_id: 10526
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Authentication Loop use ADFS with CRM

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/10526/authentication-loop-use-adfs-with-crm (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I posted this in CRM Dynamics to no avail so I'm trying here.    

I have two users (one being me) who get an authentication loop when attempting to access our CRM system via our intranet.    

I used a SAML inspection program and I get    

ws-fed error    

fds    

"requests": [    

{    

"method": "GET",    

"url": "https://removed.crm/crm365/",    

"requestId": "4229",    

"requestHeaders": [    

{    

"name": "Host",    

"value": "removedcrm.com"    

},    

{    

"name": "User-Agent",    

"value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0)    

Gecko/20100101 Firefox/72.0"    

},    

{    

"name": "Accept",    

"value":    

"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0    

.8"    

},    

{    

"name": "Accept-Language",    

"value": "en-US,en;q=0.5"    

},    

{    

"name": "Accept-Encoding",    

"value": "gzip, deflate, br"    

},    

{    

"name": "Connection",    

"value": "keep-alive"    

},    

{    

"name": "Referer",    

"value": "http://removed/default.aspx"    

},    

{    

"name": "Cookie",    

"value":    

"ReqClientId={hash:ad5343d02572c374afa16e0b739e365585f9658bfe69a945337188    

83c3475953}"    

},    

{    

"name": "Upgrade-Insecure-Requests",    

"value": "1"    

}    

],    

"get": [],    

"responseStatus": 302,    

"responseStatusText": "HTTP/2.0 302 Found",    

"responseHeaders": [    

{    

"name": "cache-control",    

"value": "private"    

},    

{    

"name": "content-type",    

"value": "text/html; charset=utf-8"    

},    

{    

"name": "location",    

"value":    

"https://removed.com/adfs/ls/?wa=wsignin1.0&wtrealm=https%3a%2    

f%2frvkcrm.crm.rvkinc.com%2f&wctx=rm%3d1%26id%3db8eb1d65-29d4-4e23-aecbe4549043bb03%    

26ru%3d%252fremoved365%252fdefault.aspx%26crmorgid%3de369084a    

-a907-e411-954e-00155d009f27&wct=2020-02-    

13T19%3a48%3a32Z&wauth=urn%3afederation%3aauthentication%3awindows"    

},    

{    

"name": "server",    

"value": "Microsoft-IIS/10.0"    

},    

{    

"name": "req_id",    

"value": "3bc91d84-7e42-49aa-9ebc-1958b0077b1a"    

},    

{    

"name": "x-aspnet-version",    

"value": "4.0.30319"    

},    

{    

"name": "x-powered-by",    

"value": "ASP.NET"    

},    

{    

"name": "date",    

"value": "Thu, 13 Feb 2020 19:48:32 GMT"    

},    

{    

"name": "content-length",    

"value": "457"    

},    

{    

"name": "X-Firefox-Spdy",    

"value": "h2"    

}    

]    

},    

{    

"method": "GET",    

"url":    

"removed.com/.../    

f%2fremovedinc.com%2f&wctx=rm%3d1%26id%3db8eb1d65-29d4-4e23-aecbe4549043bb03%    

26ru%3d%252frvkcrm365%252fdefault.aspx%26crmorgid%3de369084a    

-a907-e411-954e-00155d009f27&wct=2020-02-    

13T19%3a48%3a32Z&wauth=urn%3afederation%3aauthentication%3awindows",    

"requestId": "4229",    

"requestHeaders": [    

{    

"name": "Host",    

"value": "removed.com"    

},    

{    

"name": "User-Agent",    

"value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0)    

Gecko/20100101 Firefox/72.0"    

},    

{    

"name": "Accept",    

"value":    

"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0    

.8"    

},    

{    

"name": "Accept-Language",    

"value": "en-US,en;q=0.5"    

},    

{    

"name": "Accept-Encoding",    

"value": "gzip, deflate, br"    

},    

{    

"name": "Referer",    

"value": "http://removed/default.aspx"    

},    

{    

"name": "Connection",    

"value": "keep-alive"    

},    

{    

"name": "Upgrade-Insecure-Requests",    

"value": "1"    

}    

],    

"get": [    

[    

"wa",    

"wsignin1.0"    

],    

[    

"wtrealm",    

"https://crm.removed.com/"    

],    

[    

"wctx",    

"rm=1&id=b8eb1d65-29d4-4e23-aecbe4549043bb03&    

ru=%2fremoved365%2fdefault.aspx&crmorgid=e369084a-a907-e411-    

954e-00155d009f27"    

],    

[    

"wct",    

"2020-02-13T19:48:32Z"    

],    

[    

"wauth",    

"urn:federation:authentication:windows"    

]    

],    

"protocol": "WS-Fed",    

"saml": null,    

"responseStatus": 302,    

"responseStatusText": "HTTP/1.1 302 Found",    

"responseHeaders": [    

{    

"name": "Content-Length",    

"value": "0"    

},    

{    

"name": "Content-Type",    

"value": "text/html; charset=utf-8"    

},    

{    

"name": "Location",    

"value":    

"https://removedc.com:443/adfs/ls/wia?wa=wsignin1.0&wtrealm=htt    

ps%3a%2f%removed%2f&wctx=rm%3d1%26id%3db8eb1d65-29d4-    

4e23-aecbe4549043bb03%    

26ru%3d%252frvkcrm365%252fdefault.aspx%26crmorgid%3de369084a    

-a907-e411-954e-00155d009f27&wct=2020-02-    

13T19%3a48%3a32Z&wauth=urn%3afederation%3aauthentication%3awindows&client    

-request-id=ebb8764d-0b1c-4f4e-6b15-0080010000de"    

},    

{    

"name": "Server",    

"value": "Microsoft-HTTPAPI/2.0"    

},    

{    

"name": "Date",    

"value": "Thu, 13 Feb 2020 19:48:32 GMT"    

}    

]    

},    

"timestamp": "2020-02-13T19:48:42.736Z"    

It appears to be a problem at WS-FED.    

If a user tries a different machine it is fine, if a different user logs into the same machine they can sometimes work.    

I"ve tried accessing the ADFS and it returns the federationmetadata.xml file correctly.    

Done all the usual, changing profile, clearing cache, different browsers all with the same issue.    

Anyone have an idea?    

Thanks    

david

## Answer (community) — community member

*upvotes: 0 · updated: 2020-03-02*

Hi  

I have the fiddler trace but will see about sanitizing.

Problem that users work on most system, but some they just don't work.  

You to the link on intranet and prompts for username/pwd even in IE when it should be passed along.  

I ran on a different browser where the credentials are cached and works for the intranet site but then when try to access the crm we run into this trouble. All running ie11 btw.  

Your last point "Maybe a different maximum size for the headers and/or cookies." I will try

This is from the fiddler raw data  

HTTP/1.1 401 Unauthorized  

Content-Length: 0  

Server: Microsoft-HTTPAPI/2.0  

WWW-Authenticate: Negotiate  

WWW-Authenticate: NTLM  

Date: Mon, 02 Mar 2020 20:07:23 GMT  

Proxy-Support: Session-Based-Authentication

here is the cleaned up fiddler data, hope I did that right,  

CONNECT <removed>:443 HTTP/1.1  

Host: <removed>:443  

User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko  

Connection: close  

Cache-Control: no-cache  

Pragma: no-cache  

Connection: Keep-Alive

A SSLv3-compatible ClientHello handshake was found. Fiddler extracted the parameters below.

Version: 3.3 (TLS/1.2)  

Random: B9 61 1A C3 42 B9 1C 69 DA D2 F9 6E 80 55 B9 C2 6F C6 59 50 D7 0F 36 4D C1 86 0D 79 0C 77 5E 57  

"Time": 9/21/2073 11:07:53 PM  

SessionID: empty  

Extensions:  

NextProtocolNego empty  

server_name <removed>  

status_request OCSP - Implicit Responder  

supported_groups x25519 [0x1d], secp256r1 [0x17], secp384r1 [0x18], secp521r1 [0x19]  

ec_point_formats uncompressed [0x0]  

signature_algs rsa_pkcs1_sha256, ecdsa_secp256r1_sha256, rsa_pkcs1_sha384, ecdsa_secp384r1_sha384, rsa_pkcs1_sha512, ecdsa_secp521r1_sha512, rsa_pkcs1_sha1, ecdsa_sha1  

renegotiation_info 00  

ALPN h2, http/1.1  

SignedCertTimestamp (RFC6962) empty  

Ciphers:  

[C02F] TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256  

[C030] TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384  

[C02B] TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256  

[C02C] TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384  

[CCA8] TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256  

[CCA9] TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256  

[C013] TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA  

[C009] TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA  

[C014] TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA  

[C00A] TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA  

[009C] TLS_RSA_WITH_AES_128_GCM_SHA256  

[009D] TLS_RSA_WITH_AES_256_GCM_SHA384  

[002F] TLS_RSA_WITH_AES_128_CBC_SHA  

[0035] TLS_RSA_WITH_AES_256_CBC_SHA  

[C012] TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA  

[000A] SSL_RSA_WITH_3DES_EDE_SHA

Compression:  

[00] NO_COMPRESSION

HTTP/1.1 200 Connection Established  

FiddlerGateway: Direct  

StartTime: 12:07:22.691  

Connection: close

Encrypted HTTPS traffic flows through this CONNECT tunnel. HTTPS Decryption is enabled in Fiddler, so decrypted sessions running in this tunnel will be shown in the Web Sessions list.

Secure Protocol: Tls12  

Cipher: Aes256 256bits  

Hash Algorithm: Sha384 ?bits  

Key Exchange: ECDHE_RSA (0xae06) 255bits

== Server Certificate ==========  

<removed>  

[SubjectAltNames]  

<removed>

GET https://<removed>rvkcrm365/ HTTP/1.1  

Host: <removed>  

User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; .NET CLR 1.1.4322; wbx 1.0.0; Zoom 3.6.0)  

Accept: image/gif, image/jpeg, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, /  

Accept-Encoding: gzip, deflate  

Accept-Language: en-US  

Connection: Keep-Alive  

Cookie: ReqClientId=0ba90f69-7f25-4bbb-a695-b5f13221c285  

Referer: http://rvknow/default.aspx

HTTP/1.1 302 Found  

Cache-Control: private  

Content-Type: text/html; charset=utf-8  

Location: https://<removed>/adfs/ls/?wa=wsignin1.0&wtrealm=https%3a%2f%2f<removed>%2f&wctx=rm%3d1%26id%3d50dc8871-66cf-4d0b-b70c-65c50975ae6f%26ru%3d%252frvkcrm365%252fdefault.aspx%26crmorgid%3de369084a-a907-e411-954e-00155d009f27&wct=2020-03-02T20%3a07%3a22Z&wauth=urn%3afederation%3aauthentication%3awindows  

Server: Microsoft-IIS/10.0  

REQ_ID: e4de8c7e-1553-426e-810b-2fbf4e4413aa  

X-AspNet-Version: 4.0.30319  

X-Powered-By: ASP.NET  

Date: Mon, 02 Mar 2020 20:07:22 GMT  

Content-Length: 457

<html><head><title>Object moved</title></head><body>  

<h2>Object moved to <a href="https://<removed>/adfs/ls/?wa=wsignin1.0&wtrealm=https%3a%2f%2f<removed>%2f&wctx=rm%3d1%26id%3d50dc8871-66cf-4d0b-b70c-65c50975ae6f%26ru%3d%252f<removed>365%252fdefault.aspx%26crmorgid%3de369084a-a907-e411-954e-00155d009f27&wct=2020-03-02T20%3a07%3a22Z&wauth=urn%3afederation%3aauthentication%3awindows">here</a>.</h2>  

</body></html>

CONNECT <removed>:443 HTTP/1.1  

Host: <removed>:443  

User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko  

Connection: close  

Cache-Control: no-cache  

Pragma: no-cache  

Connection: Keep-Alive

A SSLv3-compatible ClientHello handshake was found. Fiddler extracted the parameters below.

Version: 3.3 (TLS/1.2)  

Random: 76 F3 D0 76 E0 60 F1 4F AA C3 65 F1 16 9E 97 E8 96 F1 39 DA BB B4 AA D8 4E 2D 71 1C AF DF 95 3C  

"Time": 3/2/2033 11:41:42 AM  

SessionID: empty  

Extensions:  

NextProtocolNego empty  

server_name <removed>  

status_request OCSP - Implicit Responder  

supported_groups x25519 [0x1d], secp256r1 [0x17], secp384r1 [0x18], secp521r1 [0x19]  

ec_point_formats uncompressed [0x0]  

signature_algs rsa_pkcs1_sha256, ecdsa_secp256r1_sha256, rsa_pkcs1_sha384, ecdsa_secp384r1_sha384, rsa_pkcs1_sha512, ecdsa_secp521r1_sha512, rsa_pkcs1_sha1, ecdsa_sha1  

renegotiation_info 00  

ALPN h2, http/1.1  

SignedCertTimestamp (RFC6962) empty  

Ciphers:  

[C02F] TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256  

[C030] TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384  

[C02B] TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256  

[C02C] TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384  

[CCA8] TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256  

[CCA9] TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256  

[C013] TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA  

[C009] TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA  

[C014] TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA  

[C00A] TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA  

[009C] TLS_RSA_WITH_AES_128_GCM_SHA256  

[009D] TLS_RSA_WITH_AES_256_GCM_SHA384  

[002F] TLS_RSA_WITH_AES_128_CBC_SHA  

[0035] TLS_RSA_WITH_AES_256_CBC_SHA  

[C012] TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA  

[000A] SSL_RSA_WITH_3DES_EDE_SHA

Compression:  

[00] NO_COMPRESSION

HTTP/1.1 200 Connection Established  

FiddlerGateway: Direct  

StartTime: 12:07:22.865  

Connection: close

Encrypted HTTPS traffic flows through this CONNECT tunnel. HTTPS Decryption is enabled in Fiddler, so decrypted sessions running in this tunnel will be shown in the Web Sessions list.

Secure Protocol: Tls12  

Cipher: Aes256 256bits  

Hash Algorithm: Sha384 ?bits  

Key Exchange: ECDHE_RSA (0xae06) 255bits

== Server Certificate ==========  

<removed>  

[SubjectAltNames]  

<removed>

GET https://<removed>/adfs/ls/?wa=wsignin1.0&wtrealm=https%3a%2f%2f<removed>%2f&wctx=rm%3d1%26id%3d50dc8871-66cf-46f%26ru%3d%252f<removed>%252fdefault.aspx%26crmorgid%3de369084a-a907-e411-954e-00155d009f27&wct=2020-03-02T20%3a07%3a22Z&wauth=urn%3afederation%3aauthentication%3awindows HTTP/1.1  

Host: <removed>  

User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; .NET CLR 1.1.4322; wbx 1.0.0; Zoom 3.6.0)  

Accept: image/gif, image/jpeg, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, /  

Accept-Encoding: gzip, deflate  

Accept-Language: en-US  

Connection: Keep-Alive  

Referer: http://rvknow/default.aspx

HTTP/1.1 302 Found  

Content-Length: 0  

Content-Type: text/html; charset=utf-8  

Location: https://<removed>:443/adfs/ls/wia?wa=wsignin1.0&wtrealm=https%3a%2f%2f<removed>%2f&wctx=rm%3d1%26id%3d50dc8871-66cf-4d0b-b70c-65c50975ae6f%26ru%3d%252f<removed>%252fdefault.aspx%26crmorgid%3de369084a-a9072020-03-02T20%3a07%3a22Z&wauth=urn%3afederation%3aauthentication%3awindows&client-request-id=50adfbdb-fadb-4dea-2e01-0080010000d2  

Server: Microsoft-HTTPAPI/2.0  

Date: Mon, 02 Mar 2020 20:07:23 GMT

GET https://<removed>/adfs/ls/wia?wa=wsignin1.0&wtrealm=https%3a%2f%2f<removed>%2f&wctx=rm%3d1%26id%3d50dc8871-66cf-b70c-65c50975ae6f%26ru%3d%252frvkcrm365%252fdefault.aspx%26crmorgid%3de369084a-a907-e411-954e-00155d009f27&wct=2020-03-02T20%3a07%3a22Z&wauth=urn%3afederation%3aauthentication%3awindows&client-request-id=50adfbdb-fadb-4dea-2e01-0080010000d2 HTTP/1.1  

Host: rvkservices.rvkinc.com  

User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; .NET CLR 1.1.4322; wbx 1.0.0; Zoom 3.6.0)  

Accept: image/gif, image/jpeg, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, /  

Accept-Encoding: gzip, deflate  

Accept-Language: en-US  

Connection: Keep-Alive  

Referer: http://rvknow/default.aspx

HTTP/1.1 401 Unauthorized  

Content-Length: 0  

Server: Microsoft-HTTPAPI/2.0  

WWW-Authenticate: Negotiate  

WWW-Authenticate: NTLM  

Date: Mon, 02 Mar 2020 20:07:23 GMT  

Proxy-Support: Session-Based-Authentication

GET https://<removed>/adfs/ls/wia?wa=wsignin1.0&wtrealm=https%3a%2f%2f<removed>%2f&wctx=rm%3d1%26id%3<removed>e369084a-a907-e411-954e-00155d009f27&wct=2020-03-02T20%3a07%3a22Z&wauth=urn%3afederation%3aauthentication%3awindows&client-request-id=50adfbdb-fadb-4dea-2e01-0080010000d2 HTTP/1.1  

Host: <removed>  

User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; .NET CLR 1.1.4322; wbx 1.0.0; Zoom 3.6.0)  

Accept: image/gif, image/jpeg, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, /  

Accept-Encoding: gzip, deflate  

Accept-Language: en-US  

Authorization: Negotiate <removed>  

Connection: Keep-Alive  

Referer: http://rvknow/default.aspx

HTTP/1.1 401 Unauthorized  

Content-Length: 0  

Server: Microsoft-HTTPAPI/2.0  

WWW-Authenticate: Negotiate  

WWW-Authenticate: NTLM  

Date: Mon, 02 Mar 2020 20:07:23 GMT  

Proxy-Support: Session-Based-Authentication
