<img src="./assets/hero.svg" width="100%" alt="Lao Gao · 老高 / 高鹏彬 — 把想法做成真正可用的 AI 产品" />

<p align="center"><a href="#numbers">数据仪表板</a> &nbsp; / &nbsp; <a href="#featured-products">产品现场</a> &nbsp; / &nbsp; <a href="#more-projects">更多作品</a> &nbsp; / &nbsp; <a href="#open-source">开源贡献</a> &nbsp; / &nbsp; <a href="#contact">联系我</a></p>

<a id="numbers"></a>

<img src="./assets/metrics.svg" width="100%" alt="GitHub 公开数据仪表板：Stars、Forks、发布资产下载、关注者与六个主推项目表现；更新时间见图" />

<details>
<summary>数据口径 · 公开可核查，每日自动更新</summary>

- Stars / Forks：`gaopengbin` 自有公开、非 Fork 仓库之和；不是用户数。
- Downloads：六个主推仓库现存公开 Releases 中安装包和压缩包资产的累计下载计数，包含预发行；不包含源码克隆、npm、网站或 CDN 下载，不代表独立用户或成功安装次数。
- Followers：GitHub 账号关注者。项目进度条按六个主推仓库的 Stars 相对比例展示，不是增长率。
- 数据直接来自 GitHub API，更新时间为 UTC；请求失败会保留上一份有效数据，不填假零。快照：[原始统计](./assets/profile-metrics.json) · [更新任务](https://github.com/gaopengbin/gaopengbin/actions/workflows/profile-metrics.yml)。

</details>

<a id="featured-products"></a>

## Selected work · 看得见的产品

实机截图与演示片段。点击图片查看完整演示或高清截图。

<sub>标准徽章来自 Shields.io：Stars / Forks / Downloads。徽章下载量统计全部 GitHub Release 资产（含校验文件），总览只统计安装包与压缩包；不同缓存更新时间可能略有差异，均不代表用户数。</sub>

<table>
<tr>
<td width="50%" valign="top">

### 01 / GeoD Global

<a href="https://github.com/gaopengbin/geod-global/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/gaopengbin/geod-global?style=flat&amp;logo=github&amp;label=Stars&amp;color=yellow" /></a>
<a href="https://github.com/gaopengbin/geod-global/forks"><img alt="Forks" src="https://img.shields.io/github/forks/gaopengbin/geod-global?style=flat&amp;logo=github&amp;label=Forks&amp;color=blue" /></a>
<a href="https://github.com/gaopengbin/geod-global/releases"><img alt="Downloads" src="https://img.shields.io/github/downloads/gaopengbin/geod-global/total?style=flat&amp;label=Downloads&amp;color=brightgreen" /></a>

<a href="https://geod-global.laogao.xyz/index.html#demo"><img src="./assets/geod-global-demo.gif" width="100%" alt="GeoD Global 实机演示：切换 Sentinel-2 影像并查看细节" /></a>

**遥感影像与地理数据，一个工作区。**

按区域检索、预览和下载数据，用自己的模型组织 Agent 任务。

[官网 ↗](https://geod-global.laogao.xyz/) · [源码](https://github.com/gaopengbin/geod-global) · [下载](https://geod-global.laogao.xyz/index.html#download) · [高清截图](./assets/geod-global.jpg)

<sub>实机片段 · Windows · Rust / Tauri · STAC</sub>
</td>
<td width="50%" valign="top">

### 02 / GeoD Agent

<a href="https://github.com/gaopengbin/geod-agent/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/gaopengbin/geod-agent?style=flat&amp;logo=github&amp;label=Stars&amp;color=yellow" /></a>
<a href="https://github.com/gaopengbin/geod-agent/forks"><img alt="Forks" src="https://img.shields.io/github/forks/gaopengbin/geod-agent?style=flat&amp;logo=github&amp;label=Forks&amp;color=blue" /></a>
<a href="https://github.com/gaopengbin/geod-agent/releases"><img alt="Downloads" src="https://img.shields.io/github/downloads/gaopengbin/geod-agent/total?style=flat&amp;label=Downloads&amp;color=brightgreen" /></a>

<a href="https://geod.laogao.xyz/agent#demo"><img src="./assets/geod-agent-demo.gif" width="100%" alt="GeoD Agent 实机演示：执行下载，将真实影像成果加载到地图" /></a>

**从一句需求，到本机执行与成果核验。**

对话配置图源、下载与处理；支持二维 / 三维地图、Skill 和 MCP。

[官网 ↗](https://geod.laogao.xyz/agent) · [源码](https://github.com/gaopengbin/geod-agent) · [下载](https://github.com/gaopengbin/geod-agent/releases/latest) · [高清截图](./assets/geod-agent.jpg)

<sub>实机片段 · Windows · Local Execution · MCP</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">

### 03 / GeoD

<a href="https://github.com/gaopengbin/geo-downloader/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/gaopengbin/geo-downloader?style=flat&amp;logo=github&amp;label=Stars&amp;color=yellow" /></a>
<a href="https://github.com/gaopengbin/geo-downloader/forks"><img alt="Forks" src="https://img.shields.io/github/forks/gaopengbin/geo-downloader?style=flat&amp;logo=github&amp;label=Forks&amp;color=blue" /></a>
<a href="https://github.com/gaopengbin/geo-downloader/releases"><img alt="Downloads" src="https://img.shields.io/github/downloads/gaopengbin/geo-downloader/total?style=flat&amp;label=Downloads&amp;color=brightgreen" /></a>

<a href="./assets/geod.jpg"><img src="./assets/geod.jpg" width="100%" alt="GeoD 真实界面：行政区选区、地图预览和 GeoTIFF 下载配置" /></a>

**跨平台地理数据下载、处理与导出。**

地图影像、GeoTIFF、矢量瓦片、3D Tiles 与历史影像，覆盖桌面、CLI 和 MCP。

[官网 ↗](https://geod.laogao.xyz/) · [源码](https://github.com/gaopengbin/geo-downloader) · [下载](https://github.com/gaopengbin/geo-downloader/releases/latest)

<sub>应用截图 · Windows / macOS / Linux</sub>
</td>
<td width="50%" valign="top">

### 04 / Cesium MCP

<a href="https://github.com/gaopengbin/cesium-mcp/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/gaopengbin/cesium-mcp?style=flat&amp;logo=github&amp;label=Stars&amp;color=yellow" /></a>
<a href="https://github.com/gaopengbin/cesium-mcp/forks"><img alt="Forks" src="https://img.shields.io/github/forks/gaopengbin/cesium-mcp?style=flat&amp;logo=github&amp;label=Forks&amp;color=blue" /></a>
<a href="https://github.com/gaopengbin/cesium-mcp/releases"><img alt="Downloads" src="https://img.shields.io/github/downloads/gaopengbin/cesium-mcp/total?style=flat&amp;label=Downloads&amp;color=brightgreen" /></a>

<a href="./assets/cesium-mcp.jpg"><img src="./assets/cesium-mcp.jpg" width="100%" alt="Cesium MCP 真实场景截图：纽约地图与三维建筑示例" /></a>

**让 AI 操作真实的 CesiumJS 三维场景。**

共享工具契约与独立控制运行时，连接 MCP、WebMCP 和 Browser Agent。

[文档 ↗](https://gaopengbin.github.io/cesium-mcp/) · [源码](https://github.com/gaopengbin/cesium-mcp) · [npm](https://www.npmjs.com/package/cesium-mcp-runtime)

<sub>示例场景截图 · TypeScript · CesiumJS</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">

### 05 / 微信创作工具箱

<a href="https://github.com/gaopengbin/wechat-dialog-generator/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/gaopengbin/wechat-dialog-generator?style=flat&amp;logo=github&amp;label=Stars&amp;color=yellow" /></a>
<a href="https://github.com/gaopengbin/wechat-dialog-generator/forks"><img alt="Forks" src="https://img.shields.io/github/forks/gaopengbin/wechat-dialog-generator?style=flat&amp;logo=github&amp;label=Forks&amp;color=blue" /></a>
<a href="https://chat.laogao.xyz/"><img alt="在线使用" src="https://img.shields.io/badge/Web-Open%20App-brightgreen?style=flat" /></a>

<a href="./assets/wechat-toolbox.jpg"><img src="./assets/wechat-toolbox.jpg" width="100%" alt="微信创作工具箱线上实拍：示例聊天编辑与实时手机预览" /></a>

**在线制作微信模拟图，支持批量导出。**

聊天、朋友圈、转账与红包等场景。免登录编辑预览，导出需登录。

[立即使用 ↗](https://chat.laogao.xyz/) · [源码](https://github.com/gaopengbin/wechat-dialog-generator)

<sub>线上实拍 · 示例对话 · 长图 / 批量 ZIP</sub>
</td>
<td width="50%" valign="top">

### 06 / Codex Launch Deck

<a href="https://github.com/gaopengbin/codex-launch-deck/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/gaopengbin/codex-launch-deck?style=flat&amp;logo=github&amp;label=Stars&amp;color=yellow" /></a>
<a href="https://github.com/gaopengbin/codex-launch-deck/forks"><img alt="Forks" src="https://img.shields.io/github/forks/gaopengbin/codex-launch-deck?style=flat&amp;logo=github&amp;label=Forks&amp;color=blue" /></a>
<a href="https://github.com/gaopengbin/codex-launch-deck/releases"><img alt="Downloads" src="https://img.shields.io/github/downloads/gaopengbin/codex-launch-deck/total?style=flat&amp;label=Downloads&amp;color=brightgreen" /></a>

<a href="./assets/launch-deck.jpg"><img src="./assets/launch-deck.jpg" width="100%" alt="Launch Deck 便携版真实窗口：ChatGPT / Codex 应用级代理启动与浏览器诊断" /></a>

**让 Windows 上的 Codex 启动更顺手。**

便携版提供应用级代理启动、增强代理与运行诊断，不修改系统代理。

[查看项目 ↗](https://github.com/gaopengbin/codex-launch-deck) · [下载安装](https://github.com/gaopengbin/codex-launch-deck/releases/latest)

<sub>便携版窗口实拍 · Windows · App-scoped Proxy</sub>
</td>
</tr>
</table>

<sub>画面来自公开产品演示与实际应用；版本界面可能有差异。地理数据需具备相应访问与使用权限。</sub>

<a id="more-projects"></a>

<details>
<summary><b>More projects · 更多作品与探索</b></summary>

<br/>

| 产品 | 用途 | 入口 |
| :--- | :--- | :--- |
| **CodeDrobe** | AI 桌面应用可逆主题与主题商店，兼容性以应用和版本为准 | [官网](https://codedrobe.app/) · [源码](https://github.com/CodeDrobe/core) |
| **GeoStyle** `内测` | 参考图与文字驱动的 AI 制图、可编辑样式 | [作品](https://geostyle.laogao.xyz/) · [展示仓库](https://github.com/gaopengbin/geostyle-showcase) |
| **微信同传** | 本地写作、Markdown 排版与公众号草稿同步；不自动发布 | [WeChat Writer](https://github.com/gaopengbin/wechat-writer) |
| **GaiaAgent** | LLM + CesiumJS 三维空间智能工作台 | [源码](https://github.com/gaopengbin/GaiaAgent) |
| **Spatial MCP Toolkit** | 不同地图引擎的 AI 控制工具 | [Mapbox](https://github.com/gaopengbin/mapbox-mcp) · [OpenLayers](https://github.com/gaopengbin/openlayers-mcp) · [Leaflet](https://github.com/gaopengbin/leaflet-mcp) |
| **OpenStyle** `实验` | 结构化地图样式、编译与 AI 制图工具链 | [源码](https://github.com/gaopengbin/openstyle) |

</details>

<a id="open-source"></a>

## Built in the open · 开源贡献

<img src="./assets/activity.svg" width="100%" alt="最近一年 GitHub 贡献热图，统计区间与贡献数见图；不代表产品使用量" />

持续参与 [Cesium 官方 AI 集成生态](https://github.com/CesiumGS/cesium-ai-integrations)。已合并：

[社区集成 #21](https://github.com/CesiumGS/cesium-ai-integrations/pull/21) &nbsp; / &nbsp; [影像服务 #22](https://github.com/CesiumGS/cesium-ai-integrations/pull/22) &nbsp; / &nbsp; [地形服务 #30](https://github.com/CesiumGS/cesium-ai-integrations/pull/30) &nbsp; / &nbsp; [统一 MCP 网关 #39](https://github.com/CesiumGS/cesium-ai-integrations/pull/39)

<a id="contact"></a>

## Let's build · 认识一下

我是 **老高 / 高鹏彬**，在北京，约 6 年软件开发经验。关注 **AI 应用、Agent、开发者工具与产品工程**，也把地理空间领域的经验带进真实产品。

`TypeScript` `React` `Vue` `Node.js` `Rust` `Tauri` `Python`

欢迎产品反馈、开源协作，以及 AI 应用 / Agent / 全栈开发机会。

[邮件联系](mailto:1804287165@qq.com) · [简历 PDF](https://laogao.xyz/platform-api/public/resume/gaopengbin-ai-20260906.pdf) · 公众号 **老高 Vibe Coding** · 微信 `laogaovibecoding`
