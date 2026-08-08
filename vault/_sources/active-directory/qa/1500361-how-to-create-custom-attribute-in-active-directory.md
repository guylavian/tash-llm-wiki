---
title: "How to create custom attribute in Active Directory?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1500361/how-to-create-custom-attribute-in-active-directory
question_id: 1500361
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to create custom attribute in Active Directory?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1500361/how-to-create-custom-attribute-in-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,
We have two domains: domain A and domain B. We have created a few custom attributes in domain A and want the same custom attributes in domain B. Can you please tell us how we can create?
Thanks!

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 1 · updated: 2024-01-19*

Hello Khushi kumari,
Thank you for posting in Q&A forum.
Are domain A and domain B in the same forest?
If you update the schema in domain A to add custom attributes within the same forest, these attributes will be available throughout the entire forest, including domain B.
To use the same custom properties in domains in different forests, you need to extend the Active Directory schema in each domain.
This can be achieved by using the ldifde tool. Regarding how to use the ldifde tool, I will attach relevant articles below for your reference, but I do not recommend personnel who are not familiar with AD to carry out architecture related operations.
In domain A, you need to find the schema definitions for these custom attributes and export them to an LDIF (LDAP Data Interchange Format) file.
In the generated LDIF file, you need to navigate to the section that contains your custom attribute definition and remove domain specific OIDs (object identifiers) and any other non generic attributes.
In domain B, you will need to use the ldifde tool to import the modified LDIF file to extend the schema.
After the operation is completed, you can use the repadmin tool to verify that the changes have been successfully synchronized.
Conduct testing to ensure that custom attributes work as expected.
Note: Before making changes to the Active Directory schema, please ensure that you have a complete backup. Due to the high permission requirements for architecture operations and the potential impact of changes on the entire AD environment, it is recommended to have experienced professionals familiar with AD perform the operations and avoid peak usage hours.
Import or export directory objects using ldifde
https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc758935(v=ws.10)
https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/cc731033(v=ws.11)
I hope the information above is helpful.
If you have any questions or concerns, please feel free to let us know.

Best Regards,
Daisy Zhou

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-01-19*

Have a look at an example to add an attribute here:
https://mariusene.com/2024/01/19/active-directory-schema-extension-example/
Note that you will need to know which is the class you want to inherit from. Make sure you know what you are doing because once you create the new class you cannot delete it. Also I would suggest doing it first in a test environment.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-01-18*

Hi @Khushi kumari 

If you want add custom attribute , you have to extend schema as mentioned in Microsoft articles below:

Extending the Active Directory Schema
How to extend the schema

Pleasr don't forget to accept helpful answer
