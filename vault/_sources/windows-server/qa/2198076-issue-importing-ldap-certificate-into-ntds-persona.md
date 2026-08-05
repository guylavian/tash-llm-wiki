---
title: "Issue Importing LDAP certificate into NTDS personal store for a server core 2016 server."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2198076/issue-importing-ldap-certificate-into-ntds-persona
question_id: 2198076
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-directory-services-certificates-pki"]
---
# Issue Importing LDAP certificate into NTDS personal store for a server core 2016 server.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2198076/issue-importing-ldap-certificate-into-ntds-persona (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are trying to copy/ import a LDAP certificate from a servers personal store to the NTDS personal store, however the server the certificate/ private key is on is Windows Server Core 2016. We have tried connecting remotely to the server certificate store and importing the cert, but it says you can't import a .pfx into a remote certificate store. Tried powershell commands to copy the cert aswell but similar issues. How do we get the Certificate imported so it can be used? Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-05*

Hello RFletch01,  

Good day!

Thank you for your reply and update.  

I am so glad that the problem has been resolved.  

Have a nice day!  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-02*

We did then follow the Microsoft link to manually import the reg key and that worked. Many thanks for your help.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-02*

Thank you for the detailed reply. Unfortunately i was unable to export the certificate as it comes back with - CertUtil: Unknown arg: -exportcert (i did also just try -export but same issue). And if i run CertUtil -? it doesn't list the option for exporting.

I managed to export the certificate through the Digicert utility in the end and so then tried the import command suggested, however i then get another error - Cannot open existing Cert store.  Use -f option to force Cert store creation. CertUtil: -addstore command FAILED: 0x80070002 (WIN32: 2 ERROR_FILE_NOT_FOUND). CertUtil: The system cannot find the file specified.

Many thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2024-02-02*

Hello RFletch01,

Thank you for posting on the Microsoft Community Forum.  

Did you perform all the operations you mentioned on the server core 2016?

To import a certificate into the NTDS personal store on a Windows Server Core 2016 server, you can use the Certutil command-line tool. Here are the steps:

-  Copy the .pfx file containing the certificate and private key to the server core machine.

-  Open a command prompt with administrative privileges.

-  Run the following command to import the certificate into the local machine personal store:

  “certutil -importpfx <path_to_pfx_file>”

   Replace “<path_to_pfx_file>” with the full path to the .pfx file.

-  Run the following command to export the certificate from the local machine personal store to a .cer file:

   “certutil -exportcert -user -p <password> <thumbprint> <path_to_cer_file>”

Replace “<password>” with the password used to protect the private key in the .pfx file, “<thumbprint>” with the thumbprint of the certificate in the local machine personal store (you can find it by running “certutil -store My”), and “<path_to_cer_file>” with the full path to the .cer file.

-  Copy the .cer file to the server core machine.

-  Run the following command to import the certificate into the NTDS personal store:

   “certutil -addstore NTDS <path_to_cer_file>”

   Replace “<path_to_cer_file>” with the full path to the .cer file.

After completing these steps, the certificate should be available in the NTDS personal store and can be used for LDAP authentication.

For more information about this, please refer to links below.

Import PFX / P12 File to the NTDS Service Personal Certificate Store [Server Core Workaround] | Microsoft Learn.Certutil | Microsoft Learn.

You can also refer to this, but this is imported into the 2008 sever core: Importing SSL certificates into Windows 2008 Server Core | Microsoft Learn

I hope you the information above is helpful.

If you have any questions or concerns, please do not hesitate to let us know.

Best Regards,

Daisy Zhou
