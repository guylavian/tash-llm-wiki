---
title: "Cannot completely delete Azure Active Directory behind Teams Classic"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1227072/cannot-completely-delete-azure-active-directory-be
question_id: 1227072
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-teams-teams-business-other-l1", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Cannot completely delete Azure Active Directory behind Teams Classic

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1227072/cannot-completely-delete-azure-active-directory-be (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Wanting to delete the Active Directory created for my Microsoft Teams (Classic) org, I followed the steps explained  here. When I encountered an error in the final step complaining about some enterprise applications, I followed the steps here as instructed in the error notification.

Remove-AzADServicePrincipal failed on some of the IDs saying they are Microsoft internal. Subsequent Remove-MsolServicePrincipal and Set-MsolServicePrincipal also resulted in some errors, which I assumed to be symptoms of the first error, rather than separate errors. I saw someone suggest somewhere that not being able to remove Microsoft-internal principals is normal, so I proceeded to delete the directory from the Azure Portal. To do all this, I had to create a new admin user (in the [XXX.onmicrosoft.com] domain) in the directory to be deleted and remove the original admin user that was linked to my personal Microsoft account (linked to my Gmail address) from it.

When I log in to the Azure Portal using my personal account, the deleted directory no longer appears in the “Manage Tenants” page under Azure Active Directory (https://portal.azure.com/#view/Microsoft_AAD_IAM/DirectorySwitchBlade/subtitle/). This could be simply because I’m no longer the administrator of that directory, not necessarily because the directory was successfully deleted. However, it is still listed in the page opened from the “Switch directory” link in my profile panel at the top-left corner of the portal (https://portal.azure.com/#settings/directory). When I press the “Switch” button there, I get an error message that says:

Sorry, but we’re having trouble signing you in.

AADSTS7000112: Application 'c44b4083-3bb0-49c1-b47d-974e53cbdf3c'(Azure Portal) is disabled.

Not being able to switch to that directory is not a problem because I wanted to delete it after all. I want to know why it is still listed there and what I need to do to completely delete it (though it remaining there doesn’t seem to do any harm). I can no longer log in as the admin user that I created and left as the only user of the directory specifically for the purpose of deleting it. So I can’t tell how the directory looks to that user.

## Answers

_No answers on this thread._
