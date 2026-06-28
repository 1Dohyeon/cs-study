import { User } from '@prisma/client';

// JWT 페이로드에 담기는 정보
// 최소한의 식별자(userId)만 넣어 토큰 크기를 줄인다
export interface JwtPayload {
  userId: number;
}

// Google OAuth 성공 후 passport가 req.user에 담는 객체
// authService.loginWithGoogle()의 반환값과 동일한 구조다
export interface GoogleAuthResult {
  user: User;
  token: string;
}
