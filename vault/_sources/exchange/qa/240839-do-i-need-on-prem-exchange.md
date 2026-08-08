---
title: "Do I need On-prem exchange?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/240839/do-i-need-on-prem-exchange
question_id: 240839
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Do I need On-prem exchange?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/240839/do-i-need-on-prem-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm running into an issue with not being able to edit users or security group settings in Office365 in Exchange Admin Center, I always receive a message stating that because the item/object was created on-prem that I would have to make the changes there.   

We have a one way sync with Azure AD Connect going from on-prem to Office365.  

Just to give you an example. There was a security group "Sales" created on-prem in ADUC. No issues there it will sync just fine into Office365. The issue is the person that created this security group "Sales" also added an email address in the properties of the Sales object. Now, in Office365 it says it's "mail-enabled" and users are emailing it. If I remove the email address in ADUC it still shows up in Office653 as "Mail-enabled". There is NO way around this without deleting the security group and creating another one. I have tried the GUI and powershell to edit this setting and I get the same error message "Can not make changes to this object because the object was created on-prem. Please make the chnage there instead".  

Do I need a Hybrid setup to where I have Exchange on-prem as well. If so, how hard is this to do?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-25*

Hi @Keith Hampshire      

Agree with michev's suggestion above, changes cannot be made directly in o365, we should perform the operation on-premise then they will be synced to cloud.    

Installing an Exchange server is the recommended way by Microsoft, however it can work normally without installing on-premise Exchange.    

Extending the Active Directory schema adds and updates classes, attributes, and other items. These changes are needed so that Exchange can create containers and objects to store information about the Exchange organization.     

Please also refer to this thread which discussed the similar question as yours: Is an on-premises Exchange server still required with Azure AD Connect?    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-01-22*

Hybrid will not help in this specific scenario, but generally speaking every configuration involving dirsync requires you to have at least one Exchange server on-premises for management purposes. As you've noted above, the on-premises AD is the source of authority in such scenarios and changes need to be made there, and the only supported method to create/manage Exchange-related objects and attributes is via the Exchange tools.  

If you dont care about the supported bit, you can do fine without an Exchange server, however at the very least you should extend the AD schema with the Exchange schema extensions.
