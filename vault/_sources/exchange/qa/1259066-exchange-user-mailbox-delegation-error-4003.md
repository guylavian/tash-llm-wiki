---
title: "Exchange user mailbox delegation error 4003"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1259066/exchange-user-mailbox-delegation-error-4003
question_id: 1259066
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange user mailbox delegation error 4003

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1259066/exchange-user-mailbox-delegation-error-4003 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have setup a new account on the Exchange and hidden it from the address list as it's a service account. It is also a non user account, no login.
This new user needs to send-as for all users to perform it's functions. There are a few users it will not apply the send-as right to, all of these users used to be domain admins but are no longer DA's.
When trying to add send-as permission for this user to one of the probelm users, the following error is displayed.
|error|error|
| -------- | -------- |
|Active  

Directory operation failed on HPADC01.hpgroup.xxx.com. This  

error is not retriable. Additional information: Access is denied.  

Active directory response: 00000005: SecErr: DSID-03152DB2, problem 4003  

(INSUFF_ACCESS_RIGHTS), data 0Active  

Directory operation failed on HPADC01.hpgroup.xxx.com. This  

error is not retriable. Additional information: Access is denied.  

Active directory response: 00000005: SecErr: DSID-03152DB2, problem 4003  

(INSUFF_ACCESS_RIGHTS), data 0"|User1 needs user2 to have send-as permissions.

We followed the instructions in this article. https://support.microsoft.com/en-us/topic/access-denied-when-you-try-to-give-user-send-as-or-receive-as-permission-for-a-distribution-group-in-exchange-server-505822f4-8dca-7b97-d378-c8416553f6d2  

however this didn't solve the issue. we wonder if as the article above describes Groups, this doesn't work if it's a user not a group?
our forrest looks like this.
HP Users (ou)  

user1 (needing user2 to send-as)
....Another OU (nested under HP Users)  

User2
inheritence is on for sub OUs.
Our 2019 Exchange Server is on premis and a member of the domain it serves.
How can we add this send as permission in Exchange for user2 to send as user1?
Thank you.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-04-28*

@HP Support  

Glad to see that your issue had already been resolved and thanks for sharing the solution so that others experiencing the same thing can easily reference this! Since the Microsoft Q&A community has a policy that "The question author cannot accept their own answer. They can only accept answers by others", I'll repost your solution in case you'd like to "Accept" the answer.

 

Exchange user mailbox delegation error 4003

 

Issue Symptom:

When trying to add send-as permission for this user to one of the probelm users, the following error is displayed.

 

Solution:

simply turning on the inheritance for that target user(s) did enable us to make the changes required in Exchange.

 

 

Best Regards,

Jarvis Sun

## Answer (community) — community member

*upvotes: 0 · updated: 2023-04-27*

Ah ha! we worked it out. 

The 3 users with the issue were ex AD admin users. We discovered the inheritance under the security tab was disabled for these 3 users. simply turning on the inheritance for that target user(s) did enable us to make the changes required in Exchange. 

Compairing these 3 users with normal (never were admin) users, this appeared to be the most visible difference. All the normal users had the inheritance enabled by default. 

So this issue is resolved. thank you all for reading and thank you Jarvis Sun-MSFT • for the suggestions and effort. 

Kind regards

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-04-27*

Hi @HP Support  ,

Note: For security reasons, I modified the domain name in the code you provided, please be careful not to expose any private information. 

According to your description, I have some suggestions to troubleshoot our issue:

 

1.Please check Mailbox Features on some problematic user and make sure Default Sharing Policy and Default Role Assigment Policy are selected.

 

 

 

-  Go to ADUC, User properties, select the Security tab and check if there are any deny options under Permissions for Authenticated Users.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
