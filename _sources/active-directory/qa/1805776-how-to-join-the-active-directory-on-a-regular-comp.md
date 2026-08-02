---
title: "How to join the Active Directory on a regular computer?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1805776/how-to-join-the-active-directory-on-a-regular-comp
question_id: 1805776
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to join the Active Directory on a regular computer?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1805776/how-to-join-the-active-directory-on-a-regular-comp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Detailed steps for joining an Active Directory on a Windows 10 computer

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-07-10*

Hello Min Wang,

Ensure your computer meet the basic requirements before you join an Active Directory domain:

-  Only Pro, Education, and Enterprise editions of Windows 10/11 can be joined to a domain. Note that the Active Directory domain is not supported in Home Editions;

-  Your device needs to be connected to a local network and able to access at least one AD domain controller. 

-  Make sure that your computer can resolve the domain name and can access the domain controller: `ping domain IP`

You can add your computer to the domain using the classic Control Panel in Windows:

-  Run `sysdm.cpl` and click Change;

-  Switch the Member of option to Domain and specify your domain’s name;

 3.You will be prompted to enter the name and password of a user with a domain administrator account;

4.The next thing you should see is the message Welcome to the contoso.com domain;

5.Restart your computer.

By default, when you join new computers to a domain, they are placed in the built-in Computers container in the domain root. To manually move a computer account to a different OU (Organizational Unit), you can either drag and drop it or use the Move menu item.

I hope the above steps are clear to you.

Reference: https://woshub.com/add-computer-to-active-directory-domain/

Note: Since the websites are not hosted by Microsoft, the links may change without notice. Microsoft does not guarantee the accuracy of this information. 

If the Answer is helpful, please click Accept Answer and upvote it.
