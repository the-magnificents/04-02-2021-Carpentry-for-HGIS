# Social coding on GitHub and version control with Git

This lesson is focused on understanding and implementing version control with Git to keep track of changes to a code-based project. We'll talk about the utility of version control systems for tracking changes to local projects, and how it can be used to enable remote collaboration and crediting of multiple authors to a project hosted in a remote repository like GitHub. This material draws from the [Version Control with Git](https://swcarpentry.github.io/git-novice/) lesson from the Software Carpentries. It uses the [Gizmo repository](https://github.com/wmvanvliet/gizmo) from wmvanvliet on GitHub as a basis for Python challenges and to illustrate a track changes workflow.

## Background

Version control is the lab notebook of the digital world: it’s what professionals use to keep track of what they’ve done and to collaborate with other people. Every large software development project relies on it, and most programmers use it for their small jobs as well. And it isn’t just for software code: books, papers, small data sets, and anything that changes over time or needs to be shared can and should be stored in a version control system.

A version control system is a tool that keeps track of these changes for us, effectively creating different versions of our files. It allows us to decide which changes will be made to the next version (each record of these changes is called a commit), and keeps useful metadata about them. The complete history of commits for a particular project and their metadata make up a repository. Repositories can be kept in sync across different computers, facilitating collaboration among different people. Version control systems start with a base version of the document and then record changes you make each step of the way. You can think of it as a recording of your progress: you can rewind to start at the base document and play back each change you made, eventually arriving at your more recent version.

## Remote collaboration

Collaborative writing or scripting with traditional word processors and text editors is cumbersome. Either every collaborator has to work on a document sequentially (slowing down the process of writing), or you have to send out a version to all collaborators and manually merge their comments into your document. The ‘track changes’ or ‘record changes’ option can highlight changes for you and simplifies merging, but as soon as you accept changes you will lose their history. You will then no longer know who suggested that change, why it was suggested, or when it was merged into the rest of the document. 

Some word processors let us deal with this a little better, such as Microsoft Word’s Track Changes, Google Docs’ version history, but they lack a streamlined way to customise messages about changes made and store just one latest version of the file for everyone working on it. It seems ridiculous to have multiple nearly-identical versions of the same document that we keep passing back and forth to create something whole. The result is a lot of files with names like Final_paper_EDIT01.doc or Final_paper_EDITCOMMITTEE03.doc and so on...it can get messy trying to merge suggestions and changes made by multiple people in multiple documents, sent over email...I'm sure we all know the headache!

When using a remote collaboration like Git Hub, unless multiple users make changes to the same section of the document - a conflict - you can incorporate two sets of changes into the same base document.

From [GitHub Guides](https://guides.github.com/activities/hello-world/): "GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere." GitHub hosts code and all files for each project in a **repository**, sometimes shortened to "repo". A repository on GitHub is free to create, you can add contributing members and collaborators with different permission settings as you please, and you can access it with a unique URL.

## Individual work
Teams are not the only ones to benefit from version control: lone researchers can benefit immensely. Keeping a record of what was changed, when, and why is extremely useful for all researchers if they ever need to come back to the project later on (e.g., a year later, when memory has faded).

## Setup for this lesson
Make sure you have a GitHub account and have opened your browser to www.github.com and signed in. 