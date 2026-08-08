---
title: "error when trying to generate kerberos keytab file using ktpass"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/305816/error-when-trying-to-generate-kerberos-keytab-file
question_id: 305816
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# error when trying to generate kerberos keytab file using ktpass

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/305816/error-when-trying-to-generate-kerberos-keytab-file (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

hi We are running windows server 2019 standard V 10.0 (17763) I have completed this exact same procedure before without any issues on different domain controllers but all the same configuration and setup but today i am having an issue generating the kerberos keytab file on windows server. This is the command i use ktpass -princ HTTP/proxy.org@.ORG -mapuser <user login name>@.org -pass <password> -crypto all -ptype KRB5_NT_PRINCIPAL -out fpx.keytab I get this error Targeting domain controller: ???.org Successfully mapped HTTP/proxy.org to <user login name>. Password successfully set! WARNING: pType and account type do not match. This might cause problems. Key created. The keytab file does not get created. I have treble checked the AD user on the DC , removed it re added it, checked the password is correct , all is fine. I have treble checked all the user names are correct, the domain names and the REALM and have now hit a brick wall. I have checked with our support team that the DC has the exact same configuration as previous DC's that i have successfully generated the keytab files so i am not doing anything different. The Domain controller can resolve the proxy name so DNS is fine Can you help please many thanks mac

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-10*

Hello @mac9873  ,

Thank you for posting here.

I have done a test in my lab.

1.Create an account chao in a.local domain.

2.Run command:  

ktpass /princ host/chao.a.local@A.LOCAL /mapuser chao /pass Zcl1234qwer!!@@ /out machine.keytab /crypto all /ptype KRB5_NT_PRINCIPAL /mapop set  

3.Run command:  

ktpass /princ host/chao.a.local@A.LOCAL /mapuser chao /pass Zcl1234qwer!!@@ /out machine.keytab /crypto all /ptype KRB5_NT_PRINCIPAL -out fpx.keytab  

Please check carefully if the command you are running is correct or not.

For more information baout ktpass, please refer to the link below.  

ktpass  

https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ktpass

Hope the information above is helpful.

Should you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou
