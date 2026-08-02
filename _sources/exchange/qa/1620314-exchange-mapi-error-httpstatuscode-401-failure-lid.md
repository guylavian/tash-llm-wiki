---
title: "exchange MAPI error HttpStatusCode: 401   Failure LID: 47372"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1620314/exchange-mapi-error-httpstatuscode-401-failure-lid
question_id: 1620314
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# exchange MAPI error HttpStatusCode: 401   Failure LID: 47372

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1620314/exchange-mapi-error-httpstatuscode-401-failure-lid (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,

On newly installed on prem exchange 2019 i have problem that some times (not all the time) outlook 2019 starts constantly asking password, when i type in correct password after 3 s. it ask again  and again.

Also Microsoft Remote Connectivity Analyzer some times gives 401 error for MAPI connectivity,

The logs is below.

Testing the MAPI Address Book endpoint on the Exchange server.

An error occurred while testing the address book endpoint.

 

Test Steps

 

Testing the address book "Check Name" operation for user ***@domain.com against server mail.domain.com.

An error occurred while attempting to resolve the name.

 

Additional Details

A protocol layer error occured. HttpStatusCode: 401

Failure LID: 47372

Failure Information:

REQUEST [2024-03-16T17:50:43.5572826Z] [ResolvedIPs: ...]

POST /mapi/nspi/?mailboxId=dedaeee9-c194-4869-a62a-f7d5ec4f360b@ domain.com HTTP/1.1 Content-Type: application/octet-stream

User-Agent: MapiHttpClient X-RequestId: 84d63ec9-79eb-4fdd-837b-bda52d6e2965:1

X-ClientInfo: 6ceead99-899e-41ce-9cee-ecb779c5b4b9:1

client-request-id: 5d59a05e-a548-4d22-86fa-8dad6a246911

X-ClientApplication: MapiHttpClient/15.20.7002.0

X-RequestType: Bind Authorization: Negotiate [truncated]

Host: mail.domain.com

Content-Length: 45

 

--- REQUEST BODY [+0.330] --- ..[BODY SIZE: 45]

--- REQUEST SENT [+0.330] ---

 

RESPONSE [+0.709]

HTTP/1.1 401 Unauthorized

request-id: c62cb78d-6116-4910-a6c7-f161fabe9104

X-OWA-Version: 15.2.1118.7 X-FailureContext:

FrontEnd;401;VW5hdXRob3JpemVk;;;;

Server: Microsoft-IIS/10.0

WWW-Authenticate: Negotiate,NTLM

X-Powered-By: ASP.NET

X-FEServer: MAIL

Date: Sat, 16 Mar 2024 17:50:35 GMT

Content-Length: 0

 

--- RESPONSE BODY [+0.719] ---

--- RESPONSE DONE [+0.720] ---

 

EXCEPTION THROWN [+0.768]

 

HTTP Response Headers:

request-id: c62cb78d-6116-4910-a6c7-f161fabe9104

X-OWA-Version: 15.2.1118.7

X-FailureContext: FrontEnd;401;VW5hdXRob3JpemVk;;;;

Server: Microsoft-IIS/10.0

WWW-Authenticate: Negotiate,NTLM

X-Powered-By: ASP.NET

X-FEServer: MAIL

Date: Sat, 16 Mar 2024 17:50:35 GMT

Content-Length: 0

 

HTTP Status Code: 401 Unauthorized

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-03-18*

Hi @PM  ，

From the description, in case it's an issue related to what is mentioned in this document, please try changing or adding the following registry value and see if there would be any improvement:  

(Important: Follow the steps in this section carefully. Serious problems might occur if you modify the registry incorrectly. Before you modify it, back up the registry for restoration in case problems occur.)

Key: `HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Common\Internet\`   

Value name: EnableHttpAccessTypeAutomaticProxy   

Type: REG_DWORD   

Value data: 0

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
