---
title: "Domain Controllers Replication issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/585483/domain-controllers-replication-issue
question_id: 585483
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# Domain Controllers Replication issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/585483/domain-controllers-replication-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello  

We have been facing the below issue for a long:  

We have two Windows Server 2012 DCs. Both the DCs stopped replicating for a long time and the time exceeds more than 3 years.  

I installed/promoted another DC and followed all the steps to replicate with the 1st one but when I create a user in any of the DCs, I need to refresh, and then I can see the change. Both the DCs do not replicate automatically. I did not demote the second faulty DC.  

The second issue is when I shut down the first domain, our employees cannot access shared folders and the internet.  

All our roles are in our first DC.  

Schema Master  

Domain Name Master  

PDC  

RID Pool Manager  

Infrastructure Master  

What could be the possible solution? Please provide me as soon as possible because we do not have any redundant DC and our first DC is on a virtual machine and that server is creating some problem and can go down anytime.  

Regards

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-10-14*

We can't sign you with this credential because your domain isn't available.   

Sounds like DC2 is somehow broken. dcdiag may be useful. You could also try move roles off, demote, reboot, promo it again.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-10-13*

both the DCs are replicating manually but not automatically  

Not sure what is meant here?  

added/included the IP of the 2nd DC. Now, the issue is if I check "Network Connection Details" from Network and Sharing Center, our PCs do not achieve the IP address  

May need to do ipconfig /release, ipconfig /renew  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-10-11*

If the second server has tombstoned the only solution is to size roles (if necessary) to another healthy one    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/transfer-or-seize-fsmo-roles-in-ad-ds    

remove from network and perform clean up.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564    

and rebuild the failed one from scratch.    

Make sure the DHCP server hands out only healthy / operational domain controllers for DNS.     

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-10-11*

What command are you using to refresh the objects between the domain controllers?    

To add the new DC IP address you will need to edit your existing scopes are add the new DC IP address and remove the old one from each of the DHCP options.  I believe you are not seeing the new DC's IP address the console as you haven't installed the DHCP roll on the new DC, but you don't need to do that unless you want to setup HA\redundancy for the DHCP service.    

You will need to remove the old DC once you have resolved thse issues, as it not doing any good and will probably cause more issues in the long run.     

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

Gary.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-10-11*

Hi @Yousuf Shahzad       

If you don't force replication, do the objects replicate evenually?    

Are the DCs in separate AD sites?    

If you run repadmin /replsummary from DC1 do you get any errors reported against the new DC?    

The second issues is likely to be related to the client having only the first DC as the primary DNS entry and not being able to resolve names once the first DC is switched off. Now you have a second DC, it would best to add the IP address of the new DC as a secondary DNS entry for clients.     

Gary.
