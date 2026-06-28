import { Request } from 'express';
import { JwtPayload, GoogleAuthResult } from './auth';

// Express v5의 Request 타입은 전역 namespace augmentation이 동작하지 않는다
// intersection 타입으로 커스텀 프로퍼티를 추가해 any 없이 타입 안전성을 확보한다

// authMiddleware를 통과한 요청: jwtPayload가 반드시 존재한다
export type JwtRequest = Request & { jwtPayload: JwtPayload };

// passport Google 콜백을 통과한 요청: user에 GoogleAuthResult가 담긴다
export type GoogleCallbackRequest = Request & { user: GoogleAuthResult };
