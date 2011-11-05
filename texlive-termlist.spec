# revision 18923
# category Package
# catalog-ctan /macros/latex/contrib/termlist
# catalog-date 2010-06-12 14:14:46 +0200
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-termlist
Version:	1.1
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The termlist package provides environments to indent and label
any kind of terms with a continuous number. Candidate terms may
appear inside an equation or eqnarray environment.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/termlist/termlist.sty
%doc %{_texmfdistdir}/doc/latex/termlist/README
%doc %{_texmfdistdir}/doc/latex/termlist/termlist.pdf
#- source
%doc %{_texmfdistdir}/source/latex/termlist/termlist.dtx
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
