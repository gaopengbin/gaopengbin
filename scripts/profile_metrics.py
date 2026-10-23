"""Build self-hosted profile visuals from public GitHub data. No dependencies."""
import argparse
import datetime as dt
import html
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
FEATURED = ['geo-downloader', 'cesium-mcp', 'wechat-dialog-generator',
            'geod-global', 'codex-launch-deck', 'geod-agent']
LABELS = ['GeoD', 'Cesium MCP', 'WeChat Toolbox', 'GeoD Global', 'Launch Deck', 'GeoD Agent']
COLORS = ['#66f5cc', '#8eafff', '#ffb879', '#c49bff', '#fb8dc8', '#8ae4ff']


def api(path, body=None):
    cmd = ['gh', 'api', path]
    if body is not None:
        cmd += ['--input', '-']
    result = subprocess.run(cmd, input=json.dumps(body) if body else None,
                            capture_output=True, text=True, encoding='utf-8', check=True)
    value = json.loads(result.stdout)
    if isinstance(value, dict) and value.get('errors'):
        raise RuntimeError('GitHub returned GraphQL errors; preserve previous metrics')
    return value


def pages(path):
    result = []
    for page in range(1, 101):
        batch = api(f'{path}{"&" if "?" in path else "?"}per_page=100&page={page}')
        result.extend(batch)
        if len(batch) < 100:
            return result
    raise RuntimeError('Pagination exceeded safety limit')


def collect():
    profile = api('users/gaopengbin')
    repos = [r for r in pages('users/gaopengbin/repos?type=owner') if not r['fork']]
    by_name = {r['name']: r for r in repos}
    products = []
    extensions = ('.exe', '.msi', '.msix', '.zip', '.7z', '.dmg', '.deb', '.appimage', '.tar.gz')
    for name, label, color in zip(FEATURED, LABELS, COLORS):
        repo = by_name[name]
        releases = [r for r in pages(f'repos/gaopengbin/{name}/releases') if not r['draft']]
        downloads = sum(a['download_count'] for r in releases for a in r['assets']
                        if a['name'].lower().endswith(extensions))
        products.append(dict(name=name, label=label, color=color, stars=repo['stargazers_count'],
                             forks=repo['forks_count'], downloads=downloads))
    query = '''query { user(login:"gaopengbin") { contributionsCollection {
      contributionCalendar { totalContributions weeks { contributionDays { date contributionCount } } }
    } } }'''
    calendar = api('graphql', {'query': query})['data']['user']['contributionsCollection']['contributionCalendar']
    return dict(updated=dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d'),
                repo_count=len(repos), stars=sum(r['stargazers_count'] for r in repos),
                forks=sum(r['forks_count'] for r in repos), followers=profile['followers'],
                downloads=sum(p['downloads'] for p in products), products=products, calendar=calendar)


def text(x, y, value, size=16, color='#e8efff', weight=400, extra=''):
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}" {extra}>{html.escape(str(value))}</text>'


