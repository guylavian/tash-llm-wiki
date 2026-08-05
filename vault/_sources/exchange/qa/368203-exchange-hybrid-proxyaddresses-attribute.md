---
title: "Exchange Hybrid - ProxyAddresses attribute"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/368203/exchange-hybrid-proxyaddresses-attribute
question_id: 368203
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
---
# Exchange Hybrid - ProxyAddresses attribute

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/368203/exchange-hybrid-proxyaddresses-attribute (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Team,  

In our Hybrid setup, we observed that when the user mailbox is migrated from Exchange On-premise to Exchange Online, value of "legacyExchangeDN" attribute changes, which I guess is expected. But we also see that the value of this attribute, prior to migration, can be obtained from "proxyAddresses" attribute.    

For instance, consider we have On-premise mailbox with below legacyExchangeDN value:  

```
legacyExchangeDN = /o=domain/ou=Exchange Administrative Group (FYDIBOXXX)/cn=Recipients/cn=AAA...
```

When this mailbox is migrated to Exchange Online, we can see a different value for legacyExchangeDN after migration. We can also see the previous legacyExchangeDN value under "proxyAddresses" attribute along with SMTP address.  

```
legacyExchangeDN = /o=ExchangeLabs/ou=Exchange Administrative Group (FYDIBOXXX)/cn=Recipients/cn=BBB...
proxyAddresses = /o=domain/ou=Exchange Administrative Group (FYDIBOXXX)/cn=Recipients/cn=AAA...
```

We also tried re-migrating the same user mailbox back to Exchange On-premise and noticed that "proxyAddresses" attribute now holds:  

```
proxyAddresses = /o=domain/ou=Exchange Administrative Group (FYDIBOXXX)/cn=Recipients/cn=AAA...
proxyAddresses = /o=ExchangeLabs/ou=Exchange Administrative Group (FYDIBOXXX)/cn=Recipients/cn=BBB...
```

and a new legacyExchangeDN value.  

We wanted to understand if proxyAddresses attribute will also hold previous "legacyExchangeDN" values incase of multiple migration scenarios along with the SMTP addresses and X500 addresses,etc? Is this an expected behavior?  

Thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-23*

Hi @ExUser44   ,    

Yes, you are correct, this is  by design. Based on my knowledege and test result, after you migration the mailbox, it will convert the LegacyExchangeDN value of the source mailbox to an X500 address and add it to the ProxyAddresses attribute. So after you first migration, you will see the AAA added to the proxyaddresses. After you second migration, you will see that BBB is also added to proxyaddresses.    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.
