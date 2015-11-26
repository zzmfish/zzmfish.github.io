```
#!bash
#必备软件
sudo apt-get install screen vim-gtk ctags sshfs subversion git
sudo apt-get install language-selector-gnome #缺少语言支持

#输入法
#sudo apt-get install ibus-sunpinyin
sudo apt-get install  fcitx fcitx-googlepinyin fcitx-sunpinyin im-switch
im-switch -s fcitx #or im-config -n fcitx

#git
git config --global user.email "zzmfish@163.com"
git config --global user.name "zzmfish"
git config core.quotepath false

#解决无法访问.local的问题
if [ ! -e /etc/nsswitch.conf.bak ]; then
    sudo cp /etc/nsswitch.conf /etc/nsswitch.conf.bak
    sudo sed -i "s/^hosts:.*/hosts: files dns/" /etc/nsswitch.conf
fi

#vim插件
mkdir -p ~/.vim
svn checkout --force https://github.com/vim-scripts/vcscommand.vim/tags/1.99.47 ~/.vim

#自动挂载D盘
sudo mkdir /media/d_drive
sudo cp /etc/rc.local /etc/rc.local.bak
echo "mount -t vboxsf d_drive /media/d_drive/" | sudo tee -a /etc/rc.local

#nginx
echo "include $HOME/local/etc/nginx.conf;" >> /etc/nginx/nginx.conf

#github
mkdir ~/github
cd ~/github
git clone https://github.com/zzmfish/etc.git
git clone https://github.com/zzmfish/scripts.git
```