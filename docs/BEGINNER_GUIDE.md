# GSY Flutter Demo — 初学者入门指南

本指南面向 Flutter 初学者，基于仓库 `gsy_flutter_demo`（演示大量 Flutter 效果与示例）整理。目标是帮助你快速理解项目结构、掌握关键示例并形成渐进学习路线。

> 主要文件： [pubspec.yaml](pubspec.yaml)、[README.md](README.md)、入口：[lib/main.dart](lib/main.dart)

---

**一、项目概览**
- **项目性质**：示例集，包含动画、布局、Sliver、高级渲染（Shader/Canvas）、3D/粒子效果、交互控件等大量独立 demo。
- **多平台支持**：含 `android/ ios/ web/ macos/ windows/ linux/` 目录，可直接在相应平台运行（需配置 Flutter 环境）。
- **延迟加载**：`lib/main.dart` 使用 `deferred as` 与 `ContainerAsyncRouterPage` 在运行时按需加载示例模块，便于 Web 与大规模示例管理。

**二、快速开始（最短路径）**
1. 安装 Flutter（建议 3.35 及以上；pubspec 要求 `sdk: '>=3.0.0 <4.0.0'`）。
2. 在仓库根目录执行：
```powershell
flutter pub get
flutter run        # 运行到首选设备
flutter run -d chrome  # 在浏览器运行 Web demo
```
3. 打开应用首页（由 `lib/main.dart` 提供），点击例子名称即可按需加载并查看效果。

**三、关键架构说明（要点）**
- `lib/main.dart`：应用入口与路由表（Map<String, WidgetBuilder> routers）。演示标题文本就是路由 key；跳转时会调用对应的 `deferred` 模块的 `loadLibrary()`。
- 延迟加载模式：`deferred as alias` + `alias.loadLibrary()` → 减少初始 bundle 大小，适用于大量示例的 Demo 应用（尤其 Web）。
- 资源管理：字体与 shader 在 `pubspec.yaml` 中声明（例如 `shaders/liquid_glass.frag`，以及多种自定义字体在 `assets/` 下）。
- 动态组件（Android）：`pubspec.yaml` 中包含 `deferred-components` 节点，列出了可拆分的功能模块（用于 Android 动态交付）。

**四、目录结构说明（常用）**
- `lib/`：Dart 源代码。
  - `lib/main.dart`：入口、路由、延迟加载逻辑。
  - `lib/widget/`：示例页面集合（按功能与主题拆分子文件/目录）。
- `assets/`：字体与静态资源。
- `shaders/`：自定义 GLSL shader 文件（如 `liquid_glass.frag`）。
- `docs/`：本项目生成的辅助文档（本文件所在位置）。

**五、推荐学习索引（渐进路线，含示例与文件路径）**
下面按学习阶段给出建议的示例顺序，每项都列出对应文件以便直接打开查看源码。

- 入门（理解 Widget、布局与状态）
  - 文本输入和 Controller：`lib/widget/controller_demo_page.dart`
  - Clip 与圆角：`lib/widget/clip_demo_page.dart`
  - Align 布局：`lib/widget/align_demo_page.dart`
  - 绝对定位（Positioned）：`lib/widget/positioned_demo_page.dart`

- 列表与滑动（常见 UI 场景）
  - 列表滑动监听：`lib/widget/scroll_listener_demo_page.dart`
  - 滑动到指定位置：`lib/widget/scroll_to_index_demo_page.dart`
  - Sliver 与多列表 Tab：`lib/widget/sliver_tab_demo_page.dart`, `lib/widget/sliver_list_demo_page.dart`
  - 列表停靠（Stick）：`lib/widget/stick/stick_demo_page.dart`

- 动画基础（理解动画 API 与组合）
  - 动画容器：`lib/widget/animation_container_demo_page.dart`
  - 控件组合动画：`lib/widget/anima_demo_page.dart`、`lib/widget/anima_demo_page2.dart`
  - 文本动画：`lib/widget/anim_text_demo_page.dart`

- 交互与手势
  - 拖拽与 Matrix：`lib/widget/drag_img_demo_page.dart`, `lib/widget/matrix_custom_painter_page.dart`
  - 手势密码：`lib/widget/gesture_password/gesture_password_demo_page.dart`

- 自定义渲染与 Canvas/Shader
  - Shader Canvas 示例：`lib/widget/shader_canvas_demo_page.dart`
  - Liquid glass（shader）：`lib/widget/liquid_glass_demo.dart`, `lib/widget/liquid_glass_demo2.dart`（参考 `shaders/`）
  - 自定义多渲染：`lib/widget/custom_multi_render_demo_page.dart`

- 高级视觉效果（3D / 粒子 / Rive）
  - Rive 动画：`lib/widget/anim_juejin_logo_demo_page.dart`
  - 3D 卡片：`lib/widget/card_3d_demo_page.dart`, `lib/widget/card_real_3d_demo_page.dart`
  - 粒子与黑洞效果：`lib/widget/particle/*`, `lib/widget/black_hole_simulation_page.dart`

- 实用组件与 UI 化繁为简
  - 验证码输入：`lib/widget/verification_code_input_demo_page.dart`
  - 图片画廊：`lib/widget/photo_gallery_demo_page.dart`
  - 自定义下拉筛选：`lib/widget/drop_select_menu/*`

每个阶段建议：先看演示效果（运行 APP），然后打开对应源码文件，按顺序读懂 Widget 构造、状态管理、布局与关键回调（手势/动画）。

**六、学习建议与实践任务**
- 读源码时重点关注：Widget 树层级、State 管理（StatefulWidget）、布局约束（BoxConstraints）、渲染顺序（Sliver/CustomPainter）和性能（避免重建、合理使用 const）。
- 实践题：
  1. 在 `controller_demo_page.dart` 中添加一个新的输入栏并监听变化。
  2. 在 `anima_demo_page.dart` 上修改动画时长并观察差异。
  3. 将 `shader_canvas_demo_page.dart` 的 shader 参数暴露成可交互控件（滑条）以实时调节。

**七、运行与调试常见问题**
- 依赖未安装：运行 `flutter pub get`。
- Web 上的 hash 跳转：打开 URL 如 `http://.../#<示例标题>`（`lib/main.dart` 会尝试基于 hash 自动跳转，示例标题需完整匹配）。
- 若遇到 shader/字体加载问题，检查 `pubspec.yaml` 中 `shaders` 与 `fonts` 配置，并确保资源路径正确。

**八、推荐改进（可选，便于学习）**
- 增加 `docs/widget_index.md`：把 `lib/widget` 下示例按类别生成 Markdown 索引（便于搜索与阅读）。
- 为每个示例添加顶部注释（一句话说明 + 难度标签 + 相关文章链接）。
- 在 `README.md` 添加“快速学习路径”链接到本指南。

**九、资源与引用**
- 项目 README: [README.md](README.md)
- 入口代码: [lib/main.dart](lib/main.dart)
- 包配置: [pubspec.yaml](pubspec.yaml)

---
