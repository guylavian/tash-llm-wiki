---
title: "Remove exchange contact internal smtp addresses"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1853249/remove-exchange-contact-internal-smtp-addresses
question_id: 1853249
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-hybrid-management", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-powershell"]
---
# Remove exchange contact internal smtp addresses

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1853249/remove-exchange-contact-internal-smtp-addresses (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am looking for a way to remove the internal email addresses created when creating a mail contact in Exchange 2019.  I can go into each account in Active Directory and remove them but I would rather do it with PowerShell if possible.  Specifically using the import-csv command.  Does anyone know if that is possible?

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-02*

Thank you both for your help.  It didn't work exactly like I wanted so a co worker of mine made some changes to it and now it works perfectly!!  You saved me a lot of time.  I put the modified script below.

$mailContacts = Import-Csv -Path "C:\XXXX\MailContactsToUpdate.csv"

#Loop through each contact in the CSV

foreach ($contact in $mailContacts){

```
# Get the email address from the CSV

$emailAddress = $contact.'Email Address'

# Get the mail contact

$mailContact = Get-MailContact -Identity $emailAddress -ErrorAction SilentlyContinue

# Check if the mail contact exists

if ($mailContact) {

    # Get the current email address (proxy addresses)

    $currentEmailAddresses = $mailContact.EmailAddresses

    # Remove only internal email addresses (proxy addresses starting with "SMTP:")

    $updatedEmailAddresses = $currentEmailAddresses | Where-Object { $_ -Clike 'SMTP:*' }

    # Allows the set-mailcontact command to run

    Get-Mailcontact -Identity $mailContact.Name | Set-Mailcontact -EmailAddressPolicyEnabled $false

    # Set the updated email addresses

    Set-MailContact -Identity $emailAddress -EmailAddresses $updatedEmailAddresses -ErrorAction Stop

    Write-Host "Updated: $emailAddress"

} else {

    Write-Host "Mail contact not found: $emailAddress"

}
```

}

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-02*

Hello Stace 

Here is PowerShell script:

Import the CSV file

$mailContacts = Import-Csv -Path "C:\Path\To\MailContactsToUpdate.csv"

Loop through each contact in the CSV

foreach ($contact in $mailContacts) {

```
# Get the email address from the CSV

$emailAddress = $contact.EmailAddress

# Get the mail contact

$mailContact = Get-MailContact -Identity $emailAddress -ErrorAction SilentlyContinue

# Check if the mail contact exists

if ($mailContact) {

    # Get the current email address (proxy addresses)

    $currentEmailAddresses = $mailContact.EmailAddresses

    # Remove only internal email addresses (proxy addresses starting with "SMTP:")

    $updatedEmailAddresses = $currentEmailAddresses | Where-Object { $_ -notlike 'SMTP:*' }

    # Set the updated email addresses

    Set-MailContact -Identity $emailAddress -EmailAddresses $updatedEmailAddresses -ErrorAction Stop

    Write-Host "Updated: $emailAddress"

} else {

    Write-Host "Mail contact not found: $emailAddress"

}
```

}
