def branch(e):
	from git import Repo

	repo = Repo()
	ac_br = repo.active_branch.name
	if ac_br !="fireqanquserbo":
		e.edit("**Hey, Dostum Sen Orjinal @FireqanqUserBot Reposu Kullanmıyorsun...** Kurmak İçin Gel @FireqanqSupport")
		return 
