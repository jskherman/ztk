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
  margin: 0 !important;
  font-size: 9pt !important;
  font-weight: 400 !important;
  font-family: var(--bodyFont) !important;
  color: var(--gray) !important;
}
`

export default (() => PageTitle) satisfies QuartzComponentConstructor
