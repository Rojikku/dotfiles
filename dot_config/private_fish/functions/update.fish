function update --wraps='tldr --update; sudo pacman -Syu --noconfirm && shutdown now' --description 'Update tldr, Flatpak, and pacman'
	tldr --update

	# Background flatpak update
	flatpak update -y &
	set -l flatpak_pid $last_pid

	# Run pacman in foreground
	sudo pacman -Syu --noconfirm
	set -l pacman_status $status

	# Wait for flatpak
	wait $flatpak_pid

	# Shutdown ONLY if pacman succeeds (status 0)
	if test $pacman_status -eq 0
		shutdown now
	else
		echo "Update issue"
	end
end
