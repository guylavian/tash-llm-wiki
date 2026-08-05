---
title: "Strange active directory password complexity issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/255165/strange-active-directory-password-complexity-issue
question_id: 255165
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Strange active directory password complexity issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/255165/strange-active-directory-password-complexity-issue (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

I have a strange problem with active directory password complexity.  

The password complexity policy ("Password must meet complexity requirements" = enabled) applies correctly when a user tries to change a password by pressing "Alt + Ctrl + Del".  

But when I force the user to change a password he can change to a password that is not complex, It also happens that the password has expired and in the next login it is required to change the password.  

Someone is having a similar problem? How can this be solved?  

Some details about the environment:  

Domain Controller windows server 2016  

Functional level 2016  

Thanks

## Answer (community) — community member

*upvotes: 1 · updated: 2021-02-02*

Hello,    

Thank you so much for posting here.    

Yeah, it is a little strange. The setting (Password must meet complexity requirements) is in effect immediately, but users are not impacted until a password change occurs. So when the user is trying to change the password, the setting will be applied.     

After deep research, hope something here might be helpful. We could kindly have a check.    

https://techcommunity.microsoft.com/t5/ask-the-directory-services-team/the-strange-case-of-unenforced-password-complexity/ba-p/396400    

Besides, have we configured Fine-Grained Password Policies for the specific user? To check whether configured or not, we could use the below powershell command.     

Get-ADUserResultantPasswordPolicy username    

Here is the result of the command if the user was configured the FGPP. (If the user was not configured the FGPP, the result will show nothing.)    

    

For any question, please feel free to contact us.    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-08*

Hello,    

You are welcome. Thank you so much for your kindly reply.    

We cannot edit the password complexity rules. We need to create our own password filter to replace the default.     

https://learn.microsoft.com/en-us/windows/win32/secmgmt/password-filters    

Others also had the same issue and we had discussed about this before. We could kindly have a check.    

https://learn.microsoft.com/en-us/answers/questions/118459/custom-change-in-39password-must-meet-complexity-r.html    

For any question, please feel free to contact us.    

Best regards,    

Hannah Xiong    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
