---
title: "Exchange database in ILLEGAL state. Not DIRTY. Shadow copy checksum error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/131062/exchange-database-in-illegal-state-not-dirty-shado
question_id: 131062
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange database in ILLEGAL state. Not DIRTY. Shadow copy checksum error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/131062/exchange-database-in-illegal-state-not-dirty-shado (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My server has been refusing to mount its only database; after checking it I didn't find the dirty state I expected to find. Instead it was in illegal state. At the end of the report there was something about shadow copies, which reminded me I recently enabled shadow copies on all servers on to be a little more safe but in this case it seems to have backfired.

Here's what the report showed:  

Not finding much about it online I proceeded as if it were a dirty state:

Which, TBH it's not really clear, 'cause very time somebody asks this, another person would respond with a link with some documentation that explains a little bit but leaving out huge gaps, referring to yet more links where you have to guess which is it from non-matching or all vaguely-related choices making a strong case for neither, or something like that. Microsoft's documentation besides not included with the product if it were any good, I wouldn't be here. It's another set of never-ending linking for missing pieces of a whole. I already went through it.

I then tried using the shadows copies: I restored the first three but none worked.

Next I tried deleting the log files to attempt recovery without them, it didn't work.

I restored it one last time just to undo the mess but it's obviously still not mounting.

I thought about creating a new database but last time something similar happened it was too confusing to restore recovery databases and all that I didn't want to go thought that again --that in the end it sort of fixed itself when I ignored it and just used the newer one, things sort of reappeared after some days enough for a chance to migrate them.

I have avoided anything other than just mounting the database, like mailbox migrations or things that could spread the damage. So basically just work within the server's filesystem and that's it.

Out of ideas that's when I came here,

[before I finish though, a personal observation]  

> To login here I was asked to input confirmation by entering a code sent to my email--not working--so I scrambled: I opened Apple Remote Desktop, logged into a macOS Server machine and enabled all of my domain for email, and started the malware databases downloads, I switched to Microsoft Remote Desktop to the Exchange server which has a DNS shortcut and edited the DNS, then my public DNS, added the new IMAP account, and went to the browser to resend the confirmation which arrived instantly. This took about 5 minutes even with all the logging in to multiples servers which begs the question: what is it so special about Exchange again? It's always failing for some reason, it uses and ungodly amount of resources and wears disks like nobody's business and it's expensive, the most expensive product we've ever gotten for email actually, that don't even include documentation. I'm crossing my fingers after each shutdown, even planned ones.  

> The mac mini handling email for all of the domains has I believe 6GB of RAM, can't have than 8GB, it's old, it's vastly underpowered compared to Exchange's server and it efficiently handles email, calendaring, contacts, IM, a freaking directory server (though instead it connects to Active Directory) while still keeping low resource use and still being usable as a desktop--if it had something attached to it that is, it was being used for as a NetInstall (Apple's spin on PXE) server so it's headless.  

> Being an Office365 tenant, accidentally enabled Exchange Online for a bit once and when I saw the difference in OWA online and on-prem it felt like an insult. On-prem customers are an afterthought to Microsoft, from whom they still gather data, nevertheless.

>

so, I guess that's it. Almost forgot: this happened after a planned reboot because memory was upgraded in a couple of hypervisors and opted to shut down every server to prevent too many migrations. It was orderly.

There's only one external snapshot of Exchange but it was done after the problem occurred, as a safety measure for complications resulting from using built-in snapshots (shadow copies)

Thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-20*

Have you read this thread : https://social.technet.microsoft.com/Forums/en-US/5555f9a9-25d7-4d2e-be43-5abae4cfa992/restoring-exchange-backup-on-sbs2003?forum=exchangesvravailabilityandisasterrecoverylegacy   

Did you find any errors in Event Log that indicates what happens to your database?  

See if you can find out the reason that leads to database not mounted from those events, such as hardware issues?  

If an Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in [our documentation][1] to enable e-mail notifications if you want to receive the related email notification for this thread.
