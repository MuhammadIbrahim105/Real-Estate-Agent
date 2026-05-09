# 🏠 AI-Powered Real Estate Lead Engagement System

An end-to-end autonomous sales pipeline that manages lead ingestion, personalized outreach, multi-turn AI conversation, and high-intent detection — cutting response time from hours to **under 10 seconds**.

---

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    Real Estate AI Pipeline                       │
├──────────────┬──────────────┬──────────────┬────────────────────┤
│   Layer 1    │   Layer 2    │   Layer 3    │     Layer 4        │
│              │              │              │                    │
│  Lead        │  Scraping &  │  Convo       │  Intent            │
│  Ingestion   │  RAG         │  Engine      │  Detection         │
│  (Sheets)    │  (Deep Lake) │  (LangChain) │  (LLM + Firebase)  │
└──────────────┴──────────────┴──────────────┴────────────────────┘
                              │
                    ┌─────────▼─────────┐
                    │   Layer 5         │
                    │   Pipeline        │
                    │   Analytics       │
                    └───────────────────┘
```

## ✨ Features

| Feature | Description |
|---|---|
| **Lead Ingestion** | Polls Google Sheets every 30s, auto-queues new leads |
| **Property RAG** | Scrapes Zameen.com, Booking.com, Facebook Ads → embeds → Deep Lake |
| **AI Conversation** | LangChain + GPT-4 with per-client memory, full multi-turn dialogue |
| **Intent Detection** | Flags payment/financial language → Firebase log → human handoff |
| **Analytics Dashboard** | React frontend with real-time funnel metrics |
| **Speed** | < 10 second response time vs hours manually |
| **Scale** | 200+ qualified leads/month processed autonomously |

---

## 📁 Project Structure

```
real-estate-ai-system/
├── src/
│   ├── ingestion/          # Google Sheets lead polling
│   ├── scraping/           # Property scrapers (Zameen, Booking, FB)
│   ├── conversation/       # LangChain conversation engine
│   ├── intent/             # Intent detection & Firebase logging
│   ├── analytics/          # Pipeline metrics tracker
│   └── utils/              # Shared utilities
├── frontend/               # React dashboard
│   └── src/
│       ├── components/     # UI components
│       ├── pages/          # Dashboard pages
│       ├── hooks/          # Custom React hooks
│       └── utils/          # Frontend utilities
├── config/                 # Configuration files
├── tests/                  # Unit & integration tests
├── docs/                   # Documentation
└── main.py                 # Entry point
```

---

## 🚀 Quick Start

### Prerequisites

```bash
Python 3.10+
Node.js 18+
Google Cloud credentials (Sheets API)
OpenAI API key
Firebase project
```

### Backend Setup

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/real-estate-ai-system.git
cd real-estate-ai-system

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env with your credentials

# Run the system
python main.py
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

## ⚙️ Environment Variables

```env
# OpenAI
OPENAI_API_KEY=sk-...

# Google Sheets
GOOGLE_SHEETS_CREDENTIALS_PATH=config/credentials.json
GOOGLE_SHEET_ID=your_sheet_id_here

# Deep Lake
ACTIVELOOP_TOKEN=your_activeloop_token
DEEPLAKE_DATASET_PATH=hub://your_org/real-estate-listings

# Firebase
FIREBASE_CREDENTIALS_PATH=config/firebase-credentials.json
FIREBASE_DATABASE_URL=https://your-project.firebaseio.com

# WhatsApp / Messaging
WHATSAPP_API_KEY=your_api_key
WHATSAPP_PHONE_NUMBER_ID=your_phone_number_id

# System
POLL_INTERVAL_SECONDS=30
REPLY_CHECK_INTERVAL_SECONDS=5
AGENT_NOTIFICATION_EMAIL=agent@yourcompany.com
LOG_LEVEL=INFO
```

---

## 📊 Pipeline Flow

```
New Lead in Google Sheets
         │
         ▼
    Lead Ingestion (polls every 30s)
         │
         ▼
    Property Context Fetch (RAG from Deep Lake)
         │
         ▼
    Personalized Opening Message Sent
         │
         ▼
    Polling Loop (every 5s) ◄──────────────┐
         │                                  │
         ▼                                  │
    Reply Received                          │
         │                                  │
         ├──► Intent Detection ─► FLAG? ──► Firebase Log + Agent Alert
         │                                  │
         └──► Continue Conversation ────────┘
```

---

## 🧠 Tech Stack

**Backend**
- `LangChain` — Conversation chains with memory
- `Deep Lake` — Vector store for property embeddings
- `OpenAI GPT-4` — Conversation + intent classification
- `Google Sheets API` — Lead ingestion
- `Firebase Firestore` — Event logging & flags
- `BeautifulSoup / Playwright` — Property scraping
- `FastAPI` — REST API for frontend

**Frontend**
- `React 18` — Dashboard UI
- `Recharts` — Pipeline analytics charts
- `TailwindCSS` — Styling
- `Firebase SDK` — Real-time updates

---

## 📈 Results

- ✅ **200+ leads/month** processed autonomously
- ✅ **< 10 second** response time (vs hours manually)
- ✅ **100% conversion-focused** human touchpoints (intent-flagged only)
- ✅ **Full funnel visibility** — outreach → replied → engaged → flagged → closed

---

## 📄 License

MIT License — see [LICENSE](LICENSE)

---

*Built with LangChain, Deep Lake, OpenAI, Firebase, Google Sheets API*
