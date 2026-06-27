# Express.js

> NestJS는 Express 위에서 동작하는 프레임워크다. 즉, 이미 Express의 핵심 개념(미들웨어, 요청/응답 사이클)을 간접적으로 알고 있다고 가정하여 설명한다.

## NestJS → Express 개념 대응표

| NestJS                              | Express                                           | 차이                                                 |
| ----------------------------------- | ------------------------------------------------- | ---------------------------------------------------- |
| `@Controller`, `@Get` 등 데코레이터 | `router.get()` 직접 호출                          | 데코레이터 없음, 함수 호출로 라우팅                  |
| `@Middleware` / `UseGuards`         | `app.use()` / `router.use()`                      | 미들웨어가 Guard, Interceptor, Pipe 역할을 모두 담당 |
| `@Injectable` DI 컨테이너           | 없음 (직접 인스턴스 생성·주입)                    | DI 프레임워크 없음                                   |
| `ExceptionFilter`                   | error-handling middleware `(err, req, res, next)` | 파라미터 4개짜리 미들웨어                            |
| `ValidationPipe`                    | `express-validator` 또는 `joi` 라이브러리         | 직접 연결해야 함                                     |
| `main.ts`의 `app.listen()`          | 동일                                              | 거의 같음                                            |

## 핵심 개념 학습 순서

1. [01-basics](./01-basics/) — 라우팅, req/res 객체
2. [02-middleware](./02-middleware/) — 미들웨어 체인, next()
3. [03-router](./03-router/) — Router로 모듈화
4. [04-error-handling](./04-error-handling/) — 에러 미들웨어
5. [05-rest-api](./05-rest-api/) — 실무형 REST API 구조

## Express의 핵심 원칙

미들웨어 함수의 시그니처: `(req, res, next) => void`

모든 것(라우트 핸들러 포함)이 미들웨어다. `next()`를 호출하면 다음 미들웨어로 넘어간다.
`next(err)`를 호출하면 에러 미들웨어로 점프한다.
