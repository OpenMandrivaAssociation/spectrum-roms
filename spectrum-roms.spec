%define 	version 20081224

Name:           spectrum-roms
Version:        %{version}
Release:        2
Summary:        A collection of Spectrum ROM images
Group:          Emulators
License:        Distributable
URL:            http://www.chiark.greenend.org.uk/~cjwatson/code/spectrum-roms/
Source0:        http://www.chiark.greenend.org.uk/~cjwatson/code/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}-distribution.txt
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch

%description
This package provides images of the read-only memories from various
versions of the Sinclair Spectrum. They can be used with various emulators.

%prep
%setup -q -n %{name}

%build
%make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}%{_prefix}

install -pm 0644 %{SOURCE1} distribution.txt

rm -rf %{buildroot}%{_docdir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog README distribution.txt
%{_datadir}/%{name}

