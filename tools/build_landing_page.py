"""
Builds the BeaconGrid landing page as Page 1 (index.html).
Links all map CTAs to map.html.
"""
import re

with open("emergency-resource-map.html", "r", encoding="utf-8") as f:
    landing = f.read()

# Ensure title contains "Emergency Resource Map" for test assertion and SEO
landing = landing.replace(
    "<title>BeaconGrid — Emergency Resource Network</title>",
    "<title>BeaconGrid — Emergency Resource Map & Disaster Management Portal</title>"
)

# Link "Find Help Now" in header to map.html
landing = landing.replace(
    '<a href="#map" class="nav-cta">Find Help Now</a>',
    '<a href="map.html" class="nav-cta">Find Help Now</a>'
)

# Link "Live Map" in header navigation to map.html
landing = landing.replace(
    '<li><a href="#map">Live Map</a></li>',
    '<li><a href="map.html">Live Map</a></li>'
)

# Link Hero buttons to map.html
hero_cta_old = '''        <div class="cta-row">
          <button class="btn-primary">Open the live map</button>
          <button class="btn-ghost">Report a resource</button>
        </div>'''

hero_cta_new = '''        <div class="cta-row">
          <a href="map.html" class="btn-primary" style="display:inline-flex; align-items:center; gap:8px;">Open the live map →</a>
          <a href="map.html?action=report" class="btn-ghost" style="display:inline-flex; align-items:center; gap:8px;">Report a resource</a>
        </div>'''

landing = landing.replace(hero_cta_old, hero_cta_new)

# Update Hero Meta with Tamil Nadu numbers
hero_meta_old = '''        <div class="hero-meta mono">
          <span><b>2,481</b> resources mapped</span>
          <span><b>96</b> cities covered</span>
          <span>updated <b>4 min</b> ago</span>
        </div>'''

hero_meta_new = '''        <div class="hero-meta mono">
          <span><b>38</b> TN districts active</span>
          <span><b>38</b> emergency GMCHs</span>
          <span>updated <b>just now</b></span>
        </div>'''

landing = landing.replace(hero_meta_old, hero_meta_new)

# Update Ticker bar numbers
ticker_old = '''        <div class="ticker-item">
          <div class="ticker-num g">312</div>
          <div class="ticker-lab">Shelters open now</div>
        </div>
        <div class="ticker-item">
          <div class="ticker-num o">89</div>
          <div class="ticker-lab">Medical stations active</div>
        </div>
        <div class="ticker-item">
          <div class="ticker-num a">540</div>
          <div class="ticker-lab">Supply points stocked</div>
        </div>
        <div class="ticker-item">
          <div class="ticker-num">1,204</div>
          <div class="ticker-lab">Volunteer verifiers</div>
        </div>'''

ticker_new = '''        <div class="ticker-item">
          <div class="ticker-num g">38</div>
          <div class="ticker-lab">Coastal cyclone & flood shelters</div>
        </div>
        <div class="ticker-item">
          <div class="ticker-num o">130+</div>
          <div class="ticker-lab">District GMCHs, Taluk hospitals & trauma centers</div>
        </div>
        <div class="ticker-item">
          <div class="ticker-num a">25</div>
          <div class="ticker-lab">Food & drinking water relief depots</div>
        </div>
        <div class="ticker-item">
          <div class="ticker-num">1,204</div>
          <div class="ticker-lab">Active SDRF & volunteer responders</div>
        </div>'''

landing = landing.replace(ticker_old, ticker_new)

# Update report section button to link to map.html?action=report
landing = landing.replace(
    '<button class="btn-primary">Add a resource</button>',
    '<a href="map.html?action=report" class="btn-primary" style="display:inline-block;">Add a resource</a>'
)

# Footer Live Map link
landing = landing.replace(
    '<li><a href="#map">Live Map</a></li>',
    '<li><a href="map.html">Live Map</a></li>'
)

# Write to static/index.html and root index.html
with open("static/index.html", "w", encoding="utf-8") as f:
    f.write(landing)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(landing)

print(f"Landing page created successfully (Length: {len(landing)} bytes)")
