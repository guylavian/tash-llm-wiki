---
title: "ADCS Standalone Offline Root CA - CDP/AIA only http location (no LDAP location)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1185794/adcs-standalone-offline-root-ca-cdp-aia-only-http
question_id: 1185794
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
---
# ADCS Standalone Offline Root CA - CDP/AIA only http location (no LDAP location)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1185794/adcs-standalone-offline-root-ca-cdp-aia-only-http (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

First post here, so please be kind =)

Short story:

Anybody know if in a 2-tier ADCS environment problems are to be expected if, for the Root CA, no LDAP based CDP/AIA locations are defined? Our environment would only support http based CDP/AIA for the Root CA. Issuing CAs can and will be integrated into AD/LDAP as ADCS Enterprise CAs.

What to do about Certutil -setreg CADSConfigDN “CN=Configuration, DC=Domain, DC=com” on the Root CA If I want to NOT have any LDAP/DS integration for the Root CA? Simply set it with a dummy value or not run it at all? And then later before issuing downlevel CA certificates, remove all unwanted CDP/AIA entries in the Root CA properties, only leaving a file based CDP entry (not added to certificates, only to retrieve the CRL files for manual or scripted publication) plus a http based one for CDP and AIA to be added to issued certificates?

Long story:

I am laying out the design for our future 2-tier Multi-Corp PKI and end up with some questions that seem a bit difficult to find answers for.

We want to have a single offline standalone Root CA signing the Certs for multiple Enterprise CAs, each responsible for their respective Corp AD Forest. The AD Forests are not interconnected in any way (no trusts, no knowledge, partially even no network paths).

The net result of this is, that setting up a single LDAP based CDP/AIA location for the Root CA in one of the participating forests and having the other forests access this location is a no-go. Adding multiple LDAP locations is, for multiple reasons, a bad idea : a) every Issuing Enterprise CA would have all locations noted/stored in their respective Certs, b) the list of locations can and will grow with adding participating Corps, c) CRL timeout will probably be reached for locations not within the first two or 3 entries, d)...many more downsides.

So the logical conclusion for me is, to only have a single http based CDP/AIA location for the Root CA that is reachable by all Forests/participants. Just as if the PKI were a classic "non-ad-integrated" one. 

Anybody having any experience with such thing? Root CA in "classic http only CDP/AIA location" mode, Corp/Enterprise Issuing CAs in "ADCS LDAP plus http CDP/AIA location" mode?

Any certificate inspection done by non-AD-integrated endpoints/cert handlers will surely work as ever, as they do http only anyways. But what about ad-integrated endpoints/cert handlers doing cert inspection? Are there any cert handlers that support LDAP only? Or is a fallback during CRL/AIA receival to http to be expected all-and-anywhere? I would suppose so, right?

Thanks a lot for your help in advance!

Marco

## Answer (community) — community member

*upvotes: 0 · updated: 2023-12-07*

I have same question. We have a strange problem about 801.x PEAP Auth and I am suspect on it. MS have not find the problem source yet.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-03-03*

Does somebody know of any specific AD-integrated endpoints/certificate handlers (Exchange, SQL, Kerberos, things like this come to my mind) that might have problems with "http only" CDP/AIA retreival? Google is not much of a help with this - at least not with what I used as search terms so far...

Thanks in advance =)

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-02*

Hi,

I'd be happy to help you out with your question. Sorry for the inconvenience caused.

In a 2-tier ADCS environment, it is possible to have a Root CA without LDAP-based CDP/AIA locations defined. In this case, the Root CA would only support http-based CDP/AIA. However, this may cause issues for AD-integrated endpoints/certificate handlers that rely on LDAP-based CDP/AIA. It is recommended to test and validate the environment thoroughly before implementing it in production.

If you do not want to have any LDAP/DS integration for the Root CA, you can either set the Certutil -setreg CADSConfigDN "CN=Configuration, DC=Domain, DC=com" with a dummy value or not run it at all.

When issuing down-level CA certificates, you can remove all unwanted CDP/AIA entries in the Root CA properties, leaving only a file-based CDP entry (not added to certificates, only used to retrieve the CRL files for manual or scripted publication) and a http-based one for CDP and AIA to be added to issued certificates.

It is important to note that some AD-integrated endpoints/certificate handlers may rely on LDAP-based CDP/AIA and may experience issues if they are not present. It is recommended to thoroughly test and validate the environment before implementing it in production to ensure that all endpoints/certificate handlers can access the necessary CDP/AIA locations.

For more Information please refer to Configure the CDP and AIA Extensions on CA1 - Microsoft Learn :- https://learn.microsoft.com/windows-server/networking/core-network-guide/cncg/server-certs/configure-the-cdp-and-aia-extensions-on-ca1

If you have any other questions or need assistance with anything, please don't hesitate to let me know. I'm here to help.

If the reply was helpful, please don’t forget to upvote or accept as answer, thank you.
