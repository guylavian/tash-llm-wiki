---
title: "Kerberos Re-Auth with Smart Card"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/898182/kerberos-re-auth-with-smart-card
question_id: 898182
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-devices-deployment-config-app-groups", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-devices-deployment-config-app-groups", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Kerberos Re-Auth with Smart Card

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/898182/kerberos-re-auth-with-smart-card (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Our site uses Smart Cards to login to our domain.  Before the January patches that prevents NTLM fallback everything worked fine.  After those patches certain users are having to re-auth to access network resources.  Its not everyone, just a subset of users.  One of the problems is that it has been drilled into our users to remove the smart card after they login.  90% of our users do this.      

Users are complaining that they are being prompted to put in their smartcard to re-auth when this happens.   We have had meetings with Management as well as a couple of calls to Premier Support.  Supports answer is easy and works.  Leave the smart card in since that is what its for.    

Well management does not like this answer and they want to know why it only happens to a subnet of users and not everyone.  Kerberos settings are set at the default settings.    

A couple of technical items:    

Our smart cards are mapped to several accounts including our elevated accounts and we are using named hints to choose what account we want to use.    

All laptops are using Cisco AnyConnect for VPN access from home.    

Windows 2016 Domain Controller    

2012 Functional Level    

Windows 10 clients.    

When this happens it throws an error in the event log of 40970, smart card not found.    

Anyone had any idea why a subset of users would experience this?  Microsoft said everyone should be getting this that removes the smart card when the TTL is up.  But most users are here for only 8 hours so the 10 hours never is reached.      

We also use applications where on the same laptop, we might have to sign into an app with our AD username and password, a local account and local password for the app or it might be windows pass thru for O365.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-06-23*

Hi there,    

If this issue affects a single user, the most straightforward solution to this issue is to add the user to the Remote Desktop Users group.    

If the user is already a member of this group (or if multiple group members have the same problem), check the user rights configuration on the remote Windows 10 or Windows Server 2016 computer.    

You can also try one of the following things to propagate through the issue.    

-Change your DC topology by turning off password caching on the RODC or deploying a writeable DC to the branch site.    

-Move the RDSH server to the same child domain as the users.    

-Allow users to sign in without smart cards.    

-----------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer–

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2022-06-23*

Hello CraigHuff-3236,

Thank you for posting here.

I am not sure why a subset of users would experience Kerberos Re-Auth with Smart Card.

But I have the following thoughts:

1.Based on the description "Before the January patches that prevents NTLM fallback everything worked fine.", whether you install the January patches that prevents NTLM fallback on servers or on clients? If the January patches were installed on the clients, did you try uninstall the January patches you mentioned on one test machine to see if it helps.

2.Whether you checked the "Kerberos Re-Auth with Smart Card" just occurs on the same users (a subset of users) or different users (a subset of users)?  

I mean this time they are u1,u2 and u3, they are also u1,u2 and u3 next time.  

OR maybe this time they are u1,u2 and u3, they are u2,u3 and u4 next time, and they are u3,u4 and u5 the third time.

3.Whether the the "Kerberos Re-Auth with Smart Card" just occurs on the same client computers or different clients.

4.Based on "But most users are here for only 8 hours so the 10 hours never is reached.", if some users who worked for 8 hours continues to work beyond 10 hours, whether they also experience Kerberos Re-Auth with Smart Card.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
