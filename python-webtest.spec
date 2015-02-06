%define tarname WebTest

Summary:	Helper to test WSGI applications
Name:		python-webtest
Version:	1.2.3
Release:	3
Source0:	http://pypi.python.org/packages/source/W/%{tarname}/%{tarname}-%{version}.tar.gz
Source1:	Makefile
License:	MIT
Group:		Development/Python
Url:		http://pythonpaste.org/webtest/
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
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's/.*egg-info$//' FILE_LIST
pushd docs
export PYTHONPATH=`dir -d ../build/lib*`
make html
rm -f _build/html/.buildinfo
popd docs


%files -f FILE_LIST
%doc docs/_build/html


%changelog
* Thu Mar 31 2011 Lev Givon <lev@mandriva.org> 1.2.3-1mdv2011.0
+ Revision: 649457
- import python-webtest


