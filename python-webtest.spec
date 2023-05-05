Summary:        Helper to test WSGI applications
Name:           python-webtest
Version:        3.0.0
Release:        1
License:        MIT
Group:          Development/Python
URL:            https://github.com/Pylons/webtest
Source0:		https://pypi.io/packages/source/W/WebTest/WebTest-%{version}.tar.gz
BuildRequires:  pkgconfig(python)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(wheel)

BuildArch:      noarch

%description
WebTest wraps any WSGI application and makes it easy to send test
requests to that application, without starting up an HTTP server.

This provides convenient full-stack testing of applications written
with any WSGI-compatible framework.

%files
%doc docs/* README.rst CHANGELOG.rst
%{py_puresitedir}/webtest
%{py_puresitedir}/WebTest-*.*-info

#--------------------------------------------------------------------
%prep
%autosetup -p1 -n WebTest-%{version}

# removw unwanted docs
rm -f docs/{Makefile,conf.py,changelog.rst}

%build
%py_build

%install
%py_install

