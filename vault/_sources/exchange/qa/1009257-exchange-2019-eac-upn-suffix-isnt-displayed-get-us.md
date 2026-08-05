---
title: "Exchange 2019 EAC - UPN suffix isn't displayed - \"Get-UserPrincipalNamesSuffix\" Command works ins EMS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1009257/exchange-2019-eac-upn-suffix-isnt-displayed-get-us
question_id: 1009257
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2019 EAC - UPN suffix isn't displayed - "Get-UserPrincipalNamesSuffix" Command works ins EMS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1009257/exchange-2019-eac-upn-suffix-isnt-displayed-get-us (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear community,    

I've already been researching on this so far but found no solution yet.    

Maybe somebody here is able to help me out.    

First a brief listing of our environment:    

Small domain, once created with SBS, currently on functional level of Server 2016; two DCs on Server 2019 with Azure AD Sync    

One On-Premise Exchange 2019    

My issue:    

when I try to manage user mailboxes within the ECP, it always throws the error "Can't find the organizational unit that you specified"    

I can change the mailboxes properties but as a follow-up of the error, I am not able to save them.    

When I check the event log, I see the following error in the MSExchange CmdletLogs: The cmdlet failed "Get-UserPrincipalNamesSuffix -OrganizationalUnit "mydomain.local/My CompanyOU"    

The very strange thing:     

when I run this on the EMS (Exchange Management Shell) it completes fine end displays the expected two UPNs    

What I tried so far:    

Checking appropriate permissions according to this article     

https://learn.microsoft.com/en-us/exchange/troubleshoot/administration/upn-suffix-not-display-eac-ems    

Setting the right WellKnownObjects attribute by "redirusr" and "redircmp" to overcome old SBS settings    

Checking the correct OU name - mine contains just a blank ("My CompanyOU") but no strange characters like as mentioned here:    

https://learn.microsoft.com/en-us/exchange/troubleshoot/administration/cannot-find-the-organizational-unit    

So in summary     

"Get-UserPrincipalNamesSuffix -OrganizationalUnit "mydomain.local/My CompanyOU" works fine when run as a CMDlet in EMS on the Exchange machine but fails, when it is run by the EAC.    

In result I cannot use the EAC to manage user mailboxes.    

I assume the user EAC is run with, is missing some permissions to run the CMDlet properly.    

But I don't know, which permission these are.    

Maybe somebody of you is able to help me out ?    

Thanks for your help in advance !    

Best regards    

CT Admin

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-22*

Dear JameXu,    

in case you can be more specific about the needed details, I will happily provide them.    

As pointed out a few times I think the root cause lies within the way, the script is run.    

When I run it in the Exchange Management Shell with Domain Admin permissions, it displays the expected result.    

When it's run out of the EAC it fails, an error is written to the event log and no result is passed back to the EAC.    

Thus it would be interesting to know under which account/permissions the command is run, when triggered from the EAC while logged in as Domain Admin.    

If it were with the Domain Admin's permissions it shouldn't fail.    

Best regards    

CT Admin
