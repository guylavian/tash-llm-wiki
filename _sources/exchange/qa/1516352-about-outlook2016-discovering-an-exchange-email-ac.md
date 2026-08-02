---
title: "About Outlook2016 Discovering an Exchange email account using discovery"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1516352/about-outlook2016-discovering-an-exchange-email-ac
question_id: 1516352
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# About Outlook2016 Discovering an Exchange email account using discovery

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1516352/about-outlook2016-discovering-an-exchange-email-ac (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

WARNING! There was an error parsing the document

```
The test environment is as follows:

Email server: MS Exchange2016

Outlook: Outlook2016 delivered with the Office2016 package

After opening the Outlook2016 client, I created a Microsoft Exchange type email account

Email Address: ******@semidrive.cc

Password:   【I'm not filling anything in here】or 【Fill in an incorrect password】

After finalized, I found that all can through [http://autodiscovery.semidrive.cc/autodiscover/autodiscover.xml]

An Microsoft Exchange type email account can be added successfully  
And can send and receive emails normally

How do I verify a valid password when adding a microsoft exchange type email address? 

![enter image description here](/api/attachments/9d4c0110-f814-4369-b76a-809f18b0c527?platform=QnA)
```

```

```

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-01-29*

Hi  @相 王，

Could you please check the format of the image you posted? I'm having trouble seeing the specific information.  

According to your description, you could add email account successfully, send and receive emails normally without entering a password or entering an incorrect password. This may be due to the credentials saved in the environment or the automatic authentication mechanism.

Considering this situation, you could try to clear the windows credential for Office and see if it helps:

-  Start > Control Panel > User Accounts > Credential Manager. Note: If 'View by' is set to Category, click User Accounts first, and then click Credential Manager.

-  Select the Windows Credentials option. Locate the set of credentials that has either Outlook or Microsoft Office in the name and then expand the corresponding folder.

-  Then click Remove from Vault or Remove (depending upon which version of Windows you are running).

-  Repeat step 3 for any additional sets of credentials that have the word Outlook or Microsoft Office in the name.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
