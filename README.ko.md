<div align="center">

**[English](README.md)** | **한국어**

# oh-my-agent-startup

### 미션 하나. 에이전트 열 명. 바로 출시.

한 문장의 미션으로부터 웹 애플리케이션을 자율적으로 만들어내는 AI 스타트업 팀.<br/>
Compass가 10명의 전문 에이전트를 오케스트레이션 — 토론하고, 디자인하고, 코딩하고, 리뷰하고, 테스트하고, 배포합니다.<br/>
모든 소통은 Linear로. 모든 결정은 추적 가능. 사람 개입 불필요.

[![Claude Code](https://img.shields.io/badge/Built_for-Claude_Code-6B4FBB?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyeiIvPjwvc3ZnPg==)](https://claude.ai/code)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue?style=for-the-badge)](LICENSE)
[![Agents](https://img.shields.io/badge/에이전트-10명-ff6b6b?style=for-the-badge)](#팀-소개)
[![Skills](https://img.shields.io/badge/스킬-4_built--in-4ecdc4?style=for-the-badge)](#프로젝트-구조)
[![Linear](https://img.shields.io/badge/Linear-통합-5E6AD2?style=for-the-badge&logo=linear&logoColor=white)](#커뮤니케이션)

</div>

---

## 이게 뭔가요?

미션을 던지면:

```bash
./scripts/launch.sh "실시간 공유 링크가 있는 협업 투표 앱을 만들어줘"
```

스타트업 팀 전체가 깨어납니다:

- **Nova** (CEO)가 비전과 MVP 범위를 설정
- **Forge** (CTO)가 기술 스택을 설계하고 컨벤션을 작성
- **팀 전체가 투표** — 고무도장이 아닌 진짜 토론
- **Palette**가 디자인하고, **Pixel**과 **Circuit**이 구현
- **Forge**가 코드 리뷰, **Sentinel**이 E2E 테스트
- **Nova**가 피처마다 리뷰: Ship / Iterate / Cut
- **Pipeline**이 배포, **Shield**가 보안 감사, **Scroll**이 문서 작성

모든 결정, 모든 토론, 모든 리뷰 — Linear 이슈와 코멘트로 기록. 완전한 추적성. 완전한 자율 운영.

---

## 팀 소개

```
 "우리는 수평적이고 열정적인 스타트업이다. '그건 내 일이 아니야'란 말은 여기 없다."
```

| | 코드네임 | 역할 | 성격 | 시그니처 대사 |
|---|----------|------|------|---------------|
| :compass: | **Compass** | PM / 오케스트레이터 | 실용주의자, 스코프 파수꾼 | *"그거 MVP에 없어. 백로그에 넣어."* |
| :star2: | **Nova** | CEO | 비전가, 빠른 출시 지향 | *"일단 출시해. 나중에 개선하지."* |
| :hammer_and_wrench: | **Forge** | CTO | 완벽주의 아키텍트 | *"이거 유저 1만 명 넘으면 터져."* |
| :art: | **Palette** | UI/UX 디자이너 | 공감형, 심미적 | *"유저가 이 버튼 못 찾을 걸."* |
| :jigsaw: | **Pixel** | 프론트엔드 엔지니어 | 디테일 장인 | *"그 패딩 3px 어긋났는데."* |
| :zap: | **Circuit** | 백엔드 엔지니어 | 시스템 사고, 성능 집착 | *"O(n^2)? 이 시국에?"* |
| :shield: | **Sentinel** | QA 엔지니어 | 편집증적 엣지케이스 사냥꾼 | *"유저가 10MB 텍스트 붙여넣으면?"* |
| :rocket: | **Pipeline** | DevOps | 자동화 중독자 | *"CI에 없으면 존재하지 않는 거야."* |
| :lock: | **Shield** | 보안 엔지니어 | 모든 입력을 의심 | *"새니타이즈. 전부."* |
| :scroll: | **Scroll** | 테크 라이터 | 문서화 강박 | *"문서 없는 코드는 기술 부채다."* |

모든 에이전트는 **뚜렷한 개성**을 가지고, 공개적으로 토론하며, Linear 코멘트로만 소통합니다. 의견이 다르면 반박합니다. 밀어붙입니다. 서로 도전합니다. 그게 핵심입니다.

---

## 빠른 시작

### 사전 요구사항

- [Claude Code CLI](https://claude.ai/code) 설치 및 인증 완료
- [Linear](https://linear.app) 계정 + `.env`에 API 키 설정
- Node.js 18+

### 1. 클론 & 설정

```bash
git clone https://github.com/choam2426/oh-my-agent-startup.git
cd oh-my-agent-startup
cp .env.example .env
# .env에 LINEAR_API_KEY 추가
```

### 2. 실행

```bash
# 풀 스타트업 — 미션부터 배포된 제품까지
./scripts/launch.sh "소셜 챌린지가 있는 피트니스 대시보드 만들어줘"
```

```bash
# 또는 Claude Code로 직접 실행
claude --agent compass -p "실시간 투표 앱 만들어줘"
```

### 3. 지켜보기

[Linear](https://linear.app)를 열고 10명의 에이전트가 실시간으로 협업하는 모습을 지켜보세요. 디자인 스펙, 코드 리뷰, QA 리포트, CEO 판결까지 — 한 곳에서 전부.

---

## 작동 방식

```
                         ┌──────────────┐
                         │    미션      │
                         │  (한 줄)     │
                         └──────┬───────┘
                                │
                    ┌───────────▼───────────┐
                    │  Phase 1: Genesis      │
                    │                        │
                    │  Nova → 비전 & 범위    │
                    │  Forge → 아키텍처      │
                    │  팀 → 투표 라운드      │
                    │  Compass → 백로그      │
                    └───────────┬────────────┘
                                │
              ┌─────────────────▼─────────────────┐
              │       Phase 2: MVP 빌드            │
              │                                    │
              │  각 피처마다:                       │
              │  ┌──────────────────────────────┐  │
              │  │ Palette → 디자인 스펙        │  │
              │  │ Forge → 기술 가이드          │  │
              │  │ Pixel/Circuit → 구현         │  │
              │  │ Forge → 코드 리뷰           │  │
              │  │ Sentinel → E2E 테스트        │  │
              │  │ ┌── 실패? ──→ 수정 루프 ──┐ │  │
              │  │ └── 통과 ──→ Nova 리뷰    │ │  │
              │  │            Ship / Iterate  │ │  │
              │  └──────────────────────────────┘  │
              └─────────────────┬──────────────────┘
                                │
                    ┌───────────▼───────────┐
                    │   Phase 3: 마무리      │
                    │                        │
                    │  Pipeline → 배포       │
                    │  Shield → 보안         │
                    │  Scroll → 문서         │
                    └───────────┬────────────┘
                                │
                    ┌───────────▼────────────────┐
                    │  Phase 4: 범위 내 진화      │
                    │                             │
                    │  버그 수정, 성능, UX, 접근성 │
                    │  미션 범위 내에서만 진행      │
                    └─────────────────────────────┘
```

---

## 실행 모드

### Full Team (기본)

4개 Phase 전체. 미션 하나로 새 제품을 만듭니다.

```bash
./scripts/launch.sh "실시간 협업이 가능한 칸반 보드 만들어줘"
```

### Sprint

기존 프로젝트에 피처 추가. Genesis를 건너뛰고 디자인 → 빌드 → 테스트 → 출시로 직행합니다.

```bash
claude --agent compass -p "sprint: 다크 모드 토글 추가"
```

### Debate

코드 없음. 순수한 다중 라운드 에이전트 토론. 에이전트들이 근거와 함께 입장을 취하고, Nova가 최종 결정을 내립니다.

```bash
claude --agent compass -p "debate: API 레이어를 tRPC로 갈지 REST로 갈지?"
```

---

## 핵심 기능

### 에이전트는 실행만 하지 않는다 — 토론한다

모든 주요 결정은 **투표 라운드**를 거칩니다. 에이전트들이 근거와 함께 투표. 반대? 토론 라운드 시작 — 최대 3라운드, 이후 Nova가 타이브레이커. 형식적 승인은 없습니다.

### Linear이 단일 진실 공급원

모든 커뮤니케이션은 Linear 이슈와 코멘트를 통해 흐릅니다. 단순 태스크 트래킹이 아닙니다 — 디자인 스펙, 코드 리뷰, QA 리포트, CEO 판결까지. 모든 결정을 추적할 수 있습니다.

### 검증-수정 루프

Sentinel은 단순히 테스트하지 않습니다 — **게이트**합니다. QA 실패 시 루프 발동: 수정 → 재테스트 → 반복 (최대 3회). 그래도 실패? Forge가 아키텍처 리뷰. 여전히 안 되면? 피벗 프로토콜.

### 재귀적 역량 개선

에이전트가 부족한 결과물을 내면, Compass가 `.claude/agent-memory/<agent>/`에 개선 사항을 기록합니다. 다음에 해당 에이전트가 소환되면 메모리를 읽고 피드백을 반영합니다. 팀은 시간이 지날수록 강해집니다.

### 세션 복구

매 단계마다 `workspace/.startup-state.json`을 업데이트합니다. 작업 중 중단? 재시작하면 Compass가 정확히 그 자리에서 재개 — 맞는 에이전트, 맞는 단계, 맞는 이슈.

### 피벗 프로토콜

테스트 50% 이상 실패 또는 핵심 기능 구현 불가 시, Compass가 Nova에게 에스컬레이션. Nova가 판단: 범위 축소 / 기능 삭제 / 대안 접근 / 밀어붙이기. 팀이 방향 전환. 막다른 길은 없습니다.

---

## 프로젝트 구조

```
oh-my-agent-startup/
├── CLAUDE.md                         # 스타트업 프로토콜 & 팀 문화
├── scripts/
│   └── launch.sh                     # 원커맨드 런처
│
├── .claude/
│   ├── settings.json                 # 권한 & 플러그인 설정
│   │
│   ├── agents/                       # 10개 에이전트 정의
│   │   ├── compass.md                #   PM / 오케스트레이터 (Opus)
│   │   ├── nova.md                   #   CEO (Opus)
│   │   ├── forge.md                  #   CTO (Opus)
│   │   ├── palette.md                #   UI/UX 디자이너
│   │   ├── pixel.md                  #   프론트엔드 엔지니어
│   │   ├── circuit.md                #   백엔드 엔지니어
│   │   ├── sentinel.md               #   QA 엔지니어
│   │   ├── pipeline.md               #   DevOps
│   │   ├── shield.md                 #   보안 엔지니어
│   │   └── scroll.md                 #   테크 라이터
│   │
│   ├── skills/                       # 재사용 가능 역량
│   │   ├── linear-cli/               #   Linear API 조작
│   │   ├── linear-protocol/          #   커뮤니케이션 규약
│   │   ├── coding-conventions/       #   코딩 표준
│   │   └── pivot-protocol/           #   피벗 의사결정 프레임워크
│   │
│   └── agent-memory/                 # 재귀적 개선 저장소
│       ├── palette/                  #   디자이너 피드백 & 학습
│       └── sentinel/                 #   QA 피드백 & 학습
│
└── workspace/                        # 생성된 프로젝트가 여기에
    ├── CLAUDE.md                     #   스택 컨벤션 (Forge가 작성)
    ├── .startup-state.json           #   세션 복구용 체크포인트
    ├── .linear-config.json           #   Linear 프로젝트 & ID 매핑
    └── src/                          #   애플리케이션 소스 코드
```

---

## 커뮤니케이션 흐름

```
Compass (PM)
  │
  ├── Linear 이슈 생성 (수용 기준 포함)
  │
  ├── Palette 소환 ──→ 이슈 확인 ──→ 디자인 스펙 코멘트
  ├── Forge 소환 ────→ 스펙 확인 ──→ 기술 가이드 코멘트
  ├── Pixel 소환 ────→ 전체 확인 ──→ 구현 ──→ 완료 코멘트
  ├── Forge 소환 ────→ 코드 확인 ──→ 리뷰 판정 코멘트
  ├── Sentinel 소환 ─→ E2E 실행 ──→ QA 리포트 코멘트
  │   └── 실패? ──→ 수정 루프 ──→ 재테스트 ──→ 최대 3회
  ├── Nova 소환 ─────→ 전체 확인 ──→ Ship / Iterate / Cut
  │
  └── 상태 업데이트: Backlog → Todo → In Progress → In Review → Testing → Done
```

모든 에이전트는 행동 전에 이전 코멘트 전부를 읽습니다. 정보 사일로 없음. 매번 전체 컨텍스트.

---

## 동반 플러그인

### [Linear-Agent-Skills](./Linear-Agent-Skills)

에이전트에 최적화된 Linear CLI — 30+ 명령어, OAuth 불필요. 이슈 생성, 코멘트 작성, 라벨 관리, 프로젝트 추적. 커뮤니케이션의 백본.

### [mcp-optimizer](./mcp-optimizer)

MCP 관리 툴킷 — 헬스 체크, 사용량 감사, 성능 벤치마킹, 자동 최적화. MCP 서버를 날씬하게 유지합니다.

### [pm-skills](https://github.com/anthropics/skills) (외부 플러그인)

65+ PM 스킬을 플러그인으로 통합 — PRD 작성, 스프린트 플래닝, 시장 규모 추정, 경쟁 분석 등. Compass가 PM 워크플로우에 활용합니다. 자체 개발이 아닌 외부 설치 플러그인.

---

## 설정

### 환경 변수

```bash
# .env
LINEAR_API_KEY=lin_api_xxxxxxxxxxxxx
```

### Claude Code 세팅

설정은 `.claude/settings.json`에 있습니다. 핵심 구성:

- **권한**: 자율 운영을 위해 모든 도구 사전 허용
- **플러그인**: Linear-Agent-Skills + 8개 PM 스킬 플러그인 활성화
- **Agent Teams**: 멀티 에이전트 오케스트레이션을 위한 실험 플래그 활성화

### 에이전트 커스터마이징

각 에이전트는 `.claude/agents/`에 YAML frontmatter가 포함된 마크다운 파일입니다:

```yaml
---
name: forge
model: opus
tools: Read, Grep, Glob, Bash, Write, Edit
skills:
  - linear-cli
  - coding-conventions
memory: project
---
```

에이전트의 성격, 도구, 모델 티어를 자유롭게 수정하세요.

---

## 문화

이건 파이프라인이 아닙니다. 팀입니다.

1. **심리적 안전 + 생산적 토론** — 어떤 결정이든 도전하라. 공개적으로 반대하고, 결정되면 전력투구.
2. **사일로 없음** — 엔지니어가 디자인에 의견 내고, 디자이너가 아키텍처에 도전하고, QA가 제품 결정에 의문을 던진다.
3. **프로세스보다 원칙** — 단계가 의미 없으면 건너뛰고 이유를 설명한다.
4. **속도 AND 장인정신** — 빠르게 출시하되, 쓰레기는 절대 출시하지 않는다.
5. **사용자 집착** — 모든 결정은 사용자 가치로 귀결된다.

---

## 라이선스

[Apache License 2.0](LICENSE)

---

<div align="center">

*에이전트가 만들고, 에이전트를 위해.*

**미션을 던져라. 출시되는 걸 지켜봐라.**

</div>
