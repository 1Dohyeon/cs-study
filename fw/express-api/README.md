# express-api

Google OAuth 로그인 + 프로필 조회 토이 프로젝트.
Express + TypeScript + Prisma + MySQL 조합으로 실무 구조를 익힌다.

## 기술 스택

| 역할 | 라이브러리 |
|------|-----------|
| 웹 프레임워크 | Express + TypeScript |
| OAuth | passport + passport-google-oauth20 |
| 인증 토큰 | jsonwebtoken (JWT) |
| ORM | Prisma 5 + MySQL |
| 로거 | winston |
| 환경 변수 | dotenv |
| 뷰 | EJS |

## 시작하기

```bash
npm install
cp .env.example .env   # 값 채우기

npx prisma migrate dev # DB 테이블 생성
npm run dev            # 개발 서버 실행
```

## 명령어

| 명령어 | 설명 |
|--------|------|
| `npm run dev` | ts-node-dev로 개발 서버 실행 (핫리로드) |
| `npm run build` | TypeScript 컴파일 → dist/ |
| `npm run start` | 컴파일된 파일로 서버 실행 |
| `npx prisma migrate dev` | 스키마 변경 사항을 마이그레이션으로 적용 |
| `npx prisma generate` | Prisma Client 재생성 |
| `npx prisma studio` | DB GUI 실행 |

## 프로젝트 구조

```
express-api/
  prisma/
    schema.prisma          ← User 모델 정의
    migrations/            ← 마이그레이션 이력
  src/
    app.ts                 ← 서버 진입점. 미들웨어·라우터 조립
    lib/
      prisma.ts            ← PrismaClient 싱글톤
      logger.ts            ← winston 로거 싱글톤
    types/
      auth.ts              ← JwtPayload, GoogleAuthResult 인터페이스
      request.ts           ← JwtRequest, GoogleCallbackRequest 커스텀 Request 타입
    repositories/
      user.repository.ts   ← DB 접근 (findById, upsert)
    services/
      auth.service.ts      ← Google 사용자 upsert + JWT 발급
      me.service.ts        ← userId로 프로필 조회
    middleware/
      auth.ts              ← JWT 검증, req에 jwtPayload 주입
    routes/
      auth.ts              ← Google 전략 등록, /auth 라우터 + 핸들러
      me.ts                ← /me 라우터 + 핸들러
      view.ts              ← /, /callback 뷰 라우터
  views/
    index.ejs              ← 로그인 페이지
    callback.ejs           ← 로그인 성공 페이지 (JWT 확인 + /me 테스트)
```

## 레이어 구조

Router-Service-Repository 3레이어 패턴. 라우터가 req/res 처리까지 담당하고, 비즈니스 로직은 Service, DB 접근은 Repository가 담당한다.

```
Router → Service → Repository → DB
```

| 레이어 | 역할 |
|--------|------|
| Router | 경로 등록 + req 파싱 + service 호출 + res 반환 |
| Service | 비즈니스 로직 |
| Repository | DB 접근 (Prisma) |

인스턴스는 각 라우터 파일에서 직접 연결한다.

```ts
const userRepository = new UserRepository(prisma);
const meService      = new MeService(userRepository);
```

## 인증 흐름

### Google OAuth 로그인

```
클라이언트
  │
  ├─ GET /auth/google
  │     └─ passport가 Google 로그인 페이지로 리다이렉트
  │
  └─ GET /auth/google/callback   ← Google이 code와 함께 리다이렉트
        ├─ passport가 code → Google API → 사용자 정보(email, name, googleId) 획득
        ├─ DB에 User upsert (신규면 insert, 기존이면 조회)
        ├─ JWT 발급
        └─ /callback?token=... 로 리다이렉트
```

### JWT 인증 (`/me`)

```
클라이언트
  │
  └─ GET /me
        Authorization: Bearer <token>
              │
              ├─ authMiddleware: 토큰 검증 → req에 jwtPayload { userId } 주입
              └─ 라우터 핸들러: userId로 DB 조회 → 프로필 응답
```

## 타입 설계

Express v5의 `Request` 타입은 전역 네임스페이스 augmentation이 동작하지 않아 커스텀 intersection 타입으로 해결한다.

```ts
// src/types/request.ts
type JwtRequest            = Request & { jwtPayload: JwtPayload }
type GoogleCallbackRequest = Request & { user: GoogleAuthResult }
```

JWT 미들웨어는 `JwtRequest`로 캐스팅 후 `jwtPayload`를 주입하고, OAuth 콜백 핸들러는 `GoogleCallbackRequest`로 캐스팅 후 `user.token`을 꺼낸다.
