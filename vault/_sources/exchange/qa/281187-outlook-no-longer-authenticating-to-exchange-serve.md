---
title: "Outlook no longer authenticating to exchange server 2013 after rebuild"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/281187/outlook-no-longer-authenticating-to-exchange-serve
question_id: 281187
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Outlook no longer authenticating to exchange server 2013 after rebuild

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/281187/outlook-no-longer-authenticating-to-exchange-serve (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, we are having some issues with our outlook clients our domain.  So in full originally the decision was made to do a rebuild of our exchange server after a number of things went pretty wonky.  Before the rebuild all of the exchange sites were not working (500 error) and it was not possible to add new users to the server, even with exchange management shell.  The rebuild went alright, exchange was fully uninstalled and then reinstalled which restored access to ecp and owa.  The issue we are now facing is that our Outlook 2016 clients do not connect into the exchange server.  When launching outlook it finds the users email address but it seems to fail out when it tries to authenticate into exchange.  I am looking for anything to try that might be the cause of this issue... we have looked into auto discovery a bit already, but any help would be appreciated.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-02-22*

Hi @David Bucha  ,    

Aside from the suggestions provided by AshokM, I'd like to suggest running the Test Email-AutoConfiguration on one of the problematic user's machine and check the Log tab to see if it shows as "succeeded":     

    

    

Besides, please try configuring the following registry subkeys on an affected machine and reopen Outlook to see if there would be any difference:    

(Important: Follow the steps in this section carefully. Serious problems might occur if you modify the registry incorrectly. Before you modify it, back up the registry for restoration in case problems occur.)    

HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Outlook\Autodiscover    

DWORD: ExcludeLastKnownGoodUrl    

Value: 1    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
