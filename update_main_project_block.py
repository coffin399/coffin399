from pathlib import Path

path = Path('README.md')
old = (
    '<table align="center" style="border-spacing: 18px 0;">\n'
    '  <tr>\n'
    '    <td>\n'
    '      <a href="https://github.com/coffin399/ProjectMOMOKA">\n'
    '        <img width="330" height="150" src="https://github-readme-stats.vercel.app/api/pin/?username=coffin399&repo=ProjectMOMOKA&theme=radical&bg_color=0d1117&title_color=00D9FF&icon_color=00D9FF&text_color=00D9FF&border_radius=15&hide_border=true" alt="ProjectMOMOKA"/>\n'
    '      </a>\n'
    '    </td>\n'
    '    <td>\n'
    '      <a href="https://github.com/coffin399/coffin299-Hyper-AI-Agent">\n'
    '        <img width="330" height="150" src="https://github-readme-stats.vercel.app/api/pin/?username=coffin399&repo=coffin299-Hyper-AI-Agent&theme=radical&bg_color=0d1117&title_color=00D9FF&icon_color=00D9FF&text_color=00D9FF&border_radius=15&hide_border=true" alt="coffin299-Hyper-AI-Agent"/>\n'
    '      </a>\n'
    '    </td>\n'
    '  </tr>\n'
    '</table>'
)
new = (
    '<p align="center" style="display: flex; gap: 18px; justify-content: center; flex-wrap: wrap;">\n'
    '  <a href="https://github.com/coffin399/ProjectMOMOKA" style="display: inline-block;">\n'
    '    <img width="330" height="150" src="https://github-readme-stats.vercel.app/api/pin/?username=coffin399&repo=ProjectMOMOKA&theme=radical&bg_color=0d1117&title_color=00D9FF&icon_color=00D9FF&text_color=00D9FF&border_radius=15&hide_border=true" alt="ProjectMOMOKA"/>\n'
    '  </a>\n'
    '  <a href="https://github.com/coffin399/coffin299-Hyper-AI-Agent" style="display: inline-block;">\n'
    '    <img width="330" height="150" src="https://github-readme-stats.vercel.app/api/pin/?username=coffin399&repo=coffin299-Hyper-AI-Agent&theme=radical&bg_color=0d1117&title_color=00D9FF&icon_color=00D9FF&text_color=00D9FF&border_radius=15&hide_border=true" alt="coffin299-Hyper-AI-Agent"/>\n'
    '  </a>\n'
    '</p>'
)
text = path.read_text(encoding='utf-8')
if old not in text:
    raise SystemExit('Pattern not found')
text = text.replace(old, new, 1)
path.write_text(text, encoding='utf-8')
