build:		## Build the site
	npx quartz build

serve:		## Serve the site locally
	make sync
	npx quartz build --serve

commit:		## Commit changes to GitHub
	npx quartz sync

sync: 		## Sync notes from vault to content folder
	del /s /q content\*
	python sync_notes.py
	copy "index.md" "content/index.md"
	copy "Copyright notice.md" "content/Copyright notice.md"
	copy "robots.txt" "content/robots.txt"

deploy: 	## Deploy to Cloudflare Pages
	wrangler pages deploy public --project-name jskztk --commit-dirty=true

publish:	## Build, sync, commit, and deploy
	make sync
	make build
	make deploy