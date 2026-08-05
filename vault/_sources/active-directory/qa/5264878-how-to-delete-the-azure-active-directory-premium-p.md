---
title: "How to delete the Azure Active Directory Premium P2 trial Subscription?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5264878/how-to-delete-the-azure-active-directory-premium-p
question_id: 5264878
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# How to delete the Azure Active Directory Premium P2 trial Subscription?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5264878/how-to-delete-the-azure-active-directory-premium-p (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Trial period expired and I do not need this subscription any longer nor I need weekly email that says that my subscription has expired. I have looked in all different places but can't find a way to delete it. I have also tried assigning it to a temp AD global admin account but this method also does not work now.

Please help find a solution for this.

Thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2023-08-09*

Dear Vitaliy,

Good day!

Thank you for posting to Microsoft Community. We are glad to assist!

Based on your description regarding "How to delete the Azure Active Directory Premium P2 trial Subscription?". Once the 30 day trial expires for Azure AD Premium P2, does the tenant revert back to basic? If yes, then I'm good.

Yes, once the Azure AD Premium P2 trial expires, Azure AD tenant automatically reverts back to free version.

If not, how do I go about deleting/canceling this Azure AD Premium P2 trial without having a 'work' id associated to it? the only user associated to it currently is my personal 'xxx@contoso.com' email id. Do I need to go in and create a work ID first to be able to log in to a O365 admin portal and delete it from there? In doing so, my concern is i'll get charged, not sure if the 30 day trial period has ended or not.

If you do not want to wait for 30 days for the trial to expire, you can cancel it using the Office businessstore portal. You can select the subscription from the list. and view the details of the same. It will take you to a page similar to the following where you can cancel it . You would need to sign in using your organizational account (Work ID) e.g. ******@newtenant.onmicrosoft.com as personal accounts(outlook.com , live.com ) do not work. 

Once the subscription is cancelled, you can delete it as shown below:

Before deleting the tenant, you can delete the work account and perform the tenant deletion with your hotmail account.

Note: After you delete the Azure AD Premium P2 Subscription, it might take upto 72 hours for the changes to take effect.

For extra reference kindly refer to below:

-  Delete an Azure Active Directory tenant - Microsoft Entra | Microsoft Learn

-  Cancel/Delete Azure Active Directory Premium P2 trial - Microsoft Q&A

I hope the above information will be helpful. Furthermore, if you are still getting this scenario, kindly contact our billing team via link: Get support - Microsoft 365 admin | Microsoft Learn for further check to delete the Azure Active Directory Premium P2 trial Subscription for you.

We sincerely appreciate your patience and cooperation. Thanks for your precious time. Have a nice day!

Best regards,

Inema | Microsoft Community Moderator
