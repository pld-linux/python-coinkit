#
# Conditional build:
%bcond_without	python2		# Python 2.x module
%bcond_without	python3		# Python 3.x module

%define		module	coinkit
Summary:	Tools for Bitcoin and other cryptocurrencies
Summary(pl.UTF-8):	Narzędzia do Bitcoinów i innych kryptowalut
Name:		python-%{module}
Version:	0.3
Release:	14
License:	MIT
Group:		Libraries/Python
#Source0Download: https://github.com/halfmoonlabs/coinkit/releases
#TODO: use	https://github.com/halfmoonlabs/coinkit/archive/v%{version}/%{name}-%{version}.tar.gz
Source0:	https://github.com/halfmoonlabs/coinkit/archive/v%{version}.tar.gz
# Source0-md5:	2e5bd02391fa38766a5644e7abfa9750
URL:		https://github.com/halfmoonlabs/coinkit
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	rpm-pythonprov
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-2to3
BuildRequires:	python3-devel
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
Requires:	python
Requires:	python-ecdsa >= 0.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools for Bitcoin and other cryptocurrencies.

%description -l pl.UTF-8
Narzędzia do Bitcoinów i innych kryptowalut.

%package -n python3-%{module}
Summary:	Tools for Bitcoin and other cryptocurrencies
Summary(pl.UTF-8):	Narzędzia do Bitcoinów i innych kryptowalut
Group:		Libraries/Python
Requires:	python3
Requires:	python3-ecdsa >= 0.10

%description -n python3-%{module}
Tools for Bitcoin and other cryptocurrencies.

%description -n python3-%{module} -l pl.UTF-8
Narzędzia do Bitcoinów i innych kryptowalut.

%prep
%setup -q -n coinkit-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python-%{module}-%{version}
%py_install
%endif

%if %{with python3}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS README.md
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/*egg-info
%{_examplesdir}/python-%{module}-%{version}
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc AUTHORS README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/*egg-info
%{_examplesdir}/python3-%{module}-%{version}
%endif
