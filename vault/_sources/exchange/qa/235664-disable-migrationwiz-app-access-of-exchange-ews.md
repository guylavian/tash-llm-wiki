---
title: "Disable Migrationwiz app access of Exchange EWS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/235664/disable-migrationwiz-app-access-of-exchange-ews
question_id: 235664
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Disable Migrationwiz app access of Exchange EWS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/235664/disable-migrationwiz-app-access-of-exchange-ews (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello forum,  

In our Exchange organization we have Exchange web services (EWS) enabled for all users. Some users tried migrationwiz app to export the mailbox illegally and found succeeded. We want restrict migrationwiz app from accessing Exchange server using EWS. We tried set-casmailbox -identity username -Ewsenabled:$false command and found its breaking mailbox and disabling Out of Office notification and mailtip. Can anyone give me right way to block migrationwiz app using EWS?  

Thanks,  

Kannan

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-20*

Hi Eric,  

I want to add migrationwiz app to the block list and don't know what the value is for migrationwiz app. I mean what value do I need to add for the app Migrationwiz to the EWSBlocklist? How do value defined and where the value taken from? Please let me know if my question is still not clear.   

Thanks,  

Kannan

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-20*

Hi Eric-Yin,    

Thanks for the EMS commands that you sent. I have a question here, if I allow only "owa/" all other apps are blocked? Why I ask this question is I enable only "owa/" and enabling that would block other apps that means migrationwiz will also be blocked. I don't know what I have to put on the application name for migrationwiz.    

Set-Casmailbox tony@Company portal   .com –EWSApplicationAccessPolicy:EnforceBlockList –EWSBlockList:"Migrationwiz/*"?    

Thanks,    

Kannan

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-20*

As michev suggests, you can try the following command for specific user to block specific app:    

```
Set-Casmailbox ******@contoso.com –EWSApplicationAccessPolicy:EnforceBlockList –EWSBlockList:"Mac+OS+X/*"
```

Or if you want, block all EWS application for a user:    

```
Set-Casmailbox ******@contoso.com –EwsEnabled $false
```

Only the speficied application is allowed to access the mailbox:    

```
Set-Casmalbox ******@contoso.com -EwsApplicationAccessPolicy:EnforceAllowList -EwsAllowList:"Mac+OS+X/*"
```

Reference like: https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/how-to-control-access-to-ews-in-exchange    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-19*

Hi Michev,  

I understand that we can block specific app using user level or org-wide. But can you help me how to block migrationwiz or any other app at the user level. That is the basic requirement. you second comment is true, there is no point in blocking ews where we have given the mailbox access to the outlook and their mailbox items are usable by particular user.  

Thanks for your prompt reply and it helped.   

Thanks,  

Kannan

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-01-19*

You can toggle it off on a per-user basis via Set-CasMailbox. You can also block specific apps by using the corresponding parameters (EwsAllowList/EwsBlockList), either on per-user or org-wide basis.  

End users will not be able to export anything other their own mailbox though, which they can already do via Outlook. To export other users data, they will need EWS Impersonation permissions, and if they have those, you have bigger problems to worry about :D
