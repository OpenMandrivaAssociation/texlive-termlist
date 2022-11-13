Name:		texlive-termlist
Version:	18923
Release:	1
Summary:	Label any kind of term with a continuous counter
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/termlist
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/termlist.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/termlist.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/termlist.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
