# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/turnstile
# catalog-date 2008-08-24 14:43:48 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-turnstile
Version:	1.0
Release:	7
Summary:	Typeset the (logic) turnstile notation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/turnstile
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/turnstile.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/turnstile.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/turnstile.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Among other uses, the turnstile sign is used by logicians for
denoting a consequence relation, related to a given logic,
between a collection of formulas and a derived formula.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/turnstile/turnstile.sty
%doc %{_texmfdistdir}/doc/latex/turnstile/README
%doc %{_texmfdistdir}/doc/latex/turnstile/README.en
%doc %{_texmfdistdir}/doc/latex/turnstile/README.pt
%doc %{_texmfdistdir}/doc/latex/turnstile/turnstile-en.pdf
%doc %{_texmfdistdir}/doc/latex/turnstile/turnstile-pt.pdf
%doc %{_texmfdistdir}/doc/latex/turnstile/turnstile_article.pdf
%doc %{_texmfdistdir}/doc/latex/turnstile/turnstile_article.tex
%doc %{_texmfdistdir}/doc/latex/turnstile/turnstile_artigo.pdf
%doc %{_texmfdistdir}/doc/latex/turnstile/turnstile_artigo.tex
#- source
%doc %{_texmfdistdir}/source/latex/turnstile/turnstile-en.dtx
%doc %{_texmfdistdir}/source/latex/turnstile/turnstile-en.ins
%doc %{_texmfdistdir}/source/latex/turnstile/turnstile-pt.dtx
%doc %{_texmfdistdir}/source/latex/turnstile/turnstile-pt.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 757158
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719817
- texlive-turnstile
- texlive-turnstile
- texlive-turnstile

