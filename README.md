# 와랑 디지털 AI 교육센터 · 공식 홈페이지

`warangai.kr` — Warang Digital AI Edu Center

정적 단일 페이지 사이트입니다. 빌드 도구 없이 그대로 배포됩니다.

## 구성
- `index.html` — 전체 페이지(HTML + CSS + 최소 JS, Pretendard CDN)
- `assets/wr-logo.svg` — WR 노드 로고 벡터 원본
- `assets/og-image.png` — 카카오톡·블로그 공유용 미리보기 이미지(1200×630)
- `assets/favicon.svg` — 파비콘
- `CNAME` — 커스텀 도메인 `warangai.kr` (GitHub Pages)
- `robots.txt`, `sitemap.xml` — 검색 노출용

## 내용 고칠 때
1. `index.html`에서 문구를 고칩니다. 색은 `:root` 변수(`--ink #222428`, `--magenta #B5125E`)만 바꾸면 전체 톤이 바뀝니다.
2. `git add -A && git commit -m "문구 수정" && git push origin main main:gh-pages` 하면 1~2분 뒤 사이트에 반영됩니다.
3. 연락처는 히어로 CTA·문의 섹션·푸터 세 곳에 있으니 함께 바꿔 주세요.

> 배포 브랜치: 현재 GitHub Pages는 `gh-pages` 브랜치에서 배포됩니다(`main`과 내용 동일). 저장소 Settings → Pages에서 Branch를 `main`으로 바꾸면 `main`에 push하는 것만으로 배포됩니다.

## 도메인 (가비아 DNS)
- `@` A: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
- `www` CNAME: `doyeon6333-collab.github.io`
- 메일(MX: ImprovMX)은 그대로 두면 됩니다.
