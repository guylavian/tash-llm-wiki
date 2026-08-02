---
title: "DHCP Logging Events for DNS Record Registrations"
type: reference
domain: windows-server
slug: networking-dhcp-dns-events
tier: reference
source: https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-dns-events
family: networking
documentKind: "how-to"
abstract: "This topic provides information about DHCP server logging events in Windows Server 2016."
---

# DHCP Logging Events for DNS Record Registrations

# DHCP Logging Events for DNS Registrations

DHCP server event logs now provide detailed information about DNS registration failures.

>[!NOTE]
>In many cases, the reason for DNS record registration failures by DHCP servers is that a DNS Reverse\-Lookup Zone is either configured incorrectly or not configured at all.

The following new DHCP events assist you to easily identify when DNS registrations are failing because of a misconfigured or missing DNS Reverse\-Lookup Zone.

|ID|Event|Value|
|-----|--------------------|--------------------------------------------------------|
|20317|DHCPv4.ForwardRecordDNSFailure|Forward record registration for IPv4 address %1 and FQDN %2 failed with error %3. This is likely to be because the forward lookup zone for this record does not exist on the DNS server.|
|20318|DHCPv4.ForwardRecordDNSTimeout|Forward record registration for IPv4 address %1 and FQDN %2 failed with error %3.|
|20319|DHCPv4.PTRRecordDNSFailure|PTR record registration for IPv4 address %1 and FQDN %2 failed with error %3. This is likely to be because the reverse lookup zone for this record does not exist on the DNS server.|
|20320|DHCPv4.PTRRecordDNSTimeout|PTR record registration for IPv4 address %1 and FQDN %2 failed with error %3.|
|20321|DHCPv6.ForwardRecordDNSFailure|Forward record registration for IPv6 address %1 and FQDN %2 failed with error %3. This is likely to be because the forward lookup zone for this record does not exist on the DNS server.|
|20322|DHCPv6.ForwardRecordDNSTimeout|Forward record registration for IPv6 address %1 and FQDN %2 failed with error %3.|
|20323|DHCPv6.PTRRecordDNSFailure|PTR record registration for IPv6 address %1 and FQDN %2 failed with error %3. This is likely to be because the reverse lookup zone for this record does not exist on the DNS server.|
|20324|DHCPv6.PTRRecordDNSTimeout|PTR record registration for IPv6 address %1 and FQDN %2 failed with error %3.|
|20325|DHCPv4.ForwardRecordDNSError|PTR record registration for IPv4 address %1 and FQDN %2 failed with error %3 \(%4\).|
|20326|DHCPv6.ForwardRecordDNSError|Forward record registration for IPv6 address %1 and FQDN %2 failed with error %3 \(%4\)|
|20327|DHCPv6.PTRRecordDNSError|PTR record registration for IPv6 address %1 and FQDN %2 failed with error %3 \(%4\).|
