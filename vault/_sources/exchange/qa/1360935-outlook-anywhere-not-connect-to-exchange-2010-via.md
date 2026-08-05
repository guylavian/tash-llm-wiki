---
title: "Outlook Anywhere not connect to  Exchange 2010 via Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1360935/outlook-anywhere-not-connect-to-exchange-2010-via
question_id: 1360935
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Outlook Anywhere not connect to  Exchange 2010 via Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1360935/outlook-anywhere-not-connect-to-exchange-2010-via (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all

We are migrating from Exchange 2010 to Exchange 2016.

After switching incoming https\https traffic to Exchange 2016, external mail clients for Exchange 2010 users cannot connect. Outlook writes that the Server is unavailable.

When tested with https://testconnectivity.microsoft.com/tests/exchange, with user credentials, Exchange 2010 throws several errors connecting to Autodiskover:

<testresult status="Error" errorid="a28be452-a4b2-419c-851a-37f441f3120e" contentUrl="" testdescription="The Microsoft Connectivity Analyzer is trying to get an XML response from the Autodiscover service from the URL https://autodiscover.mydomain .ru:443/Autodiscover/Autodiscover.xml for user ******@mydomain.ru." resultdescription="The Microsoft Connectivity Analyzer was unable to retrieve the Autodiscover XML response." additionaldetails="HTTP 500 response returned Unknown. HTTP response headers: request-id: ad8f3d8a-e56a-43e2-b220-010c7c66932a X-CasErrorCode: ServerNotFound Persistent-Auth: true X-FEServer: SW-MAIL16-01 Content-Length: 0 Cache-Control: private Date: Mon, 04 Sep 2023 16:31:08 GMT Server: Microsoft-IIS/10.0 X-AspNet-Version: 4.0.30319 X-Powered-By: ASP.NET "elapsedMilliseconds="3656">

<testresult status="Error" errorid="e58749b1-cd80-4cc8-9bb7-e9a5a4d74d13" contentUrl="" testdescription="Microsoft Connectivity Analyzer checks host autodiscover.mydomain.ru to redirect HTTP to autodiscover service." resultdescription="Microsoft Connectivity Analyzer was unable to get an HTTP redirect response for the Autodiscover service." additionaldetails="An HTTP 403 Forbidden response was received. This response was sent by Unknown. Response Body: HTTP Response Headers: X-FEServer: SW-MAIL16-01 Content-Length: 0 Date: Mon, 04 Sep 2023 16:31:09 GMT Server: Microsoft-IIS/10.0 X-Powered-By: ASP.NET "elapsedMilliseconds="368">

Get-OutlookAnywhere:

Identity                           : MAIL10\Rpc (Default Web Site)

ExternalHostname                   : mydomain.textile.ru

InternalHostname                   :

ExternalClientAuthenticationMethod : Basic

InternalClientAuthenticationMethod : Ntlm

IISAuthenticationMethods           : {Basic, Ntlm}

Identity                           : MAIL16\Rpc (Default Web Site)

ExternalHostname                   : mydomain.textile.ru

InternalHostname                   : mail16.local.mydomain.ru

ExternalClientAuthenticationMethod : Basic

InternalClientAuthenticationMethod : Ntlm

IISAuthenticationMethods           : {Basic, Ntlm}

Mobile mail clients on phones work fine for everyone, both in 2016 and 2010. The problem is only with Anywhere.

Thank you.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2023-09-06*

Sounds like the old ambiguous URL issue perhaps:

https://techcommunity.microsoft.com/t5/exchange-team-blog/ambiguous-urls-and-their-effect-on-exchange-2010-to-exchange/ba-p/593809
