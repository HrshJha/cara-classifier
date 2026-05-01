<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=220&section=header&text=CARA%20Classifier&fontSize=52&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Career%20Alignment%20%26%20Recommendation%20Algorithm%20for%20Healthcare%20Graduates&descAlignY=58&descSize=16&descColor=ccccff" width="100%"/>
</br>
<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)
[![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen?style=for-the-badge)](CONTRIBUTING.md)

</div>

<table align="center">
  <tr>
    <td align="center">🧠<br><b>Rule-Based</b><br>Scoring Engine</td>
    <td align="center">📊<br><b>3-Signal</b><br>Weighted Analysis</td>
    <td align="center">🎯<br><b>11 Tracks</b><br>Career Paths</td>
    <td align="center">🎓<br><b>4 Degrees</b><br>MHA/MPH/MSHI/MBA</td>
    <td align="center">📝<br><b>Explainable</b><br>Rationales</td>
  </tr>
</table>

---

> *"Intent > Experience > Background" — CARA weights stated career goals above past roles, because career classification should be forward-looking, not backward-looking.*

---

## 📌 The Problem

Healthcare graduates from diverse backgrounds — dentistry, nursing, computer science, sociology — struggle to identify which advanced degree (MHA, MPH, MSHI, MBA-HC) and career track aligns with their unique combination of academic training, professional experience, and career aspirations.

```
    Career counselor intuition → Generic advice → Mismatched degree → Wasted tuition + lost momentum
```

| Failure Type | Symptoms | Impact |
|--------------|----------|--------|
| 🔴 Critical | Clinical dentist advised to pursue MPH when they want hospital administration | $80K tuition wasted, 2 years off track |
| 🟡 Subtle | CS grad steered toward MBA instead of MSHI despite EHR experience | Skills undervalued, weaker network fit |
| 🟠 Partial | Policy-focused candidate placed in general public health track | Coursework misaligned with career goals |

> Existing career tools either use generic ML models (black box) or manual counseling (expensive, inconsistent). Neither scales.

**CARA solves this at the keyword-matching + weighted scoring level**

---

## 💡 The Solution

CARA (Career Alignment & Recommendation Algorithm) is a rule-based classification engine that evaluates three signals — SOP keywords (50%), experience keywords (30%), and academic cluster alignment (20%) — to produce explainable degree and track recommendations.

```
    "wants to transition from clinical to administrative leadership"
                        ↓ keyword extraction
         ┌────────────────────────────────────────┐
         │  leadership → T01 (Admin track)        │  ← ✅ Primary signal
         │  quality improvement → T01             │  ← ✅ Reinforcing
         │  organizational → T01                  │  ← ✅ Triple match
         │  administrative → T01                  │  ← ✅ Quadruple
         └────────────────────────────────────────┘
                        ↓ weighted aggregate
              T01: 0.82 (confidence score)
              → MHA recommended (primary degree)
```

This matters because **career transitions require explicit intent to override background signals** — a dentist who says "administrative leadership" should get MHA, not be penalized for lacking admin coursework.

---

## 🚀 Features

- 🎯 **SOP Keyword Scoring** — Parses statement of purpose for track-specific keywords (11 tracks × 8-15 keywords each) with normalized scoring
- 💼 **Experience Pattern Matching** — Scans role descriptions for career track signals (e.g., "Deloitte" → Consulting, "FHIR" → Informatics)
- 📚 **Academic Cluster Mapping** — Maps 10 subject clusters (Life Sciences, Policy, IT, etc.) to degree eligibility
- ⚖️ **Weighted Signal Fusion** — 50% SOP + 30% Experience + 20% Academic clusters = explainable recommendations
- 📝 **Keyword-Level Rationales** — Every recommendation includes exact matched keywords: `"SOP keywords matched: 'leadership', 'quality improvement'"`
- 🧪 **Debug Output** — Intermediate scores printed during classification for transparency and troubleshooting
- 📦 **JSON Candidate Profiles** — Structured input format with subjects, experience, strengths, and SOP
- 📊 **Batch Processing** — Classifies all candidates in `candidates/` directory, outputs `results.json`

---

