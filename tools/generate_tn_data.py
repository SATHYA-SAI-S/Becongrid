"""
Script to build full 38-district Tamil Nadu dataset and UI enhancements into static/index.html and index.html
"""
import json
import re

TN_DISTRICTS = {
  "all": {"name": "All Tamil Nadu (Statewide Overview)", "lat": 10.8505, "lon": 78.6856, "zoom": 7.3},
  # Chennai Metropolitan
  "chennai": {"name": "Chennai (State Capital)", "lat": 13.0827, "lon": 80.2707, "zoom": 12},
  "chengalpattu": {"name": "Chengalpattu", "lat": 12.6819, "lon": 79.9888, "zoom": 12},
  "kancheepuram": {"name": "Kancheepuram", "lat": 12.8342, "lon": 79.7036, "zoom": 12},
  "tiruvallur": {"name": "Tiruvallur", "lat": 13.1432, "lon": 79.9079, "zoom": 12},
  # Northern Region
  "cuddalore": {"name": "Cuddalore (Coastal Cyclone Zone)", "lat": 11.7480, "lon": 79.7714, "zoom": 12},
  "viluppuram": {"name": "Viluppuram", "lat": 11.9401, "lon": 79.4861, "zoom": 12},
  "kallakurichi": {"name": "Kallakurichi", "lat": 11.7384, "lon": 78.9639, "zoom": 12},
  "vellore": {"name": "Vellore", "lat": 12.9165, "lon": 79.1325, "zoom": 12},
  "ranipet": {"name": "Ranipet", "lat": 12.9272, "lon": 79.3330, "zoom": 12},
  "tirupathur": {"name": "Tirupathur", "lat": 12.4958, "lon": 78.5678, "zoom": 12},
  "tiruvannamalai": {"name": "Tiruvannamalai", "lat": 12.2253, "lon": 79.0747, "zoom": 12},
  # Western (Kongu) Region
  "coimbatore": {"name": "Coimbatore", "lat": 11.0168, "lon": 76.9558, "zoom": 12},
  "tiruppur": {"name": "Tiruppur (Textile Hub)", "lat": 11.1085, "lon": 77.3411, "zoom": 12},
  "erode": {"name": "Erode", "lat": 11.3410, "lon": 77.7172, "zoom": 12},
  "salem": {"name": "Salem", "lat": 11.6643, "lon": 78.1460, "zoom": 12},
  "namakkal": {"name": "Namakkal", "lat": 11.2189, "lon": 78.1674, "zoom": 12},
  "dharmapuri": {"name": "Dharmapuri", "lat": 12.1211, "lon": 78.1582, "zoom": 12},
  "krishnagiri": {"name": "Krishnagiri / Hosur", "lat": 12.5186, "lon": 78.2137, "zoom": 12},
  "nilgiris": {"name": "Nilgiris / Ooty (Ghats)", "lat": 11.4102, "lon": 76.6950, "zoom": 12},
  # Central & Cauvery Delta Region
  "trichy": {"name": "Tiruchirappalli (Trichy)", "lat": 10.7905, "lon": 78.7047, "zoom": 12},
  "thanjavur": {"name": "Thanjavur (Cauvery Delta)", "lat": 10.7870, "lon": 79.1378, "zoom": 12},
  "nagapattinam": {"name": "Nagapattinam (Delta Coast)", "lat": 10.7656, "lon": 79.8424, "zoom": 12},
  "mayiladuthurai": {"name": "Mayiladuthurai", "lat": 11.1075, "lon": 79.6522, "zoom": 12},
  "tiruvarur": {"name": "Tiruvarur", "lat": 10.7725, "lon": 79.6365, "zoom": 12},
  "karur": {"name": "Karur", "lat": 10.9601, "lon": 78.0766, "zoom": 12},
  "perambalur": {"name": "Perambalur", "lat": 11.2342, "lon": 78.8820, "zoom": 12},
  "ariyalur": {"name": "Ariyalur", "lat": 11.1401, "lon": 79.0786, "zoom": 12},
  "pudukkottai": {"name": "Pudukkottai", "lat": 10.3797, "lon": 78.8208, "zoom": 12},
  # Southern Region
  "madurai": {"name": "Madurai", "lat": 9.9252, "lon": 78.1198, "zoom": 12},
  "dindigul": {"name": "Dindigul", "lat": 10.3673, "lon": 77.9803, "zoom": 12},
  "theni": {"name": "Theni", "lat": 10.0104, "lon": 77.4768, "zoom": 12},
  "virudhunagar": {"name": "Virudhunagar / Sivakasi", "lat": 9.5872, "lon": 77.9514, "zoom": 12},
  "sivaganga": {"name": "Sivaganga / Karaikudi", "lat": 9.8433, "lon": 78.4809, "zoom": 12},
  "ramanathapuram": {"name": "Ramanathapuram / Rameswaram", "lat": 9.3639, "lon": 78.8395, "zoom": 12},
  "thoothukudi": {"name": "Thoothukudi (Tuticorin)", "lat": 8.7642, "lon": 78.1348, "zoom": 12},
  "tirunelveli": {"name": "Tirunelveli", "lat": 8.7139, "lon": 77.7567, "zoom": 12},
  "tenkasi": {"name": "Tenkasi / Courtallam", "lat": 8.9594, "lon": 77.3152, "zoom": 12},
  "kanyakumari": {"name": "Kanniyakumari (Nagercoil)", "lat": 8.0883, "lon": 77.5385, "zoom": 12}
}

