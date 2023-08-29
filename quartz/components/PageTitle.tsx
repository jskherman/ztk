import { pathToRoot } from "../util/path"
import { QuartzComponentConstructor, QuartzComponentProps } from "./types"

function PageTitle({ fileData, cfg }: QuartzComponentProps) {
  const title = cfg?.pageTitle ?? "Untitled Quartz"
  const subtitle = cfg?.pageSubtitle ?? ""
  const baseDir = pathToRoot(fileData.slug!)
  return (
    <div>
      <h1 class="page-title">
        <a href={baseDir}>{title}</a>
      </h1>
      <h2 class="subtitle">{subtitle}</h2>
    </div>
  )
}

PageTitle.css = `
.page-title {
  margin: 0;
}

.subtitle {
  margin: 0;
  font-size: 9pt;
  font-weight: 400;
  font-family: var(--bodyFont);
  color: var(--gray);
}
`

export default (() => PageTitle) satisfies QuartzComponentConstructor
