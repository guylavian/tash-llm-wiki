---
title: "get the security settings from GPO using xml report"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/85295/get-the-security-settings-from-gpo-using-xml-repor
question_id: 85295
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# get the security settings from GPO using xml report

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/85295/get-the-security-settings-from-gpo-using-xml-repor (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I want to export the security settings of a group policy. I have exported the gpo to xml format and then I am using the below:  $x.GPO.Computer.ExtenstionData.Extension  

Where $x contains the xml report. However I getting the result like below:  

q1                                                                                                            type  

http://www.microsoft.com/Grouppolicy/Settings/Files                          q1:FileSettings  

```
q2:SecuritySettings

                                                                                                            q3:RegistrySettings
```

How can I extract the data inside these q1:FileSettings, q2:SecuritySettings, q3:RegistrySettings?

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-06*

Example, xml file attached:22862-testgpo1.xml    

Basically I want to know how to extract information in the namespace using Select-xml or xpath.    

So in this example xml file, I want to extract all the settings defined using powershell.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-05*

Thanks for the reply. However what if there are multiple GPOs with different settings and we don't know the value we want to search is in [0], [1], [2] etc..  

If the xml has a namespace, how can I extract value from that using xpath or Select-xml.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2020-09-03*

Hi,  

It depends on how the gpo is stored in the xml file. According to the result you posted, there could be three nodes in $x.GPO.Computer.ExtenstionData.Extension and you can get them separately with $x.GPO.Computer.ExtenstionData.Extension[0], $x.GPO.Computer.ExtenstionData.Extension[1] and $x.GPO.Computer.ExtenstionData.Extension[2]. You'd better post the xml file. Otherwise no one knows how to get the data inside these nodes.

Best Regards,

Ian

Please remember to "Accept Answer" and upvote if the reply is helpful.
