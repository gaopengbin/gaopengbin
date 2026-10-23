<img src="./assets/hero.svg" width="100%" alt="Pengbin Gao · 老高 — Building useful things with AI. AI applications, agents and developer tools." />

<p align="center">
  <b>把 AI 接进真实工作流，让想法变成好用的产品。</b><br/>
  <sub>AI Agents &nbsp; / &nbsp; MCP &nbsp; / &nbsp; Desktop &amp; Web Apps &nbsp; / &nbsp; Geospatial</sub>
</p>
<p align="center">
  <a href="#featured-products">主推产品</a> &nbsp; · &nbsp;
  <a href="#more-projects">更多作品</a> &nbsp; · &nbsp;
  <a href="#open-source">开源贡献</a> &nbsp; · &nbsp;
  <a href="#contact">联系我</a>
</p>

<a id="featured-products"></a>

## Selected work · 主推产品

<table>
<tr>
<td width="50%" valign="top">
<a href="https://geod-global.laogao.xyz/"><img src="./assets/geod-global.svg" width="100%" alt="GeoD Global · 遥感与地理数据工作区" /></a>

**遥感与地理数据，一个工作区。**

按区域检索、预览和下载影像、高程与矢量数据；接入自己的模型，用 Agent 组织任务。

[访问官网 ↗](https://geod-global.laogao.xyz/) &nbsp; · &nbsp; [源码](https://github.com/gaopengbin/geod-global) &nbsp; · &nbsp; [下载](https://geod-global.laogao.xyz/index.html#download)

<sub>Windows · Rust / Tauri · STAC · BYOK Agent</sub>
</td>
<td width="50%" valign="top">
<a href="https://geod.laogao.xyz/agent"><img src="./assets/geod-agent.svg" width="100%" alt="GeoD Agent · 地理数据桌面 Agent" /></a>

**从一句需求，到本机执行与成果核验。**

独立地理数据 Agent：对话配置图源、下载与处理、二维 / 三维地图，以及 Skill / MCP 扩展。

[访问官网 ↗](https://geod.laogao.xyz/agent) &nbsp; · &nbsp; [源码](https://github.com/gaopengbin/geod-agent) &nbsp; · &nbsp; [下载](https://github.com/gaopengbin/geod-agent/releases/latest)

<sub>Windows · AI Agent · Local Execution · MCP</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://geod.laogao.xyz/"><img src="./assets/geod.svg" width="100%" alt="GeoD · 跨平台地理数据下载工具" /></a>

**跨平台地理数据下载、处理与导出。**

地图影像、GeoTIFF、矢量瓦片、3D Tiles 与历史影像工作流；桌面、CLI、MCP 多种入口。

[访问官网 ↗](https://geod.laogao.xyz/) &nbsp; · &nbsp; [源码](https://github.com/gaopengbin/geo-downloader) &nbsp; · &nbsp; [下载](https://github.com/gaopengbin/geo-downloader/releases/latest)

<sub>Windows / macOS / Linux · Rust / Tauri</sub>
</td>
<td width="50%" valign="top">
<a href="https://gaopengbin.github.io/cesium-mcp/"><img src="./assets/cesium-mcp.svg" width="100%" alt="Cesium MCP · AI 控制 CesiumJS 三维场景" /></a>

**让 AI 操作真实的 CesiumJS 三维场景。**

共享工具契约与独立控制运行时，连接 MCP、WebMCP、function calling 和 Browser Agent。

[阅读文档 ↗](https://gaopengbin.github.io/cesium-mcp/) &nbsp; · &nbsp; [源码](https://github.com/gaopengbin/cesium-mcp) &nbsp; · &nbsp; [npm](https://www.npmjs.com/package/cesium-mcp-runtime)

<sub>TypeScript · CesiumJS · MCP · WebMCP</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://chat.laogao.xyz/"><img src="./assets/wechat-toolbox.svg" width="100%" alt="微信创作工具箱 · 在线制作与批量导出" /></a>

**微信创作工具箱：在线制作，批量导出。**

聊天、朋友圈、转账与红包等模拟图，支持长图和批量 ZIP。免登录编辑预览，导出需登录。

[立即使用 ↗](https://chat.laogao.xyz/) &nbsp; · &nbsp; [源码](https://github.com/gaopengbin/wechat-dialog-generator)

<sub>React · TypeScript · Web App · Batch Export</sub>
</td>
<td width="50%" valign="top">
<a href="https://github.com/gaopengbin/codex-launch-deck"><img src="./assets/codex-launch-deck.svg" width="100%" alt="Codex Launch Deck · Windows 启动与代理工具" /></a>

**让 Windows 上的 Codex 启动更顺手。**

便携版提供应用级代理启动、增强代理与运行诊断，不修改系统代理。主题能力见 CodeDrobe。

[查看项目 ↗](https://github.com/gaopengbin/codex-launch-deck) &nbsp; · &nbsp; [下载安装](https://github.com/gaopengbin/codex-launch-deck/releases/latest)

<sub>Windows · App-scoped Proxy · Diagnostics</sub>
</td>
</tr>
</table>

<sub>地理数据产品需使用具备访问与使用权限的数据源；各产品的版本与支持范围以对应文档为准。</sub>

<a id="more-projects"></a>

## Also building · 更多作品

| 产品 | 用途 | 探索 |
| :--- | :--- | :--- |
| **CodeDrobe** | AI 桌面应用的可逆主题运行时与主题商店 | [官网 ↗](https://codedrobe.app/) · [源码](https://github.com/CodeDrobe/core) |
| **GeoStyle** `内测` | 参考图与文字驱动的 AI 制图、可编辑样式 | [作品 ↗](https://geostyle.laogao.xyz/) · [展示仓库](https://github.com/gaopengbin/geostyle-showcase) |
| **微信同传** | 本地优先写作、Markdown 排版与公众号草稿同步 | [WeChat Writer ↗](https://github.com/gaopengbin/wechat-writer) |
| **GaiaAgent** | LLM + CesiumJS 三维空间智能桌面工作台 | [源码 ↗](https://github.com/gaopengbin/GaiaAgent) |
| **Spatial MCP Toolkit** | 面向不同地图引擎的 AI 控制工具 | [Mapbox](https://github.com/gaopengbin/mapbox-mcp) · [OpenLayers](https://github.com/gaopengbin/openlayers-mcp) · [Leaflet](https://github.com/gaopengbin/leaflet-mcp) |
| **OpenStyle** `实验` | 结构化地图样式、编译与 AI 制图工具链 | [源码 ↗](https://github.com/gaopengbin/openstyle) |

<sub>CodeDrobe 兼容性以应用和版本为准；微信同传只同步草稿，不自动发布文章。</sub>

<a id="open-source"></a>

## Built in the open · 开源贡献

持续参与 [Cesium 官方 AI 集成生态](https://github.com/CesiumGS/cesium-ai-integrations)。已合并的贡献：

**[社区集成 #21](https://github.com/CesiumGS/cesium-ai-integrations/pull/21)** &nbsp; / &nbsp; **[影像服务 #22](https://github.com/CesiumGS/cesium-ai-integrations/pull/22)** &nbsp; / &nbsp; **[地形服务 #30](https://github.com/CesiumGS/cesium-ai-integrations/pull/30)** &nbsp; / &nbsp; **[统一 MCP 网关 #39](https://github.com/CesiumGS/cesium-ai-integrations/pull/39)**

<a id="contact"></a>

## Let's build · 关于与联系

我是 **老高 / 高鹏彬**，在北京，约 6 年软件开发经验。关注 **AI 应用、Agent、开发者工具与产品工程**，也把地理空间领域的经验带进真实产品。

`TypeScript` `React` `Vue` `Node.js` `Rust` `Tauri` `Python`

欢迎交流产品反馈、开源协作，以及 AI 应用 / Agent / 全栈开发机会。

[邮件联系](mailto:1804287165@qq.com) &nbsp; · &nbsp; [简历 PDF](https://laogao.xyz/platform-api/public/resume/gaopengbin-ai-20260906.pdf) &nbsp; · &nbsp; 公众号 **老高 Vibe Coding** &nbsp; · &nbsp; 微信 `laogaovibecoding`
