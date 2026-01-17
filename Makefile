profile := windows-x64

create/%:
	conan create recipes/$*/all \
	--profile:all=profiles/$(profile) \
	--build=missing
