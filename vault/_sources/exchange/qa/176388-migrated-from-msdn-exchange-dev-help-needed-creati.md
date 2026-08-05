---
title: "[Migrated from MSDN Exchange Dev]Help needed creating custom DLP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/176388/migrated-from-msdn-exchange-dev-help-needed-creati
question_id: 176388
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# [Migrated from MSDN Exchange Dev]Help needed creating custom DLP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/176388/migrated-from-msdn-exchange-dev-help-needed-creati (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

[Note]  

This question was originally asked on the MSDN Exchange Development forum which focuses on development questions on Exchange.  

As the former Outlook forums on TechNet have been migrated to Microsoft Q&A forum, we migrated this question manually in order to continue the discussion here.

[MSDN Link]  

Help needed creating custom DLP

[Original post]  

Hi all,

I am trying to build a custom DLP to block PPS numbers in Exchange 2013 on-prem.

PPSN number have the following format of 1234567X, so 7 numbers, one letter.

I built an xml file and tried to import it using the following:

New-ClassificationRuleCollection -FileData ([Byte[]]$(Get-Content -Path "C:\PPSN.xml" -Encoding Byte -ReadCount 0))

but get the following error:

We couldn't import that rule collection because it isn't encoded properly. Please try one of the following steps to resolve the issue:  

-  CategoryInfo : InvalidData: (:) [New-ClassificationRuleCollection], ClassificationR...yptionException  

-  FullyQualifiedErrorId : [Server=EX01,RequestId=c450a6d7-a052-4b30-b2d1-aedddc53982d,TimeStamp=25/11/2020 10:05:35] [FailureCategory=Cmdlet-ClassificationRuleCollec  

tionDecryptionException] D4629348,Microsoft.Exchange.Management.ClassificationDefinitions.NewClassificationRuleCollection  

-  PSComputerName : EX01.CONTOSO.COM  

The xml is at the foot of my post. Can anyone point me where to go from here?

Thanks in advance.

<?xml version="1.0" encoding="UTF-8"?>

<RulePackage xmlns="http://schemas.microsoft.com/office/2011/mce">

<RulePack id="3c155c44-a133-462d-956c-7731367429e2">

<Version revision="0" build="0" minor="0" major="1"/>

<Publisher id="37f35efc-1ad4-4e0f-868e-158be3052f34"/>

<Details defaultLangCode="en-us">

<LocalizedDetails langcode="en-us">

<PublisherName>COMPANYNAME</PublisherName>

<Name>PPSN BLOCK</Name>

<Description>PPSN BLOCK</Description>

</LocalizedDetails>

</Details>

</RulePack>

<Rules>

<Entity id="d4fc5e01-3b9e-4332-8649-c30d590be331" recommendedConfidence="85" patternsProximity="">

<Pattern confidenceLevel="85">

<IdMatch idRef="PPSN"/>

</Pattern>

</Entity>

<Regex id="PPSN ">(\d{7})([A-Z]{1,2})</Regex>

<Keyword id="">

<Group matchStyle="word">

</Keyword>

</Group>

<LocalizedStrings>

<Resource idRef="d4fc5e01-3b9e-4332-8649-c30d590be331">

<Name langcode="en-us" default="true">PPSN BLOCK</Name>

<Description langcode="en-us" default="true">PPSN BLOCK</Description>

</Resource>

</LocalizedStrings>

</Rules>

</RulePackage>

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-26*

Hi,

There are several places need to be modified.  

1.You need to configure a value for "patternsProximity" which defines the distance (in Unicode characters) from the IdMatch location for all other Matches specified for that Pattern.Usually it is configured 300.

2.There is a extra blank here:<Regex id="PPSN ">  

It is supposed to be the same as IdMatch (PPSN)

3.You need to change the positions of </Keyword> and </Group>.  

It should be </Group> and then </Keyword>.

4.Under <Group matchStyle="word">,you need to add some Term elements to specify that the content must match the keyword exactly, including lower- and upper-case letters.  

For example, <Term>yourkeywordhere</Term>

For more detailed information,please refer to this document: Create a custom sensitive information type in Security & Compliance Center PowerShell  

It is for Office365 but should also apply to Exchange 2013.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
