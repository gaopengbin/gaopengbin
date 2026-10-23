<div align="center">

# Pengbin Gao · 高鹏彬

### AI applications, agents & tools that get things done.

把 AI 接进真实工作流，做能使用、能交付、持续迭代的产品。

`AI Agents` · `MCP` · `Desktop Apps` · `Full-Stack` · `Geospatial`

[主推产品](#featured-products) · [更多项目](#more-projects) · [开源贡献](#open-source) · [联系我](#contact)

</div>

<a id="featured-products"></a>

## Featured products / 主推产品

<table>
<tr>
<td width="50%" valign="top">

### GeoD Global

**遥感影像与地理空间数据，一个工作区。**

按区域检索、预览和下载卫星影像、高程、专题与矢量数据；支持接入自己的模型，用 Agent 组织检索与下载任务。

Imagery, terrain and geospatial data discovery — with a BYOK Agent.

[官网 / Website](https://geod-global.laogao.xyz/) · [源码](https://github.com/gaopengbin/geod-global) · [下载](https://geod-global.laogao.xyz/index.html#download)

`Windows` `Rust` `Tauri` `STAC` `AI Agent`

</td>
<td width="50%" valign="top">

### GeoD Agent

**用对话配置图源、组织任务，交给本机执行。**

独立的地理数据桌面 Agent：AI 对话、本机下载与处理、二维 / 三维地图，以及 Skill / MCP 扩展。

A desktop geospatial agent for conversations, local execution and verified results.

[官网 / Website](https://geod.laogao.xyz/agent) · [源码](https://github.com/gaopengbin/geod-agent) · [下载](https://github.com/gaopengbin/geod-agent/releases/latest)

`Windows` `AI Agent` `Skills` `MCP`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### GeoD

**跨平台地理数据下载、处理与导出。**

面向地图影像、GeoTIFF、矢量瓦片、3D Tiles 与历史影像等工作流；提供桌面应用及配套 CLI / MCP 入口。数据源需具备相应访问与使用权限。

A cross-platform geospatial downloader, with desktop, CLI and MCP interfaces.

[官网 / Website](https://geod.laogao.xyz/) · [源码](https://github.com/gaopengbin/geo-downloader) · [下载](https://github.com/gaopengbin/geo-downloader/releases/latest)

[![Release](https://img.shields.io/github/v/release/gaopengbin/geo-downloader?label=Release&style=flat-square)](https://github.com/gaopengbin/geo-downloader/releases/latest)

`Windows / macOS / Linux` `Rust` `Tauri` `GeoTIFF`

</td>
<td width="50%" valign="top">

### Cesium MCP

**让 AI 操作真实的 CesiumJS 三维场景。**

独立的 AI 控制运行时与共享工具契约，连接 MCP、WebMCP、function calling 和 Browser Agent，不限于单一聊天客户端。

A protocol-agnostic AI control runtime for CesiumJS.

[文档 / Docs](https://gaopengbin.github.io/cesium-mcp/) · [源码](https://github.com/gaopengbin/cesium-mcp) · [npm](https://www.npmjs.com/package/cesium-mcp-runtime)

[![Stars](https://img.shields.io/github/stars/gaopengbin/cesium-mcp?label=Stars&style=flat-square)](https://github.com/gaopengbin/cesium-mcp)

`TypeScript` `CesiumJS` `MCP` `WebMCP`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 微信创作工具箱

**聊天、朋友圈与微信页面模拟，一站式制作。**

在线编辑聊天与批量聊天、朋友圈、转账、红包等模拟图，支持普通截图、长图和批量 ZIP 导出。免登录编辑预览，导出需登录。

A browser-based toolkit for illustrative WeChat-style mockups and batch exports.

[在线使用 / Try it](https://chat.laogao.xyz/) · [源码](https://github.com/gaopengbin/wechat-dialog-generator)

`React` `TypeScript` `Batch Export` `Web App`

</td>
<td width="50%" valign="top">

### Codex Launch Deck

**Windows 上的 Codex 启动与应用级代理工具。**

当前便携版提供代理启动、增强代理与运行诊断，不修改 Windows 系统代理；主题相关能力见下方 CodeDrobe 与项目版本说明。

A Windows launcher for Codex, with app-scoped proxy support and diagnostics.

[项目 / Repository](https://github.com/gaopengbin/codex-launch-deck) · [下载](https://github.com/gaopengbin/codex-launch-deck/releases/latest)

`Windows` `Desktop Tool` `Codex`

</td>
</tr>
</table>

<a id="more-projects"></a>

## More projects / 更多项目与探索

| 项目 | 方向 | 入口 |
| :--- | :--- | :--- |
| **CodeDrobe** | AI 桌面应用的可逆主题运行时、主题商店与验证恢复；兼容范围以对应应用和版本为准 | [官网](https://codedrobe.app/) · [源码](https://github.com/CodeDrobe/core) |
| **GeoStyle** | 参考图与文字驱动的 AI 制图、可编辑样式与真实地图作品；**内测中** | [产品与作品](https://geostyle.laogao.xyz/) · [公开展示仓库](https://github.com/gaopengbin/geostyle-showcase) |
| **微信同传 / WeChat Writer** | 本地优先公众号写作、Markdown 排版、素材与草稿同步；**只创建草稿，不自动发布** | [源码与使用说明](https://github.com/gaopengbin/wechat-writer) |
| **GaiaAgent** | LLM + CesiumJS 的三维空间智能桌面工作台 | [源码](https://github.com/gaopengbin/GaiaAgent) |
| **Spatial MCP Toolkit** | Mapbox、OpenLayers 与 Leaflet 的 AI 地图控制工具 | [Mapbox](https://github.com/gaopengbin/mapbox-mcp) · [OpenLayers](https://github.com/gaopengbin/openlayers-mcp) · [Leaflet](https://github.com/gaopengbin/leaflet-mcp) |
| **OpenStyle** | 结构化地图样式、编译与 AI 制图工具链；实验性项目 | [源码](https://github.com/gaopengbin/openstyle) |

<a id="open-source"></a>

## Open-source contributions / 开源贡献

在 [Cesium 官方 AI 集成生态](https://github.com/CesiumGS/cesium-ai-integrations)中，以下贡献已合并：

- [Community integration · #21](https://github.com/CesiumGS/cesium-ai-integrations/pull/21)：将 Cesium MCP 纳入社区集成目录。
- [Imagery server · #22](https://github.com/CesiumGS/cesium-ai-integrations/pull/22)：影像图层管理工具。
- [Terrain server · #30](https://github.com/CesiumGS/cesium-ai-integrations/pull/30)：地形服务操作。
- [Unified MCP gateway · #39](https://github.com/CesiumGS/cesium-ai-integrations/pull/39)：统一网关、领域与工具管理。

<a id="contact"></a>

## About & contact / 关于与联系

我是老高，约 6 年软件开发经验，关注 **AI 应用、Agent、开发者工具与产品工程**。GIS 是我的业务背景，不是应用方向的边界。

`TypeScript` · `React` · `Vue` · `Node.js` · `Rust` · `Tauri` · `Python`

欢迎交流产品反馈、开源协作，以及 AI 应用 / Agent / 全栈开发机会。

**Beijing, China** · [1804287165@qq.com](mailto:1804287165@qq.com) · [简历 PDF](https://laogao.xyz/platform-api/public/resume/gaopengbin-ai-20260906.pdf)

公众号：**老高 Vibe Coding** · 微信号：`laogaovibecoding`
