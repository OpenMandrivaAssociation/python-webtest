%define tarname WebTest
%define name	python-webtest
%define version	1.2.3
%define release %mkrel 1

Summary:	Helper to test WSGI applications
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/W/%{tarname}/%{tarname}-%{version}.tar.gz
Source1:	Makefile
License:	MIT
Group:		Development/Python
Url:		http://pythonpaste.org/webtest/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python-webob
BuildRequires:	python-setuptools
BuildRequires:	python-sphinx

%description
This package wraps any WSGI application and makes it easy to send test
requests to that application, without starting up an HTTP server.

It provides convenient full-stack testing of applications written with
any WSGI-compatible framework.

WebTest is based on paste.fixture.TestApp.

%prep
%setup -q -n %{tarname}-%{version}
cp -f %SOURCE1 docs/

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
pushd docs
export PYTHONPATH=`dir -d ../build/lib*`
make html
rm -f _build/html/.buildinfo
popd docs

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc docs/_build/html
