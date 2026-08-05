---
title: "Unable to contact Active Directory to access or verify claim types & central policy tab missing"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/404460/unable-to-contact-active-directory-to-access-or-ve
question_id: 404460
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-high-availability-storage-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Unable to contact Active Directory to access or verify claim types & central policy tab missing

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/404460/unable-to-contact-active-directory-to-access-or-ve (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear community,    

TL;DR: two problems: Unable to contact Active Directory to access or verify claim types & central policy tab missing. Servers can reach each other when for example I ping them or search for AD users.     

I'm setting up an environment with (a.o.) a Domain Controller and File Server and am running into an issue I hope you can help with. I'm trying to use Claim Types to specify access to SMB shares but keep running into the error 'Unable to contact Active Directory to access or verify claim types'. This occurs when I try to set a condition on a folder which is used as an SMB share.     

My test setup looks as follows:    

-  Domain Controller which is also the DNS server (updated win 2019)    

-  File Server (updated win 2019)    

-  Both servers are added to a private network and can ping each other over local and public IP.     

I've followed the steps as outlined on https://learn.microsoft.com/nl-nl/windows-server/identity/solution-guides/deploy-a-central-access-policy--demonstration-steps-and also consulted https://learn.microsoft.com/nl-nl/windows-server/identity/solution-guides/appendix-b--setting-up-the-test-environment    

I've set up a Department Claim type, for now left the resource properties as they are as the departments I needed for now were already present. I created a Central Access Rule and Central Access Policy, applied the CAP through group policy, enabled support for claims, and deployed the policy.    

In the advanced security settings > add screen for my SMB share, I can reach the DC without any issues to select a principal, but in the bottom under conditions I'm getting the error 'Unable to contact Active Directory to access or verify claim types'. Oddly enough, in the advanced security settings screen of the folder also the central policy tab is missing.     

For good measure I ran gpupdate /force again, rebooted the servers, disabled the firewall on the DC, but still no luck. Does anyone have an idea where I'm going wrong?    

ps: tried to add tags that better described this topic, but anything related to smb, file server, dc seemed to not work.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-12-11*

Hello I have the same problem, Someone can help us?.

Thanks!!

## Answer (community) — community member

*upvotes: 0 · updated: 2023-12-11*

Hello I have the same problem, Someone can help us?.

Thanks!!

## Answer (community) — community member

*upvotes: 0 · updated: 2022-07-11*

I just noticed the same error on one of my two DCs running Windows 2012 R2 Std servers that share AD and "load balance" DHCP and DNS. We didn't make any changes to both servers recently and only applied Windows updates so one of them must have caused this.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-05-25*

Hi Danny,   

Thank you for taking your time to help me, I appreciate it very much :)  

I believe you've already pointed me in the right direction: Repadmin /showreps * gives me an LDAP error: LDAP error 81 (Server Down) Win32 Err 58.  

I'm a bit pressed for time today, but I'll investigate this further a.s.a.p. to see if something is wrong with the LDAP server and will post the results back.  

regards,  

Steven

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-24*

Hi,    

Please try these commands first:    

Dcdiag /v >c:\dcdiag1.log     

Repadmin /showrepl >C:\repl.txt    

Repadmin /showreps *    

If any error pops out, please provide us with the screenshots.    

Thanks for your understanding.    

Best regards,    

Danny    

-----------------------------    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
