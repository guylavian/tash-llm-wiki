---
title: "ActiveSync email account by Microsoft 365 within a hour into not Synchronizing status ?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/165711/activesync-email-account-by-microsoft-365-within-a
question_id: 165711
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-online", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ActiveSync email account by Microsoft 365 within a hour into not Synchronizing status ?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/165711/activesync-email-account-by-microsoft-365-within-a (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

MX account created SyncActive for  Outlook  by Microsoft 365   

```
- working well at start moment Computer power on , 

          - few hours online later , failed to send, receive email when other device tested alright ?
```

Sincerely

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-11-26*

@BleuOisou-3552       

This doesn't mean EAS supported only MOBILE. Based on my knowledge, for some other mail systems and accounts, it's also supported to synchronize with Exchange ActiveSync in Outlook. However, for Exchange, EAS connection doesn't provide all the features of a standard connection to Exchange. So Outlook doesn't support this method to connect to Exchange. This is also mentioned in the official document (provided in previous reply):    

    

If your organization uses on-premises Exchange or Exchange Online, Autodiscover is more suggested. We just have to enter the account and password, Autodiscover service configures the user profile settings automatically. For your reference: How To Add An Exchange Account To Microsoft Outlook (Desktop).    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-24*

ActiveSync exch account at Outlook updating seen, just none Emails in no folders?    

https://social.msdn.microsoft.com/Forums/office/en-US/b95b33bc-104a-4afc-adcf-a53bf8405ede/activesync-exch-account-at-outlook-updating-seen-ju… 3/4    

Thank you LydiaZhou  caring this to return and advising resources  :     

missed your 7 days before replying , today just got notice to writing you here.  Some functions for this new migrated from social.technect.microsoft.com need time to test and work well understood.     

"    

Exchange ActiveSync is used for mobile devices, and Outlook for windows doesn't    

support to use EAS to connect Exchange. In general, we suggest to setup your    

account with Autodiscover." by Expert Community Zhou.    

```
- My windows 10pro with EAS since office 365 years   (-> Microsoft 365)  
                      - where to use this **Autodiscover ?**
```

for enhancing THE :     

Exchange ActiveSync is a Microsoft Exchange synchronization protocol that's    

optimized to work together with high-latency and low-bandwidth networks.    

The protocol, based on HTTP and XML, lets mobile phones access an organization's    

information on a server that's running Microsoft Exchange. Exchange ActiveSync    

enables mobile phone users to access their email, calendar, contacts, and tasks,    

and to continue to access this information while they're working offline.    

See:    

https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchangeonline/exchange-activesync/exchange-activesync?redirectedfrom=MSDN    

As the Oct. 2020 caught MX EAS on windows 10 pro was not working interminably more , so created IMAP/SMTP in two profile then after ,   the EAS showing updated folders without emails in none which folders ?!    

=> Enterprise , Business , Personal , Family license at Microsoft control unclear . . .     

"EAS supported only MOBILE is not true .  On Personal 365 windows 10 pro"  was working around years well until Sept 2020 .    

As Well, em.isphost.com server on Mobile setting at "Email" app  Sync better to the desktop Outlook is true .   The server imap.isphost.com testing this couple months caught times Sync to Desk , other way direction not in Real Time is true.     

Sincerely

## Answer (community) — community member [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-11-18*

@BleuOisou-3552       

Is the mailbox created on Exchange Online?    

What does MX account mean?    

Do you mean you used Exchange ActiveSync to setup the account? If I misunderstood, please point out.    

Outlook for windows doesn't support connections to Exchange by using the EAS protocol. It's suggested to use Autodiscover to setup your account.     

You can check this for more details: Outlook doesn't support connections to Exchange by using ActiveSync and error: Log onto Exchange ActiveSync mail server (EAS).    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
