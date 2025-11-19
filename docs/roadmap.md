# 🗺️ Dibble Roadmap

> **Repository:** [github.com/mister-chicken/dibble](https://github.com/mister-chicken/dibble)
> **Vision:** A beautiful, open-source restaurant review app that helps you remember, reflect on, and share where you eat — starting with effortless map-based logging and photo association.

---

## 🎯 End Goal: Problems We Solve

### What Problems Does This App Solve?

**Problem 1: Lost Dining Memories**
- You've eaten at amazing restaurants but can't remember where they were or what made them special
- Photos from meals are scattered across your phone with no context or connection to the place
- You want to revisit that perfect spot but can't find it on a map

**Problem 2: Disconnected Review Experience**
- Existing review platforms are cluttered, impersonal, and focused on ratings rather than personal experiences
- Your dining history is fragmented across multiple apps and services
- You want a personal, visual way to track your own restaurant journey

**Problem 3: Sharing Without Context**
- Hard to share restaurant recommendations with friends in a meaningful way
- No easy way to see where your friends are eating and discover new places through trusted connections
- Want to build a personal food map that tells your story

### What In This App Helps Solve These Problems?

**Solution 1: Effortless Location-Based Logging**
- **Map-centric interface** puts restaurants in their geographic context — see where you've been and where you want to go
- **Automatic photo association** tags your meal photos as you eat, creating visual memories tied to places
- **Visual restaurant pins** on a map make it easy to rediscover places you've visited

**Solution 2: Personal Experience Tracking**
- **Your own restaurant journal** where every visit, photo, and review is stored in one place
- **Rich detail views** combine photos, notes, and reviews to recreate the full experience of each meal
- **Timeline of dining experiences** helps you reflect on your food journey over time

**Solution 3: Social Discovery & Sharing**
- **Social feed** lets you see where friends are eating and discover new places through trusted recommendations
- **Visual storytelling** through photos and reviews makes recommendations more meaningful than star ratings alone

**Solution 4: Data-Based Recommendations**
- **AI-driven suggestions** analyze your dining history, preferences, and taste patterns to recommend restaurants you'll love
- **Smart discovery** suggests new places based on similar restaurants you've enjoyed, cuisine types you prefer, and locations you frequent
- **Personalized insights** help you explore new cuisines and neighborhoods while staying true to your preferences

### The Ideal User Experience

When you open Dibble, you see:
- **A map of your dining life** — pins showing every restaurant you've visited, with photos and memories attached
- **Effortless logging** — take a photo at a restaurant, and it's automatically associated with that location and the menu items
- **Rich memories** — tap any pin to see photos, reviews, and notes from your visits, recreating the full experience
- **Social discovery** — browse your friends' dining adventures and discover new places through people you trust
- **Smart recommendations** — AI-powered suggestions for new restaurants based on your taste history and preferences
- **Your story** — a personal, visual record of where you eat, what you love, and the memories you've made
- **Next Steps** -- a currated view for what you crave, driven by you and your network
**In short:** Dibble transforms scattered dining memories into a beautiful, map-based journal that helps you remember, reflect on, and share your food experiences.

---

## 🚀 Version 0.1.0 — Navigation Foundation
**Goal:** Establish core navigation structure with bottom tab bar and placeholder pages.

- [ ] Bottom tab bar navigation with three tabs: Map View (center), Account (right), Social Feed (left)
- [ ] Placeholder pages for all three main views with basic routing between tabs
- [ ] Tab state management with visual indicators for active tab state

---

## 👤 Version 0.2.0 — Account & Data Integration
**Goal:** Basic account functionality and local data persistence with SurrealDB.

- [ ] Account page with profile form (name, preferences) and settings UI
- [ ] SurrealDB integration with user profile data model and CRUD operations
- [ ] Server functions for profile data persistence and frontend integration

---

## 🗺️ Version 0.3.0 — Basic Map Component
**Goal:** Integrate map component and display local restaurant data.

- [ ] OpenStreetMap or Mapbox integration with basic map controls (zoom, pan) in center tab
- [ ] Restaurant data model in SurrealDB with server functions for coordinate-based queries
- [ ] Restaurant markers/pins displayed on map with data fetched from SurrealDB

---

## 🏪 Version 0.4.0 — Restaurant Component
**Goal:** Interactive restaurant details from map interactions.

- [ ] Click handlers on map markers to open restaurant detail view/modal
- [ ] Restaurant detail component displaying name, location, and notes
- [ ] Server function to fetch individual restaurant details with expanded data model

---

## 📝 Version 0.5.0 — Add Your Experience
**Goal:** Enable users to add photos, reviews, and experiences to restaurants.

- [ ] Photo upload functionality with association to restaurants and thumbnail gallery display
- [ ] Review input form and display system with text feedback stored in SurrealDB
- [ ] Server functions for photo upload, review submission, and data persistence

---

## 🥚 Version 1.0.0 — Core Experience (MVP)
**Goal:** Complete MVP with full map-based restaurant logging, photo association, and review system.

- [ ] Complete map experience with user location detection, restaurant pins, and full CRUD operations for restaurants
- [ ] Full restaurant detail views with photo galleries, review system, and shared app state management
- [ ] Infrastructure: Dockerfile, CI workflows, SurrealDB deployment, and complete REST API endpoints

> 📆 **Milestone:** [V1.0.0 — MVP Core Experience](../../milestone/1)

---

## 🍳 Version 1.1.0 — Sharing & Sync
**Goal:** Sync your reviews and share feedback with other users.

- [ ] User accounts with authentication (basic auth or OAuth via GitHub/Google) and cloud sync
- [ ] Privacy controls: toggle visibility for private vs. shared reviews with feed view for friends' reviews
- [ ] Hosted image storage, API versioning, and enhanced user profile with follow interactions

> 📆 **Milestone:** [V1.1.0 — Sync + Social](../../milestone/2)

---

## 🍽️ Version 2.0.0 — Native + AI Integration
**Goal:** Deliver native builds for desktop/mobile and integrate AI-assisted features for menu parsing and photo tagging.

- [ ] AI features: menu parsing (OCR/HTML), auto-suggest dish tags for photos (vision models), and review summarization
- [ ] Native builds: desktop (macOS/Windows/Linux) and mobile (iOS/Android) via Dioxus with shared component logic
- [ ] UX enhancements: offline mode with sync, in-app search, and map clustering/filtering

> 📆 **Milestone:** [V2.0.0 — Native + AI](../../milestone/3)

---

## 🔮 Future Ideas
These are stretch or post-1.0 ideas that can evolve as the community grows.

- AI-driven restaurant recommendations based on taste history.
- Automatic categorization (breakfast, dinner, coffee spots).
- Export data to CSV / JSON for personal tracking.
- Integration with photo libraries (Apple Photos / Google Photos).
- Optional privacy-first public profiles (“Sam’s top 5 NYC cafés”).

---

## 🧭 Project Management

| Resource | Link |
|-----------|------|
| 📊 Live Roadmap Board | _Coming soon: [GitHub Projects View](../../projects/1)_ |
| 🐞 Issues | [Open Issues](../../issues) |
| 💡 Feature Requests | [Discussions](../../discussions) |
| 📘 Documentation | `/docs/` folder in repo |

---

### ✨ Contribution Vision
Dibble is built to be approachable, modular, and fun to contribute to.
Future contributors should be able to:
- Build or run locally with `cargo run`.
- Work on shared Rust structs across frontend and backend.
- Extend Dioxus components without platform rewrites.

---

_“Every meal tells a story. Dibble helps you remember it.”_
