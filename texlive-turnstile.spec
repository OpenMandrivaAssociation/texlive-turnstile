%global tl_name turnstile
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Typeset the (logic) turnstile notation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/turnstile
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/turnstile.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/turnstile.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/turnstile.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Among other uses, the turnstile sign is used by logicians for denoting a
consequence relation, related to a given logic, between a collection of
formulas and a derived formula.

