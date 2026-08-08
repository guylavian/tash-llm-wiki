---
title: "unable to export/import the transport rules from Ex2010 to Ex2016."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/218408/unable-to-export-import-the-transport-rules-from-e
question_id: 218408
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# unable to export/import the transport rules from Ex2010 to Ex2016.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/218408/unable-to-export-import-the-transport-rules-from-e (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

i am in the process of decommisioning the exchange 2010 server which are coexistence with 2016 in the process i came across an article to copy, or move or recreate the transport rules in exchange 2016.  

in the process of moving the transport rules i have exported the rule to .xml in Ex2010 and imported them to ex2016, but after the import the rule version still shows 14.0 instead of 15.0. when i am trying to recreate them in ex2016 EAC or ECP it is creating with the version 14.0 not 15.x.x.  

Do i need this step to move the transport rules? if yes, is there any steps that i need to follow.  

thanks in advance.  

Pavan.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-05*

Hi @Pavan Cherlapally   ,    

I agree with Andy, you could still use 14.0 rules in Exchange 2016. You can import 2010 rules to 2016 directly.    

Based on my test, the version(14.x.x.x or 15.x.x.x) depends on the Condition/Exception/Action version.    

Which means if one of the three properties is only available in Exchange 2013 or later, the version could be 15.x.x.x.    

     

    

Here you can find the Conditions/Exceptions/Actions : Mail flow rule conditions and exceptions (predicates) in Exchange Server.    

You could also accept Andy's answer as Accepted Answer so it will help others have the same question.    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
