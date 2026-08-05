---
title: "MS Exchange on premise: Multiple user mailbox in outlook password prompting isue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2118177/ms-exchange-on-premise-multiple-user-mailbox-in-ou
question_id: 2118177
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# MS Exchange on premise: Multiple user mailbox in outlook password prompting isue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2118177/ms-exchange-on-premise-multiple-user-mailbox-in-ou (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

I have an exchange server on premise:   

server1 holds domain1.com & domain2.com  

server2 holds domainA.com & domainB.com

in client PC outlook app I'm configuring mails from server1 & server2   

i.e. ******@domain1.com, ******@domain2.com & ******@domainA.com - all in 1 outlook profile only   

the issue is, every after 3 days or a week when opening the outlook its prompting to input the passwords for this mails connecting to the server (Like you are configuring it again - windows password prompts).  

Is there anyway to resolve this issue?  

Thank you!!!!

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-12-10*

Hi @GDT，

Glad to hear this issue has been resolved, thanks for sharing! 

However, due to a recent update to the forum policy, the question author cannot now accept his own answer. So, I have briefly summarized the solution to this issue. Feel free to accept it as an answer, which will benefit others in the forum with similar issues. 

Problem: 

When opening Outlook, you are prompted to enter the password for connecting to the mail server when you open Outlook after every 3 days or a week. 

Solution: 

In Windows, click Start > Control Panel > Credential Manager. Then find the credential set with Outlook in its name, expand the credential set, and click Remove from Vault to delete the credentials and reconfigure the desired mail in the profile.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-11-30*

Hello Mengying,

I removed the credentials from the control panel (windows credential manager) and reconfigured the required multiple mails in 1 profile, till now its working fine.

Im just observing if the issue still persists in next week.

Thank you

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-11-13*

Hi, @GDT

Thank you for posting your question in the Microsoft Q&A forum.

According to your description, you are experiencing a problem where you are prompted to enter the password for connecting to the server's mail every few days when you open Outlook. You can try the following steps to see if it helps:

-  If your administrator uses the Microsoft Office Group Policy Template, Outlook may be configured not to save basic authentication credentials, so that when you enable the Remember my credentials option, the stored credentials will not be overwritten. You can try in Windows, click Start > Control Panel > Credential Manager. Then find the credential set with Outlook in its name, expand the credential set, and click Remove from Vault.

-  If the Outlook profile is damaged or corrupted, it may also cause Outlook to behave unexpectedly. You can try to repair the Outlook profile by following the steps below:

-  Open Outlook, click File, and then click Account Settings. Select your email account, and then click Repair.

-  This problem may also occur if the Allow Office to connect to the Internet check box under Trust Center Privacy Options is not selected. You can try to solve it by following the steps below:

-  On the File tab, select Options.

-  Select Trust Center, and then select Trust Center Settings.

-  Select Privacy Options, and then select the Allow Office to connect to Microsoft's online services to provide usage and preference-related functionality check box.

-  Select OK twice to close the Outlook Options dialog box.

If you have any questions, please feel free to contact me. If the answer is helpful, please click "Accept Answer" because it can help other members of the Microsoft Q&A community who are experiencing similar problems and are looking for solutions. Thank you.

Best,

Jeanne
