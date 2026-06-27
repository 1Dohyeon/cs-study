# express-api

Google OAuth 로그인 + 프로필 조회 토이 프로젝트.
Express + TypeScript + Prisma + MySQL 조합으로 실무 구조를 익힌다.

## 기술 스택

| 역할 | 라이브러리 |
|------|-----------|
| 웹 프레임워크 | Express + TypeScript |
| OAuth | passport + passport-google-oauth20 |
| 인증 토큰 | jsonwebtoken (JWT) |
| ORM | Prisma |
| DB | MySQL |
| 환경 변수 | dotenv |

## 구현 범위

### 인증 흐름

```
클라이언트
  │
  ├─ GET /auth/google
  │     └─ Google 로그인 페이지로 리다이렉트
  │
  └─ GET /auth/google/callback   ← Google이 code와 함께 리다이렉트
        ├─ code → Google API → 사용자 정보(email, name, googleId) 획득
        ├─ DB에 User upsert (신규면 insert, 기존이면 그냥 조회)
        └─ JWT 발급 후 응답
```

### 엔드포인트

| 메서드 | 경로 | 인증 | 설명 |
|--------|------|------|------|
| GET | `/auth/google` | 불필요 | Google OAuth 시작 |
| GET | `/auth/google/callback` | 불필요 | OAuth 콜백, JWT 발급 |
| GET | `/me` | JWT 필요 | 내 프로필 조회 |

## 프로젝트 구조

Controller-Service-Repository 패턴 적용. NestJS와 동일한 레이어 분리지만 DI 컨테이너 없이 직접 인스턴스를 연결한다.

```
express-api/
  prisma/
    schema.prisma               ← User 모델 정의
  src/
    controllers/
      auth.controller.ts        ← req/res 처리만 담당
      me.controller.ts
    services/
      auth.service.ts           ← 비즈니스 로직 (JWT 발급, upsert 판단)
    repositories/
      user.repository.ts        ← Prisma 호출만 담당
    routes/
      auth.ts                   ← Router에 controller 연결
      me.ts
    middleware/
      auth.ts                   ← JWT 검증, req.user 주입
    lib/
      prisma.ts                 ← Prisma Client 싱글톤
    app.ts                      ← Express 앱 진입점
  .env
  package.json
  tsconfig.json
```

### 레이어 역할

| 레이어 | 역할 | NestJS 대응 |
|--------|------|------------|
| Router | 경로 등록, controller 연결 | `@Controller` 경로 부분 |
| Controller | req 파싱 → service 호출 → res 반환 | `@Controller` 메서드 |
| Service | 비즈니스 로직 | `@Injectable` Service |
| Repository | DB 접근 (Prisma) | `@Injectable` Repository |

### 수동 DI

NestJS는 프레임워크가 인스턴스를 주입하지만 Express는 직접 연결한다.

```ts
const userRepository = new UserRepository(prisma);
const authService    = new AuthService(userRepository);
const authController = new AuthController(authService);
```

## DB 스키마

```prisma
model User {
  id        Int      @id @default(autoincrement())
  googleId  String   @unique
  email     String   @unique
  name      String
  createdAt DateTime @default(now())
}
```

## 구현 순서

1. 패키지 설치 및 tsconfig 설정
2. `.env` 작성 (DB URL, Google Client ID/Secret, JWT Secret)
3. Prisma 스키마 작성 및 `npx prisma migrate dev`
4. `src/lib/prisma.ts` — Prisma Client 싱글톤
5. `src/repositories/user.repository.ts` — DB 접근 (findByGoogleId, upsert)
6. `src/services/auth.service.ts` — Google 사용자 정보로 upsert + JWT 발급
7. `src/controllers/auth.controller.ts` — passport 콜백 처리, JWT 응답
8. `src/middleware/auth.ts` — Authorization 헤더에서 JWT 검증, req.user 주입
9. `src/services/me.service.ts` — userId로 프로필 조회
10. `src/controllers/me.controller.ts` — 프로필 응답
11. `src/routes/` — Router에 controller 연결
12. `src/app.ts` — 라우터 조립

## 환경 변수 (.env)

```
DATABASE_URL="mysql://root:password@localhost:3306/express_api"
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
GOOGLE_CALLBACK_URL=http://localhost:3000/auth/google/callback
JWT_SECRET=
```
