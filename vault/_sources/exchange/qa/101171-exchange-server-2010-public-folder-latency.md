---
title: "exchange server 2010 public folder latency"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/101171/exchange-server-2010-public-folder-latency
question_id: 101171
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# exchange server 2010 public folder latency

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/101171/exchange-server-2010-public-folder-latency (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hello guys,  

i need your advise with the below:  

i have one exchange server 2010 with many public folders under one pf database.  

all the pfs are configured the same way, the only difference is the users permissions.  

im facing the following issue on just one pf, emails sent to this pfs are delayed like sometimes they are delivered after 15mins.  

users are complaining on this behavior, and the issue is just with this public folder.  

any ideas dears?  

thank you

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-09-23*

dears,  

after several troubleshooting, i create a new one and same issue occured.  

i realized that if the dbs are mounted on exch2010-1 member of my dag, users sending emails to pfs will have issue and latency.  

however, if i switch my dbs to the second member emails sent to pfs will not face a latenct issue.  

in addition, all my db copies are healty.  

so what could be thenissue?  

how can i proceed with the troubleshooting?  

what could be the issue from one member to the other  

thank you in advance

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-09-22*

If the issue is just one Public Folder, I would not even bother troubleshooting this.  

Create a new Public Folder and mail-enable it with a new SMTP address.   

Send a message to that new public Folder.  

If it arrives quickly as expected, move the items in the current folder to the new one.  

Remove the email addresses from the bad folder that is slow and mail-disable it.  

Add those email addresses to the new folder.  

Rename the old folder to something to indicate its not used anymore or delete it.  

Name the new folder the same as the old

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-22*

Hi @eg1995   ,  

In order to better solve the issue, I need to ask some questions.  

Did you changed any settings before this issue occurred?  

Only one user have this issue or all users have?  

Will this issue occur when using the same user to send mail to another public folder?  

Please following the steps and see if the issue is resolved:  

-  Please run the following command to check the size of all items in the public folder. By default the public folder quota is 2GB. If the quota used is close to 2GB, it may affect the performance of the Public folder.    Get-PublicFolderStatistics | Format-List  

2.Pease send a test email to public folder and then run the following command to view which step took longer.

```
Get-MessageTrackingLog -start <> -End <> -Sender <> | fl
```

  

3.You could send a test email, and then put the email header into the Message Header Anaylzer in ExRCA for analysis. If there is a delay in the transmission process, it will be displayed.  

About ExRCA: Microsoft Remote Connectivity Analyzer  

  

4.Please close the third-party anti-virus software, and run outlook.exe /safe in "Run". Please open Outlook in safe mode to send and receive emails sent to the Public Folder to rule out the possibility of add-in causing this issue.  

5.Unstable network or slow network speed could also cause slow mail sending. Please check your network.

In addition, Exchange 2010 will end support on October 13, 2020, so it is recommended that you upgrade Exchange to a higher version as soon as possible.  

For more information: Exchange 2010 end of support roadmap

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
