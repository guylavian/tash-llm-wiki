---
title: "Exchange Import Contacts from CSV and Add / Modify information"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/216848/exchange-import-contacts-from-csv-and-add-modify-i
question_id: 216848
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange Import Contacts from CSV and Add / Modify information

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/216848/exchange-import-contacts-from-csv-and-add-modify-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone,

I have about 5000 contacts to add in the Global Address List in the Exchange Server and I need to use the Exchange Management shell and use a CSV.

Of what I have noticed, I cannot define all CSV fields in the New-MailContact so they all are added so I need to just create the contacts and then add/modify the rest of the values.

I have the following Code:

```
Import-Csv C:\Stefanos\MyCSV.csv | %{New-MailContact -Name $_.Alias -FirstName $_.FirstName -LastName $_.LastName -Alias $_.Alias -ExternalEmailAddress $_.Email -OrganizationalUnit $_.OUpath}
```

the above successfully creates the contact but after that, I need to modify some contact information like change DisplayName, add MobilePhone, Phone (BusinessPhone), JobTitle etc

```
$ContactInfo = Import-Csv C:\Stefanos\DummyCSMCYGAL4CSMITA.csv
$contacts | ForEach {Set-Contact $_.Name -DisplayName $_.DisplayName -Phone $_.Phone -MobilePhone $_.MobilePhone -Pager $_.Pager -HomePhone $_.HomePhone -Company $_.Company -Title $_.Title -OtherTelephone $_.OtherTelephone -Department $_.Department}
```

the above command on the other hand, shows an error:

Cannot bind argument to parameter 'Identity' because it is null.  

-  CategoryInfo : InvalidData: (:) [Set-Contact], ParameterBindingValidationException  

-  FullyQualifiedErrorId : ParameterArgumentValidationErrorNullNotAllowed,Set-Contact  

-  PSComputerName : servername.domain

I tried to add Identity or define it in my CSV but it seems I cannot get it right

Does someone have a recommendation or how I can fix the problem?

## Answers

_No answers on this thread._
