---
title: "Orphaned Mail-User in Exchange Online - Azure AD"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1017242/orphaned-mail-user-in-exchange-online-azure-ad
question_id: 1017242
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Orphaned Mail-User in Exchange Online - Azure AD

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1017242/orphaned-mail-user-in-exchange-online-azure-ad (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, I have an orphaned mail user which I cannot delete.

With the command to delete the mail user, I get an error message that a user is assigned in Azure Active Directory.

PS C:\Users\admin.lehnert> Remove-MailUser -PermanentlyDelete -Identity e89d036d-00f0-44fc-b83e-***********  

Write-ErrorMessage : |Microsoft.Exchange.Management.Tasks.RecipientTaskException|This mail enabled user cannot be permanently  

deleted since there is a user associated with this mail enabled user in Azure Active Directory. You will first need to delete  

the user in Azure Active Directory. Please refer to documentation for more details.  

At C:\Users\admin.lehnert\AppData\Local\Temp\12\tmpEXO_pfqedgqw.psu\tmpEXO_pfqedgqw.psu.psm1:1107 char:13  

-  Write-ErrorMessage $ErrorObject $IsFromBatchingRequest  

-  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

-  CategoryInfo : NotSpecified: (Soft Deleted Objects*Username*s:ADObjectId) [Remove-MailUser], RecipientTaskExcep  

tion  

-  FullyQualifiedErrorId : [Server=DBBPR09MB3477,RequestId=dae09a36-5ff9-bd00-420e-f8b027d4f634,TimeStamp=Wed, 21 Sep 2022 08  

:36:07 GMT],Write-ErrorMessage

However, the associated user no longer exists, it has already been deleted. Im sure about that, i have check it many times.

The only thing I noticed is that InPlace Holds are assigned here. But LitigationHoldEnabled is set to false.

InPlaceHolds : {-mbx22786ae8c97f40be89a47c2596e6015b, -mbx31c09d18f08e4522b17a8e98d991c392}

LitigationHoldEnabled : False

Could this also be a reason which blocks the deletion and only an incorrect error message is displayed ?

Is anyone able to help me.

I need to delete this referenced object because it is blocking an email address that I want to use again.

I have also already tried to change the PrimarySmtpAdress and the WindowsEMailAdress, but i can not change the EmailAdresse, becaus of the WindowsLiveID which is assigned.

The commands of mail-user in contrast to mailbox are much more restricted in the shell

Many Thanks

Alex

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-22*

Hello Andy,    

thank you for your Answer.    

No i have final find how to create an case, i will open one.     

Thanks.
