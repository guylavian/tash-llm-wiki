---
title: "Exchange 2016 cu 19 failing because OWA (Exchange Back End) couldn't be found - ON WRONG SERVER"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/304889/exchange-2016-cu-19-failing-because-owa-exchange-b
question_id: 304889
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2016 cu 19 failing because OWA (Exchange Back End) couldn't be found - ON WRONG SERVER

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/304889/exchange-2016-cu-19-failing-because-owa-exchange-b (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Trying to install CU 19, and getting [ERROR] The operation couldn't be performed because object 'XXX\OWA (Exchange Back End)' couldn't be found on 'YYY.ZZZ.local' YYY is the domain controller, and XXX is the Exchange server. I have no idea why it is looking for the OWA (Exchange Back End) directory on the domain controller. It is definitely on the Exchange server. this server is down until I can fix this, or restore from backup, and lose a day.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-09-22*

Did you manage to fix this?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-09-12*

Running into a similar issue installing Exchange 2016 CU21. The upgrade fails on the Client Access Front End Service.   

[Error] The operation couldn't be performed because object '[ExchangeServer]\owa (Default Web Site)' couldn't be found on '[DC].domain.com'.   

Our OWA isn't in the Default Web Site it's in a custom site. And it's not on the domain controller it's on the Exchange Server. The error makes it look like it's looking on a DC for it. ADSI lists the correct location for OWA in the custom site on the Exchange Server.   

Any ideas?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-03-09*

Hi @Natalie Bennett   ,    

Exchange virtual directory information will be stored in AD.     

Any issues with AD replication or commuication issues between Exchange & AD?    

Is this is a new install or upgrade. Incase of upgrade from previous CU, based on the current CU, Exchange may need schema update, so try running the below commands before the CU install    

Setup /PrepareSchema /IAcceptExchangeServerLicenseTerms    

Setup /PrepareAD /IAcceptExchangeServerLicenseTerms    

Also, check if the OWA virtual directory exist in the Exchange server. If not try re-creating it once. If still errors occurs, please share the error message from Exchange setup log by covering personal information.    

https://theitbros.com/recreate-owa-ecp-virtual-directories-exchange-server-2016/    

If the above suggestion helps, please click on "Accept Answer" and upvote it.
