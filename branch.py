def branch(e):
	from git import Repo
	from userbot.language import get_value
	LANG = get_value("branch")

	repo = Repo()
	ac_br = repo.active_branch.name
	if ac_br !="fireqanquserbot":
		return e.edit(LANG['NOT_BRANCH'])