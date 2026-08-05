---
title: "Deploy shared printer by GPO not successfull"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/4173114/deploy-shared-printer-by-gpo-not-successfull
question_id: 4173114
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
answer_author_roles: ["Independent Advisor"]
---
# Deploy shared printer by GPO not successfull

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/4173114/deploy-shared-printer-by-gpo-not-successfull (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Experts:

In my company, some users have installed printer by IP address (assume 192.168.1.10) and the port 192.168.1.10 was occupied. ( Printer driver also been installed). Others not installed the printer.

Now we need to set the printing preference to default 2-sided&BW , so I created a printer server (WinSvr2019 -> printer management) and add the printer to the server and then "Deploy with Group Policy". And I used a new printer name which is different from the old name.

It is actually a simple computer GPO settings: .

But in product environment, it is not so good:

-  It is working on those laptops which didn't installed the printer, but it is not working on those have installed the printer.  Is it possible that the printer port was occupied? will the group policy create a new port: 192.168.1.10_1 ?   

-  gpupdate /force     -> computer group policy successfully    gpresult /r              -> the group policy was applied.    check result from GPO also successful (No changes were detected.

  Is the group policy found the same IP address's printer was installed then it thought deployed successfully? 

-  User rebooted the laptop, there is still the printer with the old name. No new printing port or new printer name/printer was added. Just like nothing happened.

What should I do in this scenario? should I uninstall the printer or change the Printers's IP address first , then to deploy? 

Thanks again.

Best regards

George

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2023-03-13*

Hello George,

Good day! I'm John DeV a Windows user like you and I'll be happy to assist you today.

Due to the scope of your question, it is best to ask this on Microsoft Site Q&A which is a technical community platform where most of the members were IT professionals that would greatly help you with the issue.

Microsoft Site Q&A

https://learn.microsoft.com/en-us/answers/quest...

Kind regards,

John DeV

Independent Advisor