DISTRICT_SELECTOR_OPTIONS = """
              <option value="all">📍 All Tamil Nadu (Statewide Overview)</option>
              <optgroup label="── Chennai Metropolitan ──">
                <option value="chennai" selected>🏙️ Chennai (State Capital)</option>
                <option value="chengalpattu">🏙️ Chengalpattu</option>
                <option value="kancheepuram">🏛️ Kancheepuram</option>
                <option value="tiruvallur">🏭 Tiruvallur</option>
              </optgroup>
              <optgroup label="── Northern Region ──">
                <option value="cuddalore">🌊 Cuddalore (Coastal Cyclone Zone)</option>
                <option value="viluppuram">🌾 Viluppuram</option>
                <option value="kallakurichi">🌾 Kallakurichi</option>
                <option value="vellore">🏙️ Vellore</option>
                <option value="ranipet">🏭 Ranipet</option>
                <option value="tirupathur">🌄 Tirupathur</option>
                <option value="tiruvannamalai">⛰️ Tiruvannamalai</option>
              </optgroup>
              <optgroup label="── Western (Kongu) Region ──">
                <option value="coimbatore">🏙️ Coimbatore</option>
                <option value="tiruppur">👕 Tiruppur (Textile Hub)</option>
                <option value="erode">🏭 Erode (Turmeric City)</option>
                <option value="salem">⛰️ Salem (Steel City)</option>
                <option value="namakkal">🥚 Namakkal</option>
                <option value="dharmapuri">🥭 Dharmapuri</option>
                <option value="krishnagiri">🏭 Krishnagiri / Hosur</option>
                <option value="nilgiris">🏔️ Nilgiris / Ooty (Ghats)</option>
              </optgroup>
              <optgroup label="── Central & Delta Region ──">
                <option value="trichy">🏙️ Tiruchirappalli (Trichy)</option>
                <option value="thanjavur">🌾 Thanjavur (Cauvery Delta)</option>
                <option value="nagapattinam">🌊 Nagapattinam (Delta Coast)</option>
                <option value="mayiladuthurai">🌊 Mayiladuthurai</option>
                <option value="tiruvarur">🌾 Tiruvarur</option>
                <option value="karur">🏭 Karur</option>
                <option value="perambalur">🌾 Perambalur</option>
                <option value="ariyalur">🏭 Ariyalur</option>
                <option value="pudukkottai">🏛️ Pudukkottai</option>
              </optgroup>
              <optgroup label="── Southern Region ──">
                <option value="madurai">🏙️ Madurai (Cultural Hub)</option>
                <option value="dindigul">⛰️ Dindigul</option>
                <option value="theni">🌄 Theni</option>
                <option value="virudhunagar">🏭 Virudhunagar / Sivakasi</option>
                <option value="sivaganga">🏛️ Sivaganga / Karaikudi</option>
                <option value="ramanathapuram">🌊 Ramanathapuram / Rameswaram</option>
                <option value="thoothukudi">⚓ Thoothukudi (Port City)</option>
                <option value="tirunelveli">🏙️ Tirunelveli</option>
                <option value="tenkasi">🌊 Tenkasi / Courtallam</option>
                <option value="kanyakumari">🌊 Kanniyakumari (Cape Comorin)</option>
              </optgroup>
"""

print("TN config ready")
