---
title: "Temporarily allow Kerberos authentication to Windows 2003 boxes after applying November 2022 updates"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1106875/temporarily-allow-kerberos-authentication-to-windo
question_id: 1106875
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_affiliations: ["Mvp"]
---
# Temporarily allow Kerberos authentication to Windows 2003 boxes after applying November 2022 updates

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1106875/temporarily-allow-kerberos-authentication-to-windo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Please let's skip the part "what? 2003???" etc :P That's nothing into production, but I need to be able to allow communication with them for some more week if possibile.    

As you know (and if I correctly understood), November updates, I think the kb5021131 in particular for this issue, set the default enc type to AES for Kerberos authentication, if not else specified for the specific account.    

I traced the traffic between my Win 10 box and the Windows 2003, and I see the following (as you see etype is AES256 and 2003 does not support that):    

    

Then, it follows the error:    

    

My question is:    

How can I define that just for that computer account the Enc type must be RC4? Is that possible? I was looking for the "msDS-SupportedEncryptionTypes" attribute for the computer object in AD, but it has been added starting from Windows 2008. Thank you.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-05*

Did you successfully figure out how to authenticate your 2003 servers?  

We have two 2003 servers in our environment that cannot be upgraded any time soon as they run essential software that isn't compatible with newer operating systems.  Each time we have attempted to update our domain controllers since the November 2022 update, we lose connection to the 2003 servers and need to revert the domain controllers.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-12-02*

The settings here are all there is to work with regarding KB5021131    

https://support.microsoft.com/en-us/topic/kb5021131-how-to-manage-the-kerberos-protocol-changes-related-to-cve-2022-37966-fd837ac3-cdec-4e76-a6ec-86e67501407d    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-11-29*

Read on here.    

https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/network-security-configure-encryption-types-allowed-for-kerberos    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-11-29*

You may need to upgrade the operating system to something supported.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
