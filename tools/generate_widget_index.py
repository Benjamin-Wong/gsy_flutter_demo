import re
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / 'lib' / 'main.dart'

def parse_imports(text):
    # match: import 'package:gsy_flutter_demo/widget/xxx.dart'\n    #     deferred as alias;
    imports = {}
    pattern = re.compile(r"import\s+'(?P<path>[^']+)'\s+\n\s+deferred as (?P<alias>[a-zA-Z0-9_]+);")
    for m in pattern.finditer(text):
        imports[m.group('alias')] = m.group('path')
    return imports

def parse_routers(text):
    # Extract the routers map block
    m = re.search(r"Map<String, WidgetBuilder> routers = \{([\s\S]*?)\};", text)
    if not m:
        return []
    block = m.group(1)
    entries = []
    # Entry pattern: "Title": (context) { ... ContainerAsyncRouterPage(alias.loadLibrary(), (context) { return alias.ClassName(); });
    entry_pattern = re.compile(r'"(?P<title>[^"\\]+)"\s*:\s*\(context\)\s*\{[\s\S]*?ContainerAsyncRouterPage\((?P<alias>[a-zA-Z0-9_]+)\.loadLibrary\(\)\s*,\s*\(context\)\s*\{[\s\S]*?return\s+(?P<return>[^;\)]+)')
    for em in entry_pattern.finditer(block):
        title = em.group('title').strip()
        alias = em.group('alias').strip()
        ret = em.group('return').strip()
        # ret like alias.ClassName() or alias.ClassName(params)
        class_match = re.match(r'%s\.(?P<class>[A-Za-z0-9_]+)' % re.escape(alias), ret)
        classname = class_match.group('class') if class_match else None
        entries.append({'title': title, 'alias': alias, 'class': classname})
    return entries

def alias_to_path(alias, imports):
    p = imports.get(alias)
    if not p:
        return None
    # convert package:... to workspace relative path if possible
    if p.startswith('package:gsy_flutter_demo/'):
        rel = p.replace('package:gsy_flutter_demo/', '')
        return str((ROOT / 'lib' / rel).as_posix())
    return p

def main():
    txt = MAIN.read_text(encoding='utf-8')
    imports = parse_imports(txt)
    routers = parse_routers(txt)
    out = []
    for r in routers:
        path = alias_to_path(r['alias'], imports)
        out.append({
            'title': r['title'],
            'alias': r['alias'],
            'class': r['class'],
            'import': imports.get(r['alias']),
            'file': path,
        })
    out_path = ROOT / 'docs' / 'widget_index.json'
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(json.dumps({'generated_from':'lib/main.dart','count':len(out),'items':out}, ensure_ascii=False, indent=2), encoding='utf-8')
    print('Wrote', out_path)

if __name__ == '__main__':
    main()
