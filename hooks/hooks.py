#!/usr/bin/env python
    
import sys
import charmhelpers.contrib.ansible

# Create the hooks helper, passing a list of hooks which will be
# handled by default by running all sections of the playbook
# tagged with the hook name.
hooks = charmhelpers.contrib.ansible.AnsibleHooks(
    playbook_path='playbooks/sites.yml',
    default_hooks=['start', 'stop', 'config-changed',
                   'solr-relation-changed'])

@hooks.hook()
def install():
    charmhelpers.contrib.ansible.install_ansible_support(from_ppa=True)


if __name__ == "__main__":
        hooks.execute(sys.argv)

