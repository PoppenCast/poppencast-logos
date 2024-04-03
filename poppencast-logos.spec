%global forgeurl https://github.com/emansom/poppencast-logos

Version: 0.0.1

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
mkdir -p %{buildroot}/usr/share/dconf/db/site.d
install -m 644 gdm-greeter-icon.dconf %{buildroot}/usr/share/dconf/db/site.d/99-gdm-poppencast
mkdir -p %{buildroot}/usr/share/dconf/db/site.d/locks
install -m 644 gdm-greeter-icon.dconf-lock %{buildroot}/usr/share/dconf/db/site.d/locks/99-gdm-poppencast

%check
# not needed, just copying files

%files
/usr/share/pixmaps/logo/poppencast-icon-small.png
/usr/share/dconf/db/site.d/99-gdm-poppencast
/usr/share/dconf/db/site.d/locks/99-gdm-poppencast
%doc README.md
%license LICENSE

%post
/usr/bin/dconf update

%preun
/usr/bin/dconf update

%postun
/usr/bin/dconf update

%changelog
