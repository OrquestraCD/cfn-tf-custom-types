# Terraform::NewRelic::Dashboard

Use this resource to create and manage New Relic dashboards.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NewRelic::Dashboard",
    "Properties" : {
        "<a href="#editable" title="Editable">Editable</a>" : <i>String</i>,
        "<a href="#icon" title="Icon">Icon</a>" : <i>String</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>,
        "<a href="#visibility" title="Visibility">Visibility</a>" : <i>String</i>,
        "<a href="#filter" title="Filter">Filter</a>" : <i>[ <a href="filter.md">Filter</a>, ... ]</i>,
        "<a href="#widget" title="Widget">Widget</a>" : <i>[ <a href="widget.md">Widget</a>, ... ]</i>,
        "<a href="#comparewith" title="CompareWith">CompareWith</a>" : <i>[ <a href="comparewith.md">CompareWith</a>, ... ]</i>,
        "<a href="#metric" title="Metric">Metric</a>" : <i>[ <a href="metric.md">Metric</a>, ... ]</i>,
        "<a href="#presentation" title="Presentation">Presentation</a>" : <i>[ <a href="presentation.md">Presentation</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NewRelic::Dashboard
Properties:
    <a href="#editable" title="Editable">Editable</a>: <i>String</i>
    <a href="#icon" title="Icon">Icon</a>: <i>String</i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
    <a href="#visibility" title="Visibility">Visibility</a>: <i>String</i>
    <a href="#filter" title="Filter">Filter</a>: <i>
      - <a href="filter.md">Filter</a></i>
    <a href="#widget" title="Widget">Widget</a>: <i>
      - <a href="widget.md">Widget</a></i>
    <a href="#comparewith" title="CompareWith">CompareWith</a>: <i>
      - <a href="comparewith.md">CompareWith</a></i>
    <a href="#metric" title="Metric">Metric</a>: <i>
      - <a href="metric.md">Metric</a></i>
    <a href="#presentation" title="Presentation">Presentation</a>: <i>
      - <a href="presentation.md">Presentation</a></i>
</pre>

## Properties

#### Editable

Determines who can edit the dashboard in an account. Valid values are `all`,  `editable_by_all`, `editable_by_owner`, or `read_only`.  Defaults to `editable_by_all`.
* `widget` - (Optional) A nested block that describes a visualization.  Up to 300 `widget` blocks are allowed in a dashboard definition.  See [Nested widget blocks](#nested-`widget`-blocks) below for details.
* `filter` - (Optional) A nested block that describes a dashboard filter.  Exactly one nested `filter` block is allowed. See [Nested filter block](#nested-`filter`-block) below for details.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Icon

The icon for the dashboard.  Valid values are `adjust`, `archive`, `bar-chart`, `bell`, `bolt`, `bug`, `bullhorn`, `bullseye`, `clock-o`, `cloud`, `cog`, `comments-o`, `crosshairs`, `dashboard`, `envelope`, `fire`, `flag`, `flask`, `globe`, `heart`, `leaf`, `legal`, `life-ring`, `line-chart`, `magic`, `mobile`, `money`, `none`, `paper-plane`, `pie-chart`, `puzzle-piece`, `road`, `rocket`, `shopping-cart`, `sitemap`, `sliders`, `tablet`, `thumbs-down`, `thumbs-up`, `trophy`, `usd`, `user`, and `users`.  Defaults to `bar-chart`.
* `visibility` - (Optional) Determines who can see the dashboard in an account. Valid values are `all` or `owner`.  Defaults to `all`.
* `editable` - (Optional) Determines who can edit the dashboard in an account. Valid values are `all`,  `editable_by_all`, `editable_by_owner`, or `read_only`.  Defaults to `editable_by_all`.
* `widget` - (Optional) A nested block that describes a visualization.  Up to 300 `widget` blocks are allowed in a dashboard definition.  See [Nested widget blocks](#nested-`widget`-blocks) below for details.
* `filter` - (Optional) A nested block that describes a dashboard filter.  Exactly one nested `filter` block is allowed. See [Nested filter block](#nested-`filter`-block) below for details.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

The title of the dashboard.
* `icon` - (Optional) The icon for the dashboard.  Valid values are `adjust`, `archive`, `bar-chart`, `bell`, `bolt`, `bug`, `bullhorn`, `bullseye`, `clock-o`, `cloud`, `cog`, `comments-o`, `crosshairs`, `dashboard`, `envelope`, `fire`, `flag`, `flask`, `globe`, `heart`, `leaf`, `legal`, `life-ring`, `line-chart`, `magic`, `mobile`, `money`, `none`, `paper-plane`, `pie-chart`, `puzzle-piece`, `road`, `rocket`, `shopping-cart`, `sitemap`, `sliders`, `tablet`, `thumbs-down`, `thumbs-up`, `trophy`, `usd`, `user`, and `users`.  Defaults to `bar-chart`.
* `visibility` - (Optional) Determines who can see the dashboard in an account. Valid values are `all` or `owner`.  Defaults to `all`.
* `editable` - (Optional) Determines who can edit the dashboard in an account. Valid values are `all`,  `editable_by_all`, `editable_by_owner`, or `read_only`.  Defaults to `editable_by_all`.
* `widget` - (Optional) A nested block that describes a visualization.  Up to 300 `widget` blocks are allowed in a dashboard definition.  See [Nested widget blocks](#nested-`widget`-blocks) below for details.
* `filter` - (Optional) A nested block that describes a dashboard filter.  Exactly one nested `filter` block is allowed. See [Nested filter block](#nested-`filter`-block) below for details.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Visibility

Determines who can see the dashboard in an account. Valid values are `all` or `owner`.  Defaults to `all`.
* `editable` - (Optional) Determines who can edit the dashboard in an account. Valid values are `all`,  `editable_by_all`, `editable_by_owner`, or `read_only`.  Defaults to `editable_by_all`.
* `widget` - (Optional) A nested block that describes a visualization.  Up to 300 `widget` blocks are allowed in a dashboard definition.  See [Nested widget blocks](#nested-`widget`-blocks) below for details.
* `filter` - (Optional) A nested block that describes a dashboard filter.  Exactly one nested `filter` block is allowed. See [Nested filter block](#nested-`filter`-block) below for details.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No

_Type_: List of <a href="filter.md">Filter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Widget

_Required_: No

_Type_: List of <a href="widget.md">Widget</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompareWith

_Required_: No

_Type_: List of <a href="comparewith.md">CompareWith</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

_Required_: No

_Type_: List of <a href="metric.md">Metric</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Presentation

_Required_: No

_Type_: List of <a href="presentation.md">Presentation</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DashboardUrl

Returns the <code>DashboardUrl</code> value.

#### Id

Returns the <code>Id</code> value.

