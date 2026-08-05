---
title: "Active Directory Sites & Services throws errors with link-local addresses"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/164731/active-directory-sites-services-throws-errors-with
question_id: 164731
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory Sites & Services throws errors with link-local addresses

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/164731/active-directory-sites-services-throws-errors-with (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good afternoon, all!  

I've been tasked with, among other things, cleaning and verifying a customer's ADSS structure. It's basically sound, but I found some events  showing where NETLOGON throws an error NO_CLIENT_SITE that refers to a link-local address.   

I don't know how this would happen, but I don't think it's anything wrong with ADSS. Looking if anyone has had similar events and perhaps some insight into how ADSS would have picked up on these. Don't think   

Thanks to all for looking!  

Gregg

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-11-16*

This particular one is Server 2019. The domain is 2008R2, which we are working to update. Hence, the cleanup.....

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-11-16*

What operating system is installed on this domain controller?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-11-16*

Hello, DSP!  

Here's the text from the Event Log. The Event Source is NETLOGON and the EventID is 5807:  

Warning	11/11/2020 13:31	NETLOGON	5807	None	During the past 4.21 hours there have been 9 connections to this Domain Controller from client machines whose IP addresses don't map to any of the existing sites in the enterprise. Those clients, therefore, have undefined sites and may connect to any Domain Controller including those that are in far distant locations from the clients. A client's site is determined by the mapping of its subnet to one of the existing sites. To move the above clients to one of the sites, please consider creating subnet object(s) covering the above IP addresses with mapping to one of the existing sites.  The names and IP addresses of the clients in question have been logged on this computer in the following log file '%SystemRoot%\debug\netlogon.log' and, potentially, in the log file '%SystemRoot%\debug\netlogon.bak' created if the former log becomes full. The log(s) may contain additional unrelated debugging information. To filter out the needed information, please search for lines which contain text 'NO_CLIENT_SITE:'. The first word after this string is the client name and the second word is the client IP address. The maximum size of the log(s) is controlled by the following registry DWORD value 'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters\LogFileMaxSize'; the default is 20000000 bytes.  The current maximum size is 20000000 bytes.  To set a different maximum size, create the above registry value and set the desired maximum size in bytes.  

And the log snip from netlogon.log:   

10/08 06:52:04 [2748] CLIENT DOMAIN: NO_CLIENT_SITE: USER1 169.254.218.179  

11/09 05:35:37 [2732] CLIENT DOMAIN: NO_CLIENT_SITE: USER2 169.254.172.57  

11/09 05:35:38 [2732] CLIENT DOMAIN: NO_CLIENT_SITE: USER2 169.254.172.57  

11/09 08:37:03 [2732] CLIENT DOMAIN: NO_CLIENT_SITE: USER3 169.254.204.30  

11/09 08:37:04 [2732] CLIENT DOMAIN: NO_CLIENT_SITE: USER3 169.254.204.30  

11/09 08:40:45 [7348] CLIENT DOMAIN: NO_CLIENT_SITE: USER3 169.254.204.30  

11/09 08:40:45 [2996] CLIENT DOMAIN: NO_CLIENT_SITE: USER3 169.254.204.30  

Thanks!

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-11-16*

Do you have a screenshot? What process or action is reporting the error?
