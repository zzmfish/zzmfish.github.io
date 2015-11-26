```bash
#安装
pip install ansible

#配置
cat >/etc/ansible/hosts <<EOF
[cluster]
myhost[01:99] ansible_ssh_port=1234
EOF

#ping
ansible all -m ping

#查看时间
ansible all -a 'date'
```

## 参考
* [ansible](http://www.ansible.com/home)
* [Getting Started](http://docs.ansible.com/ansible/intro_getting_started.html)
* [Ansible 快速上手](https://linuxtoy.org/archives/hands-on-with-ansible.html)