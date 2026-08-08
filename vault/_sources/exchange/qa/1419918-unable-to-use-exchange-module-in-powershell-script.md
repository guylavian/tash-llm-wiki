---
title: "Unable to use Exchange Module in PowerShell script - No sign-in window"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1419918/unable-to-use-exchange-module-in-powershell-script
question_id: 1419918
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online", "windows-business-windows-server-user-experience-powershell"]
---
# Unable to use Exchange Module in PowerShell script - No sign-in window

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1419918/unable-to-use-exchange-module-in-powershell-script (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am currently using a powershell script for some management tasks. This script runs a WPF UI for gathering data from the user and then uses those inputs in some powershell functions. This worked well for a while but now it does nothing. When i run this particular function, the interactive sign-in window just doesn't show. I've tried removing all switches from the connect-exchange and still nothing.

Anyone have any ideas?

```
function ExchangeOffboard {
    
    try {

        Write-Host "Getting email"

        if ($WPFcmbTech.Text -eq 'User 1') { #WPFcmb is a combobox

            $offboarderemail = "******@domain.co.uk" 
            
        }
        elseif ($WPFcmbTech.Text -eq 'User 2') {
            $offboarderemail = "******@domain.co.uk"
            
        }
        elseif ($WPFcmbTech.Text -eq 'User 3'){
            $offboarderemail = "******@domain.co.uk"
        }
        else {       
        }

        Import-Module ExchangeOnlineManagement

        Write-Host ("Connecting to Exchange with email: " + $offboarderemail)
        Connect-ExchangeOnline -UserPrincipalName $offboarderemail -ShowBanner:$false #connect to exchange
        Write-Host "Exchange Connected"
       

        Start-Sleep -s 1

        Write-Host "Finding mailbox address"
        $userGetUser = Get-ADUser -Filter {SamAccountName -eq $WPFtxtUsername.Text} -Properties mail
        $userEmail = $userGetUser.mail
        Write-Host ("Found address " + $userEmail)

        Write-Host "Setting mailbox to shared"
        Set-Mailbox -Identity $userEmail -Type Shared
        [System.Windows.Forms.MessageBox]::Show($userEmail + " has been changed to a shared mailbox.")

        if ($WPFchkDelegateRequired.IsChecked -eq $true){
            
            Add-MailboxPermission -Identity $userEmail -User $WPFtxtDelegate.Text -AccessRights FullAccess
            start-sleep -s 2
            [System.Windows.Forms.MessageBox]::Show($WPFtxtDelegate.Text + " has been given full access to the mailbox.")
        }
    }
    catch {
        Write-Warning "Error occurred while performing Exchange mailbox operations: $($_.Exception.Message)"
        [System.Windows.Forms.MessageBox]::Show("An error occurred during the Exchange mailbox operations.")
    }
    finally {
        # Ensure the connection to Exchange Online is disconnected at the end of the function.
        Disconnect-ExchangeOnline -Confirm:$false
    }
    return
}
```

## Answers

_No answers on this thread._
