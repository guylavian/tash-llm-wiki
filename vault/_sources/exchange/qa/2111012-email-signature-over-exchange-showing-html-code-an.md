---
title: "Email Signature over Exchange showing html code and placeholder text instead of required information"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2111012/email-signature-over-exchange-showing-html-code-an
question_id: 2111012
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Email Signature over Exchange showing html code and placeholder text instead of required information

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2111012/email-signature-over-exchange-showing-html-code-an (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I need assistance on how to navigate through email signature showing the html code or placeholder text instead of the required filled document

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2024-10-28*

Hi, @Jesse Ayenor || PAYINC GROUP  

From your description, can I understand that your email signature is displayed as HTML plain text or placeholders?

There is some information that needs to be confirmed with you:

1.Do you create an email signature in the Exchange admin centre or in the Outlook built-in signer? Try both methods and see if there's a difference.

2.When you edit a new email, will the email signature be displayed at the bottom of the email? Will recipients be able to view email signatures as normal?

3.Do Outlook clients and OWA have the same issue?

Here are some common solutions:

1.Save the message format as HTML.

2.Use basic HTML and inline styling, as Outlook supports limited CSS. Avoid using external stylesheets or advanced CSS features.

3.If any images are linked via HTTP, switch them to an HTTPS link. Outlook blocks unsafe content.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".
