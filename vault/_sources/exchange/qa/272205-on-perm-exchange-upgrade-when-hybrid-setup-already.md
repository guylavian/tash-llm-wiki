---
title: "On-perm Exchange Upgrade when hybrid setup already done with O365"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/272205/on-perm-exchange-upgrade-when-hybrid-setup-already
question_id: 272205
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# On-perm Exchange Upgrade when hybrid setup already done with O365

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/272205/on-perm-exchange-upgrade-when-hybrid-setup-already (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all  

My environment is using Exchange 2010 and hybrid setup with O365, and majority of the users are in O365 already but I  still have dozens of user stay in on-perm exchange 2010. We need to upgrade the exchange 2010 to 2016/2019 now due to the end of support, so if anyone can share with me the experience related to the below?  

-  I will add Exchange 2016 to the on-perm organisation, then I will change the public IP of those internet facing FQDN such as Autodiscovery, Outlook anywhere, EWS, OWA...etc to the exchange 2016 after we configured all URL/URL in Ex16 virtual directory. But I understanding the federation such as free/busy will also use the autodiscover and EWS to exchange the info.  So if I change the public IP of those FQDNs to Exchange 2016, anything need to do to make the federation work?  

-  How about the mail connector between O365 and on-perm? Any best practice to migrate them from Exchange 2010 to Exchange 2016?  

-   If there nothing need to do in the above? Do we need to run the hybrid setup wizard again before we do decommission of the exchange 2010?  

Best regards  

Alex Tsang

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2021-02-14*

-  Yes, run the Hybrid Wizard again after you make those changes. Ensure you apply a valid, trusted 3rd party certificate to the 2016 server that will be used for client / endpoint connections and set the URLs correctly.     

-  Change the source server on the on-prem Exchange Side from the 2010 server to the 2016 for any send connector    

-  Recreate any custom receive connectors you have in 2010 on the 2016 server. Ensure the 2016 has the same settings for the connectors that the 2010 server does for the hybrid mail flow    

-  Yes, re-run the Wizard and set to the 2016 server instead of the 2010.    

Detailed Steps:    

https://www.c-sharpcorner.com/article/hybrid-exchange-2010-to-hybrid-exchange-2016-part-one/    

Use the latest version of the Wizard as well:    

https://learn.microsoft.com/en-us/exchange/hybrid-configuration-wizard-faqs

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-02-15*

Installing Exchange 2016 into Exchange 2010 organization is like a normal migration procedure. You could refer to Microsoft official tool:    

Exchange Deployment Assistant    

https://assistants.microsoft.com/     

Then run HCW (Hybrid Configuration wizard) to update the hybrid configuration.    

For your questions, my answers are as below:    

-  Run HCW again after you have changed all the configurations to Exchange 2016. It will update the hybrid configuration.     

-  When running HCW, it will allow you to choose where to create the connectors, just select Exchange 2016 server.    

-  Yes.     

For your reference:    

Step-by-Step: How to upgrade a Legacy Hybrid Exchange Server to 2016    

https://www.itpromentor.com/upgrade-hybrid-2016/    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
