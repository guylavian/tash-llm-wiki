---
title: "Microsoft Deployment Toolkit (MDT) documentation — pages 1721-1729"
type: reference
domain: sccm
slug: sccm-intune-configmgr-mdt-p1721-1729
tier: reference
source: https://learn.microsoft.com/en-us/intune/configmgr/intune-configmgr-mdt-p1721-1729
family: sccm
documentKind: "doc"
abstract: "Attribute Value Contents Stage Element Attributes Table 103 lists the attributes of the StageGroup element and a description of the attribute. Table 103. Attributes and Corresponding Values for the StageGroup Element ﾉ Expand table Attribute Description DisplayName Specifies the"
---

# Microsoft Deployment Toolkit (MDT) documentation — pages 1721-1729

<!-- p.1721 -->

 Attribute                         Value

 Contents                          Stage

Element Attributes

Table 103 lists the attributes of the StageGroup element and a description of the
attribute.

Table 103. Attributes and Corresponding Values for the
StageGroup Element

                                                                              ﾉ   Expand table

 Attribute     Description

 DisplayName   Specifies the user-friendly name of the stage group displayed in the UDI Wizard
               Designer. This name is usually more descriptive than the Name attribute.

Remarks

None.

Example

None.

StageGroups
This element groups a set of stage groups within a UDI Wizard configuration file.

Element Information

Table 104 provides information about the StageGroups element.

Table 104. StageGroups Element Information

                                                                              ﾉ   Expand table

<!-- p.1722 -->

 Attribute                            Value

 Number of occurrences                Zero or one within a Wizard element

 Parent elements                      Wizard

 Contents                             StageGroup

Element Attributes

This element has no attributes.

Remarks

None.

Example

None.

Setter

This element specifies a property setting for the value for a property that is named in
the Property property.

Element Information

Table 105 provides information about the Setter element.

Table 105. Setter Element Information

                                                                             ﾉ   Expand table

 Attribute               Value

 Number of occurrences   Zero or more within each parent element (This element is optional.)

 Parent elements         Data, DataItem, Page, Style, Task, Validator

 Contents                Contains a string value in the Property attribute

Element Attributes

<!-- p.1723 -->

Table 106 lists the attribute of the Setter element and provides a description of it.

Table 106. Attributes and Corresponding Values for the
Setter Element

                                                                                  ﾉ   Expand table

 Attribute   Description

 Property    Specifies the property name being set. The property name is set to the value that this
             attribute brackets.

Remarks

None.

Example

None.

Stage

This element specifies a Stage within a StageGroup and contains one or more PageRef
elements.

Element Information

Table 107 provides information about the Stage element.

Table 107. Stage Element Information

                                                                                  ﾉ   Expand table

 Attribute                            Value

 Number of occurrences                One or more within a StageGroup element

 Parent elements                      StageGroup

 Contents                             PageRef

<!-- p.1724 -->

Element Attributes

Table 108 lists the attributes of the Stage element and provides a description of each.

Table 108. Attributes and Corresponding Values for the
Stage Element

                                                                                ﾉ   Expand table

 Attribute     Description

 DisplayName   Specifies the user-friendly name of the wizard page displayed in the UDI Wizard
               Designer. This name is usually more descriptive than the Name attribute.

 Name          Specifies the name of the stage. The value of this element is used when starting
               the UDI Wizard with the /stage: name command line parameter.

Remarks

None.

Example

None.

Style

This element groups the individual Setter elements that configure the UDI Wizard look
and feel, including the title shown at the top of the wizard and the banner image shown
on the UDI Wizard.

Element Information

Table 109 provides information about the Style element.

Table 109. Style Element Information

                                                                                ﾉ   Expand table

 Attribute                                                              Value

 Number of occurrences                                                  One

<!-- p.1725 -->

 Attribute                                                         Value

 Parent elements                                                   Wizard

 Contents                                                          Setter

Element Attributes

This element has no attributes.

Remarks

None.

Example

  XML

  <Style>
    <Setter Property="bannerFilename">UDI_Wizard_Banner.bmp</Setter>
    <Setter Property="title">Operating System Deployment (OSD) Refresh
  Wizard</Setter>
  </Style>

Task

This element specifies a task that is to be run on the page specified in the parent Page
element.

Element Information

Table 110 provides information about the Task element.

Table 110. Task Element Information

                                                                            ﾉ   Expand table

 Attribute                           Value

 Number of occurrences               One or more within a Tasks element

 Parent elements                     Tasks

<!-- p.1726 -->

 Attribute                              Value

 Contents                               ExitCodes, File, Setter

Element Attributes

Table 111 lists the attributes of the Task element and provides a description of each.

Table 111. Attributes and Corresponding Values for the
Task Element

                                                                                  ﾉ   Expand table

 Attribute     Description

 DependsOn     Specifies whether the task is dependent on another task. The value of this
               attribute is set to the Name attribute of another Task element. Note: This
               attribute cannot be configured using the UDI Wizard Designer. However, you can
               manually add this attribute to a Task element by directly modifying the .xml file.

 DisplayName   Specifies the user-friendly name of the task displayed in the UDI Wizard Designer.
               This name is usually more descriptive than the Name attribute.

 Name          Specifies the name of the task. This name must be unique.

 Type          Specifies the task type for the task to be run, which is defined in the DLL that
               contains the task.

Remarks

None.

Example

None.

Tasks

This element groups a set of tasks for a Page element.

Element Information

Table 112 provides information about the Tasks element.

<!-- p.1727 -->

Table 112. Tasks Element Information

                                                                                   ﾉ   Expand table

 Attribute                    Value

 Number of occurrences        Zero or one within each Page element (This element is optional.)

 Parent elements              Page

 Contents                     Task

Element Attributes

Table 113 lists the attributes of the Tasks element and provides a description of each.

Table 113. Attributes and Corresponding Values for the
Tasks Element

                                                                                   ﾉ   Expand table

 Attribute     Description

 NameTitle     Specifies the caption that appears at the top of the column that contains the name
               of the tasks in the appropriate wizard page.

 StatusTitle   Specifies the caption that appears at the top of the column that contains the status
               of the tasks in the appropriate wizard page.

Remarks

None.

Example

None.

Validator
This element specifies a validator for the field control that is specified in the parent Field
element.

<!-- p.1728 -->

Element Information

Table 114 provides information about the Validator element.

Table 114. Validator Element Information

                                                                                    ﾉ   Expand table

 Attribute                                  Value

 Number of occurrences                      Zero or one within a Field element

 Parent elements                            Field

 Contents                                   Setter

Element Attributes

Table 115 lists the attribute of the Validator element and provides a description of it.

Table 115. Attributes and Corresponding Values for the
Validator Element

                                                                                    ﾉ   Expand table

 Attribute   Description

 Type        Specifies the type for the validator, which is defined in the DLL that contains the
             validator

Remarks

None.

Example

None.

Wizard

This element specifies the root for all other elements.

<!-- p.1729 -->

Element Information

Table 116 provides information about the Wizard element.

Table 116. Wizard Element Information

                                                                            ﾉ   Expand table

 Attribute                                Value

 Number of occurrences                    One

 Parent elements                          None

 Contents                                 DLLs, Pages, StageGroups, Style

Element Attributes

This element has no attributes.

Remarks

None.

Example

  C#

  <Wizard>
     + <DLLs>
     + <Style>
     + <Pages>
     + <StageGroups>
  </Wizard>

Feedback
Was this page helpful?      Yes    No

Provide product feedback
