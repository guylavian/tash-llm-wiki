---
title: "Adding non-exchange 365 users to distribution list"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/221644/adding-non-exchange-365-users-to-distribution-list
question_id: 221644
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-online-server", "office-exchange-office-exchange-server-management"]
---
# Adding non-exchange 365 users to distribution list

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/221644/adding-non-exchange-365-users-to-distribution-list (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Got kind of an edge case here...  

We have a parent company, and several subsidiaries. Parentcompany.com has its own on-prem non-Microsoft mail server. Subsidiaries.com are all in one tenant using 365 for Exchange email.   

 We've added the parentcompany.com domain to the 365 tenant, and we've added several users from that domain to 365, so that users at the parent can log into 365 using their existing email address. These users also have a Business Basic license so they can access apps such as Teams and OneDrive. We have specifically UNchecked the Exchange option during creation of these users, so that 365 does not try to route mail to them. This setup has been in place for some time, and mail flow between users in the two realms is fine.  

The question is this: how do we add ******@parentcompany.com as a recipient on a 365 distribution list? (it's strictly a distribution list, not a 365 group)  

You can't do it through the admin portal GUI, because those users do not show up in the GAL.  And you cannot add them as an Exchange Contact, since that email address is already "in use". I did however successfully add them to the distro list via Powershell using the add-distributiongroupmember command.  But they're not receiving mail sent to the distro group.  Other external contacts that are members of the group are receiving fine.  

I've ruled out any spam problems at parentcompany.com; the emails aren't hitting our edge filtering service. And when I do a detailed message trace report in 365 on ******@subsidiary.com as a recipient, I see that it's successfully turning the messages outbound to the other recipients on the list, but ******@parentcompany.com isn't even listed among the other recipients in the recipient_address field. It's like that email address is persona non grata to Microsoft.  

I did a get-azureaduser and get-msoluser full detail command on ******@parentcompany.com, and that email address is correctly populated in the following fields: "mail", "MailNickName", "ProxyAddresses" (shows as primary SMTP), "UserPrincipalName".  For good measure, I even put the address into the alternate email address field.  

Any thoughts?

## Answers

_No answers on this thread._
