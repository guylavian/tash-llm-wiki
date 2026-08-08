---
title: "Exchange Cross Forest Mailbox Move"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/236739/exchange-cross-forest-mailbox-move
question_id: 236739
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange Cross Forest Mailbox Move

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/236739/exchange-cross-forest-mailbox-move (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Folks,

I need some suggestion on moving the mailboxes in cross forest.

Source Server : Exchange 2013

Target Server: Exchange 2016

New-MoveRequest –Identity '******@careexchange.in' –Remote –Remotehostname 'sourceExchange.CareExchange.in' -RemoteCredential $RemoteCredentials –TargetDeliverydomain 'targetexchange.in'

-   I am using the above command and getting some error like increase timeout ( Seems like need to increase the timeout in  

    MRS proxy on source exchange server

-   Source forest has internal load balancer so do we need to increase the timeout value on there as well

-   Also one more query in the above command in the section of -remotehostname which parameter we have to enter its the  

    server FQDN ( like example exchange01.abc.com )or the URL name of the EWS virtual Directory ( like example  

    mail.abc.com )

Note: I have entered the FQDN of the server and got the error like certificate is invalid and SSL/TLS issue then tried entering the mail.abc.com after 55% mailbox move failed and now getting the timeout error.

Appreciate your quick feedback folks.

Thanks,  

Arif

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-26*

Hi anonymous user ,    

Thank you for sharing these steps!     

For the SSL Certificate Issue, if you use the self-signed certificate, you need to export the root certificate from legacy Exchange and import to the target Exchange certificate root.    

- 	Export from the Source forest certificate root    

     

- 	Copy the .Cer file to Target forest.    

- 	Install certificate to local computer -> trusted root certificate authorities.    

     

You can try to open https://<SourceServerFQDN>/EWS/mrsproxy.svc form the target forest, if there is no certificate issue, it will directly ask for your account and password.    

As for the TransientFailureSource failure, does the migration go well after you changed the MRS proxy timeout and DataImportTimeout?    

And does the Test-MigrationServerAvailability cmdlet succeed? I think if it’s a success, you can do the migration as expected.    

Looking forward to your good news!    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-22*

Hi @Anonymous  ,    

Thanks for your reply !!    

My steps for migrating the users mailbox from source to target exchange    

Step1: PrepareMoveScript.ps1 to copy the user attributes and ensure mail enabled user object is created in target domain    

Step2: Move the security groups via ADMT tool    

Step3: Move the user with password, SID history, fix group membership via ADMT tool    

Step4: Mailbox move request  after creating a migration end point     

Step5: Complete and finalize the migration job for the mailbox    

Noted: Moved pilot mailboxes and its completed successfully but one time i got transientfailuresource     

Issues faced:     

SSL certificate issue as the target exchange doesn't have internet access    

TransientFailureSource while moving the mailbox, Could be the issue with load balancer session timeout or the MRS proxy timeout.    

Also i will make the load balancer session as persistent.    

Note: I will apply the changes on the timeout value as suggested by you on the load balancer and MRS proxy on the source exchange server    

Regards,    

Arif
