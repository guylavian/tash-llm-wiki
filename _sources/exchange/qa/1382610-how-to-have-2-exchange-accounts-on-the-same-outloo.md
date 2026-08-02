---
title: "How to have 2 exchange accounts on the same outlook profile with specify the data file location for each"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1382610/how-to-have-2-exchange-accounts-on-the-same-outloo
question_id: 1382610
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# How to have 2 exchange accounts on the same outlook profile with specify the data file location for each

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1382610/how-to-have-2-exchange-accounts-on-the-same-outloo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

We are using microsoft emails from Godaddy and we want to access inbox from outlook.

We are able to create a profile for the first business email and change its file location.

When we add the second business email, the option to change the data file location is disabled

How can I change the data file location for the other business email? I can't create a new profile since I will lose the access for the first email.

Thanks in advance

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-10-06*

Hi @BM136  ，

Seems to be an expected behavior in Outlook 2013 and later versions due to the deprecation of the classic offline mode. 

Assuming that the data file location you want to specify for the two accounts are the same, (As far as I know, currently it's not feasible to specify different locations for different accounts in Outlook 2013 and later versions) , as a workaround, you can change the default location of the .ost file by setting the ForceOSTPath registry entry so that the data files of both accounts can be generated in the new specified location.

Note: The value of the ForceOSTPath registry entry only works for a new Outlook profile.

Step 1: Add the ForceOSTPath registry entry.

-  Select Start, select Run, type regedit in the Open box, and then select OK.

-  Locate and then select the registry subkey: `HKEY_CURRENT_USER\Software\Microsoft\Office\xx.0\Outlook`  

Note: The xx.0 placeholder represents your version of Office (16.0 = Office 2016, Microsoft 365, Office 2019, or Office LTSC 2021, 15.0 = Office 2013).

-  Right-click Outlook, select New, and then select Expandable String Value.

-  Type ForceOSTPath, and then press Enter.

-  Right-click ForceOSTPath, and then select Modify.

-  In the Value data box, type the full path of where you want to store the `.ost` file (such as C:\OST), and then select OK.  

-  On the File menu, select Exit to exit Registry Editor.

Step 2: Create a new Outlook profile and add the two Exchange accounts in sequence.

-  Open Control Panel, search for Mail.

-  Click on Show Profiles, then Add, type the name of the profile file and choose "Prompt for a profile to be used".

-  Follow the wizard to add the two Exchange accounts. 

-  Open Outlook and choose the new created profile, check the data file location and you would see they are located in the new path specified by the ForceOSTPath registry entry.

Reference: You can't change the location of the offline Outlook Data File (.ost) in Microsoft Outlook.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
