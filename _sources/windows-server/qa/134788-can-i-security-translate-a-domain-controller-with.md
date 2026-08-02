---
title: "can i security translate a domain controller with file services role using admt?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/134788/can-i-security-translate-a-domain-controller-with
question_id: 134788
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# can i security translate a domain controller with file services role using admt?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/134788/can-i-security-translate-a-domain-controller-with (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,  

I would like to ask for your expertise if below scenario is possible.  

We have domain1.com and we are planning to migrate all users, computers and servers to domain2.com  

We only have 1 DC in domain1.com and has file service role.   

My question is, what is the best course of action to migrate this DC with file service role on the new domain? Can i security translate it and computer migrate using ADMT? or Security Translate and manual disjoin and join?  

Thank you in advance.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-23*

Hello,

Thank you so much for posting here.

Firstly we should configure forest trust between the two domains.  

Then we could migrate users, groups and computers ,ect with ADMT.  

And then we could migrate file server & file shared.

1) We could use Robocopy to migrate the file server include NTFS permission. After the migration, we will need to configure share permission manually.

https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy

https://www.petenetlive.com/KB/Article/0000427

2) Or we could perform Security Translation on the file server. It will automatically update the permission based on the migrated objects.

Similar case: https://social.technet.microsoft.com/Forums/lync/en-US/e4a5e311-b699-4f5e-b42e-a29db629f10b/admt-32-how-to-migrate-file-server?forum=winserverDS

Here we would like to share more information about Active Directory Migration Tool:

Best Practices for Using the Active Directory Migration Tool  

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc974358(v=ws.10)

Thank you so much for your time and support.

Please note: Information posted in the given link is hosted by a third party. Microsoft does not guarantee the accuracy and effectiveness of information.

Best regards,  

Hannah Xiong

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
