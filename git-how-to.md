Инструкция
Для создания ssh: 	ssh-keygen -t ed25519 -C "yushin.aleks2004@yandex.ru"
			eval "$(ssh-agent -s)"
			$ssh-add -/.ssh/id_ed25519

Для работы с git:	git config --global user.name "Александр"
			git config --global user.email "yushin.aleks2004@yandex.ru"
			git status

Для конирования github:	git clone git@github.com:AleksandrYushin/Yushin.git
			ssh -T git@github.com

Для связи:		git commit -m “initial commit”
			git push