def shell(height, title, content):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{height}" viewBox="0 0 1200 {height}" role="img">
<title>{html.escape(title)}</title><defs>
<linearGradient id="bg" x2="1" y2="1"><stop stop-color="#111c32"/><stop offset="1" stop-color="#090d19"/></linearGradient>
<linearGradient id="line"><stop stop-color="#66f5cc"/><stop offset=".5" stop-color="#8eafff"/><stop offset="1" stop-color="#c49bff"/></linearGradient>
</defs><rect width="1200" height="{height}" rx="24" fill="url(#bg)"/>
<rect x=".5" y=".5" width="1199" height="{height-1}" rx="24" fill="none" stroke="#28364d"/>
<g font-family="Inter,Segoe UI,Arial,sans-serif">{content}</g></svg>'''


def metrics(data):
    s = text(34, 42, 'OPEN SOURCE / BY THE NUMBERS', 15, '#78eacf', 600, 'letter-spacing="3"')
    s += text(1166, 42, f'PUBLIC DATA · {data["updated"]} UTC', 13, '#97a7bf', extra='text-anchor="end"')
    cards = [('TOTAL STARS', data['stars'], 'Owned public repos · excludes forks'),
             ('TOTAL FORKS', data['forks'], f'{data["repo_count"]} owned non-fork public repos'),
             ('RELEASE DOWNLOADS', data['downloads'], '6 featured repos · binary / archive assets'),
             ('FOLLOWERS', data['followers'], 'People following this GitHub profile')]
    for i, (label, value, caption) in enumerate(cards):
        x = 26+i*291
        s += f'<rect x="{x}" y="65" width="275" height="145" rx="14" fill="#111c2d" stroke="#2a3b50"/>'
        s += f'<rect x="{x+18}" y="85" width="22" height="3" rx="1.5" fill="{COLORS[i]}"/>'
        s += text(x+18, 112, label, 12, '#a7b6cd', 600, 'letter-spacing="1.5"')
        s += text(x+18, 162, f'{value:,}', 43, COLORS[i], 700)
        s += text(x+18, 189, caption, 10, '#94a5be')
    s += text(34, 253, 'FEATURED REPOSITORIES', 13, '#a7b6cd', 600, 'letter-spacing="2"')
    max_stars = max(p['stars'] for p in data['products']) or 1
    for i, p in enumerate(data['products']):
        x, y = 34+(i%2)*580, 290+(i//2)*85
        s += text(x, y, p['label'], 18, '#eef4ff', 600)
        s += text(x+527, y, f'{p["stars"]:,} stars  /  {p["forks"]:,} forks', 13, p['color'], extra='text-anchor="end"')
        s += f'<rect x="{x}" y="{y+16}" width="527" height="7" rx="3.5" fill="#243046"/>'
        s += f'<rect x="{x}" y="{y+16}" width="{max(3,527*p["stars"]/max_stars):.1f}" height="7" rx="3.5" fill="{p["color"]}"/>'
        s += text(x, y+43, f'github.com/gaopengbin/{p["name"]}', 11, '#899ab4')
    s += '<path d="M34 513H1166" stroke="#27364c"/>'
    s += text(34, 541, 'SOURCE: GITHUB API  /  REFRESHED DAILY  /  NO THIRD-PARTY STATS IMAGE SERVICE', 11, '#9bacc2', extra='letter-spacing="1"')
    return shell(564, 'Public GitHub metrics, dated snapshot', s)


def activity(data):
    cal = data['calendar']
    s = text(34, 40, 'BUILD / SHIP / REPEAT', 15, '#78eacf', 600, 'letter-spacing="3"')
    s += text(1166, 40, f'{cal["totalContributions"]:,} contributions · GitHub calendar', 17, '#e8efff', 600, 'text-anchor="end"')
    days = [d for w in cal['weeks'] for d in w['contributionDays']]
    peak = max(d['contributionCount'] for d in days) or 1
    palette = ['#1d2b3d', '#174c4b', '#217f70', '#39b88f', '#74efbc']
    previous_month = None
    for wi, week in enumerate(cal['weeks']):
        for d in week['contributionDays']:
            date = dt.date.fromisoformat(d['date'])
            row = (date.weekday()+1)%7
            value = d['contributionCount']
            level = 0 if value == 0 else min(4, 1+int((value/peak)**0.5*3))
            x,y = 35+wi*21, 79+row*21
            if row == 0 and date.month != previous_month:
                s += text(x, 68, date.strftime('%b'), 10, '#8d9db6')
                previous_month = date.month
            s += f'<rect x="{x}" y="{y}" width="16" height="16" rx="3" fill="{palette[level]}"><title>{d["date"]}: {value} contributions</title></rect>'
    s += text(34, 256, f'{days[0]["date"]} — {days[-1]["date"]} · GitHub contribution calendar, not product usage', 12, '#95a6bf')
    return shell(280, 'GitHub contribution activity over the last year', s)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cached', action='store_true')
    args = parser.parse_args()
    snapshot = ROOT / 'assets/profile-metrics.json'
    data = json.loads(snapshot.read_text(encoding='utf-8')) if args.cached else collect()
    # Only write after every request and render succeeds; preserve last valid visuals on API failure.
    output = metrics(data), activity(data)
    (ROOT/'assets/metrics.svg').write_text(output[0], encoding='utf-8')
    (ROOT/'assets/activity.svg').write_text(output[1], encoding='utf-8')
    snapshot.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k:v for k,v in data.items() if k not in ('calendar','products')}, ensure_ascii=False))


if __name__ == '__main__':
    main()
