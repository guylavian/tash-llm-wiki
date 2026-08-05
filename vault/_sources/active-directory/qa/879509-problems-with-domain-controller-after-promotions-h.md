---
title: "Problems with Domain controller after promotions. How to fix 5721 event ID"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/879509/problems-with-domain-controller-after-promotions-h
question_id: 879509
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-networking-network-connectivity-file-sharing"]
answer_author_affiliations: ["Mvp"]
---
# Problems with Domain controller after promotions. How to fix 5721 event ID

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/879509/problems-with-domain-controller-after-promotions-h (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

Yesterday I promoted new DC in our domain in our one of remote site. This is migration to Windows Server 2019 so there are other DCs (about 20 on Windows 2016 and 2019).  

It was re-IPed and renamed. Before promotion I demoted old DC in that site.  

Everything was fine. I configured server did a promotion. Used IFM to make the replication faster.  

Promotion finished with success "This server was successfully configured as a domain controller"  

Then DC automatically rebooted. Once up I was not able to log into it via RDP or HyperV console.   

I am receiving "The sign-in method you're trying to use isn't allowed. For more info. contact your network administrator"  

I use my Domain Administrator account, I am able to log in with this account to any other DC in domain.  

Ok, I thought that IFM went wrong and get rid of this server, cleared metadata and prepared new server. This time I replicated AD DB from another DC.  

Unfortunately after the restart I have got the same problem.  

Was able to log into this DC in DSRM mode and noticed that all AD and DNS services are not working. When I tried to run these I wasn't able.  

There are events created NETLOGON 5721 each time I try to run AD DS.  

"The session setup to the Windows Domain Controller name for the domain name failed because the Windows Domain Controller does not have an account for the computer computer name."  

DNS doesn't want to start (event ID 7001) and says that it depends on NTDS service which failed to start.  

I have checked and there is computer object in AD for DC correctly placed in DC OU. There are no other AD objects with the same name.  

I was not able to find the solution for this issue. Since it happend twice I believe preparing third server without solution doesn't make sense.  

This is not related for sure to GPO "Allow users to log on locally" I checked and there is Administrator group. As well tried to add my account directly.  

Any ideas appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-06-08*

Thanks for suggestions. I am going to try to promote DC in different site in the meantime to check if this is not site related and get back to you with findings.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-06-08*

Hello    

Thank you for your question and reaching out. I can understand you are  having issues  related  to event ID 5721 on new Domain controller.    

Please note this can happen if AD replication is not completed or in-progress,    

-  Please try to run AD replication status tool to verify AD replication health of all your 20 Domain controllers.    

https://www.microsoft.com/en-in/download/details.aspx?id=30005    

-  Please verify Date and Time should be synced with PDC.    

3 .Please check on new Domain controller DNS ip should be of your Primary DC and not of Firewall or Router IP.    

-  Disable any Antivirus program or Windows firewall you may have for temporary purpose.    

-  Please AD Site and services and verify IP subnet is defined    

-----------------------------------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept as answer--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-06-07*

Maybe this one.    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/user-profiles-and-logon/interactive-logon-isnt-allowed    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2022-06-07*

Hi  

Our AD functional level is 2016. There is already one DC on Windows server 2019.  

I used repadmin tool and replication was running smoothly.  

I don't see any other sights of issues.

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2022-06-07*

I'd check the domain health is 100% before making any changes or adding new domain controllers (dcdiag, repadmin tools). Also note; The two prerequisites to introducing the first 2019 or 2022 domain controller are that domain functional level needs to be 2008 or higher and older sysvol FRS replication needs to have been migrated to DFSR  

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
