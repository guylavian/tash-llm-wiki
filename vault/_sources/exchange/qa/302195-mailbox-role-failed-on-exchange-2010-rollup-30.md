---
title: "Mailbox Role Failed on Exchange 2010 Rollup 30"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/302195/mailbox-role-failed-on-exchange-2010-rollup-30
question_id: 302195
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Mailbox Role Failed on Exchange 2010 Rollup 30

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/302195/mailbox-role-failed-on-exchange-2010-rollup-30 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Can someone help... I cannot apply the rollup 30 on my Exchange 2010 server.

At Mailbox Role, it says failed....

Is there a permission error? I can't see why my permissions wouldn't be sufficient.... or which account has a permission issue...

This is the error as documented:

Error:  

The following error was generated when "$error.Clear();  

if ($RoleIsDatacenter -ne $true)  

{  

if (test-ExchangeServersWriteAccess -DomainController $RoleDomainController -ErrorAction SilentlyContinue)  

{  

# upgrade the discovery mailboxes to R5 version, this will fix the RecipientDisplayType property of the discovery mailbox which was wrong in R4.  

get-mailbox -RecipientTypeDetails DiscoveryMailbox -DomainController $RoleDomainController | where {$_.IsValid -eq $false} | set-mailbox -DomainController $RoleDomainController  

$name = [Microsoft.Exchange.Management.RecipientTasks.EnableMailbox]::DiscoveryMailboxUniqueName;  

$dispname = [Microsoft.Exchange.Management.RecipientTasks.EnableMailbox]::DiscoveryMailboxDisplayName;  

$mbxs = @( get-mailbox -Filter {name -eq $name} -IgnoreDefaultScope -resultSize 1 );  

if ( $mbxs.length -eq 0)  

{  

$dbs = @(get-MailboxDatabase -Server:$RoleFqdnOrName -DomainController $RoleDomainController);  

if($dbs.Length -ne 0)  

{  

$mbxUser = @(get-user -Filter {name -eq $name} -IgnoreDefaultScope -ResultSize 1);  

if ($mbxUser.Length -ne 0)  

{  

enable-mailbox -Discovery -identity $mbxUser[0] -DisplayName $dispname -database $dbs[0].Identity;  

}  

}  

}  

}  

else  

{  

write-exchangesetuplog -info "Skipping creating Discovery Search Mailbox because of insufficient permission."  

}  

}  

" was run: "Database is mandatory on UserMailbox. Property Name: Database".

Database is mandatory on UserMailbox. Property Name: Database  

Click here for help... http://technet.microsoft.com/en-US/library/ms.exch.err.default(EXCHG.141).aspx?v=14.3.123.3&e=ms.exch.err.Ex88D115&l=0&cl=cp

Elapsed Time: 00:08:10

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-08*

Hi @Just Ask  ,    

Please ensure that you are running the Exchange 2010 Setup wizard with an account that has the permissions required (Schema Admins, Domain Admins, and Enterprise Admins).     

Then agree with AshokM that it's suggested to verify all arbitration mailboxes are attached to the database. You can refer to the steps and link he shared above.    

Besides, in case the issue persists, I'd recommend deleting the Discovery Search Mailbox mentioned in the error message, then follow the blog below to recreate it:    

Exchange 2010: How to recreate System Mailbox, FederatedEmail & DiscoverySearchMailbox    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-07*

Hi @Just Ask   ,    

Run the command in Exchange management shell,    

Get-Mailbox –Arbitration | Select Name,Database    

there would be a warning for one of the system mailboxes, if yes, run the below command to set the database to that system mailbox    

Set-Mailbox "System Mailbox xxxxx" –Database "DB Name" –Arbitration    

Then re-run the setup.    

Also, please note that Exchange 2010 is out of support. Kindly plan to upgrade to the supported version.    

https://www.petenetlive.com/KB/Article/0001221    

If the above suggestion helps, please click on "Accept Answer" and upvote it.
