Name:		texlive-datetime2-en-fulltext
Version:	36705
Release:	1
Summary:	English Full Text styles for the datetime2 package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/datetime2-en-fulltext
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2-en-fulltext.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2-en-fulltext.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2-en-fulltext.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
English date and time styles that use words for the numbers and
ordinals. This package provides the following date and time
styles: "en-fulltext", "en-FullText", "en-FULLTEXT", and the
additional time style "en-Fulltext". (The date equivalent can
be obtained through commands like \Today.) Unlike the base
styles provided by datetime2.sty, these styles aren't
expandable styles. This means that you can't use the date or
time in PDF bookmarks or in the argument of certain commands,
such as \MakeUppercase, while these styles are in use.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/datetime2-en-fulltext
%{_texmfdistdir}/tex/latex/datetime2-en-fulltext
%doc %{_texmfdistdir}/doc/latex/datetime2-en-fulltext

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
