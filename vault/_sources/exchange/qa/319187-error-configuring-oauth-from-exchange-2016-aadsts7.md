---
title: "Error configuring OAuth from Exchange 2016 (AADSTS700027)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/319187/error-configuring-oauth-from-exchange-2016-aadsts7
question_id: 319187
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Error configuring OAuth from Exchange 2016 (AADSTS700027)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/319187/error-configuring-oauth-from-exchange-2016-aadsts7 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I'm in the process of configuring OAuth from en on-premises Exchange 2016 CU19+ install to in order to have calendar integration within Microsoft Teams.  

The HCW wizard has completed successfully, but no calender tab is visible within the Teams client (thick or web - same issue).  

I've tested with   

```
Test-OAuthConnectivity -Service EWS -TargetUri https://outlook.office365.com/ews/exchange.asmx -Mailbox ******@localdomain.tld
```

And the error is  

AADSTS700027: Client assertion contains an invalid signature. [Reason - The key was not found., Thumbprint of key used by client: xxxxxxxxx  

I've tried verifying the certificate used for OAuth and it looks OK.  

Running this command I've saved the certificate and compared it to the thumbprint from get-authConfig - they match and have not expired  

```
Get-MsolServicePrincipalCredential -ServicePrincipalName "00000002-0000-0ff1-ce00-000000000000" -ReturnKeyValues $true
```

I'm kind of stumped as to how to solve this issue.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-03-17*

Run through the troubleshooter:    

https://learn.microsoft.com/en-us/microsoftteams/troubleshoot/known-issues/teams-exchange-interaction-issue    

and test here:    

https://testconnectivity.microsoft.com/tests/TeamsCalendarMissing/input

## Answer (community) — community member

*upvotes: 0 · updated: 2021-03-18*

Check below links may help:    

https://github.com/pnp/cli-microsoft365/issues/1532    

https://learn.microsoft.com/en-us/exchange/troubleshoot/administration/exchange-oauth-authentication-could-not-find-the-authorization    

https://social.technet.microsoft.com/Forums/windows/en-US/58249c8d-c8be-4b28-88fe-a23899d1b8d3/server-error-code-invalidclient-description-aadsts700027-client-assertion-contains-an?forum=Exch2016SD

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-17*

Doing the invoke-restmethod failed, but I've tried the same URI from a regular browser, and that completes as expected    

    

I was looking through the next step, https://testconnectivity.microsoft.com/tests/TeamsCalendarMissing/input    

but cannot quite figure out how to do it as I have NO on-line mailboxes. Only On-premises.    

We actually do not need the hybrid configuration - only OAuth, but that is the supported way of configuring it so we completed the HCW.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-17*

Hmmm, I wonder if you should open a ticket with 365 support. I havent seen that one before

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-17*

Wow! That was quick.    

I've already tried the test connectivity, and that gives the following error    

The specified user mailbox is marked as undiscoverable by the Teams middle-tier service.    

Running through the troubleshooting tips from https://learn.microsoft.com/en-us/microsoftteams/troubleshoot/known-issues/teams-exchange-interaction-issue    

I get to step number two    

Invoke-RestMethod -Uri "https://autodiscover.domain.tld/autodiscover/autodiscover.json?Email=mymailbox@keyman  .tld&Protocol=EWS&RedirectCount=5" -UserAgent Teams    

Running it from a computer within the domain I get the following error    

    

Running the same command from a computer outside of the windows domain, it completes as expected