## 🛠 Tech Stack

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![JSON](https://img.shields.io/badge/JSON-Data-000000?style=flat-square&logo=json&logoColor=white)](https://www.json.org/)

</div>

| Component | Technology | Why |
|-----------|------------|-----|
| Runtime | Python 3.8+ | String matching, dict operations, no external deps needed |
| Data Format | JSON | Candidate profiles portable, human-readable, API-ready |
| Scoring Logic | Custom rule-based engine | Transparent weights, debuggable, no black-box ML |
| Output | Structured JSON | Machine-consumable results, easy to build UI on top |

---

## 📂 Project Structure

```
cara-classifier/
├── 📁 framework.py          ← CLUSTERS, DEGREES, TRACKS constants (10 clusters, 11 tracks)
├── 📁 scorer.py             ← Scoring engine: score_clusters(), score_sop(), classify()
├── 📁 classifier.py         ← Main runner: loads JSONs, runs classify(), writes results
├── 📁 candidates/           ← Input candidate profiles
│   ├── 📄 freshgrad_01.json      ← BDS dentist → MHA/T01
│   ├── 📄 mph_community_01.json  ← Sociology BA → MPH/T05
│   ├── 📄 mba_finance_01.json    ← Finance BCom → MBA-HC/T03
│   ├── 📄 mshi_tech_01.json      ← CS BTech → MSHI/T09
│   ├── 📄 mha_ltc_01.json        ← Nursing BSc → MHA/T01
│   └── 📄 mph_policy_01.json     ← PolSci BA → MPH/T07
├── 📁 outputs/              ← Generated results
│   └── 📄 results.json           ← Final classification output
└── 📄 README.md             ← This file
```

---

## ⚙️ Installation & Setup

| Requirement | Version | Link |
|-------------|---------|------|
| Python | 3.8+ | [python.org](https://www.python.org/downloads/) |
| pip | Included | Bundled with Python |

### Step 1 — Clone or Download

```bash
git clone https://github.com/hrshjha/cara-classifier.git
cd cara-classifier
```

### Step 2 — Verify Python Version

```bash
python --version  # Should show Python 3.8 or higher
```

### Step 3 — Run the Classifier

```bash
python classifier.py
```

### Step 4 — Verify Output

```bash
cat outputs/results.json
```

Expected: 6 classified candidates with `recommended_degree` and `top_3_tracks`.

### Step 5 — Access Results

Results saved to `outputs/results.json` — open in any JSON viewer or parse programmatically.

---

## 🌐 Demo & API

**Live Demo:** Coming Soon — CLI tool currently, web interface planned in roadmap.

**What you can try right now:**
1. Add your own candidate JSON to `candidates/`
2. Run `python classifier.py`
3. See your candidate classified alongside the 6 sample profiles

**Flow:**
```
Your candidate JSON → classifier.py → scorer.classify() → results.json
```

---

## 🧪 Usage

### Endpoints (Function Interface)

| Method | Function | Description |
|--------|----------|-------------|
| `classify()` | `scorer.classify(candidate_dict)` | Main entry point — returns structured classification result |
| `score_clusters()` | `scorer.score_clusters(subjects_list)` | Maps subjects to degree scores |
| `score_sop()` | `scorer.score_sop(sop_text)` | Returns track scores + matched keywords |
| `score_experience()` | `scorer.score_experience(roles_list)` | Returns track scores + matched keywords |

### Example: Classify a Custom Candidate

```python
from scorer import classify

candidate = {
    "id": "Custom_Candidate_01",
    "degree": "BDS",
    "university": "Maharashtra University of Health Sciences",
    "subjects": ["anatomy", "physiology", "biochemistry", "pathology", "pharmacology", "community medicine"],
    "experience_years": 0,
    "experience_roles": [],
    "sop": "wants to transition from clinical to administrative leadership; interested in organizational leadership and quality improvement"
}

result = classify(candidate)
print(result)
```

### Example Output

```json
{
  "candidate_id": "Custom_Candidate_01",
  "recommended_degree": "MHA",
  "degree_rationale": "Academic clusters most strongly support MPH and MSHI. Top-ranked track T01 has MHA as primary degree. Combined signal points to MHA.",
  "top_3_tracks": [
    {
      "rank": 1,
      "track_id": "T01",
      "track_name": "Healthcare Administration, Operations, Quality & Risk",
      "score": 0.2429,
      "rationale": "SOP keywords matched: 'leadership', 'quality improvement', 'organizational', 'administrative'. Academic background supports MHA (degree alignment score: 0.5)."
    }
  ]
}
```

### Claim/Label Reference

| Track ID | Label | Primary Degree |
|----------|-------|----------------|
| T01 | Healthcare Administration | MHA |
| T02 | Healthcare Consulting | MBA-HC |
| T03 | Healthcare Finance | MBA-HC |
| T04 | Behavioral Health | MPH |
| T05 | Public/Community Health | MPH |
| T06 | Population Health Analytics | MPH |
| T07 | Health Policy | MPH |
| T08 | Environmental/Occupational Health | MPH |
| T09 | Digital Health/Informatics | MSHI |
| T10 | Clinical Research/Regulatory | MBA-HC |
| T11 | Healthcare Entrepreneurship | MBA-HC |

---

## 🔬 Pipeline — Deep Dive

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                           CARA CLASSIFICATION PIPELINE                       │
└──────────────────────────────────────────────────────────────────────────────┘

    ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
    │  CANDIDATE  │     │  CANDIDATE  │     │  CANDIDATE  │
    │   SUBJECTS  │     │     SOP     │     │  EXPERIENCE │
    └──────┬──────┘     └──────┬──────┘     └──────┬──────┘
           │                   │                   │
           ▼                   ▼                   ▼
    ┌─────────────────────────────────────────────────────────┐
    │              score_clusters()                           │
    │   subjects → lowercase → match against 10 clusters      │
    │   each match → +1 to cluster's supported degrees        │
    │   normalize → max_score = 1.0                           │
    └─────────────────────────────────────────────────────────┘
           │
           ▼
    ┌─────────────────────────────────────────────────────────┐
    │              score_sop()                                │
    │   SOP → lowercase → match against 11 track keywords     │
    │   score = hits / total_keywords_per_track               │
    │   returns: {track_scores, matched_keywords}             │
    └─────────────────────────────────────────────────────────┘
           │
           ▼
    ┌─────────────────────────────────────────────────────────┐
    │              score_experience()                         │
    │   roles → join → lowercase → match experience keywords  │
    │   score = hits / total_keywords_per_track               │
    │   returns: {track_scores, matched_keywords}             │
    └─────────────────────────────────────────────────────────┘
           │
           ▼
    ┌─────────────────────────────────────────────────────────┐
    │              COMBINE SIGNALS                            │
    │   final[T] = sop[T]×0.50 + exp[T]×0.30 + deg[T]×0.20   │
    │   deg[T] = cluster_score[track.primary_degree]          │
    └─────────────────────────────────────────────────────────┘
           │
           ▼
    ┌─────────────────────────────────────────────────────────┐
    │              RANK & SELECT TOP 3                        │
    │   sort by final_score descending                        │
    │   take top 3 track IDs                                  │
    │   build rationales from matched keywords                │
    └─────────────────────────────────────────────────────────┘
           │
           ▼
    ┌─────────────────────────────────────────────────────────┐
    │              score_degree_from_tracks()                 │
    │   rank_weights = [1.0, 0.5, 0.25] for top 3             │
    │   add cluster_degree_scores × 0.1                       │
    │   return max(degree_votes)                              │
    └─────────────────────────────────────────────────────────┘
           │
           ▼
    ┌─────────────────────────────────────────────────────────┐
    │              OUTPUT                                     │
    │   { candidate_id, recommended_degree,                   │
    │     degree_rationale, top_3_tracks: [...] }             │
    └─────────────────────────────────────────────────────────┘
```

### Aggregation Rules

| Signal | Weight | Normalization |
|--------|--------|---------------|
| SOP Keywords | 50% | hits / total_keywords_per_track |
| Experience | 30% | hits / total_keywords_per_track |
| Degree Alignment | 20% | cluster_degree_score / max_cluster_score |

### Decision Logic

- **Top track determines primary degree** — T01 → MHA, T09 → MSHI, etc.
- **Cluster scores break ties** — If SOP and experience are weak, academic background provides signal
- **Intent overrides background** — Clinical degree + admin SOP → admin track wins

---

## 🐳 Docker Deployment

Coming in v2.0 — currently CLI-only. Planned Docker support:

```bash
# Build
docker build -t cara-classifier .

# Run
docker run -v $(pwd)/candidates:/app/candidates -v $(pwd)/outputs:/app/outputs cara-classifier

# Verify
docker run cara-classifier python classifier.py --test
```

---

## ⚙️ Configuration

CARA uses hardcoded constants in `framework.py`. To adjust scoring weights:

```python
# In scorer.py, classify() function:

# Current weights:
SOP_WEIGHT = 0.50        # Stated intent (highest priority)
EXP_WEIGHT = 0.30        # Actual experience
DEGREE_WEIGHT = 0.20     # Academic background

# To change: modify these values (must sum to 1.0)
```

### Track Keyword Customization

```python
# In framework.py, TRACKS dict:

"T01": {
    "sop_keywords": ["leadership", "operations", "quality improvement", ...],
    "experience_keywords": ["hospital", "operations", "administrator", ...]
}
```

| Setting | Default | Effect |
|---------|---------|--------|
| SOP_WEIGHT | 0.50 | Higher = intent matters more than background |
| EXP_WEIGHT | 0.30 | Higher = work history weighted more heavily |
| DEGREE_WEIGHT | 0.20 | Higher = academic clusters more influential |
| rank_weights | [1.0, 0.5, 0.25] | Top track's degree gets strongest vote |

---

## 📦 Scope & Limitations

**CARA does NOT:**
- Use machine learning or neural networks (rule-based only)
- Handle candidates without an SOP (empty SOP = 0 score for all tracks)
- Support degrees outside MHA/MPH/MSHI/MBA-HC (extensible in framework.py)
- Provide real-time API (batch CLI tool only, currently)

**Performance depends on:**
- SOP length and keyword density (shorter SOPs = fewer matches)
- Specificity of experience role descriptions
- Subject list completeness in candidate JSON

> **Ideal use case:** Healthcare career counseling at scale — process 100+ candidates, generate explainable recommendations, human counselor reviews edge cases.

---

## 📈 Future Roadmap

| Status | Feature |
|--------|---------|
| ✅ | Core scoring engine (cluster, SOP, experience) |
| ✅ | 6 sample candidates with validated classifications |
| ✅ | Keyword-level rationale generation |
| 🔜 | REST API with FastAPI (POST /classify endpoint) |
| 🔜 | Web UI for candidate JSON input + results visualization |
| 🔜 | Docker container for one-command deployment |
| 🔜 | PDF report generation with charts and track descriptions |
| 🔜 | Admin dashboard to manage keyword dictionaries |

---

## 🤝 Contributing

```bash
# 1. Fork the repo
git fork https://github.com/hrshjha/cara-classifier

# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/cara-classifier

# 3. Create feature branch
git checkout -b feature/add-new-track

# 4. Make changes + test
python classifier.py  # Verify all 6 candidates still classify correctly

# 5. Commit with conventional commits
git commit -m "feat: add T12 track for Medical Education"

# 6. Push + open PR
git push origin feature/add-new-track
# Then open PR at github.com/hrshjha/cara-classifier/pulls
```

**Contribution standards:**
- ✅ Add new tracks in `framework.py` with 8+ SOP keywords and 5+ experience keywords
- ✅ Update unit tests if modifying scoring logic
- ✅ Include example candidate JSON for new tracks
- ✅ Document rationale for keyword choices in PR description
- ✅ Run `python classifier.py` and verify no regressions

**All PRs welcome** — whether you're fixing a typo or adding a new career track.

---

## 📜 License

```
MIT License

Copyright (c) 2026 hrshjha

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

<div align="center">

## 🌟 Support the Project

<table>
  <tr>
    <th>Action</th>
    <th>Impact</th>
  </tr>
  <tr>
    <td>⭐ Star</td>
    <td>Helps others discover CARA</td>
  </tr>
  <tr>
    <td>🍴 Fork</td>
    <td>Customize for your use case</td>
  </tr>
  <tr>
    <td>🐛 Issue</td>
    <td>Report bugs or suggest features</td>
  </tr>
  <tr>
    <td>📢 Share</td>
    <td>Spread the word on Twitter/LinkedIn</td>
  </tr>
  <tr>
    <td>💬 Feedback</td>
    <td>Tell me how CARA could serve you better</td>
  </tr>
</table>

[![Star](https://img.shields.io/badge/⭐_Star_this_Repo-black?style=for-the-badge)](https://github.com/hrshjha/cara-classifier)
[![Fork](https://img.shields.io/badge/🍴_Fork-black?style=for-the-badge&color=blue)](https://github.com/hrshjha/cara-classifier/fork)
[![Issue](https://img.shields.io/badge/🐛_Report_Issue-black?style=for-the-badge&color=orange)](https://github.com/hrshjha/cara-classifier/issues)

</div>

---

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=130&section=footer&animation=fadeIn&fontColor=ccccff" width="100%"/>

<div align="center">

**Built with ❤️ by [@hrshjha](https://github.com/hrshjha)**

*"Career transitions require explicit intent to override background signals."*

[![GitHub followers](https://img.shields.io/github/followers/hrshjha?style=social)](https://github.com/hrshjha?tab=followers)
[![Twitter](https://img.shields.io/twitter/follow/hrshjha?style=social)](https://twitter.com/hrshjha)

</div>
