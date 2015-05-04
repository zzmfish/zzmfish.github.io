```
#!bash
#必备软件
sudo apt-get install screen vim-gtk ctags sshfs subversion git

#fcitx
install fcitx fcitx-googlepinyin im-switch
im-config -n fcitx

#git
git config --global user.email "zzmfish@163.com"
git config --global user.name "zzmfish"

#解决无法访问.local的问题
if [ ! -e /etc/nsswitch.conf.bak ]; then
    sudo cp /etc/nsswitch.conf /etc/nsswitch.conf.bak
    sudo sed -i "s/^hosts:.*/hosts: files dns/" /etc/nsswitch.conf
fi

#vim插件
mkdir -p ~/.vim
svn checkout --force https://github.com/vim-scripts/vcscommand.vim/tags/1.99.47 ~/.vim
```