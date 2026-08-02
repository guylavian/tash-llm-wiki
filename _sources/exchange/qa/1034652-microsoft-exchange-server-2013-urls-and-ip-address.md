---
title: "Microsoft Exchange server 2013 URLs and IP address ranges"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1034652/microsoft-exchange-server-2013-urls-and-ip-address
question_id: 1034652
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Microsoft Exchange server 2013 URLs and IP address ranges

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1034652/microsoft-exchange-server-2013-urls-and-ip-address (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Team     

Our project is planning to Block the internet for our exchange servers , Hence i would like to inform to my security team to provide the URLs and IP address ranges to be whitelisted from there end .     

For Office365 i have found the article - https://learn.microsoft.com/en-us/microsoft-365/enterprise/urls-and-ip-address-ranges?view=o365-worldwide    

but i did not able to find the similar article stating about Microsoft exchange servers 2013 , Can you please help with the above request and provide me the URL's & IP Address ranges so it wont create any disruption post internet blockage     

Regards    

Naga sai

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-05*

@Nagasai Andra      

Here are ports that Exchange 2013 used: Network ports for clients and mail flow in Exchange 2013    

About the IP address is decided which IP address that you need to access your Exchange server from.    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".     

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-10-04*

ITs the same IPs for all Exchange Versions, so it will work with 2013 as well If you are in hybrid mode:     

    

and for port 25:

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2022-10-04*

Hi,    

I think you can check this link and details on the ports, services that require connectivity over the network - network-ports    

Hope this helps.    

==    

Please "Accept the answer" if the information helped you. This will help us and others in the community as well.
