---
title: "Troubleshooting installation issues"
type: reference
domain: openshift
slug: microshift-troubleshooting-4-22-microshift-installing-troubleshooting
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/microshift_troubleshooting/microshift-installing-troubleshooting
version: 4.22
family: microshift_troubleshooting
documentKind: "Documentation"
---

# Troubleshooting installation issues

[id="microshift-installing-troubleshooting"]
= Troubleshooting installation issues

[role="_abstract"]
To troubleshoot a failed {microshift-short} installation, you can run an `sosreport` archive. Use the `sos report` command to generate a detailed report that shows all of the enabled plugins and data from the different components and applications in a system.

// Module included in the following assemblies:

// * microshift_support/microshift-sos-report

[id="gathering-data-microshift-sos-report_{context}"]
= Gathering data from an sos report

[role="_abstract"]
You can create an `sosreport` archive about a failing {op-system-full} host that you can share with Red{nbsp}Hat support for troubleshooting.

.Prerequisites

* You must have the `sos` package installed.
* You have root access to the host.

.Procedure

. Log in to the failing host as a root user.

. Perform the debug report creation procedure by running the following command:
+
[source,terminal]
----
$ microshift-sos-report
----
+
.Example output
[source,terminal]
----
sosreport (version 4.5.1)

This command will collect diagnostic and configuration information from
this Red Hat Enterprise Linux system and installed applications.

An archive containing the collected information will be generated in
/var/tmp/sos.o0sznf_8 and may be provided to a Red Hat support
representative.

Any information provided to Red Hat will be treated in accordance with
the published support policies at:

        Distribution Website : https://www.redhat.com/
        Commercial Support   : https://www.access.redhat.com/

The generated archive may contain data considered sensitive and its
content should be reviewed by the originating organization before being
passed to any third party.

No changes will be made to system configuration.

 Setting up archive ...
 Setting up plugins ...
 Running plugins. Please wait ...

  Starting 1/2   microshift      [Running: microshift]
  Starting 2/2   microshift_ovn  [Running: microshift microshift_ovn]
  Finishing plugins              [Running: microshift]

  Finished running plugins

Found 1 total reports to obfuscate, processing up to 4 concurrently

sosreport-microshift-rhel9-2023-03-31-axjbyxw :    Beginning obfuscation...
sosreport-microshift-rhel9-2023-03-31-axjbyxw :    Obfuscation completed

Successfully obfuscated 1 report(s)

Creating compressed archive...

A mapping of obfuscated elements is available at
	/var/tmp/sosreport-microshift-rhel9-2023-03-31-axjbyxw-private_map

Your sosreport has been generated and saved in:
	/var/tmp/sosreport-microshift-rhel9-2023-03-31-axjbyxw-obfuscated.tar.xz

 Size	444.14KiB
 Owner	root
 sha256	922e5ff2db25014585b7c6c749d2c44c8492756d619df5e9838ce863f83d4269

Please send this file to your support representative.
----

[id="additional-resources_microshift-installing-troubleshooting"]
[role="_additional-resources"]
== Additional resources
* About {microshift-short} sos reports

* Generating an sos report for technical support
