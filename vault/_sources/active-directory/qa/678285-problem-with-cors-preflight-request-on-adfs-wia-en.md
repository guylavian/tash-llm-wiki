---
title: "Problem with CORS preflight request on ADFS WIA endpoint"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/678285/problem-with-cors-preflight-request-on-adfs-wia-en
question_id: 678285
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Problem with CORS preflight request on ADFS WIA endpoint

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/678285/problem-with-cors-preflight-request-on-adfs-wia-en (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I have got a problem with the WIA authentication endpoint on ADFS in Windows Server 2019 in combination with a CORS preflight request:  

If a client session of a web application expires and the user then clicks on some link in a page, client Javascript produces an XHR request and server responds with redirection to ADFS server to WS-Federation authentication endpoint (/adfs/ls). Client sends CORS preflight request (OPTIONS), to which the server successfully responds, and the next subsequent GET request is responded with redirection to Windows Integrated Authentication (WIA) endpoint (/adfs/ls/wia). The client then sends CORS preflight request (OPTIONS) to this endpoint as well, but server responds with 401 Unauthorized HTTP status code without necessary CORS headers. The next GET XHR request is blocked by web browser because the previous preflight request failed.  

Below is a slightly generalized log of the communication.  

I think the /adfs/ls/wia endpoint should respond to the CORS preflight request with an HTTP 200 OK status code and CORS response headers. Then the following GET request will not be blocked by the web browser and should be responded by HTTP 401 Unauthorized status code.  

Similar behavior is also found in other commonly used web browsers (Edge, Chrome).  

I tried to find some configuration solution, but to no success. CORS is configured correctly in the ADFS server (CORSEnabled and CORSTrustedOrigins properties) and I could not find any other configuration, i. e. for WIA authentication endpoint.  

Could anyone advise how to get the adfs/ls/wia endpoint to process the CORS preflight request correctly, or is this a bug in the ADFS server implementation?  

Thank you very much for any advice.  

Communication log:  

```
POST /iportal/exec/dashboard HTTP/1.1
Host: appserver.somedomain.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0
Accept: */*
Accept-Language: cs,sk;q=0.8,en-US;q=0.6,en-GB;q=0.4,en;q=0.2
Accept-Encoding: gzip, deflate, br
Referer: https://appserver.somedomain.com/iportal/dashboard-procHistory
Content-Type: application/json
Origin: https://appserver.somedomain.com
Content-Length: 77695
Connection: keep-alive
Cookie: CID=AgAAAGHtQYyYOLLYcYfbBOwcSI0=; WBSID=5832b34f4e02f00f;
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Pragma: no-cache
Cache-Control: no-cache

HTTP/1.1 302 Found
Date: Tue, 28 Dec 2021 12:10:06 GMT
Location: https://adfs.somedomain.com/adfs/ls/?wa=wsignin1.0&wtrealm=https%3A%2F%2Fappserver.somedomain.com%2F&wctx=ru%3Dhttps%253A%252F%252Fappserver.somedomain.com%252Fiportal%252Fexec%252Fdashboard&wct=2021-12-28T13%3A10%3A06Z
Content-Length: 0

OPTIONS /adfs/ls/?wa=wsignin1.0&wtrealm=https%3A%2F%2Fappserver.somedomain.com%2F&wctx=ru%3Dhttps%253A%252F%252Fappserver.somedomain.com%252Fiportal%252Fexec%252Fdashboard&wct=2021-12-28T13%3A10%3A06Z HTTP/1.1
Host: adfs.somedomain.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0
Accept: */*
Accept-Language: cs,sk;q=0.8,en-US;q=0.6,en-GB;q=0.4,en;q=0.2
Accept-Encoding: gzip, deflate, br
Access-Control-Request-Method: GET
Referer: https://appserver.somedomain.com/
Origin: https://appserver.somedomain.com
Connection: keep-alive
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
Pragma: no-cache
Cache-Control: no-cache

HTTP/1.1 200 OK
Allow: OPTIONS, GET, HEAD, POST
Content-Length: 0
Content-Type: text/html; charset=utf-8
Vary: Origin
Server: Microsoft-HTTPAPI/2.0
Strict-Transport-Security: max-age = 31536000
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Content-Security-Policy: default-src 'self' 'unsafe-inline' 'unsafe-eval'; img-src 'self' data:;
Access-Control-Allow-Origin: https://appserver.somedomain.com
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: CONNECT, DELETE, GET, MERGE, OPTIONS, POST, PUT, PATCH, TRACE
Access-Control-Max-Age: 86400
Date: Tue, 28 Dec 2021 12:10:07 GMT

GET /adfs/ls/?wa=wsignin1.0&wtrealm=https%3A%2F%2Fappserver.somedomain.com%2F&wctx=ru%3Dhttps%253A%252F%252Fappserver.somedomain.com%252Fiportal%252Fexec%252Fdashboard&wct=2021-12-28T13%3A10%3A06Z HTTP/1.1
Host: adfs.somedomain.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0
Accept: */*
Accept-Language: cs,sk;q=0.8,en-US;q=0.6,en-GB;q=0.4,en;q=0.2
Accept-Encoding: gzip, deflate, br
Origin: https://appserver.somedomain.com
Referer: https://appserver.somedomain.com/
Connection: keep-alive
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
Pragma: no-cache
Cache-Control: no-cache

HTTP/1.1 302 Found
Content-Length: 0
Content-Type: text/html; charset=utf-8
Location: https://adfs.somedomain.com:443/adfs/ls/wia?wa=wsignin1.0&wtrealm=https%3A%2F%2Fappserver.somedomain.com%2F&wctx=ru%3Dhttps%253A%252F%252Fappserver.somedomain.com%252Fiportal%252Fexec%252Fdashboard&wct=2021-12-28T13%3A10%3A06Z&client-request-id=b3a8414e-1afc-4be7-a200-0080000000c1
Vary: Origin
Server: Microsoft-HTTPAPI/2.0
Strict-Transport-Security: max-age = 31536000
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Content-Security-Policy: default-src 'self' 'unsafe-inline' 'unsafe-eval'; img-src 'self' data:;
Access-Control-Allow-Origin: https://appserver.somedomain.com
Access-Control-Allow-Credentials: true
Date: Tue, 28 Dec 2021 12:10:07 GMT

OPTIONS /adfs/ls/wia?wa=wsignin1.0&wtrealm=https%3A%2F%2Fappserver.somedomain.com%2F&wctx=ru%3Dhttps%253A%252F%252Fappserver.somedomain.com%252Fiportal%252Fexec%252Fdashboard&wct=2021-12-28T13%3A10%3A06Z&client-request-id=b3a8414e-1afc-4be7-a200-0080000000c1 HTTP/1.1
Host: adfs.somedomain.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0
Accept: */*
Accept-Language: cs,sk;q=0.8,en-US;q=0.6,en-GB;q=0.4,en;q=0.2
Accept-Encoding: gzip, deflate, br
Access-Control-Request-Method: GET
Access-Control-Request-Headers: content-type
Referer: https://appserver.somedomain.com/
Origin: https://appserver.somedomain.com
Connection: keep-alive
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
Pragma: no-cache
Cache-Control: no-cache

HTTP/1.1 401 Unauthorized
Content-Length: 0
Server: Microsoft-HTTPAPI/2.0
WWW-Authenticate: Negotiate
WWW-Authenticate: NTLM
Date: Tue, 28 Dec 2021 12:10:07 GMT

(Firefox network debugger reports error "CORS Missing Allow Origin")

GET /adfs/ls/wia?wa=wsignin1.0&wtrealm=https%3A%2F%2Fappserver.somedomain.com%2F&wctx=ru%3Dhttps%253A%252F%252Fappserver.somedomain.com%252Fiportal%252Fexec%252Fdashboard&wct=2021-12-28T13%3A10%3A06Z&client-request-id=b3a8414e-1afc-4be7-a200-0080000000c1 undefined
Host: adfs.somedomain.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0
Accept: */*
Accept-Language: cs,sk;q=0.8,en-US;q=0.6,en-GB;q=0.4,en;q=0.2
Accept-Encoding: gzip, deflate, br
Origin: https://appserver.somedomain.com
Referer: https://appserver.somedomain.com/
Connection: keep-alive
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site

(Request not sent to server, Firefox network debugger reports error "NS_ERROR_DOM_BAD_URI")
```

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-16*

Thanks SH. Sorry for my late response. I was not notified.

In the end we also build our own refresh mechanism in the frontend. Its a shame that Microsoft is not willing to help in this. One more reason to ditch this product.

Thanks for all the replies!

## Answer (community) — community member

*upvotes: 0 · updated: 2022-05-25*

Hi, did you manage to find a solution?   

I got official microsoft support on this issue and an engineer told me that these WIA endpoint don't offer CORS headers and will never do. They are not willing to change this. We are struggling already for a few months now to get this to work without any succes.   

Please let me know if you have anything that works.  

Regards,  

Marc
