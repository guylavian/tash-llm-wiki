---
title: "Exchange in two different sites"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/287308/exchange-in-two-different-sites
question_id: 287308
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange in two different sites

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/287308/exchange-in-two-different-sites (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all, I am unsure about best practise, and I would like to get your opinion. We have two different sites in two different countries. Each site has its own subnet. But there is only one AD domain, one public domain and one Exchange 2016 Server (CU19) in our network. (typical branch situation - Site to Site VPN between the sites). Now the users in the second site complain about slow connection to the mailbox in Outlook. So I would like to install a second mailserver in the branch office. I suppose the way to go is the "Database Availability Group" Sending and receiving mails should be done thru the mail server located in the first site. But how can I reach the goal that the branch office users automatically choose the local server and the users in the First site also chooses their local server? Will DNS be my friend? Or do I miss something? Maybe DAG isnt't the way to go. Is it maybe better to work with a second database and send them thru the primary site? Users: First site around 65, Second site: 15 Thanks for your help. Best regards, Bernhard

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-25*

If I understand you right, it could help to split our database on my primary Exchange: One for the users in the first site, and one for the users in the second site. And this new database I could try to synchronise with DAG.  

But for this: If I go to the second site as visitor, will I be able to access my non synced mailbox then?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-02-25*

You could try it, but like I said, if you are seeing issues with outlook clients, you may have issues with a DAG and make things worse.    

https://learn.microsoft.com/en-us/exchange/high-availability/plan-ha?view=exchserver-2019#:~:text=Each%20DAG%20must%20have%20no,can%20be%20added%2C%20as%20needed.    

Regardless of their geographic location relative to other DAG members, each member of the DAG must have round trip network latency no greater than 500 milliseconds between each other member. As the round trip latency between two Mailbox servers hosting copies of a database increases, the potential for replication not being up to date also increases. Regardless of the latency of the solution, customers should validate that the networks between all DAG members is capable of satisfying the data protection and availability goals of the deployment. Configurations with higher latency values may require special tuning of DAG, replication, and network parameters, such as increasing the number of databases or decreasing the number of mailboxes per database, to achieve the desired goals.    

Round trip latency requirements may not be the most stringent network bandwidth and latency requirement for a multi-datacenter configuration. You must evaluate the total network load, which includes client access, Active Directory, transport, continuous replication, and other application traffic, to determine the necessary network requirements for your environment.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-25*

Maybe I should be mor specific related to our connection speed. The two sites are connected with 200mbit - Fiber. It's not that bad. But the lag between the two "datacenters" is 48ms. So the connection could be better.  

Will this delay cause trouble when I install a DAG?  

Best regards, Bernhard

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-25*

Hi @BECK Automation   ,    

Agree with what Andy said.    

I think the first consideration is whether you could improve the network conditions between the two sites. The network has a great influence on the Outlook connection speed. And DAG also has certain requirements for network delay.    

If you install a second Exchange server in the second site, you could consider migrating user mailboxes of users in the second site to the second Exchange server. According to my test, because of both Exchange servers in the same domain, users can still share information such as Free/Busy information and mail tracking logs.    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-02-24*

Honestly, if the connection is too slow for users in Outlook Cache mode, you can't really use  a DAG either since the replication will most likely be impacted and impact other traffic.  

If you can't increase the bandwidth between the sites, consider simply building a separate DAG with a minimum of 3 servers in each site  ( 2 DAGS in the org)  

Each user base connects to their local server.  

With 15 users....hmm, prob not worth a DAG in each site. How about a single stand-alone server in the site with 15 users?   

So one server in one site, and another server in the other site - No DAG. and ensure you are getting backups.
