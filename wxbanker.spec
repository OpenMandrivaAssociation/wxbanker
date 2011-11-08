Summary: 	Simple personal finance
Name: 		wxbanker
Version:	0.8.2
Release:	%mkrel 1
License:	GNU GPL 3
Group:		Office
URL:		https://launchpad.net/wxbanker
Source0:	http://launchpad.net/wxbanker/0.8/0.8.2/+download/%{name}-%{version}.tar.xz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python-devel
BuildRequires:	wxPythonGTK
BuildRequires:  python-dateutil
Requires:	wxPythonGTK
Requires:  	python-dateutil
Requires:  	python-simplejson
Requires:  	python-numpy

%description
While wxBanker can synchronize account balances online via Mint.com, the point of wxBanker is to keep your own separate balances to compare with your online banks and other accounts; think of wxBanker as an advanced digital checkbook register.

You can also create arbitrary accounts for keeping track of reimbursable deposits, loans with friends, or allocating monthly savings for special purchases.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.txt COPYING.txt CHANGELOG.txt
%_localedir/*/LC_MESSAGES/%{name}.mo
%_datadir/icons/hicolor/*/apps/%{name}.png
%_datadir/%{name}/*
%_datadir/pixmaps/%{name}.png
%_datadir/applications/%{name}.desktop
%_bindir/%{name}
%py_puresitedir/%{name}/*
%py_puresitedir/wxBanker*.egg-info
