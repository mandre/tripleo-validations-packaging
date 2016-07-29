%{!?upstream_version: %global upstream_version %{version}}
%global upstream_name tripleo-validations

Name:           openstack-tripleo-validations
Summary:        Ansible playbooks to detect potential issues with TripleO deployments
Version:        0.0.1
Release:        1%{?dist}
License:        ASL 2.0
URL:            http://tripleo.org
Source0:        http://tarballs.openstack.org/tripleo-validations/tripleo-validations-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
BuildRequires:  git
Requires: ansible >= 2

Provides:  tripleo-validations = %{version}-%{release}
Obsoletes: tripleo-validations < %{version}-%{release}

%prep
%autosetup -n %{upstream_name}-%{upstream_version} -S git
rm -rf *.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}

%description
A collection of Ansible playbooks to detect and report potential issues during
TripleO deployments.

%files
%license LICENSE
%doc README.rst AUTHORS ChangeLog
%{python2_sitelib}/tripleo_validations*
%exclude %{python2_sitelib}/tripleo_validations/test*
%{_datadir}/%{name}

%changelog

