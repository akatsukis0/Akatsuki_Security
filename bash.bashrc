if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
	command_not_found_handle() {
		/data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
	}
fi

PS1='\$Akatsuki - Security|\w| >> '
python /data/data/com.termux/files/usr/etc/banner.py
export LS_COLORS=$LS_COLORS:'di=1;31:'
