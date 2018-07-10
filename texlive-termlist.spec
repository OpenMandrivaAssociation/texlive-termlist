# revision 18923
# category Package
# catalog-ctan /macros/latex/contrib/termlist
# catalog-date 2010-06-12 14:14:46 +0200
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-termlist
Version:	1.1
Release:	11
Summary:	Label any kind of term with a continuous counter
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/termlist
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/termlist.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/termlist.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/termlist.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The termlist package provides environments to indent and label
any kind of terms with a continuous number. Candidate terms may
appear inside an equation or eqnarray environment.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/termlist/termlist.sty
%doc %{_texmfdistdir}/doc/latex/termlist/README
%doc %{_texmfdistdir}/doc/latex/termlist/termlist.pdf
#- source
%doc %{_texmfdistdir}/source/latex/termlist/termlist.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 756590
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 719670
- texlive-termlist
- texlive-termlist
- texlive-termlist

