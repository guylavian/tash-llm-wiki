---
title: "Connect-ExchangeOnline (OAth fun)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/204156/connect-exchangeonline-oath-fun
question_id: 204156
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Connect-ExchangeOnline (OAth fun)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/204156/connect-exchangeonline-oath-fun (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good evening,  

Been going round and round with with this and must be missing something.  Seen and read plenty of articles, but the fix is not yet clear to me.  I'm hoping for a new nugget of information that might help get me over the hump (more clarity).  When I run Connect-ExchangeOnline, it takes me through the pop-ups (credentials) as it should along with the MFA prompt via device.  It then presents me with the following error.  Any advice or tips from experience would be very appreciated.  Can access the O365 portal without issue (MFA etc) and the ExchangeOnlineManagement module is definitely installed.  

Command:  

Connect-ExchangeOnline  

Error:  

New-ExoPSSession : Create Powershell Session is failed using OAuth  

Thanks much,  

CWT

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-21*

Thank you for the replies and instructions.  I could have better explained my issue, so I have updated the original thread to essentially reflect the following problem I have yet to resolve.  

Command:  

Connect-ExchangeOnline  

Error:  

New-ExoPSSession : Create Powershell Session is failed using OAuth  

Thanks,  

CWT

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-21*

@CWT      

Make sure the way that you used is correct:    

Way 1:    

-  Download "Exchange Online PowerShell Module" from Exchange Online Admin center:    

     

-  Create connection request:        Connect-EXOPSSession [-UserPrincipalName -ConnectionUri <ConnectionUri> -AzureADAuthorizationEndPointUri <AzureADUri> -DelegatedOrganization <String>]  

    

Way 2(V2 module):    

Run PowerShell with administrator privileges to install EXO V2 module    

```
Install-Module PowershellGet -Force  
Set-ExecutionPolicy RemoteSigned
```

Close PowerShell Windows, then open a new one, then run command below:    

```
Install-Module -Name ExchangeOnlineManagement
```

Connect to Exchange online with MFA(Make sure your account is enabled MFA, otherwise you will get an error)    

    

     

V1 module - Connect to Exchange Online PowerShell using MFA    

Exchange Online PowerShell V2 module    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-20*

I'm not sure how to get the Microsoft Exchange Online PowerShell Module. but you can download it directly by going to your EXO admin portal > hybrid > then click on "configure" below where it says "The Exchange Online PowerShell Module supports multi-factor authentication"    

Then it will download and you will be able to install it. But make sure you use IE browser or else it will fail with other browsers.    

Finally, you will then be able to connect to EXO-PowerShell using below cmdlets.    

Connect-EXOPSSession -UserPrincipalName admin@mathieu.company  .com    

if you're already connected to your exo admin portal from the browser, it will automatically sign you in without prompting you to the MFA page. Hope that help.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-12-19*

If will help if you share the exact cmdlet you are using to connect. New-ExoPSSession is an internal cmdlet, you should not be using that. Use Connect-ExchangeOnline instead.
