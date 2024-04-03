%global forgeurl https://github.com/emansom/poppencast-logos

Version: 0.0.2

%forgemeta

Name:    poppencast-logos
Release: 1%{?dist}
Summary: PoppenCast related icons and pictures

License: GPL-3.0-or-later
URL:	 %{forgeurl}
Source:  %{forgesource}

Requires: gdm
Requires: dconf

BuildRequires: dconf
BuildArch:     noarch

%description
Site specific branding for PoppenCast appliances

%prep
%forgesetup

%build
# not needed, just copying files

%install
mkdir -p %{buildroot}/usr/share/pixmaps/logo
install -m 644 poppencast-icon-small.png %{buildroot}/usr/share/pixmaps/logo/poppencast-icon-small.png
mkdir -p %{buildroot}/etc/dconf/db/site.d
install -m 644 gdm-greeter-icon.dconf %{buildroot}/etc/dconf/db/site.d/99-gdm-poppencast
mkdir -p %{buildroot}/etc/dconf/db/site.d/locks
install -m 644 gdm-greeter-icon.dconf-lock %{buildroot}/etc/dconf/db/site.d/locks/99-gdm-poppencast

%check
# not needed, just copying files

%files
/usr/share/pixmaps/logo/poppencast-icon-small.png
/etc/dconf/db/site.d/99-gdm-poppencast
/etc/dconf/db/site.d/locks/99-gdm-poppencast
%doc README.md
%license LICENSE

%post
/usr/bin/dconf update

%preun
/usr/bin/dconf update

%postun
/usr/bin/dconf update

%changelog
* Wed Apr 03 2024 Ewout van Mansom <ewout@vanmansom.name> 0.0.2-1
- new package built with tito

