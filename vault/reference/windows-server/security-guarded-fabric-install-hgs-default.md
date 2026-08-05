---
title: "Install HGS in a new forest"
type: reference
domain: windows-server
slug: security-guarded-fabric-install-hgs-default
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/security/guarded-fabric-shielded-vm/guarded-fabric-install-hgs-default
family: security
documentKind: "install-set-up-deploy"
abstract: "Learn more about: Install HGS in a new forest"
---

# Install HGS in a new forest

# Install HGS in a new forest

## Add the HGS server role

Run the following commands in an elevated PowerShell session to add the HGS server role and install HGS.

[!INCLUDE [Install the HGS server role](../../../includes/guarded-fabric-install-hgs-server-role.md)]

## Install HGS

[!INCLUDE [Install HGS by default](../../../includes/install-hgs-default.md)]

## Next steps

- For the next steps to set up TPM-based attestation, see [Initialize the HGS cluster using TPM mode in a new dedicated forest (default)](guarded-fabric-initialize-hgs-tpm-mode-default.md).
- For the next steps to set up host key attestation, see [Initialize the HGS cluster using key mode in a new dedicated forest (default)](guarded-fabric-initialize-hgs-key-mode-default.md).
- For the next steps to set up Admin-based attestation (deprecated in Windows Server 2019), see [Initialize the HGS cluster using AD mode in a new dedicated forest (default)](guarded-fabric-initialize-hgs-ad-mode-default.md).

## Next step

> [!div class="nextstepaction"]
> [Initialize HGS](guarded-fabric-initialize-hgs.md)
