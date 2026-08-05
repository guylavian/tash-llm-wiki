---
title: "Error while enabling Exchange 2013 Hybrid - Update-EmailAddressPolicy"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/275731/error-while-enabling-exchange-2013-hybrid-update-e
question_id: 275731
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
---
# Error while enabling Exchange 2013 Hybrid - Update-EmailAddressPolicy

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/275731/error-while-enabling-exchange-2013-hybrid-update-e (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Everyone,

While attempting to configure our Exchange 2013 environment in Hybrid mode the wizard is failing on the Update-EmailAddressPolicy -Identity "Default Policy" -UpdateSecondaryAddressesOnly: $true

I see it worked on some users but there is still over a thousand that it did not work on. We are one CU23 with up to date servers.

Is there a way to scope the update-emailaddresspoilcy to certain users?

Can't read all of the recipient objects that you want to update update using LDAP recipient filter "(mailNickname=*)"  

of object "Default Policy". The following exception occurred: Active Directory operation failed on  

DC01.domain.com. Additional information: Active Directory rejected paged search cookie because a cookie  

handle was discarded by a Domain Controller or a different LDAP connection was used on subsequent page retrieval.  

Paged search needs to be restarted and will succeed.  

Additional information: The parameter is incorrect.  

Active directory response: 00000057: LdapErr: DSID-0C090B26, comment: Error processing control, data 0, v4563.  

-  CategoryInfo : InvalidOperation: (Default Policy:ADObjectId) [Update-EmailAddressPolicy], InvalidOperat  

ionException  

-  FullyQualifiedErrorId : [Server=ExchMBX01,RequestId=fbc467bd-4e5b-4c7e-840b-6f13b0aef520,TimeStamp=2/16/2021 8:  

42:21 PM] [FailureCategory=Cmdlet-InvalidOperationException] C6E7F98,Microsoft.Exchange.Management.SystemConfigura  

tionTasks.UpdateEmailAddressPolicy  

-  PSComputerName : ExchCAS01.domain.com

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-17*

Hi Andy and Lucas,  

Thanks for the update and information.  I was under the impression I could scope the Update-EmailAddressPolicy cmdlet to certain users or an OU.  But it appears I need to do that via the Set-EmailAddressPolicy cmdlet.  I can look more into that.  

We are running the Default Policy and only that policy.  I was thinking that error was happening because the volume of accounts the Update-EmailAddressPolicy was running through.  

What about the option of targeting the users that need the alias directly, could that be an option?  

The domain controller is running Windows 2019.
