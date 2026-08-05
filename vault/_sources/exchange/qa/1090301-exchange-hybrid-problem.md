---
title: "Exchange hybrid problem"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1090301/exchange-hybrid-problem
question_id: 1090301
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
---
# Exchange hybrid problem

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1090301/exchange-hybrid-problem (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good day

We have Microsoft 365 in cloud some time. Now we plan in additional deploy Exchange server and move part of user's to it.

We study Exchange and don't have big experiences. The existing system is by and large a laboratory stand, but in the future we plan to study all the details and launch it in production

During testing have some problem and we can't find a solution (

before installing exchange on-premise server we use the following scheme - new user create in local AD, sync Azure AD connect and assign license in Office 365 admin in cloud. all work w/o problem.

Install Exchange 2019, install certificates. Run Hybrid configuration wizard in full classic hybrid mode. All work w/o problem.

After install Exchange we create test user - create it in AD, next add User Mailbox - Existing user. and 1st problem.

1) new user can receive email from everywhere and send email only for user on-premise. to send mail for Cloud users we manually add attributes - ProxyAddresses, mailNickName and TargetAddress. it need for every cloud user. no problem to automate it through PS but еs there really no standard way to do this when setting up once and for all ?

2) what is the correct way to remove user from on-prem exchange? if i delete user in exchange admin center - it completely removed from Active Directory. But what to do if the account in AD must be saved ? what is the right way ?

it 2 main problems now. There are more but they require research and maybe I will contact the community later.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-11-18*

you wrote earlier:    

You could use Disable-Mailbox command to disable user mailbox, in this way mailbox will disconnect from AD account. Related AD account will still exist in ADUC.    

it don't work for shared mail and I couldn't find commands to disable (    

I mistakenly specified the parameter connecting the user box from the cloud as shared mailbox. maybe there is another way how to fix it    

can you help ?
