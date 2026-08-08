---
title: "Exchange 2016 uninstall failing at language pack"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1262850/exchange-2016-uninstall-failing-at-language-pack
question_id: 1262850
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2016 uninstall failing at language pack

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1262850/exchange-2016-uninstall-failing-at-language-pack (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have one exchange server whose uninstall is stuck at the language pack step and no matter what i do, it is just not letting the uninstall, below are the things i have done:

-  Restarted it like a 10 to 20 times.

-  Left overnight and then tried again.

-  Downloaded CU21 ISO file and then mounted and and ran the uninstall from the drive i mounted , still failed.

-  I tried from the install files that existed in one of the drives, it failes there too

I have just ran out of options

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 1 · updated: 2023-04-28*

Hi @Niranjan T Pattana Shetty  ,

 

Please provide more detailed error message to help further troubleshooting. By my experience, I have below suggestions for your reference.

 

1.Please try to use the command below via Command Prompt(run as Administrator) to see if the uninstallation can be successful.

```
Setup.exe /mode:Uninstall /IAcceptExchangeServerLicenseTerms
```

 

2.If the cmd doesn’t work, please run ADSIEdit.msc and remove Exchange 2016 from the location below:   

`CN=configuration -> DC=domain name,DC=com -> CN=Services -> CN=Microsoft Exchange -> CN=<YourExchOrgName> -> CN=Administrative Group -> CN=Exchange Administrative Group -> CN=Servers`  

(Important: ADSI Edit must be handled with care. Modifying the attributes using ADSIEdit can cause significant issues with your infrastructure if something is done in a wrong way. We would suggest you make a backup before modifying.)

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-04-28*

Based on my research, one of the possible causes of this issue is the antivirus. The solution is to disable the real-time protection of your antivirus before installing or upgrading Exchange. Ensure you have all the exceptions in place, as this Microsoft TechNet article outlines. 

See Exchange Install Hangs on Languages Step for more details.
