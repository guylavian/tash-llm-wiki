---
title: "\"Branch\" office access to HQ files, Exchange, etc - best practise and recommendations"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/202142/branch-office-access-to-hq-files-exchange-etc-best
question_id: 202142
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# "Branch" office access to HQ files, Exchange, etc - best practise and recommendations

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/202142/branch-office-access-to-hq-files-exchange-etc-best (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, we are a small cosmetic company, 250 employers with about 150 users distributed equally across two sites. Sites are connected with ipsec vpn. Wan links are FTTH (optical fiber) 100/30 Mbps (just activated, until yesterday we had vDSL links). Currently my datacenter is only in site A (HQ site). Site B (grown over time) users connect to services through RDP with remote desktop services. Due to our ERP old architecture I cannot do withouth rds services but I'd like, for a better user experience with services like file, print and Outlook, to make users directly use their PCs. So, I was thinking at a solution like this:  

-  Create an AD site "B"  

-  Put in the site B rack an host with esxi on which power up a DC (not read only dc), a file and print server, a dhcp server.  

-  create a dfs name space with my currently mapped shares (now shares are directly mapped with \server-name\share).  

-  setup dfsr across sites for these shares, with primary replication on site A and secondary site B.  

-  let Outlook clients connect directly to my Exchange server located in site A: cached mode or online mode (I'm worried about link saturation...)? Now with RDS they are used to work in online mode.  

-  RDS will remain in place to keep ERP software being used by my remote users.  

Is this a suitable solution? I like simple but functional approaches. Any suggestions or recommendations?  

Thank you,  

Francesco.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-12-18*

Hi @BK IT Staff  ,    

Welcome to Microsoft Q&A forum.    

According to your description, seems that your solution involves multiple products at the same time. Please kindly understand that engineers here may mainly research their own field and know few about others, for example, I mainly focus on general issues about Outlook desktop client here. So, I tried to discuss about your problem from the perspective of Outlook client.    

I tried to contact the colleagues of Exchange Team, we discussed about your issue and found that the solution you mentioned `let Outlook clients connect directly to my Exchange server located in site A: cached mode or online mode (I'm worried about link saturation...)? Now with RDS they are used to work in online mode.` is indeed available. As for cached mode or online mode, Cached Exchange Mode gives users a seamless online and offline Outlook experience by caching the user's mailbox and the Offline Address Book (OAB) locally. While Online Mode works by using information directly from the server, the mailbox data is only cached in memory and never written to disk. Usually, we recommend using Cached Exchange Mode for better experience. You could learn more information about Outlook Cached Exchange Mode and Online Mode from here.    

Hope this can be helpful.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
