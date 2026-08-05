---
title: "KB5000871 installation on Exchange 2016 CU9"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/321061/kb5000871-installation-on-exchange-2016-cu9
question_id: 321061
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# KB5000871 installation on Exchange 2016 CU9

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/321061/kb5000871-installation-on-exchange-2016-cu9 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We run Hybrid Exchange server linked to O365 for email. It currently has Exchange 2016 CU9 installed. If I download the CU9 security patch for the current Exchange vulnerability KB5000871, can I just install this patch for now to fix security issue and update CU to higher later and reinstall security update? As I understand if you install the SU KB5000871 and are not on latest version of CU you will have to reinstall the SU again if you update to later version of Exchange. This is fine if we have to reinstall security update as right now we need to hold off on updating our Hybrid Exchange box CU to later version.   

Can someone let me know if it's ok to install this SU on my existing Exchange version 2016 CU9?  

Thank you!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-18*

@Andy David - MVP    Thank you so much for the fast reply! I will reboot the server 1st and then run command line as admin and run msp file via recommended method. Hopefully I don't run into any issues. It's Hybrid server so it's just relaying mail really. Seems fairly straight forward. Will be taking a backup of server before hand just incase. However, if anything is horribly bad, I will just uninstall patch and try again. Or roll back to previous server backup.     

Then once installed I will run the EOMT.PS1 post install pending all is well.     

Am I missing anything?    

Thank you very much!
