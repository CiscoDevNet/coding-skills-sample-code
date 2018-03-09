# DevNet Writing Guidelines (Public)

Welcome to the DevNet Writing Guidelines. This repo contains DevNet's guidelines on creating learning labs, code samples, slides and setting up sandboxes for labs. 

The topics below are some of the topics of most interest to newbies.  For more the complete set of writing guidelines see this repo's [wiki](https://github.com/CiscoDevNet/devnet-writing-guidelines/wiki) page.

<b>On this page</b><br>

> [Learning Labs](#learning-labs)<br>
    [How do I author a learning lab?](#learning-labs)<br>
>   [Templates](#templates)<br>
> [Code Conventions](#code-conventions)<br>
> [Author Scripts](##author-scripts)<br>
> [Recommended Tools](##recommended-tools)<br>

## Learning Labs

The source markdown for all of DevNet's learning labs are stored in the repos of the [CiscoDevNet](https://github.com/CiscoDevNet) organization. 

If you want to create and publish a lab on the DevNet site, you must commit the lab and its associated files to a repo within the [CiscoDevNet](https://github.com/CiscoDevNet) organization.  The lab's markdown, images, JSON metadata, etc must exist in a certain directory structure.  The next section explains how to do that. 

### How do I author a learning lab?

See the wiki page: [How To Create A New Lab](https://github.com/CiscoDevNet/devnet-writing-guidelines/wiki/How-To-Create-A-New-Lab)

### Templates

There are two kinds of templates: one for labs and one for sample code. 

#### Lab template

The learning lab template is stored in the following directory:

> https://github.com/CiscoDevNet/devnet-writing-guidelines/tree/master/labs


#### Sample Code template

The template for code samples is here:

> https://github.com/CiscoDevNet/devnet-writing-guidelines/tree/master/code-samples

## Code Conventions

See the [wiki](https://github.com/CiscoDevNet/devnet-writing-guidelines/wiki) for the style guide on DevNet coding conventions.


## Author Scripts

The `scripts` folder contains python scripts that might be useful when authoring. You do not have to use these scripts to author labs. They are just helpful tools that other authors have created.

For example, the `create_new_lab.py` script creates a directory structure and copies the template used to create a new lab. You could do the same thing manually.


## Recommended Tools

Check the [wiki](https://github.com/CiscoDevNet/devnet-writing-guidelines/wiki/Tools-to-Write-Learning-Labs) section for recommended tools.
