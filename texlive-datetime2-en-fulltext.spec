%global tl_name datetime2-en-fulltext
%global tl_revision 36705

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	English Full Text styles for the datetime2 package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/datetime2-contrib/datetime2-en-fulltext
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2-en-fulltext.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2-en-fulltext.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2-en-fulltext.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
English date and time styles that use words for the numbers and
ordinals. This package provides the following date and time styles: "en-
fulltext", "en-FullText", "en-FULLTEXT", and the additional time style
"en-Fulltext". (The date equivalent can be obtained through commands
like \Today.) Unlike the base styles provided by datetime2.sty, these
styles aren't expandable styles. This means that you can't use the date
or time in PDF bookmarks or in the argument of certain commands, such as
\MakeUppercase, while these styles are in use.

