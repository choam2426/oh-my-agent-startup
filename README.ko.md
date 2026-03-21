<div align="center">

**[English](README.md)** | **한국어**

# oh-my-agent-startup

### 솔로 개발자를 위한 열정적인 AI 스타트업 팀.

아무 프로젝트에나 투입하세요 — 새 프로젝트든 기존 프로젝트든. 계획하고, 설계하고, 토론하고, 구현하고, 리뷰하고, 테스트하고, 배송합니다.

[![Claude Code](https://img.shields.io/badge/Built_for-Claude_Code-6B4FBB?style=for-the-badge)](https://claude.ai/code)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue?style=for-the-badge)](LICENSE)
[![Linear](https://img.shields.io/badge/Linear-Integrated-5E6AD2?style=for-the-badge&logo=linear&logoColor=white)](#커뮤니케이션-흐름)

</div>

---

## 이게 뭔가요?

솔로 개발자는 모든 결정을 혼자 내립니다. 코드 리뷰해줄 사람도, 아키텍처에 도전할 사람도, 보안 구멍을 잡아줄 사람도, 엣지 케이스를 테스트할 사람도 없습니다.

**이 프로젝트가 스타트업 팀 전체를 줍니다.**

```bash
claude --agent compass -p "실시간 투표 앱 만들어줘"
```

10명의 에이전트가 진짜 스타트업처럼 일하기 시작합니다:

1. **Nova** (CEO)가 비전과 MVP 범위를 설정
2. **Forge** (CTO)가 아키텍처를 제안 — 팀이 투표
3. **Palette**가 디자인하고, **Pixel**과 **Circuit**이 구현
4. **Forge**가 코드 리뷰, **Sentinel**이 E2E 테스트
5. 테스트 실패 시 팀이 자동으로 수정하고 재테스트
6. **Nova**가 피처마다 리뷰: Ship / Iterate / Cut
7. **Shield**가 보안 감사, **Scroll**이 문서 작성

모든 결정, 모든 리뷰 — Linear 이슈와 코멘트로 기록됩니다.

### 왜 AI 하나가 아니라 팀인가?

- **팀의 힘** — 혼자서는 놓치는 걸 10명이 잡는다
- **투명한 과정** — 모든 토론과 결정이 Linear에 남아 추적 가능
- **관찰을 통한 성장** — 팀의 협업을 지켜보며 자신의 판단력도 날카로워진다

---

## 팀 소개

| | 코드네임 | 역할 | 성격 |
|---|----------|------|------|
| :compass: | **Compass** | PM / 오케스트레이터 | 실용주의 스코프 파수꾼 |
| :star2: | **Nova** | CEO | 비전가, 빠른 출시 지향 |
| :hammer_and_wrench: | **Forge** | CTO | 완벽주의 아키텍트 |
| :art: | **Palette** | UI/UX 디자이너 | 사용자 대변인, 심미적 |
| :jigsaw: | **Pixel** | 프론트엔드 엔지니어 | 디테일 집착 구현자 |
| :zap: | **Circuit** | 백엔드 엔지니어 | 시스템 사고, 성능 집착 |
| :shield: | **Sentinel** | QA 엔지니어 | 편집증적 엣지케이스 사냥꾼 |
| :rocket: | **Pipeline** | DevOps | 자동화 우선 |
| :lock: | **Shield** | 보안 엔지니어 | 모든 입력을 의심 |
| :scroll: | **Scroll** | 테크 라이터 | 명확성 우선 문서가 |

에이전트들은 Linear 코멘트로 공개 토론합니다. 반대하고, 밀어붙이고, 서로의 결정에 도전합니다.

---

## 빠른 시작

### 사전 요구사항

- [Claude Code CLI](https://claude.ai/code) 설치 및 인증 완료
- [Linear](https://linear.app) 계정 + API 키
- Node.js 18+

### 1. 클론 & 설정

```bash
git clone https://github.com/choam2426/oh-my-agent-startup.git
cd oh-my-agent-startup
```

`.env` 파일에 Linear API 키를 설정합니다:

```bash
echo "LINEAR_API_KEY=lin_api_xxxxxxxxxxxxx" > .env
```

### 2. 실행

```bash
# 풀 팀 — 미션부터 배포된 제품까지
./scripts/launch.sh "소셜 챌린지가 있는 피트니스 대시보드 만들어줘"
```

```bash
# 또는 Claude Code로 직접 실행
claude --agent compass -p "실시간 투표 앱 만들어줘"
```

### 3. 지켜보기

[Linear](https://linear.app)를 열고 에이전트들의 실시간 협업을 지켜보세요 — 디자인 스펙, 코드 리뷰, QA 리포트, CEO 판결까지.

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

기존 프로젝트에 팀을 투입합니다. 팀이 먼저 코드베이스를 파악한 뒤, 설계하고 구현하고 테스트하고 배송합니다.

```bash
claude --agent compass -p "sprint: 다크 모드 토글 추가"
```

### Debate

코드 없음. 다중 라운드 에이전트 토론. Nova가 최종 결정을 내립니다.

```bash
claude --agent compass -p "debate: API 레이어를 tRPC로 갈지 REST로 갈지?"
```

---

## 핵심 기능

### 투표 라운드

주요 결정은 투표를 거칩니다. 에이전트들이 근거와 함께 투표 — 반대가 있으면 토론 시작. 최대 3라운드, 이후 Nova가 결정.

### Linear이 단일 진실 공급원

모든 소통은 Linear을 통해 흐릅니다. 디자인 스펙, 코드 리뷰, QA 리포트, CEO 판결, 단계 요약 — 모든 결정을 추적할 수 있습니다.

### 검증-수정 루프

Sentinel이 품질을 게이트합니다. E2E 테스트 실패 시 팀이 자동으로 수정하고 재테스트 (최대 3회). 계속 실패하면 아키텍처 리뷰 또는 피봇 프로토콜 발동.

### 세션 복구

매 단계마다 `workspace/.startup-state.json`을 업데이트합니다. 중단된 세션은 정확히 그 자리에서 재개됩니다.

### 단계 요약

각 Phase 완료 후 Compass가 Linear에 구조화된 요약을 게시 — 결정 사항, 투표 결과, 발견된 버그, 배송된 기능.

### 재귀적 개선

에이전트가 부족한 결과물을 내면 Compass가 `.claude/agent-memory/<agent>/`에 개선점을 기록. 다음 스폰 시 반영합니다.

### 피봇 프로토콜

테스트 대규모 실패 또는 핵심 기능 구현 불가 시, Compass가 Nova에게 에스컬레이션. Nova가 판단: 범위 축소 / 기능 삭제 / 대안 접근 / 밀어붙이기.

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
│   │   ├── compass.md                #   PM / 오케스트레이터
│   │   ├── nova.md                   #   CEO
│   │   ├── forge.md                  #   CTO
│   │   ├── palette.md                #   디자이너
│   │   ├── pixel.md                  #   프론트엔드
│   │   ├── circuit.md                #   백엔드
│   │   ├── sentinel.md               #   QA
│   │   ├── pipeline.md               #   DevOps
│   │   ├── shield.md                 #   보안
│   │   └── scroll.md                 #   테크 라이터
│   │
│   ├── skills/                       # 빌트인 스킬
│   │   ├── linear-cli/               #   Linear API 조작
│   │   ├── linear-protocol/          #   커뮤니케이션 규약
│   │   ├── coding-conventions/       #   코딩 표준
│   │   └── pivot-protocol/           #   피봇 의사결정 프레임워크
│   │
│   └── agent-memory/                 # 재귀적 개선 저장소
│
└── workspace/                        # 생성된 프로젝트 출력
    ├── CLAUDE.md                     #   스택 컨벤션 (Forge가 작성)
    ├── .startup-state.json           #   세션 복구 체크포인트
    └── .linear-config.json           #   Linear 프로젝트 & ID 매핑
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

모든 에이전트는 행동 전에 이전 코멘트 전부를 읽습니다. 매번 전체 컨텍스트.

---

## 설정

### 환경 변수

```bash
# .env
LINEAR_API_KEY=lin_api_xxxxxxxxxxxxx
```

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

## 라이선스

[Apache License 2.0](LICENSE)

---

<div align="center">

**미션을 던져라. 배송되는 걸 지켜봐라.**

</div>
