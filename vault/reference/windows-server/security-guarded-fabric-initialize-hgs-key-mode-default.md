---
title: "Initialize the HGS cluster using key mode in a new dedicated forest (default)"
type: reference
domain: windows-server
slug: security-guarded-fabric-initialize-hgs-key-mode-default
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/security/guarded-fabric-shielded-vm/guarded-fabric-initialize-hgs-key-mode-default
family: security
documentKind: "how-to"
abstract: "Learn more about: Initialize the HGS cluster using key mode in a new dedicated forest (default)"
---

# Initialize the HGS cluster using key mode in a new dedicated forest (default)

# Initialize the HGS cluster using key mode in a new dedicated forest (default)


1.  [!INCLUDE [Initialize HGS](../../../includes/guarded-fabric-initialize-hgs-default-step-one.md)]
2.  [!INCLUDE [Obtain certificates for HGS](../../../includes/guarded-fabric-initialize-hgs-default-step-two.md)]

3.  Run [Initialize-HgsServer](/powershell/module/hgsserver/initialize-hgsserver) in an elevated PowerShell window on the first HGS node. The syntax of this cmdlet supports many different inputs, but the 2 most common invocations are below:

    -   If you are using PFX files for your signing and encryption certificates, run the following commands:

        ```powershell
        $signingCertPass = Read-Host -AsSecureString -Prompt "Signing certificate password"
        $encryptionCertPass = Read-Host -AsSecureString -Prompt "Encryption certificate password"

        Initialize-HgsServer -HgsServiceName 'MyHgsDNN' -SigningCertificatePath '.\signCert.pfx' -SigningCertificatePassword $signingCertPass -EncryptionCertificatePath '.\encCert.pfx' -EncryptionCertificatePassword $encryptionCertPass -TrustHostkey
        ```

    -   If you are using non-exportable certificates that are installed in the local certificate store, run the following command. If you do not know the thumbprints of your certificates, you can list available certificates by running `Get-ChildItem Cert:\LocalMachine\My`.

        ```powershell
        Initialize-HgsServer -HgsServiceName 'MyHgsDNN' -SigningCertificateThumbprint '1A2B3C4D5E6F...' -EncryptionCertificateThumbprint '0F9E8D7C6B5A...' --TrustHostKey
        ```

4.  [!INCLUDE [Initialize HGS](../../../includes/guarded-fabric-initialize-hgs-default-step-four.md)]

5.  [!INCLUDE [Initialize HGS](../../../includes/guarded-fabric-initialize-hgs-default-step-five.md)]


## Next step

> [!div class="nextstepaction"]
> [Create host key](guarded-fabric-create-host-key.md)
