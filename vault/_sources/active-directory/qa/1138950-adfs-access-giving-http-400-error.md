---
title: "ADFS access giving HTTP 400 error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1138950/adfs-access-giving-http-400-error
question_id: 1138950
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 2
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS access giving HTTP 400 error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1138950/adfs-access-giving-http-400-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

I'm migrating our ADFS server from Windows Server 2012 R2 to Windows Server 2019.    

I managed to add the new server to the farm and to get it to work, but I'm getting some trouble while accessing the /adfs/ls/Idpinitiatedsignon.aspx page.    

The ADFS farm name is adfs1.company.com, access to the URL https://adfs1.company.com/adfs/ls/Idpinitiatedsignon.aspx is working fine, however we need access through https://adfs2.company.com/adfs/ls/Idpinitiatedsignon.aspx URL as well for specific reasons.    

The issue I'm facing is that the new server is throwing a HTTP 400 error whenever I try access through adfs2.company.com, and after deeper digging I found that it also throws the same error when I try accessing the URL using the server's IP address instead of the DNS name.    

I tried changing netsh http bindings (added a new bind for 0.0.0.0:443) but it doesn't seem to help.    

The ADFS URL "/adfs/ls/Idpinitiatedsignon.aspx" is only responding if accessed via localhost, hostname FQDN, or the FQDN of the ADFS farm, otherwise it throws the HTTP error 400.    

The weird thing about this is that the old server is responding to all the requests using the ADFS2 alias, server's IP address and even when using 127.0.0.1 when accessing the webpage internally, and never throwing the HTTP 400 error.    

I did a side-by-side comparison between configurations of both old and new servers and the config is matching.    

Any help would be appreciated. I'm pretty sure it's a missing config in the HTTP service but I can't point my finger to the issue.    

Thank you.

## Answer (community) — community member

*upvotes: 2 · updated: 2023-09-29*

I am having the same issue. Is there any resolution?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 2 · updated: 2023-07-16*

The page is disabled by default starting AD FS on Windows Server 2016.

You can enable it with the following command:  

`Set-ADFSProperties -EnableIdPInitiatedSignonPage:$True`

Note that the reason it is disable is because it allows anyone to see the list of SAML-2 enable relying party trust you have in your farm. IDP initiated signin are kinda old school. Do you still have apps requiring it? 

Also, you can consider using Azure AD (Entra ID) to publish your application, then no AD FS issues anymore :)

## Answer (community) — Q&A User

*upvotes: 2 · updated: 2023-07-05*

I have the same problem in Windows 2019. However, it work in Windows Server 2016.

## Answer (community) — Q&A User

*upvotes: 2 · updated: 2023-05-26*

I have the same problem on Windows 2022, is there any workaround if there isn't a solution ?

## Answer (community) — Q&A User

*upvotes: 2 · updated: 2023-04-19*

Hello,
Any news ? I have the same problem on Windows Server 2022 if you have any news ;)
