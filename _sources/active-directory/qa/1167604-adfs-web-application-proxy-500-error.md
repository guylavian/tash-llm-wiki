---
title: "ADFS Web Application Proxy 500 error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1167604/adfs-web-application-proxy-500-error
question_id: 1167604
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 1
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Volunteer Moderator"]
---
# ADFS Web Application Proxy 500 error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1167604/adfs-web-application-proxy-500-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Odd problem with my ADFS WAP applications. A year ago, our users started having issues in which our WAP applications showed a 500 error page after logging into ADFS. Clearing the browser cookies fixes the issue, bit of a pain for 2000+ users but didn't find a different fix at the time. A few days ago, it started happening again. On the user side, they sign into ADFS, and then 500 error. This has happened in Chrome, Edge, and Firefox.

On the WAP server, I'm getting the following error repeated:

Log Name:      Microsoft-Windows-WebApplicationProxy/Admin

Source:        Microsoft-Windows-WebApplicationProxy

Date:          2/1/2023 11:38:03 AM

Event ID:      12027

Task Category: None

Level:         Error

Keywords:      

User:          NETWORK SERVICE

Computer:      [redacted]

Description:

Web Application Proxy encountered an unexpected error while processing the request.

Error: Unspecified error

 (0x80004005)

Details:

Transaction ID: [redacted]

Session ID: [redacted]

Published Application Name: [redacted]

Published Application ID: [redacted]

Published Application External URL: [redacted]

Published Backend URL: [redacted]

User: <Unknown>

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36

Device ID: <Not Applicable>

Token State: NotFound

Cookie State: NotFound

Client Request URL: [redacted]

Backend Request URL: <Not Applicable>

Preauthentication Flow: <Not Applicable>

Backend Server Authentication Mode: 

State Machine State: OuOfOrderFEHeadersWriting

Response Code to Client: 500

Response Message to Client: <Not Applicable>

Client Certificate Issuer: <Not Found>

Response Code from Backend: <Not Applicable>

Frontend Response Location Header: <Not Applicable>

Backend Response Location Header: <Not Applicable>

Backend Request Http Verb: <Not Applicable>

Client Request Http Verb: GET

I found another post describing this issue, but there isn't a resolution:

https://learn.microsoft.com/en-us/answers/questions/516478/sometimes-web-application-proxy-get-500-error-and  

Any ideas or troubleshooting tips would be most welcome.  

Thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-06*

Hi. Thank you for your question and reaching out. I’d be more than happy to help you with your query

This error message indicates that the Web Application Proxy (WAP) encountered an unexpected error while processing the request. The error is likely related to an issue with the token state or cookie state, as noted in the log. Some steps you can try to resolve this issue include:

Clearing the browser cache and cookies for the affected users, as you have already tried this and it has worked in the past.

Checking the WAP server event logs for additional information and error messages that may shed light on the issue.

Verifying that the WAP server is running the latest version of the software and that all updates have been installed.

Verifying that the WAP configuration settings are correct, including the published application settings, the external URL, and the backend URL.

Restarting the WAP server and the ADFS server to see if that resolves the issue.

If the issue persists, you may want to consider seeking assistance from Microsoft support, as this may be a bug in the software or a configuration issue that requires additional troubleshooting.

If the reply was helpful, please don’t forget to upvote or accept as answer, thank you.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-02-06*

Double post

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2023-02-04*

Hi,

It seems related to the Kerberos Ticket and SPN check the troubleshooting guide over here - 

https://learn.microsoft.com/en-us/windows-server/remote/remote-access/web-application-proxy/troubleshooting-web-application-proxy

Hope this helps.

JS

==

Please Accept the answer if the information helped you. This will help us and others in the community as well.
