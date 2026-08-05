---
title: "Select domain at ADFS login page"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/17091/select-domain-at-adfs-login-page
question_id: 17091
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Select domain at ADFS login page

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/17091/select-domain-at-adfs-login-page (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My ADFS connect to two AD Domain for authentication, can I let users select the domain they belong instead of typing the domain name?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 1 · updated: 2020-03-23*

Are those domains in the same forest?    

If so, you could set the same UPN suffix for both domains and then use the JavaScript trick to autocomplete: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/advanced-customization-of-ad-fs-sign-in-pages#customizing-the-ad-fs-sign-in-experience-by-using-onloadjs (the "Example 2: accept SAM-account name as a login format on an AD FS form-based sign-in page" section, you can customize it to work with UNPs).    

You could also have them sign-in with their email address for example: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configuring-alternate-login-id    

If the above doesn't fit your needs, we can always do a custom JavaScript that will display a drop down menu for your users... but it will then disclose what is your internal domain names (since the JavaScript will be loaded on the client side, which by the way is the case too for the suggested solution in my first point).    

Let us know what you prefer!
