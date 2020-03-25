# Terraform::VSphere::VirtualMachine Clone

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#linkedclone" title="LinkedClone">LinkedClone</a>" : <i>Boolean</i>,
    "<a href="#ovfnetworkmap" title="OvfNetworkMap">OvfNetworkMap</a>" : <i>[ <a href="clone-ovfnetworkmap.md">OvfNetworkMap</a>, ... ]</i>,
    "<a href="#ovfstoragemap" title="OvfStorageMap">OvfStorageMap</a>" : <i>[ <a href="clone-ovfstoragemap.md">OvfStorageMap</a>, ... ]</i>,
    "<a href="#templateuuid" title="TemplateUuid">TemplateUuid</a>" : <i>String</i>,
    "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
    "<a href="#customize" title="Customize">Customize</a>" : <i>[ <a href="clone-customize.md">Customize</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#linkedclone" title="LinkedClone">LinkedClone</a>: <i>Boolean</i>
<a href="#ovfnetworkmap" title="OvfNetworkMap">OvfNetworkMap</a>: <i>
      - <a href="clone-ovfnetworkmap.md">OvfNetworkMap</a></i>
<a href="#ovfstoragemap" title="OvfStorageMap">OvfStorageMap</a>: <i>
      - <a href="clone-ovfstoragemap.md">OvfStorageMap</a></i>
<a href="#templateuuid" title="TemplateUuid">TemplateUuid</a>: <i>String</i>
<a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
<a href="#customize" title="Customize">Customize</a>: <i>
      - <a href="clone-customize.md">Customize</a></i>
</pre>

## Properties

#### LinkedClone

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OvfNetworkMap

_Required_: No

_Type_: List of <a href="clone-ovfnetworkmap.md">OvfNetworkMap</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OvfStorageMap

_Required_: No

_Type_: List of <a href="clone-ovfstoragemap.md">OvfStorageMap</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateUuid

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Customize

_Required_: No

_Type_: List of <a href="clone-customize.md">Customize</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

