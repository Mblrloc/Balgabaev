ssh-keygen создает ssh-ключи
ssh-add "путь к ключу" пихает ключ в ssh-agent
git clone git@github.com:HTTPS
git branch branchname создает ветку с именем branchname
git checkout branchname переключается в ветку с именем
в репозитории друга создать ветку со своей фамилией: git branch surname
переключиться в новую ветку: git checkout surname
добавить в репозиторий файл branch-how-to.md
написать в новом файле пару строк о том, как пользоваться ветками
проверить статус репозитория: git status
подготовить новый файл для комита: git add branch-how-to.md
проверить статус репозитория: git status
сделать комит: git commit -m “branch instructions”
отправить изменения на сервер: git push