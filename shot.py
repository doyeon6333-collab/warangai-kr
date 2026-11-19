import asyncio, sys, os
from playwright.async_api import async_playwright

URL = sys.argv[1] if len(sys.argv) > 1 else "file:///workspace/work/warangai-site/index.html"
OUT = sys.argv[2] if len(sys.argv) > 2 else "/workspace/work/warangai-site/shots"
os.makedirs(OUT, exist_ok=True)

SIZES = [("desktop", 1440, 900), ("mobile", 390, 844)]

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/workspace/.cache/ms-playwright/chromium-1255/chrome-linux64/chrome", args=["--no-sandbox", "--hide-scrollbars", "--disable-dev-shm-usage"])
        for name, w, h in SIZES:
            ctx = await b.new_context(viewport={"width": w, "height": h}, device_scale_factor=2 if name == "mobile" else 1)
            pg = await ctx.new_page()
            r = await pg.goto(URL, wait_until="networkidle", timeout=60000)
            print(name, "status", r.status if r else None)
            await pg.evaluate("document.fonts.ready")
            await pg.wait_for_timeout(1200)
            # viewport shot
            await pg.screenshot(path=f"{OUT}/{name}_viewport.png")
            # full page shot
            await pg.screenshot(path=f"{OUT}/{name}_full.png", full_page=True)
            hgt = await pg.evaluate("document.documentElement.scrollHeight")
            wid = await pg.evaluate("document.documentElement.scrollWidth")
            print(name, "scroll", wid, hgt, "viewport", w, h)
            # horizontal overflow check
            over = await pg.evaluate("""() => {
              const out=[]; const vw=document.documentElement.clientWidth;
              document.querySelectorAll('*').forEach(el=>{
                const r=el.getBoundingClientRect();
                if(r.right>vw+1.5||r.left<-1.5){out.push(el.tagName+'.'+(el.className||'')+' '+Math.round(r.left)+'..'+Math.round(r.right));}
              });
              return out.slice(0,15);
            }""")
            print(name, "overflow:", over)
            fonts = await pg.evaluate("getComputedStyle(document.body).fontFamily")
            print(name, "font:", fonts)
            await ctx.close()
        await b.close()

asyncio.run(main())
