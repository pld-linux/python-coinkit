#
# Conditional build:
%bcond_without	python2		# Python 2.x module
%bcond_without	python3		# Python 3.x module

%define 	module	coinkit
Summary:	Tools for Bitcoin and other cryptocurrencies
Name:		python-%{module}
Version:	0.3
Release:	2
License:	MIT
Group:		Libraries/Python
Source0:	https://github.com/halfmoonlabs/coinkit/archive/v%{version}.tar.gz
# Source0-md5:	2e5bd02391fa38766a5644e7abfa9750
URL:		https://github.com/halfmoonlabs/coinkit
BuildRequires:	rpm-pythonprov
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-modules
%endif
%if %{with python3}
BuildRequires:	python3-2to3
BuildRequires:	python3-devel
BuildRequires:	python3-modules
%endif
Requires:	python
Requires:	python-ecdsa >= 0.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools for Bitcoin and other cryptocurrencies.

%package -n	python3-%{module}
Summary:	Tools for Bitcoin and other cryptocurrencies
Group:		Libraries/Python
Requires:	python3
Requires:	python3-ecdsa >= 0.10

%description -n python3-%{module}
Tools for Bitcoin and other cryptocurrencies.

%prep
%setup -q -n coinkit-%{version}

%build
%if %{with python2}
%{__python} setup.py build --build-base py2
%endif
%if %{with python3}
%{__python3} setup.py build --build-base py3
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python-%{module}-%{version}
%{__python} setup.py build \
	--build-base py2 \
	install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT
%endif

%if %{with python3}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
%{__python3} setup.py build \
	--build-base py3 \
	install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT
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
