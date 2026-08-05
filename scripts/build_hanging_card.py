from pathlib import Path
import base64

root = Path(__file__).resolve().parents[1]
img = (root / "assets/images/profile.png").read_bytes()
b64 = base64.b64encode(img).decode("ascii")

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="260" height="380" viewBox="0 0 260 380" fill="none">
  <defs>
    <linearGradient id="cardBg" x1="20" y1="50" x2="240" y2="360" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#071018"/>
      <stop offset="100%" stop-color="#0A1A2E"/>
    </linearGradient>
    <linearGradient id="border" x1="20" y1="50" x2="240" y2="360" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#00F0FF"/>
      <stop offset="55%" stop-color="#39FF14"/>
      <stop offset="100%" stop-color="#00F0FF"/>
    </linearGradient>
    <linearGradient id="vGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#00F0FF"/>
      <stop offset="100%" stop-color="#39FF14"/>
    </linearGradient>
    <linearGradient id="metal" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#8BE9FF"/>
      <stop offset="100%" stop-color="#00F0FF"/>
    </linearGradient>
    <clipPath id="avatarClip">
      <circle cx="130" cy="118" r="38"/>
    </clipPath>
    <filter id="cardShadow" x="-25%" y="-10%" width="150%" height="130%">
      <feDropShadow dx="0" dy="10" stdDeviation="8" flood-color="#00F0FF" flood-opacity="0.35"/>
    </filter>
  </defs>

  <ellipse cx="130" cy="368" rx="70" ry="7" fill="#00F0FF" opacity="0.16"/>

  <g transform="rotate(-2.5 130 18)">
    <animateTransform attributeName="transform" type="rotate" values="-3.2 130 18; 3.2 130 18; -3.2 130 18" dur="3.5s" repeatCount="indefinite" calcMode="spline" keySplines="0.42 0 0.58 1; 0.42 0 0.58 1" keyTimes="0;0.5;1"/>

    <rect x="108" y="4" width="44" height="9" rx="3" fill="#0A1524" stroke="url(#metal)" stroke-width="1.4"/>
    <rect x="114" y="12" width="32" height="14" rx="2.5" fill="#071525" stroke="#00F0FF" stroke-width="1.2"/>
    <circle cx="130" cy="19" r="3.5" fill="#050A12" stroke="#39FF14" stroke-width="1.2"/>

    <path d="M120 26 Q114 40 108 56" stroke="#39FF14" stroke-width="2.6" stroke-linecap="round" fill="none"/>
    <path d="M140 26 Q146 40 152 56" stroke="#00F0FF" stroke-width="2.6" stroke-linecap="round" fill="none"/>
    <circle cx="108" cy="58" r="4.5" fill="#071525" stroke="#00F0FF" stroke-width="1.4"/>
    <circle cx="152" cy="58" r="4.5" fill="#071525" stroke="#00F0FF" stroke-width="1.4"/>

    <g filter="url(#cardShadow)">
      <rect x="22" y="52" width="216" height="300" rx="16" fill="url(#cardBg)" stroke="url(#border)" stroke-width="2"/>
      <rect x="22" y="52" width="216" height="28" rx="16" fill="#061525"/>
      <rect x="22" y="66" width="216" height="14" fill="#061525"/>
      <text x="130" y="71" text-anchor="middle" fill="#00F0FF" font-family="Arial, Helvetica, sans-serif" font-size="9" font-weight="700" letter-spacing="2">DEVELOPER ID</text>

      <circle cx="130" cy="118" r="42" fill="none" stroke="#00F0FF" stroke-width="1.8"/>
      <circle cx="130" cy="118" r="39.5" fill="none" stroke="#39FF14" stroke-width="1" opacity="0.75"/>
      <circle cx="130" cy="118" r="38" fill="#071525"/>
      <image href="data:image/png;base64,{b64}" xlink:href="data:image/png;base64,{b64}" x="92" y="80" width="76" height="76" clip-path="url(#avatarClip)" preserveAspectRatio="xMidYMid slice"/>

      <text x="130" y="178" text-anchor="middle" fill="#FFFFFF" font-family="Arial, Helvetica, sans-serif" font-size="14" font-weight="800">Chetan Selukar</text>
      <text x="130" y="196" text-anchor="middle" fill="#39FF14" font-family="Arial, Helvetica, sans-serif" font-size="9" font-weight="600">Technical Architect</text>
      <text x="130" y="210" text-anchor="middle" fill="#8BE9FF" font-family="Arial, Helvetica, sans-serif" font-size="8">AI Developer | .NET | Azure</text>
      <text x="130" y="224" text-anchor="middle" fill="#A0B4C8" font-family="Arial, Helvetica, sans-serif" font-size="8">14+ Years | Ahmedabad</text>

      <path d="M48 236 H212" stroke="url(#border)" stroke-width="1" opacity="0.65"/>

      <g transform="translate(105,246)">
        <rect width="50" height="30" rx="8" fill="#071525" stroke="url(#vGrad)" stroke-width="1.2"/>
        <path d="M14 24 L25 7 L36 24 H30 L25 15 L20 24 Z" fill="url(#vGrad)"/>
      </g>
      <text x="130" y="292" text-anchor="middle" fill="#00F0FF" font-family="Arial, Helvetica, sans-serif" font-size="8" font-weight="700" letter-spacing="1.5">VEDAUTOM</text>

      <g transform="translate(98,302)">
        <rect width="64" height="34" rx="5" fill="#050A12" stroke="#00F0FF" stroke-width="1"/>
        <g fill="#39FF14">
          <rect x="6" y="5" width="7" height="7"/><rect x="15" y="5" width="3" height="3"/><rect x="20" y="5" width="7" height="7"/>
          <rect x="6" y="14" width="3" height="3"/><rect x="11" y="14" width="7" height="3"/><rect x="20" y="15" width="3" height="3"/><rect x="25" y="14" width="3" height="7"/>
          <rect x="6" y="22" width="7" height="7"/><rect x="15" y="23" width="3" height="3"/><rect x="20" y="22" width="7" height="7"/>
          <rect x="34" y="5" width="6" height="6"/><rect x="42" y="6" width="3" height="3"/><rect x="48" y="5" width="8" height="8"/>
          <rect x="34" y="15" width="3" height="6"/><rect x="40" y="16" width="8" height="3"/><rect x="50" y="15" width="6" height="6"/>
          <rect x="34" y="24" width="7" height="5"/><rect x="44" y="25" width="3" height="3"/><rect x="50" y="24" width="7" height="5"/>
        </g>
      </g>
      <text x="130" y="348" text-anchor="middle" fill="#8BE9FF" font-family="Arial, Helvetica, sans-serif" font-size="7" letter-spacing="1.5">SCAN TO CONNECT</text>
    </g>
  </g>
</svg>
"""

out = root / "assets/developer-card-v4.svg"
out.write_text(svg, encoding="ascii", newline="\n")
print(f"wrote {out} bytes={out.stat().st_size}")
