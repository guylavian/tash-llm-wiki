---
title: "Cannot login to Domain Controller because \"Domain isn't available\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/482526/cannot-login-to-domain-controller-because-domain-i
question_id: 482526
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 2
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Cannot login to Domain Controller because "Domain isn't available"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/482526/cannot-login-to-domain-controller-because-domain-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,     

When trying to login to the Domain Controller, the following error is displayed.     

We can't sign you in with this credential because youd domain isn't available. Make sure your device is connected to your organization's network and try again. If you previously signed in on this device with another credential, you can sign in with that credential.     

    

This issue occured after a reboot  I did on the Server.     

The Windows Server OS is 2019.     

Please for your assisstance and thank you beforehand.     

KR     

Kostas

## Answer (community) — community member

*upvotes: 1 · updated: 2023-09-18*

changing the ip to a static on client machine worked for me on this issue

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-13*

I am using DC 2003, and sharing folder server OS is windows storage server 2016,user want access share folder from OS 2016 to window 10 os  system

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-07-26*

Just checking if there's any progress or updates?  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-07-21*

Hello @mousmoulisKostas  ,

Thank you for posting here.

Hope the information provided by DSPatrick is helpful.

If it does not work, please confirm the following information or troubleshoot as below:

1.If your AD forest is a single forest with single domain?  

2.Do you have other DCs in this domain?  

3.If you have multiple DCs in this domain, please check if you can log on other DC with this credential.  

4.Have you logged on this DC using other domain Admin credentials, if so, you can try other domain Admin credentials to log on this DC to see if it helps.  

5.Check if this DC is virtual machine or physical machine? Please check if the network cable is intact and plugged in.  

6.At last, you can reboot the DC again to check if the issue disappears or persists.

Hope the information above is helpful to you.

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-07-20*

Are there other domain controllers? If not then try F8 at startup and log on DSRM mode to see what might have happened.    

    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
