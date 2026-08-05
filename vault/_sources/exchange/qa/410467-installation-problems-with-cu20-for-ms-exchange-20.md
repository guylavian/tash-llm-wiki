---
title: "Installation problems with CU20 for MS Exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/410467/installation-problems-with-cu20-for-ms-exchange-20
question_id: 410467
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Installation problems with CU20 for MS Exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/410467/installation-problems-with-cu20-for-ms-exchange-20 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,   

I have a problem with the installation of the Cumulative Update 20 for MS Exchange 2016 on a fresh VM (So currently, there is no Exchange installed). I first installed .NET and the other required prerequisites and then I started the setup with an appropriate admin account (which is a domain admin, an organisation admin and a schema admin) using the command line with the attribute /prepareAD. This worked fine.    

Afterwards, I tried to start the actual installation with EXCHANGESERVER.msi. Then, a window opened, which disappeared after about 3-5 minutes without an error message. However, nothing was installed.   

I have to say that Exchange 2016 was already installed on another VM (which does not exist anymore but had the same computer name) in the same domain. I have also deleted all Exchange entries from the AD.    

I hope you can help me. Thank you!

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-05-27*

Hi @Exchange-Admin  ,

then I started the setup with an appropriate admin account (which is a domain admin, an organisation admin and a schema admin)

According to this official document, please also ensure that the admin account is a member of the Enterprise Admins security group.

I tried to start the actual installation with EXCHANGESERVER.msi.

By this, do you mean you clicked the EXCHANGESERVER.msi file to try installing the Exchange server? Actually in order to start Exchange Setup, we need to double-click "Setup.exe". So basically the process is as follows:

-   Install Exchange Server prerequisites.

-   Prepare AD and domains.

-   Install the Exchange CU using the Setup wizard  

    

Or you can install the CU using the command line:

```
E:\Setup.exe /IAcceptExchangeServerLicenseTerms /Mode:Install
```

In case you still failed to complete the installation, it's suggested to check the Exchange Setup log which is by default available at <system drive>:\ExchangeSetupLogs\ExchangeSetup.log and see if there would be any clues.

If an Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
